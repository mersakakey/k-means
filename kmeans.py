"""
k-means法
"""

from cmath import inf
import csv
import numpy as np
import random

 
#f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

data = np.loadtxt('ここにcsvファイル名を追加', delimiter=',', dtype='float')

#data = np.array([[1,1,1,1,1],[9,9,9,9,9],[2,2,2,2,2],[3,3,3,3,3],[8,8,8,8,8],[7,7,7,7,7],[4,4,4,4,4],[6,6,6,6,6]])
#data=np.array(list(f))
"""
a=data[0][:]
b=data[1][:]
dist = np.linalg.norm(a-b)
print(dist)
"""

count = 1 #繰り返し回数
num_cluster =2 #クラスタ数
daihyo=np.array([]) #代表ベクトルの配列
becs=[] #データの添字

for i in range(len(data)): #データの添字を取得
    becs.append(i)


#ここからアルゴリズム
choice = random.sample(becs,num_cluster) #ランダムにクラスタ数の数だけ要素を選択
print("First choice:",choice)

for j in choice:
    daihyo = np.append(daihyo,data[j],axis=0) #代表要素の行列を作成

daihyo=daihyo.reshape(num_cluster,data.shape[1]) #変形
#print(daihyo)
for i in range(count): #countの回数繰り返す
    cluster=[] #クラスターを初期化

    for i in range(num_cluster):
        cluster.append([]) #クラスターのリストを用意
    

    for num, bec in enumerate(data): #各データに処理
        a = bec #対象の要素a
        sim_dist=np.inf #最も近いクラスターへの距離（初期値無限）
        cluster_count = 0 #最も近いクラスターの添字
        for k,j in enumerate(daihyo):

            b = j #代表ベクトルb

            dist = np.linalg.norm(a-b) #a,bの距離を計算

            if(dist < sim_dist):#最近傍を更新 
                sim_dist = dist 
                cluster_count = k
    
        cluster[cluster_count].append(num) #対象の要素をクラスターに追加
    daihyo=np.array([])
    
    for c in cluster: #代表ベクトルを更新
        #print("c",c)
        sum = np.zeros(data.shape[1])
        for d in c:
            sum += data[d]
            #print("sum1:",sum)
        sum = sum/len(c)
        #print("sum2:",sum)
        daihyo = np.append(daihyo,sum,axis=0)
    daihyo=daihyo.reshape(num_cluster,data.shape[1])


print(cluster)