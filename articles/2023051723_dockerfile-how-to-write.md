Dockerfileの書き方入門
Docker,Dockerfile,初心者
dockerfile-how-to-write

こんにちは。今回は、Dockerについて初心者エンジニアに向けて、Dockerfileの書き方について解説します。

## はじめに

Dockerfileは、Dockerイメージを作成するための設定ファイルです。Dockerfileを作成することで、Dockerイメージのビルドが自動化され、同じ環境を簡単に再現できるようになります。

## Dockerfileの書き方

Dockerfileは、テキストファイルで作成します。基本的な書き方は、以下のような形式になります。

```Dockerfile
# ベースイメージの指定
FROM イメージ名:タグ

# パッケージのインストールや設定の実行
RUN コマンド1 \
    && コマンド2 \
    && ...

# ポートの公開
EXPOSE ポート番号

# コンテナ実行時に実行されるコマンドの指定
CMD ["コマンド", "引数1", "引数2", ...]
```

### ベースイメージの指定

Dockerfileの最初の行には、ベースとなるDockerイメージを指定します。ベースイメージは、Dockerイメージの元となるイメージで、その上に必要なパッケージや設定を追加していきます。

```Dockerfile
FROM python:3.9
```

### パッケージのインストールや設定の実行

ベースイメージに追加するパッケージのインストールや設定の実行は、`RUN`命令を使用して行います。

```Dockerfile
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/example/example.git
```

### ポートの公開

Dockerコンテナ内で使用するポートを公開する場合は、`EXPOSE`命令を使用します。

```Dockerfile
EXPOSE 8000
```

### コンテナ実行時に実行されるコマンドの指定

コンテナ実行時に実行されるコマンドは、`CMD`命令を使用して指定します。`CMD`命令は、Dockerfileで一度しか使用できず、最後に書く必要があります。

```Dockerfile
CMD ["python", "app.py"]
```

## サンプルコード

以下は、Flaskを使用するPythonアプリケーションをDockerイメージ化するためのDockerfileの例です。

```Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## 注意点

- Dockerfileのインデントは、スペース2つを使用してください。
- ベースイメージやパッケージのバージョンは、必ず指定してください。
- `EXPOSE`命令で指定したポート番号と、実際にアプリケーションが使用するポート番号が一致していることを確認してください。

## まとめ

Dockerfileを作成することで、Dockerイメージのビルドを自動化し、環境の再現性を高めることができます。Dockerfileの書き方について基本的な書き方を紹介しました。Dockerfileの設定を理解し、より高度な設定を行えるようになることをお勧めします。

## 参考文献

- [Docker公式ドキュメント](https://docs.docker.com/engine/reference/builder/)
- [DockerfileでWebアプリをDocker化するチュートリアル](https://qiita.com/ksh-fthr/items/9fcf0200d6d99f6b2f4c)
