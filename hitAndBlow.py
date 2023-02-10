import random
# ０、１、２、３、４、５
# 青、赤、緑、黄。桃、白
#8ターン

list_true = [0,0,0,0]
list_ans = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(4):
    list_true[i] = str(int(random.random()*100//10%4))

for i in range(8):
    hit = 0
    blow = 0
    
    list_ans[i][0] = input("1つ目：")
    list_ans[i][1] = input("2つ目：")
    list_ans[i][2] = input("3つ目：")
    list_ans[i][3] = input("4つ目：")

    for j in range(4):
        for k in range(4):
            if list_ans[i][j] == list_true[k]:
                if j == k:
                    hit += 1
                else:
                    blow += 1
        
    print(str(hit) + "ヒット")
    print(str(blow) + "ブロー")

for i in range(4):
    print(list_true[i])
