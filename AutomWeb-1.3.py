import requests
from bs4 import BeautifulSoup
import time
import random

def login(session, username, password):
    # URL da página de login
    login_url = 'https://moodle.densm.mar.mil.br/login/index.php'
    
    # Dados do formulário de login
    login_data = {
        'username': username,
        'password': password
    }
    
    # Fazer login no site
    session.post(login_url, data=login_data)

def acessa_links(session, links):
    for link in links:
        response = session.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Aqui você pode analisar o conteúdo da página usando BeautifulSoup
        print(soup.prettify())
        
        time.sleep(10)

def main():
    # Iniciar uma sessão de requests
    session = requests.Session()

    username = '01.0673.97'
    password = 'Joao3.16'

    links = [
        'https://moodle.densm.mar.mil.br/mod/assign/view.php?id=63459',
        'https://moodle.densm.mar.mil.br/mod/forum/view.php?id=63460',
        'https://moodle.densm.mar.mil.br/mod/lesson/view.php?id=63461'
    ]

    login(session, username, password)

    while True:
        random.shuffle(links)
        selected_links = links[:2]

        acessa_links(session, selected_links)

        time.sleep(5*60)

if __name__ == '__main__':
  main()