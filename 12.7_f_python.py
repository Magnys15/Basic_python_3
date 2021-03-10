money = int(input("Сколько денег: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

tkb = int(money*0.01*per_cent['ТКБ'])
ckb = int(money*0.01*per_cent['СКБ'])
vtb = int(money*0.01*per_cent['ВТБ'])
sber = int(money*0.01*per_cent['СБЕР'])

deposit = [tkb, ckb, vtb, sber]
deposit_max = max(deposit)
print('Максимальная сумма, которую вы можете заработать: ', deposit_max)
