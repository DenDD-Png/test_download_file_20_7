import time
from selene import query
import os
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.abspath("tmp"),
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
browser.config.driver = driver

browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
dowmload_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
time.sleep(6)

with open("tmp/readme2.rst") as file:
    file_content_str = file.read()
    assert "test_answer" in file_content_str
