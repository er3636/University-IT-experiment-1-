# University-IT-experiment-1-
大学の情報工学実験１という講義で作ったプログラムをまとめてみました

# Regular Expression Experiment
grep コマンド と 正規表現を用いて様々な検索を行ってみた。

課題１～５はscript.txtに記載している。課題６はautomaton.c に記載している。

# 課題１
配布ファイルexample1.txt に対して、grep により母音で始まる駅名だけを出力する。

# 課題２
配布ファイルexample1.txt に対して、grep により母音以外が2 文字以上連続して現れる駅名だけを出力する。

# 課題３
配布ファイルexample1.txt に対して、grep により母音以外が2 文字以上連続して現れ、母音を挟んだ後、再び母音以外が2 文字以上連続して現れる駅名だけを出力する。

# 課題４
配布ファイルexample2.txt に工学部の各学科の定員が記載されている。grep により定員が60 名以上90 名未満の学科が記載された行だけを出力する。

# 課題５
配布ファイルexample3.txt に対して、以下の言語（パターン）から成る行をgrep により出力する。
（a）00 で始まり11 で終わる系列から成る言語
（b）01 で始まり01 で終わる系列から成る言語。
（c）長さが3 の倍数の系列から成る言語。
（d）101 を部分系列として含む系列から成る言語。
（e）0 が偶数回出現する系列から成る言語

# 課題６
問い5d の言語を受理する決定性有限オートマトンを模倣したC 言語によるプログラムを作成する。
