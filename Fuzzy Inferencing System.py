temperature = float(input("Enter temperature: "))

if temperature <= 20:
    cold = 1
    hot = 0
elif temperature >= 40:
    cold = 0
    hot = 1
else:
    cold = (40 - temperature) / 20
    hot = (temperature - 20) / 20

print("Cold membership:", round(cold, 2))
print("Hot membership:", round(hot, 2))

if hot > cold:
    print("Result: High temperature")
else:
    print("Result: Low temperature")
