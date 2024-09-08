total = 10
while total in range (100):
  total += 10
  print(total)


amount = 1000
rate = 0.05

for year in range (1,11):
  amount = amount + (amount * rate)
  print(year,"and",amount)
  