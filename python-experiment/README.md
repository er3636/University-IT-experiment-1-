# University-IT-experiment-1-
大学の情報工学実験１という講義で作ったプログラムをまとめてみました

# PYTHON 実験

# 課題と設計
授業内で与えられた課題を次に示す。
1) 授業で指定された ファイル（"data2018.txt"）の記事の 行列を作成する。
2) 非負値行列因子分解を実装する。また、指定のデータに対して、重みの行列と特徴の行列を計算し、特徴解析の結果を表示する。
3) 乗法的更新ルール適用時のコスト関数の変化を折れ線グラフで示す。
応用) 日本語の記事データに対して、非負値行列因子分解を行い、記事の特徴解析を行う。

# 課題 1
　本課題では、 授業で指定されたファイルの記事の行列を作成する。
作成処理を3ステップに分ける。
1. ファイル読み込みおよび単語分割
2. 行列の列として利用される単語リストの作成
3. 単語リストに登録された単語に対して、各記事に登場する単語数を数え、記事の行列を生成する

# 課題 2
　本課題では、 非負値行列因子分解を実装する。また、指定のデータに対して、重みの行列と特徴の行列を計算し、特徴解析の結果を表示する。
記事の行列を因子分解することで共通の特徴を捉えた小さな集合に減らすことができる。今回は重みの行列と特徴の行列を非負値行列因子分解で計算する。

本課題では特徴の数を予め決めなければならないので 、少なすぎない・多すぎないように特徴数を 10にする。重みの行列（W ）の、
・行が記事
・列が特徴
である。そして特徴の行列（H）の
・行が特徴
・列が単語
である。それを基にW と H を生成し、ランダムな値を代入する。

生成した行列 W に H をかけたら結果が記事の行列 V になるはずである。しかし、結果が異なっていれば、行列 W と H を乗法的更新ルールにそって更新しなければならない。 V と WH の違いの程度をコスト関数で計算できる。

# 課題 3
　本課題では、乗法的更新ルール適用時のコスト 関数の変化を折れ線グラフで示す。そのためにはx 軸を代表する a rray x と y 軸を代表する arrayyを定義する。課題 2 において更新を行った for ループの中で、繰り返し数である count 変数を x に、コスト関数の結果である cost 変数を yに加えていく。よって、 count の変化を示す array x と cost 変数を示す array y を得る。それをmatplotlib ライブラリの中にある plot 関数に渡すとグラフができる。

# 課題 4
　本課題では日本語の記事に対して非負値行列因子分解を行い、記事の特徴解析を行う。Reuterseuters日本のトップニュースから1010個の記事を取得し、それを個の記事を取得し、それを’data_jp.txt’というファイルに保存し、課題1課題2と同様に保存したファイルから記事を読み、解析を行う。。
 本課題ではある url から読み取りを行うためにはurllib.requesturllib.requestライブラリを使用する。また、読み取ったHTMLファイルから記事を取るためにBeautifulSoupライブラリを用いる。今回読み取りを行う urlは（"https://jp.reuters.com/news/topNews""https://jp.reuters.com/news/topNews"）である。

# 課題1・2の結果
特徴の行列の上位6単語、重みの行列の上位3記事を表示：

['for', 'securities', 'rules', 'new', 'is', 'and']

China relaxes rules for securities firmsBEIJING (Reuters)

Golf's new boy wonder? He's been mistaken for Tiger Woods' ball

Cracking football's glass ceiling

['but', 'not', 'were', 'no', 'dinosaur', 'this']

Researchers say Neanderthals were not our dimwitted inferiors

Scientists unearth unique long

Golf's new boy wonder? He's been mistaken for Tiger Woods' ball
.
.
.

# 応用課題結果
形式：

「記事に出ている強い単語」

記事番「記事に関する情報」

記事番「記事に関する情報」

記事番「記事に関する情報」

結果：

['サウジ ', 投資 ', を ', 金融 ', から ', 閣僚]

3［リヤド ２３日 ロイター］

1［アンカラ ２３日 ロイター］

0［東京 ２３日 ロイター］


['米 ', か ', 認定 ', 為替 ', し ', 派]

9［東京 ２３日］

4［東京 ２３日 ロイター］

7［東京 ２３日 ロイター］
