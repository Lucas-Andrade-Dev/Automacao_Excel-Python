from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

for cont in range(1000):
 class Navegar:

    def __init__(self, meusite):
        
        self.meusite = meusite
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def pesquisar(self):   
        driver = self.driver
        driver.get('https://google.com/')
        time.sleep(5)
        pesquisar = driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']")
        pesquisar.clear()
        pesquisar.send_keys(self.meusite)
        time.sleep(5)
        pesquisar.send_keys(Keys.ENTER)
        time.sleep(3)
        clicar = driver.find_element(By.XPATH, "//a[@href='https://www.liftdetoxafl.com/']")
        clicar.click()
        time.sleep(5)
    
        time.sleep(5)
        trafegar = driver.find_element(By.XPATH, '//a[@href="#compra"]')
        trafegar.click()
        time.sleep(5)
        entrar = driver.find_element(By.XPATH, "//a[@href='https://app.monetizze.com.br/r/AXV21179106?u=c&pl=CY99176']")
        entrar.click()
        time.sleep(10)


lift = Navegar('liftdetoxafl')
lift.pesquisar()

#href="#compra"
#href="https://app.monetizze.com.br/r/AXV21179106?u=c&pl=CY99176"