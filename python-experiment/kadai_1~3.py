Salic Ertugrul(エルトゥール)
#################################    KADAI 1    #######################################

import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.family']='Osaka'


# {単語 : 単語出現回数} の辞書型の作成
def creat_jisho_tangosuu(tmp_tango):#単語リストを受け取る
    jisho = {i: tmp_tango.count(i) for i in tmp_tango}
    return jisho


# 出現回数によって単語のフィルターを行う
def tangosuu_filter(tmp_tango):#単語リストを受け取る
    temp_list = []
    jisho = creat_jisho_tangosuu(tmp_tango)# {単語 : 単語出現回数} の辞書型の作成
    for tango, kaisuu in jisho.items():
        if kaisuu > 1 and kaisuu < 15:#出現回数が多すぎる・少なすぎる単語以外をリストに追加する
            temp_list.append(tango)
    return temp_list#できた新しい単語リストを返す

#全体の単語リストを作成
def zentai_tango_bunkai(str):
    lst_mushi = [',', '-', '(', ')', '.', '?'] #記事の中から消す文字グループ
    word = "" #一時的に使う文字列
    tmp_tango = [] #単語リスト

    # 単語分解処理
    for i in range(0, len(str)):#全ての文字を一々確認していく
        for j in range(0, len(str[i])):
            if str[i][j] in lst_mushi:#もし消すべき文字が出たら無視する
                j += 1
            elif str[i][j] == ' ':#空白が出たら単語できた単語をリストに追加する
                if (word != ""):
                    word = word.lower()#全ての文字を小文字にする
                    tmp_tango.append(word)
                    word = ""
            else:
                word += str[i][j]#上記以外の文字であれば、その文字を途中の単語に加える
    tmp_tango = tangosuu_filter(tmp_tango)#単語の出現回数によってリストのフィルターを行う
    return tmp_tango#できた単語リストを返す

#記事ごとの単語リストを作成（辞書として）
def kiji_tango_bunkai(str):
    lst_mushi = [',', '-', '(', ')', '.', '?', '']#記事の中から消す文字グループ
    word = ""
    list_tango = []
    for j in range(0, len(str)):#全ての文字を一々と確認していく
        if str[j] in lst_mushi:#もし消すべき文字が出たら無視して次の文字に移る
            j += 1
        elif str[j] == ' ':#空白が出たら単語できた単語をリストに追加する
            if (word != ""):
                word = word.lower()#全ての文字を小文字にする
                list_tango.append(word)#できた単語を単語リストに追加する
                word = ""
        else:
            word += str[j]#上記以外の文字であれば、その文字を途中の単語に加える
    jisho = creat_jisho_tangosuu(list_tango)#各単語　対　各単語の記事での出現回数を示す辞書を作成する
    return jisho#辞書を返す



##################### 初期設定 ###################
##ファイル読み取り
data = open('data2018.txt')  # 指定のファイルから読み取りを行う
str = data.readlines() #記事ごとを読み取る

##変数などの定義
kijisuu = len(str)#記事の数
kiji = []#「単語の出現回数」対 「単語」の辞書リスト（各記事の辞書リスト）
kiji_titles = []#記事のタイトルリスト
temp = ""
##################################################



################################################
############# 単語リストの作成（全体+記事毎）########
################################################

## 全体の単語リスト作成
list_tango = zentai_tango_bunkai(str)  

# kiji毎の単語の辞書を作成
for i in range(0, len(str)):
    #記事毎の単語辞書からなるリストを作成する
    kiji.append(kiji_tango_bunkai(str[i]))
    
    #記事のタイトルからなるリストを作成する（課題2で使用する）
    for j in range(len(str[i])):
        if str[i][j]== "-":
            break
        else:
            temp += str[i][j]
    kiji_titles.append(temp)
    temp = ""

# リストの中に2つ以上含まれている単語を一つにする
set_zentai_tango = set(list_tango)
list_tango = list(set_zentai_tango)

################################################



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



#---------------------------------------------------------------------------------------#
##################################    KADAI 2    ######################################
#---------------------------------------------------------------------------------------#


################# 初期設定 ##################

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

#グラフのx軸とy軸に使用するarrayの定義
x = np.array([])
y = np.array([])

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
    
    #グラフのx軸とy軸に使用するarrayに値を代入していく
    x = np.append(x,count)
    y = np.append(y,cost)
    


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
    
##課題3 グラフ作成
plt.xlabel("繰り返し数")#繰り返し数
plt.ylabel("コスト関数の値")#コスト関数の値
t = plt.plot(x, y)

