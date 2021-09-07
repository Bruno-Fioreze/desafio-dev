from  selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

browser.get("http://127.0.0.1:8000/")
browser.implicitly_wait(3)
browser.maximize_window()
elemento = browser.find_element(By.XPATH, "//*[@id='file']")
path = "/home/bruno/Área de Trabalho/bycoders/desafio-dev/CNAB.txt"
elemento.send_keys(path)
browser.implicitly_wait(3)
browser.quit()