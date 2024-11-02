def invest(amount, rate, year):
    rate = rate/100 + 1
    for i in range(1, year+1):
        amount*=rate
        print("year", f'{i}:', round(amount, 2))
invest(100, 5, 4)