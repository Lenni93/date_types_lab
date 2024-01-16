n = int(input())

for num in range(1, n + 1):
    sum_digit = 0
    digits = num
    while digits > 0:
        sum_digit += digits % 10
        digits = int(digits / 10)
    if (sum_digit == 5) or (sum_digit == 7) or (sum_digit == 11):
        print(f'{num} -> True')
    else:
        print(f"{num} -> False")
# Iterate from 1 to n (we write n+1 because the for loop in Python iterates from 1 to n-1 by default):
# · To calculate the sum of digits of given number num, you might repeat the following:
# sum the last digit (num % 10) and remove it (sum = sum / 10) until num reaches 0.