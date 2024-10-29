from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
opts = ChromeOptions()

opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get(r"https://pichau.com.br")
navegador = webdriver.Chrome(options = opts)
