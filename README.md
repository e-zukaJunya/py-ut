# Pytest series sample

This is a sample repo of pytest series library.

- pytest
- pytest-cov
- pytest-mock

It's explains just a simple usage.

## requirements

- VSCode
- VSCode extensions
  - Remote-Containers

## usage

### Prepare a .env

Put a file named .env at the same position of This README. And write the content berow.

Warning: It doesn't work with the utf-8 encoding.

```ini
# docker-compose project name(as you like)
COMPOSE_PROJECT_NAME="my_devcontainer"
```

### Start up your development environment

Open this dir as root with VScode, and open the command pallet by Ctrl + Shift + p, then select Reopen in Container.

It sometimes pops a dialog about starting up was fault, but it often goes well when you retry.

If it doesn't work, you should go back to your host following the message , and look the error log.

It takes about 5 min to set up a container.

## composition

Just a main ones.

- .devcontainer/: vscode devcontainer settings
- .vscode/: vscode settings(It's for devcontainer env)
- src/: main codes
- test/: test codes
- develop/: useful tools for develop. Just a jupyter sample now...

## debug

VSCodeのデバッグ機能で今開いているファイルをエントリーポイントとしてデバッグ実行ができる。

test/ディレクトリ以下に、目的のステップを起動するコードを書いてそのスクリプトをデバッグ実行する。

## memo about a test

- -s: generate print messages
- -vv: 
- --cov: take the coverage of the tests.
- --durations: show test behavior in order of slowness. If it's set 0, show all the behaviors and dulations.
- --cov-report: generate a test report as html.
