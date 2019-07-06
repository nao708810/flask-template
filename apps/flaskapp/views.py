"""
Controller
"""

import os
from flask import request, redirect, url_for, render_template, session
from flaskapp import app

#Mainルート
@app.route('/')
def start():
    """初期化後にsampleページに遷移"""
    init()
    return redirect(url_for('sample'))

#Sample Start
@app.route('/sample', methods=['GET', 'POST'])
def sample():
    """サンプルページを表示"""

    return render_template('sample.html')

#初期化用
def init():
    """セッション情報初期化処理"""
    app.secret_key = os.urandom(32)
