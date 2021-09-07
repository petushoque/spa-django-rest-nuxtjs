#Вам дан массив цен price, где price[i] цена на i+1 день.
#Вы хотите увеличить вашу выгоду выбрав один день чтобы купить акцию по выгодной цене и выбрать столько дней сколько возможно чтобы продать и купить заново для получения максимальной выгоды.
#Верните максимальную выгоду. Если вы не можете получить выгоду, то верните 0.
#Например дан массив цен [7,1,5,3,6,4]. Покупая на второй день по цене 1, вы можете выгодно продать акцию на 3 день по цене 5. Выгода 5 - 1 = 4. Затем еще раз купить на 4й день по цене 3 и продать по цене 6. Выгода 6 - 3 = 3. Итоговая выгода 4 + 3 = 7.

price = [int(i) for i in  input().split(',')]
print(price)

# создание отдельного списка, в котором все элементы списка расположены в убывающем порядке
profit = 0
price_sorted = []
for i in range(len(price)):
    price_sorted.append(price[i])
price_sorted.sort(reverse=True)

# если цена только падала, прибыли быть не могло
if price == price_sorted:
    print(0)


else:
    for i in range(1, len(price)):
        if price[i] - min(price[:i]) > profit:
            profit = price[i] - min(price[:i])

#print(price_sorted)
#print(price)
print('Profit: ', profit)