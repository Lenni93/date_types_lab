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
# Explanation:
# In the above example, the key is 5. The program takes 3 lines of input, each containing
# a lowercase and uppercase letter. The key is then added to each character, resulting in the decrypted message 
