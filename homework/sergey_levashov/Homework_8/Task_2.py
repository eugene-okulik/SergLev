def fibonacci_generator():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


gen = fibonacci_generator()

targets = [5, 200, 1000, 100000]
targets.sort()
results = {}

count = 1
target_index = 0

while target_index < len(targets):
    num = next(gen)
    if count == targets[target_index]:
        print(f"{count}-е число Фибоначчи: {num}")
        target_index += 1
    count += 1
