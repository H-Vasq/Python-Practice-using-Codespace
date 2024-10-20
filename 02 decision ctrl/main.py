tot = 600
bought_sale = True
dis = 0

if tot >= 1000 or bought_sale:
    dis = 10

total = tot - tot*dis/100
print(tot*dis/100)
print(total)