def calculate(price, tax): # taxは%で入力
    total = price + (price * tax * 0.01)
    print(total)

# 1000円の買い物
calculate(1000, 10)
