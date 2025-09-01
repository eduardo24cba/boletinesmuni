from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

import time

firefox_options = Options()

#establecemos estas opciones para poder descargar pdf con el navegador firefox
#se establece 2 para poder expecificar la ruta
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.dir", "C:\\Users\\dizarate\\Downloads")
firefox_options.set_preference("browser.download.useDownloadDir", True)
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
firefox_options.set_preference("pdfjs.disabled", True)


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                           options=firefox_options)

#url
driver.get("https://boletinoficial.cba.gov.ar/")

#accedemos al contenido de la pagina 
content = driver.find_element(By.ID, "container_portada")

#accedemos a la seccion donde estan los boletines
publicaciones = content.find_element(By.CLASS_NAME, "left")

#accedemos a los boletines
boletines = publicaciones.find_elements(By.TAG_NAME, "ul")

for item in boletines:
    url = item.find_elements(By.TAG_NAME, "li")[1].find_element(By.TAG_NAME, "a").get_attribute("href")
    driver.execute_script('''window.open("%s","_blank");''' % url)
    time.sleep(4)# para que no se note tanto que es un boot jaja
