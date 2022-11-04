from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.google.com.br/")

print(driver.current_url)
print(driver.title)
print(driver.capabilities['browserVersion'])


"""element = driver.find_element_by_name("q")
AttributeError: 'WebDriver' object has no attribute 'find_element_by_name' """

element = driver.find_element("name", "q")
element.click()
element.send_keys("PyJamas Conf")
element.submit()

sleep(3)

assert driver.title == "PyJamas conf - Buscar con Google"

driver.close()