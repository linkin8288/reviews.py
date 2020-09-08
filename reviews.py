data = []
count = 0 # 計數器
with open('reviews.txt', 'r') as f: # 讀取txt檔案當作f
	for line in f: # 每次讀取都讀取一行，取名為line
		data.append(line) # 將每一行加入空data清單裡面
		# 新的清單放前面，append(line)
		count += 1 
		if count % 100000 == 0: # 每讀100000筆資料印出來，%是求餘數
			print(len(data))

print('檔案讀取玩了，總共有', len(data), '筆資料') # len()是讀取長度

# 找每筆留言的平均長度
# 每筆資料就叫做d
sum_len = 0 # 總留言長度 = 0
for d in data: # 將每筆資料一筆一筆叫出來
	sum_len = sum_len + len(d) # 將目前的長度加上資料的長度，再存回目前的長度
print('每筆留言的平均長度是', sum_len/len(data)) # 每筆留言的平均長度

# 查有幾筆留言長度小於100
new = [] # 新增空清單
for d in data: # 將每筆資料一筆一筆叫出來
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) #將第一筆長度小於100的資料印出來

# 找有good的留言
nice = []
for d in data:
	if 'nice' in d:
		nice.append(d) # 將此留言加入nice清單裡面
print('一共有', len(nice), '筆留言提到nice')
print(nice[0])
