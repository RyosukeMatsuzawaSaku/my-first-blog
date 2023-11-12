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

## cookieの設定/呼び出し
- [Cookieの設定/呼び出し]https://sleepless-se.net/2020/08/01/how-to-set-cookie-in-django/
- cookie 
  - 簡単に確認できてしまうためセキュリティとしては弱い
  - 基本設定ではCookieを受け取ったサーバ（Domain)とは異なるWebサーバに対してはCookieを送らない
- セッション
  - セッションIDをCookieに設定する
  - Webブラウザを閉じるまで保存

## API連携

## スクレイピング
- [スクレイピングのやり方](https://ai-inter1.com/python-webscraping/)
- Pythonで実行する場合は専用のライブラリが存在する
- scraping.pyに作成

## 静的コンテンツをWebサーバやCDNに配置する
- [Webサーバ上に配置](https://itpfdoc.hitachi.co.jp/manuals/link/cosmi_v0970/03Y0460D/EY040237.HTM)
- CloudFrontはディストリビューションとオリジンという設定がある
  - ディストリビューションはS3、オリジンはALBを指定するとのこと

## コンテナ化
- DockerFileとdocker-compose.yamlを事前に準備する
- [docker-compose](https://qiita.com/tegnike/items/bcdcee0320e11a928d46)
- `docker compose run -d` でバックグラウンドで起動

## dockerイメージをPush
- [push手順](https://qiita.com/blueskyarea/items/7ddd5441d9212c5a6570)
- 登録したリポジトリ：https://hub.docker.com/r/ryousuke0409/django-web
- リポジトリ名をDockerImage名に含める必要がある。
1. `docker build`でDockerFileをもとにイメージ作成
2. `docker login`でDockerHubへログイン
3. `docker push`でPush
