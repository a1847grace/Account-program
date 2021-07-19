# 讀取檔案，使用strip刪除/n並使用Split作為逗點切割分句
# 使用continue直接進行下一回合迴圈
products =[]
with open ('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
		print (products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input ('請輸入商品價格')
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	products.append([name,price])
print(products)	

# 印出所有商品價格
for product in products:
	print(product[0], '的價格是：', product[1], '元')
print (products)


with open ('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')