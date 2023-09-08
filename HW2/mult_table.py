def multiplication_table(n):
    for i in range(1, n+1):
        print(f"Умножение на {i}:")
        for j in range(1, n+1):
            print(f"{i} * {j} = {i * j}")
        #print("\n")

n = int(input("Введите число n: "))
multiplication_table(n)