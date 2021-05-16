'''
Resurese folosite:https://selenium-python.readthedocs.io/index.html
'''
#Am importat libraria Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Urmatoarele 2 linii de cod stocheaza variabile pentru username si parola.
username = input("Enter in your username: ")
password = input("Enter your password: ")

#Am stocat cararea catre driver-ul de la Chrome si am stocat-o inntr-o variabila.
driver = webdriver.Chrome("C:\\Users\\Catalin\\PycharmProjects\\poriectlp2\\chromedriver.exe")

#Am accesat campusul online.
driver.get("https://cv.upt.ro/")

#Am cautat dupa ID elementul username de pe campus si am introdus parola din variabila username.
username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)

#Am facut la fel si pentru parola.
password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

#Am cautat butonul de login dupa ID si dupa am folosit 'submit' pentru a da click.
login_button = driver.find_element_by_id("loginbtn")
login_button.submit()

#Am folosit folosit WebDriverWait ca programul sa astepte 10 secunde pana se incarca pagina.
#Si am localizat 'S2-L-ETCTI-IETCTI2-BUC-LP2' folosind LINK_TEXT si am folosit 'click'
try:
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.LINK_TEXT,'S2-L-ETCTI-IETCTI2-BUC-LP2'))
   )
   element.click()

#In caz ca 'S2-L-ETCTI-IETCTI2-BUC-LP2' nu este localizata.Chrome-ul se va inchide.
except:
    driver.quit()
