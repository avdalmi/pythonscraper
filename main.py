from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.ah.nl/producten"

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

cookies = driver.find_element(By.ID, "accept-cookies")
cookies.click()

# driver.implicitly_wait(20)
# survey_button = driver.find_element(By.CLASS_NAME, "close-modal")
# survey_button.click()
button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, './/*[@id="closeModalBtn"]')))

button.click()

product_categories = driver.find_elements(By.CLASS_NAME,
                                          "product-category-overview_category__vqzcb")

for category in product_categories:
    category_title = category.find_element(By.XPATH,
                                           './/*[@id="start-of-content"]/div[1]/div/div/div/div[1]/div/div').text
    print(category_title)
# add more here dont forget .

# print(product_categories)

driver.quit()
