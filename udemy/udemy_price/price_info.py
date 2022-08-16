from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def get_chrome_driver():
      chrome_options = webdriver.ChromeOptions()
      
      driver = webdriver.Chrome(
          service=Service(ChromeDriverManager().install()),
          options=chrome_options
      )
      return driver

url = "https://www.udemy.com/courses/development/web-development/?p=1"

driver = get_chrome_driver()
driver.get(url)

# driver.get(url)
# price_info_list = []

# def get_price_info(page):
#     driver = get_chrome_driver()
#     url = f"https://www.udemy.com/courses/development/web-development/?p={page}"
#     driver.get(url)
#     page_info = driver.find_elements( By.CSS_SELECTOR,
#                          "#udemy > div.main-content-wrapper > div.main-content > div > div > div:nth-child(8) > div.course-directory--container--5ZPhr > div.filter-container--container--3A8k6 > div.course-list--container--3zXPS")
    
#     for price_info in page_info:
#         price = price_info.find_element( By.CSS_SELECTOR, "#u155-popper-trigger--569 > div.course-card--main-content--2XqiY.course-card--has-price-text--1c0ze > div.price-text--container--103D9.course-card--price-text-container--XIYmk > div > span:nth-child(2) > span").text
#         price_info_list.append(price)
        
#     print(f"Crawling: {page}")
    
#     driver.quit()
    
# for page in range(1,3):
#     get_price_info(page)