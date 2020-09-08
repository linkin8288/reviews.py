data = []
count = 0 # 計數器
with open('reviews.txt', 'r') as f: # 讀取txt檔案當作f
	for line in f: # 每次讀取都讀取一行，取名為line
		data.append(line) # 將每一行加入空data清單裡面
		# 新的清單放前面，append(line)
		count += 1 
		if count % 100000 == 0: # 每讀100000筆資料印出來，%是求餘數
			print(len(data))

print(len(data)) # 讀取長度
print(data[0]) # 將清單中的第一筆數據印出來-索引
print('---------------')
print(data[1])