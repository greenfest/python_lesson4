# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.

with open("icecream_all.txt", "r") as f:
    allList = f.read().split(", ")

with open("icecream_stock.txt", "r") as f:
    stockList = f.read().split(", ")    

outOfStockList = []

for iceCream in allList:
    if iceCream not in stockList:
        outOfStockList.append(iceCream)

print(f"Закончилось: {outOfStockList}")