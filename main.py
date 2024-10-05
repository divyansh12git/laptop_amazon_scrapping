from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&ref=nb_sb_noss")
file=0
elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")
print(len(elems))
for elem in elems:
    d=elem.get_attribute("outerHTML")
    with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
        f.write(d)
    file+=1
# time.sleep(5)
driver.close()