# 計算機の処理速度のあれこれ

## 1. はじめに

さて，弊学部の授業では基本的に表面的な実装(つまるところライブラリ依存,アルゴリズムをあんまり考えなくても問題ない)の授業が多い傾向があります.「とりあえず結果が出力できれば速度とかいろいろなことは考えなくていいや」と思った方も多いでしょう.

今回は, 普段処理速度を一切考えていない人向けに素数判定を中心として処理速度とアルゴリズムについてざっくりかつ簡単に書いていきます.

これを見て少しでも処理速度とかアルゴリズムについて興味を持っていただけたら幸いです.


## 2. 今回扱う問題

1. 整数nが存在(1 <= n <= 750)
2. n行の 2~10^8 までの間の整数がランダムに与えられている`./src/test_data.txt`がある
3. test_data.txt内に存在する素数が合計いくつ存在したかをint型で出力する
4. pythonのバージョンなどは任意である

* 補足事項
  * `./src/gen_testdata.py`でtest_data.txt を生成できます
  * `./test_prob.py`内のmain関数内に,テストデータの読み込みを含む出力結果を返すものを記述すると,実際にかかった時間も含め出力されます.
  * この問題は プログラミングコンテスト攻略のためのアルゴリズムとデータ構造 内に記載されている問題をベースに作成しています



## 3. アルゴリズムと処理速度

すぐに思いつく素数判定のアルゴリズムとして,ひたすら割っていき、あまりが出なければ合成数,最後まであまりが出続けたら素数.と判定するシンプルなものがあります.(以下 "単純素数判定"と呼びます.正式な名前がもし存在していたら教えてください.)

ただ,入力値までの整数でそれぞれ割り算処理を入れているため計算処理がどうしても遅くなるである点が存在します.

