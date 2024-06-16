import random

alphabet = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password=''
password_value = int(input("Введите длинну пароля: "))


for i in range(password_value):
    key = random.choice(list(alphabet))
    password+=key
    
print(password)
# made by Alan
