import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')


input("Escanea el código QR y presiona Enter una vez autenticado en WhatsApp...")


contacto ="Mi Num"  

mensaje = "Hola desde el Bot    "  # Mensaje a enviar

wait = WebDriverWait(driver, 20)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
search_box.send_keys(contacto)
search_box.send_keys(Keys.ENTER)

# Esperar a que se abra el chat
chat_xpath = f'//span[@title="{contacto}"]'
chat = wait.until(EC.presence_of_element_located((By.XPATH, chat_xpath)))
chat.click()

# Encontrar el cuadro de texto para el mensaje e ingresar el texto
input_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, input_box_xpath)))
input_box.send_keys(mensaje + Keys.ENTER)

# Esperar un tiempo para que el mensaje se envíe
time.sleep(5)

# Cerrar el navegador
driver.quit()
