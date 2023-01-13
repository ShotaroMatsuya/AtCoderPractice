## AtCoderへのログイン
```bash
    oj login https://atcoder.jp/
```

## テストディレクトリの作成
```bash
    # AtcoderBeginnersContest256回のA問題を解く場合を想定しフォルダを作ります
    mkdir -p works/abc/abc256/abc256a
    # カレントディレクトリをworks/abc/abc256/abc256aに移動させる
    cd works/abc/abc256/abc256a
```

## テストインプットのダウンロード
```bash
    oj d https://atcoder.jp/contests/abc256/tasks/abc256_a
```

## テストスクリプトの作成
```bash
    touch abc256a.py
```


## テストの実行
```bash
    oj t -c "python3 abc256a.py" -d test
```

## コードの提出
```bash
    oj s https://atcoder.jp/contests/abc256/tasks/abc256_a abc256a.py
```

## pypyで提出する場合
```bash
    oj s --guess-python-interpreter pypy abc256a.py
```