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
    mc.postToChat("Let's "+str(num1)+" pyramid!!")

#　ピラミッドの作成
pos_x, pos_y, pos_z = map(int,mc.player.getPos()) # 現在位置の取得

mc.player.setPos(pos_x + 0.5, pos_y + num1 + 2, pos_z + 0.5)

for i in range(num1-1,-1,-1):
    mc.setBlocks(pos_x - i, pos_y + (num1 - i - 1), pos_z - i, pos_x + i, pos_y + (num1 - i - 1), pos_z + i, 1)