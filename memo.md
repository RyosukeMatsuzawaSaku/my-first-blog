# 各種リンク
- [チュートリアル](https://tutorial.djangogirls.org/ja/)
- [オプション](https://tutorial.djangogirls.org/ja/)
- [チートシート](https://qiita.com/maisuto/items/bcdb0fd6c63cf0c544d6)

# よく使うコマンド
- サーバを起動
  - python manage.py runserver

# Linuxコマンド
## yum
- yum = rpm + 「リポジトリ」による自動更新機能 + 依存関係の管理(検出だけじゃない)

- yumは`/etc/yum.repos.d/*.repo`
に記載されているリポジトリ場所にあるパッケージらに対してrpm経由でDLしたり、インストールしたり、必要であればインストール時に依存関係のあるパッケージを検出して一緒にインストールしたりします。

- [参考](https://www.wantedly.com/companies/rakus/post_articles/139373)

# 機能追加
## API取得
- [DjangoでAPI呼び出し](https://qiita.com/egplnt/items/9cc0dec14d1b3eb7e34c)

# cookieの設定/呼び出し
- [Cookieの設定/呼び出し]https://sleepless-se.net/2020/08/01/how-to-set-cookie-in-django/
- cookie 
  - 簡単に確認できてしまうためセキュリティとしては弱い
  - 基本設定ではCookieを受け取ったサーバ（Domain)とは異なるWebサーバに対してはCookieを送らない
- セッション
  - セッションIDをCookieに設定する
  - Webブラウザを閉じるまで保存

# スクレイピング
- [スクレイピングのやり方](https://ai-inter1.com/python-webscraping/)
- Pythonで実行する場合は専用のライブラリが存在する
- scraping.pyに作成
