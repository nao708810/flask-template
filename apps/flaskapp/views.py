"""
Controller
"""

import os
from flask import request, redirect, url_for, render_template, session
from apps.flaskapp.models.azure.storage import Storage
from apps.flaskapp.common import const
from flaskapp import app
import requests

#Mainルート
@app.route('/')
def start():
    """初期化後にsampleページに遷移"""
    init()
    list_q = _make_list()
    userid = session.get('userid')
    if userid == None:
        userid = ""
    return render_template('vote.html', userid=userid, list_q=list_q)

#Sample Start
@app.route('/total', methods=['GET', 'POST'])
def sample():
    """サンプルページを表示"""
    ans_list = []    
    storage = Storage(app.config['STORAGE_NAME'], app.config['STORAGE_KEY'])
    answer = {}
    answer = storage.userid_search(app.config['TABLE_NAME'], "answer").items
    all_data = {}
    all_data = storage.get_storage_all(app.config['TABLE_NAME']).items
    
    for ans in answer:
        for data in all_data:
            if data["RowKey"] != "answer":
                point = 0
                for num in const.list_q:
                    if ans["Q"+str(num)] == data["Q"+str(num)]:
                        point += 1
                obj = {"point":point,"userid":data["RowKey"]}
                ans_list.append(obj)
    
    ans_list = sorted(ans_list, key=lambda x: x["point"], reverse=True)

    return render_template('total.html', list=ans_list)

#回答受信
@app.route('/vote', methods=['GET', 'POST'])
def vote():
    example = ''
    userid = session.get('userid')
    list_q = _make_list()
    # ストレージオブジェクト存在確認
    storage = session.get("storage")
    if storage == None:
        storage = Storage(app.config['STORAGE_NAME'], app.config['STORAGE_KEY'])
    if request.method == 'POST':
        # フォーム情報取得
        userid = request.form['userid']
        question = request.form['question']
        answer = request.form['radio']
        # ストレージ更新
        entities = {}
        entities = storage.userid_search(app.config['TABLE_NAME'],userid).items
        if len(entities) != 0:
            for entity in entities:
                entity["Q"+question] = answer
                storage.update_entity(app.config['TABLE_NAME'],entity)
        else:
            entity = {"PartitionKey":"F-1","RowKey":userid,"Q"+question:answer}
            storage.insert_entity(app.config['TABLE_NAME'],entity)
        
        # 次問題ページ情報作成
        if len(const.list_q) > int(question):
            list_q[int(question)]["select"] = 'selected'
        else:
            # セッション破棄
            session.pop("userid", None)
            session.pop("storage", None)
            return render_template('thanks.html')
        
        # セッション情報の保存
        session['userid'] = userid
        session['storage'] = storage
        
    return render_template('vote.html', userid=userid, list_q=list_q)

#リスト作成
def _make_list():
    list_select = []
    for num in const.list_q:
        select_option = {"num":num,"select":''}
        list_select.append(select_option)
    return list_select

#初期化用
def init():
    """セッション情報初期化処理"""
    app.secret_key = os.urandom(32)
