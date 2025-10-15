for i in range(17):
    print(f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}")

y = 50
x = 3

print(f"y/x = {y/x:.5f}")

width = 10
for num in range(12):
    print(f" {num:^{width}} {num**2:^{width}} {num**3:^{width}}" )

completion = 0.756
formatted = f"{completion:.4%}"
print(formatted)  # Виведе: '75.6%'
