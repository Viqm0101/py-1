n = int(input('Введите секунды'))
if n > 60:
    s = n // 3600
    l = n // 60 % 60
    g = n %60

    print(f"равно ч: {s}, м: {l}, с: {g}")