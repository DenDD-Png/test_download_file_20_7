import time

import requests
from selene import query
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from test_script_os import TMP_DIR
def test_file():

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR, #Вытащил из test_script_os
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    #Поиск url на странице
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))

    #Работа с API скачиваем файлик
    content = requests.get(url=download_url).content
    #Ключ "wb" записывает и передает
    #with это контекстный менеджер, который позволяет открывапть и работать с файлом
    with open("tmp/readme3.rst", "wb") as file:
        file.write(content)
    #Ключ "r" не обязателен, но написать можно, r значит читает
    with open("tmp/readme3.rst", "r") as file:
        file_content = file.read()
        assert "test_answer" in file_content



