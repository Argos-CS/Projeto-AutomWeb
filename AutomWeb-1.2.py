# Funcionalidade:
 # Importação de bibliotecas e drivers
 # Portabilidade automática entre os SO Windows, Liniux e MAC
 # Suporte aos navegadores Mozilla Firefox, Google Chrome e Microsoft Edge
 # Detecção do navegador do SO e instalação automática dos drivers necessários
 # Pré definição de credenciais de acesso para páginas login
 # Pré definição de Lista infinita e flexível de links para páginas a serem visitadas
 # Acesso randomizado das páginas
 # Intervalo de tempo pré definido e randomizado entre cada acesso a nova página
 # Pré definição de horário limite
 # Fechamento automático

# Install:
 # Python 3.7.0
 # selenium==3.141.0
 # pytz==2021.1
 # webdriver_manager==3.4.2
 # urllib3==1.26.6

import os
from selenium import webdriver
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import random
import pytz  
from datetime import datetime

if os.name == 'nt':
  barra = '\\' 
else:
  barra = '/'

def converter_path(caminho):
  return caminho.replace('\\', barra)

drivers = [
    lambda: webdriver.Chrome(ChromeDriverManager().install()),
    lambda: webdriver.Firefox(GeckoDriverManager().install()),
    lambda: webdriver.Edge(EdgeChromiumDriverManager().install())
]

for driver_func in drivers:
    try:
        driver = driver_func()
        break
    except:
        continue
else:
    print("Nenhum navegador web compatível encontrado: Google Chrome, Mozilla Firefox ou Microsoft Edge.")
    exit()
    
def login(driver, username, password):
  driver.get(converter_path('https://moodle.densm.mar.mil.br/'))
  driver.find_element(By.ID, 'username').send_keys(username) 
  driver.find_element(By.ID, 'password').send_keys(password)
  driver.find_element(By.ID, 'loginbtn').click()

def acessa_links(driver, links):
  for link in links:
    driver.get(converter_path(link))
    time.sleep(10)
  
def main():

  username = '01.0673.97'
  password = 'Joao3.16'

  links = [
    converter_path('https://moodle.densm.mar.mil.br/mod/assign/view.php?id=63459'),
    converter_path('https://moodle.densm.mar.mil.br/mod/forum/view.php?id=63460'),
    converter_path('https://moodle.densm.mar.mil.br/mod/lesson/view.php?id=63461')
  ]

  login(driver, username, password)

  while True:
    
    random.shuffle(links)
    selected_links = links[:2]

    acessa_links(driver, selected_links)

    time.sleep(5*60)

    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    if now.time() > datetime(2350, 1, 1, 21, 40).time():
      break

  driver.quit()
  
if __name__ == '__main__':
  main()