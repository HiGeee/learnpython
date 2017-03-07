from random import randint
name = raw_input('请输入你的名字:')

f = open('D:\py_log\ddd.txt')
lines = f.readlines()
f.close()

scores ={} #初始化一个空字典
for l in lines:
    s =l.split() #把每一行的数据拆分成list
    scores[s[0]] = s[1:] #把第一项作为key，剩下的作为value
score =scores.get(name) #查找当前玩家的数据
if score is None:
    score=[0,0,0]#c初始化数据


game_times = int(score[0])
min_times  = int(score[1])
total_times = int(score[2])


if game_times >0:
    avg_times = float(total_times)/game_times
else:
    avg_times =0
print('你已经玩了%d次，最少%d轮猜出答案，平均%d轮猜出答案'%(game_times,min_times,avg_times))

num = randint(1, 100)
times = 0
print('Guess what I think?')
bingo  =False
while bingo == False :
    times +=1
    answer = int(input())
    if answer <num :
        print('too small!')
    if answer >num :
        print('too big!')
    if answer ==num :
        print('bingo')
        bingo = True

if game_times ==0 or times<min_times:
    min_times = times
total_times+=times 
game_times +=1


#吧成绩更新到对应的玩家数据
#加str转成字符串，为后面的格式化做准备
scores[name]=[str(game_times),str(min_times),str(total_times)]
result=''

for n in scores:
        line = n+''+''.join(str(scores[n])+'\n')
        result += line # 添加到result里去
f=open('D:\py_log\ddd.txt','w')
f.write(result)
f.close()
