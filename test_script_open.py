#Скрипт создает файл Hello и записывает в этот файл запись Hello word
#Повторный вызов скрипта перезапишет файл
def test_script_open():
    with open("Hello", "w") as file:
        file.write("Hello word")

#Скрипт добавляет в файл Hello запись Hello word в конец файла
def test_script_open():
    with open("Hello", "a") as file:
        file.write("Hello word")

#Скрипт переносит строку с помощью \n
def test_script_open():
    with open("Hello", "a") as file:
        file.write("Hello word\n")

#Запрет на перезапись файла
def test_script_open():
    with open("Hello", "x") as file:
        file.write("Hello word\n")