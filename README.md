# potterin
高知県様IoT研修

## How to use

1. アプリケーションをローカルにクローンします。

```cmd
git clone https://github.com/FujitsuLearningMedia/potterin.git
```

2. appsフォルダに移動します。

```cmd
cd apps
```

3. パッケージをインストールします。

```cmd
pip install -r requirements.txt
```

4. apps\config.sampleファイルをコピーして、config.pyにリネームします

5. config.pyにダミーデータを設定します。

```python
#Settingファイル
SECRET_KEY='secretkey'
#---------------------------------------------
# Azure アカウント関連
#---------------------------------------------
#STORAGE
STORAGE_KEY         = "ffffffffffff"
STORAGE_NAME        = "ffffffffffff"
TABLE_NAME          = "ffffffffffff"

#BLOB
BLOB_URL            = "https://" +  STORAGE_NAME + ".blob.core.windows.net/"

#CUSTOM VISION
TRAINING_KEY        = "ffffffffffff"
PREDICTION_KEY      = "ffffffffffff"
ENDPOINT            = "ffffffffffff"
VISION_PROJECT_NAME = "ffffffffffff"
PUBLISH_ITERATION_NAME = "ffffffffffff"
#---------------------------------------------
# Google Maps アカウント関連
#---------------------------------------------」
MAPS_KEY            = "ffffffffffff"

```

4. アプリケーションを起動します。

```cmd
python manage.py
```