# Salic Ertugrul(エルトゥール)

import numpy as np
import MeCab
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://jp.reuters.com/news/topNews"

# urlopen()でデータを取得
res = req.urlopen(url)

# BeautifulSoup()で解析
soup = BeautifulSoup(res, 'html.parser')

# 任意のデータを抽出
#title1 = soup.find("h1").string
#print("title = ", title1)

file=open('data_jp.txt', 'w')

p_list = soup.find_all("p")

for i in range(10):
    str_out = str(p_list[i].get_text())
    str_out = str_out.rstrip()
    file.write(str(i)+str_out)
    if i != 10 : file.write('\n')
    
    
kiji_titles = []# 記事のタイトルリスト

# {単語 : 単語出現回数} の辞書型の作成
def creat_jisho_tangosuu(tmp_tango):  # 単語リストを受け取る
    jisho = {i: tmp_tango.count(i) for i in tmp_tango}
    return jisho

# 出現回数によって単語のフィルターを行う
def tangosuu_filter(tmp_tango):  # 単語リストを受け取る
    temp_list = []
    jisho = creat_jisho_tangosuu(tmp_tango)  # {単語 : 単語出現回数} の辞書型の作成
    for tango, kaisuu in jisho.items():
        if kaisuu > 1 and kaisuu < 15:  # 出現回数が多すぎる・少なすぎる単語以外をリストに追加する
            temp_list.append(tango)
    return temp_list  # できた新しい単語リストを返す

# 全体の単語リストを作成
def zentai_tango_bunkai(mojiretsu):
    lst_mushi = ['。', '、', '(', ')', '「', '」', '・','\n','／','─','\\','（','）','０','１','２','３','４','５','６','７','８','９','1','2','3','4','5','6','7','8','9','0']  # 記事の中から消す文字グループ
    word = ""  # 一時的に使う文字列
    tmp_tango = []  # 単語リスト

    kiji = []
    # 単語分解処理
    tagger = MeCab.Tagger("-Owakati")

    for i in range(len(mojiretsu)):
        for j in range(len(mojiretsu[i])):
            if mojiretsu[i][j] == '-':
                kiji_titles.append(mojiretsu[i][0:j])
                tmp_tango.append(mojiretsu[i][j+2:])
                break

    for i in range(len(tmp_tango)):
        for j in range(len(tmp_tango[i])):
            if tmp_tango[i][j] not in lst_mushi:
                word += tmp_tango[i][j]
            else:
                j += 1
        kiji.append(word)
        word=""
        list_kiji_tango =[]

    for i in range(len(kiji)):
        str_output = tagger.parse(kiji[i])
        list_output = str_output.split(' ')
        list_output.remove("\n")
        list_kiji_tango.append(list_output)
    
    return list_kiji_tango



#################### 初期設定 ###################
##ファイル読み取り
data = open('data_jp.txt')  # 指定のファイルから読み取りを行う
mojiretsu = data.readlines()  # 記事ごとを読み取る
list_tango = []
kiji = []
kijisuu = len(mojiretsu)#記事の数

list_kiji_tango = zentai_tango_bunkai(mojiretsu)
for i in range(len(list_kiji_tango)):
    list_tango.extend(list_kiji_tango[i])
    kiji.append(creat_jisho_tangosuu(list_kiji_tango[i]))
list_tango = tangosuu_filter(list_tango)



# リストの中に2つ以上含まれている単語を一つにする
set_zentai_tango = set(list_tango)
list_tango = list(set_zentai_tango)

##############  記事行列生成 #############
# 記事の行列を生成
V = np.zeros(kijisuu*len(list_tango))
V.shape = kijisuu, len(list_tango)


# ---記事の行列に値を代入---
# 行列の全ての行と列をループ
for i in range(len(kiji)):
    for j in range(0, len(list_tango)):
        jisho = kiji[i]#記事の辞書（単語の出現回数：単語）を代入
        tango = list_tango[j]#全ての記事の単語リストから単語を一つ代入
        if tango in jisho:#代入した単語が辞書（記事）に含まれたらその出現回数を記事行列の要素に代入
            V[i][j] = jisho[tango]
#########################################


################# 非負値行列因子分解 ##################
features = 10 #特徴数を事前に決める

#重みの行列と特徴の行列を生成し、要素の値をランダムに選ぶ
# W=(行:記事 x 列:特徴数)------H=(行:特徴 x 列:単語リスト)
W=np.matrix([[np.random.random() for i in range(features)] for j in range(kijisuu)])
H=np.matrix([[np.random.random() for i in range(len(list_tango))] for j in range (features)])

#############################################



############ 式2：コスト関数##############
def func_cost(a, b):
    dif = 0
    #行列の全ての要素にアクセスする
    for i in range(np.shape(a)[0]):
        for j in range(np.shape(a)[1]):
            #差を足し合せて2乗をとる
            dif += pow(a[i, j] - b[i, j], 2)
    return dif
#######################################


##################
#最大で500回だけ操作を繰り返す
for count in range(500):
    WH = np.dot(W, H)

    #差を計算
    cost = func_cost(V, WH)

    #差が0となったら終了
    if cost == 0:
        break
    
    #特徴の行列を更新
    Ha = (W.T) * V
    Hb = (W.T) * W * H
    H = np.matrix(np.array(H) * np.array(Ha) / np.array(Hb))

    #重みの行列を更新
    Wa = V * (H.T)
    Wb = W * H * (H.T)
    W = np.matrix(np.array(W) * np.array(Wa) / np.array(Wb))


#全ての特徴を確認していく（ループする）
for i in range(features):
    #単語とその重みのリストを作る
    list_omomi = []
    for j in range(len(list_tango)):
        list_omomi.append((H[i,j], list_tango[j]))
    #ソートし、逆にする
    list_omomi.sort(reverse=True)
    
    #トップ6の単語を出力させる
    tmp_str = [k[1] for k in list_omomi[0:6]]
    print(tmp_str)
    
    #扱う特徴の記事のリストを作る
    kiji_tmp_list = []
    #記事とその重みを一緒にリストに追加する
    for j in range(len(kiji_titles)):
        kiji_tmp_list.append((W[j,i], kiji_titles[j]))
    #ソートして逆にする
    kiji_tmp_list.sort(reverse=True)
    
    #トップ3を出力させる
    for j in kiji_tmp_list[0:3]:
        print(j[1])

    print('\n')
    
