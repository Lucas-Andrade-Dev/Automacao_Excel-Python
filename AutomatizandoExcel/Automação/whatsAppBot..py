from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(40)

contatos = ['Coisas2.0','Amor']
mensagem = 'teste'

def buscar_contato(contatos):
   campo_pesquisa = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
   time.sleep(3)
   campo_pesquisa.click()
   campo_pesquisa.send_keys(contatos)
   campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH, '//div[contains(@class,"fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv")]')
    campo_mensagem.click()
    time.sleep(5)
    campo_mensagem.send_keys(mensagem)
    campo_mensagem.send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

#campo de pesquisa class="copyable-text selectable-text" fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv
#campo de mensagem class= fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv
#outro possivel campo de mensagem   selectable-text copyable-text