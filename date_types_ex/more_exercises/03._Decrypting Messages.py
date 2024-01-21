# key = int(input())
# print(*[chr(ord(input()) + key) for _ in range(int(input()))], sep ="")

key = int(input())
n = int(input())

message = ""
for _ in range(n):
    line = input().split()
    for letter in line:
        decrypted_letter = chr(ord(letter) + key)
        message += decrypted_letter

print(message)
