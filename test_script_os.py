import os


#Скрипт поиска пути объекта
CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)

print(os.path.abspath("test_script_open"))

current_file = os.path.abspath(__file__)
print(os.path.dirname(current_file))

TMP_DIR = os.path.join(CURRENT_DIR, "tmp")
print(TMP_DIR)