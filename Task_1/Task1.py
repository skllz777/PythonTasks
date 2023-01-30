# Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

sum = int(input("Enter three-digit number: "))
print(sum // 100 + (sum // 10) % 10 + sum % 10)