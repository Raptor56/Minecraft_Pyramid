import sys
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Let's create!!!") #さぁ、つくるよ！

num1 = input("何段ピラミッド？(最大32段): ")
num1 = int(num1)

if num1>32:
    mc.postToChat("No,create.")
    sys.exit()
   
else:
    mc.postToChat("Let's"+str(num1)+"pyramid!!")

num2 = num1 + 1

lList = [0 for l in range(num2)] #とりあえず枠つくっといて
   
n = 0
for k in range(num1+1):
    L = k + n - 1
    lList[k] = L
    k = k + 1
    n = n + 1

lList=lList[1:num1+1]
lList.reverse()

#　ピラミッドの作成
pos_x, pos_y, pos_z = mc.player.getPos() # 現在位置の取得

for i in range(num1):
    l = lList[i]
    mc.setBlocks(pos_x, pos_y, pos_z, pos_x + l - 1, pos_y, pos_z +l - 1, 1)
    pos_x = pos_x + 1
    pos_y = pos_y + 1
    pos_z = pos_z + 1