そこで以下のサイト(https://qiita.com/ppza53893/items/e0f464340d6f97760cd5) を参考に,他のアルゴリズムと実行結果の速度を比較した実行結果を以下に示します.

* 補足
  * 使用するpython : 3.11.3
  * 実行したコードは`al_pnum.py`
  * 出力時のフォーマットは以下の通り

```
algorithm : 使用したアルゴリズム
result : 出力値
time : 実行結果(秒)
```

**出力結果**

```
algorithm: 単純素数判定
result:  38
time:  48.230408668518066
-----
algorithm: Wheel factorization
result:  38
time:  0.010618925094604492
-----
algorithm: ミラーラビン素数判定法(kを使用)
result:  38
time:  0.0018906593322753906
-----
algorithm: ミラーラビン素数判定法(k不使用)
result:  38
time:  0.0012345314025878906
-----
```

出力結果を見ればわかる通り,単純素数判定に比べて他のアルゴリズムでの結果が圧倒的に速くなったことがわかると思います.
同じものを出力するにしてもアルゴリズムによっては大幅に計算速度が変わることがわかります.

それぞれのアルゴリズムがどのようなものかの解説はここでは省略します.(気になった方はぜひ調べて実行していただければ.)



## 4. pythonのバージョンによる処理速度の差異

ところで, pythonのバージョンによって処理速度が違うことはご存知でしょうか.

この記事(https://atmarkit.itmedia.co.jp/ait/articles/2211/01/news027.html) にもあるように python3.11ではランタイムの高速化などがあり,処理速度が改善されているとのこと.

そこで,pythonのバージョンごとに速度が変わるかどうかを試してみました.

* 使用するアルゴリズム: 単純素数判定
* 使用したコード: `./src/v_pnum.py`

**表1. 実行結果とpythonのバージョン**(pcの状況とかにもよって変動するので参考程度に)

|version|time(s)|
|-|-|
|3.7.17|59.56197190284729|
|3.8.16|63.020644426345825|
|3.9.16|55.928969621658325|
|3.10.11|56.88713550567627|
|3.11.3|46.2251250743866|

環境によって数秒の誤差はありますが3.11.3の結果が従来のバージョンより若干速くなっていることがわかります.

こういった事例もあるため,pythonで計算処理をするときはバージョンも加味すると良いかもしれません.



## 5. PyPyなどで高速化

参考: https://zenn.dev/turing_motors/articles/e23973714c3ecf

pythonの処理速度が非常に遅い要因として, インタプリタ言語であることが挙げられます.(対義語にはコンパイラ言語)
大まかに言うとプログラム実行時にコードを１行ずつ機械語に変換&実行するタイプの言語のことを指します.


pythonではこの特性上プログラムを即座に実行するメリットを得ていますが,(故にipynbとかの便利なことができる) １行ずつ実行しているため計算処理が非常に遅くなってしまいます.

そこでJITコンパイル(実行時にコードを一回コンパイルする方法)で高速化を図ってみます.

<br>

ライブラリではnumba(超便利)などがありますが，今回はPyPyを使用していきます.
参考(https://www.sejuku.net/blog/90319)

pyenv環境なら他のバージョンと同じようにインストール&実行できるのでぜひ.


* 使用したバージョン: pypy3.9-7.3.11
* 使用したコード: `./src/v_pnum.py`
* 使用するアルゴリズム: 単純素数判定


**実行結果**

```
finish
result:  38
time:  3.5401909351348877
```

時間(time)に着目すると, なんと約3.5秒となっています.
言わずもがな先程(表1)までの実行時間よりも圧倒的に速いです.

既存のpythonプロジェクトなどで計算処理を多く実装している場合は,目に見えて速くなるかもしれません.

<br>



## まとめ

簡素なものになりますが,アルゴリズムや使用する環境によって処理速度が変わることが確認できたでしょうか.

1回の処理ではあまり速度を気にする必要のない処理でも100回なら,10^n なら? と値がどんどん増えていくと最終的な処理にかかる時間が大幅に変わることがあります.

プログラムを書くときに処理速度とアルゴリズムを少しでも考えるきっかけになれば幸いです.



## おまけ: エラトステネスのふるい

素数判定として使えるものとしてエラトステネスのふるいというものがあります(どこかで聞いた人も多いのではないでしょうか).これは入力値以下のすべての素数を発見するアルゴリズムです.
大きな流れとしては,入力値nが与えられたとき,n個のTrueの配列を作成.作成後小さい値から順に倍数のものをFalseにして素数以外をふるい落としていくものです.

さて,このアルゴリズムをそのまま他のものと同じように実装(1行ごとに実行)していくととても時間がかかります.
ただ,冒頭にも書いた通り入力値以下のすべての素数を算出できるので関数を実行するのは1回で済みそうです.

4.での環境で実際に動かして速度を測ってみます.

実装したコードは`./src/era_pnum.py` に記述しています.

**実行結果**

```
eratosthenes
result:  38
time:  11.617347717285156
```

ミラーラビン素数判定法などに比べると遅いですが単純素数判定よりだいぶ改善されていることが確認できると思います.


## 参考にしたもの(まとめ)

1. 渡部有隆.(15版 2022/2/18).プログラミングコンテスト攻略のためのアルゴリズムとデータ構造.(kindle版: https://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%82%B3%E3%83%B3%E3%83%86%E3%82%B9%E3%83%88%E6%94%BB%E7%95%A5%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0-%E6%B8%A1%E9%83%A8-%E6%9C%89%E9%9A%86-ebook/dp/B00U5MVXZO)
2. @ppza53893.最終更新日 2023年06月08日.素数判定アルゴリズムいろいろ.(https://qiita.com/ppza53893/items/e0f464340d6f97760cd5)
3. 高速動作するPython「PyPy」とは？概要と速度をチェック.(https://www.sejuku.net/blog/90319)
4. ymg_aq.あなたのPythonを100倍高速にする技術 / Codon入門.(https://zenn.dev/turing_motors/articles/e23973714c3ecf)