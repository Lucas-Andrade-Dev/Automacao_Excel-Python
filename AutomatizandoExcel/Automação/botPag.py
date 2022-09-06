from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

for cont in range(1000):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://liftdetoxafl.com/')
    time.sleep(5)
    clicar = driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-success btn-lg btn3d")]')
    clicar.click()
    time.sleep(3)
   
   


time.sleep(3)

#pesquisa no google input @class="gLFyf gsfi"
#meu site a @href="https://www.liftdetoxafl.com/"