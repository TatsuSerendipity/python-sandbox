import random
# ０、１、２、３、４、５
# 青、赤、緑、黄。桃、白
#8ターン

list_true = [0,0,0,0]
list_ans = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#[0,1,2,1]
#[1,3,2,3]


for i in range(4):
    list_true[i] = str(int(random.random()*100//10%4))

for i in range(8):
    hit = 0
    blow = 0
    
    print(str(i+1) + "回目")
    for j in range(4):
        list_ans[i][j] = input(str(j + 1) + "つ目：")

    for j in range(4):
        for k in range(4):
            if list_ans[i][j] == list_true[k]:
                if j == k:
                    hit += 1
                else:
                    blow += 1
                break
        
    print(str(hit) + "ヒット")
    print(str(blow) + "ブロー")

for i in range(4):
    print(list_true[i])
