import pyautogui
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
import pandas as pd

pyautogui.PAUSE = 2

driver = webdriver.Firefox()
# DOLAR
driver.get("https://www.google.com.br/")
pyautogui.write("Cotacao do dolar")
pyautogui.hotkey("Enter")
cotacao_dolar = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# EURO
driver.get("https://www.google.com.br/")
pyautogui.write("Cotacao do Euro")
pyautogui.hotkey("Enter")
cotacao_euro = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# BITCOIN
driver.get("https://www.google.com.br/")
pyautogui.write("cotacao do BitCoin")
pyautogui.hotkey("Enter")
cotacao_bitcoin = driver.find_element(By.XPATH, '//*[@id="crypto-updatable_2"]/div/div[5]/div[2]/input').get_attribute("value")
print(cotacao_bitcoin)

# CLOSE
driver.close()

# TABELA

tabela = {
    'Cotação': ["Euro","BitCoin","Dolar"],
    'Conversão': [cotacao_euro, cotacao_bitcoin, cotacao_dolar]
}

df = pd.DataFrame(tabela)
print(df)
df.to_excel(r"Tabela.xlsx",index=False)