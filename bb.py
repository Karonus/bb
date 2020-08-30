import os

port = input("Введите порт сервера (Пример: 8080) => ")

print()
print("Чтобы остановить, нажмите ctrl+z")

os.system("php -S localhost:"+port)
