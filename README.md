# VS Codeのdevcontainerを利用するための参考プロジェクト

pythonすぐ動かせる版。

## 準備

- VSCode
- VSCode拡張
  - Remote-Containers

### .envの用意

このREADMEと同じディレクトリに.envという名前のファイルを作り、以下の内容を記載する。

文字コードがUTF-8以外だとだめなので注意。

```ini
# docker-compose プロジェクト名
COMPOSE_PROJECT_NAME="my_devcontainer"
```

### 開発環境の起動

このディレクトリをルートとしてVSCodeで開き、Ctrl + Shift + p でコマンドパレットを開き、Reopen in Containerを選ぶ。

起動に失敗したようなダイアログが出ることがあるが、Retryするとうまく行くことが多い。それでもダメなら案内に従っておとなしくホスト側に戻り、エラーログを見る。

コンテナのセットアップには5分ほどかかる。

## 構成

- .devcontainer/: vscode devcontainerのための設定が入っている。
- .vscode/: vscodeの設定ファイルが入っている。
- controllers/: C#のController的立場のファイルを配置。
- services/: Controllerと対応するService的立場のファイルを配置。
- common/: 各バッチ共通で使用するものを配置。
  - constants/: 固定値を配置。
    - 各ファイルについてはファイル内のサンプルやコメント参照。
  - logger/: ロガーを配置。
  - services/: 外部とやり取りを行う共通モジュールを配置。
  - utils/: 共通処理を配置。
  - decorators/: デコレータを配置。
- test/: 各種テスト用コードを配置。
- develop/: 開発中に使用する便利なものを置く。今はjupyterのサンプルのみ。

## デバッグ

VSCodeのデバッグ機能で今開いているファイルをエントリーポイントとしてデバッグ実行ができる。

test/ディレクトリ以下に、目的のステップを起動するコードを書いてそのスクリプトをデバッグ実行する。
