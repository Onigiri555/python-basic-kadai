def calculate(price, tax): # taxは%で入力
    total = price + (price * tax * 0.01)
    return total

# 1000円の商品
print(f"{calculate(1000, 10)}円")
