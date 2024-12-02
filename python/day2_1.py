#!/bin/python
f = open("input2_1", "r").read()

lines = f.split("\n")
lines.pop(len(lines)-1)

num_of_safe:int = 0

for line in lines: 
    numbers = list(map(int, line.split()));
    if all(numbers[i] < numbers[i + 1] if abs(numbers[i] - numbers[i + 1]) >= 1 and abs(numbers[i] - numbers[i + 1]) <= 3 else False for i in range(len(numbers) - 1)) or all(numbers[i] > numbers[i + 1] if abs(numbers[i] - numbers[i + 1]) >= 1 and abs(numbers[i] - numbers[i + 1]) <= 3 else False for i in range(len(numbers) - 1)):
        num_of_safe+=1

print(num_of_safe)
