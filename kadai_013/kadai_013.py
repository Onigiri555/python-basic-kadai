def calculate(price, tax = 10): # taxは%で入力(デフォルトは10%)
    total = price + (price * tax * 0.01)
    return total

# 1000円の買い物
calculate(1000, 10)