def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


c = float(input("Введите температуру в Цельсиях: "))
f = celsius_to_fahrenheit(c)

print("Температура в Фаренгейтах:", f)
