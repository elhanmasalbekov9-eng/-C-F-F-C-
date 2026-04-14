def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


f = float(input("Введите температуру в Фаренгейтах: "))
c = fahrenheit_to_celsius(f)

print("Температура в Цельсиях:", c)
