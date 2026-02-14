# CRUD base

- Create: /create
- Read: /
- Update: /update/<id>/
- Delete: /delete/<id>/

# 機能

- Sell: /sell/<id>/?<quantity>
- 売上/利益算出

# コマンド

①仮想環境・virtualenv
　　└python -m venv venv
　　└venv\Scripts\activate.bat　　※仮想環境に入る (activate)
　　└deactivate　　　　　　　　　　 ※仮想環境から抜ける(deactivate)

　　
②環境の一貫性を保つために、環境パッケージの現在の状態を
「フリーズ」することは良い考えです。
　　└python -m pip freeze > requirements.txt　（or　フォルダー先に直接に「requirements.txt」を作成）

　　
　　例：requirementsの内容
　 古バージョン
　　　　　　Django==2.1.15
　　　　　　django-pyodbc-azure-2019==2.1.0.0
　　新バージョン
　　　　　　Python 3.11
　　　　　　Django==5.0.6
　　　　　　mssql-django==1.5
　　　　　　pyodbc==5.1.0

③requirements.txt ファイル生成以下コマンドラインで実行すること
　　└python -m pip install -r requirements.txt

④Djangoプロジェクト作成
　　└django-admin startproject project_name　　※project_name　プロジェクト名です。英語文字であれば、何でもＯＫです

　　
⑤Djangoアプリケーション作成
　　└python manage.py startapp app_name　　　　※app_name　プロジェクト名です。英語文字であれば、何でもＯＫです

⑥サイト起動確認
　　└python manage.py runserver
　　└python manage.py runserver　192.168.0.xxx　※社内ネットで公開
　　　※Googleでhttp://127.0.0.1:8000/　

⑦モデルをデータベースに反映するためにmigrateを実行します。
　　└python manage.py migrate
　　※上記、コマンド実行する前、サーバーにDB名を作成するのは必要です。

　　
⑧モデル更新後、2段階で実行する
　　└python manage.py makemigrations　（※段階1：モデルを読み取る）
　　└python manage.py migrate　　　　　（※段階2：モデルをデータベースに反映する）

⑨サイトのadminユーザー作成
　　└python manage.py createsuperuser
　　　　※ユーザー名、メール名、パスワードを入力

⑪プロジェクトの中に不具合が無いかチェックします。
　　└python manage.py check
