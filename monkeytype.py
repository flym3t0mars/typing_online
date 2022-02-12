#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import system as s
from time import sleep as zz
import pyautogui as pg

# search=input("Search: ")
# print('just a moment. .. ...')

# ------------

url="https://www.monkeytype.com"
# driver=webdriver.Chrome('required/chromedriver')
# driver.set_window_size(500,500)
# driver.get(url)

# ------------


with webdriver.Chrome('required/chromedriver') as driver:
	driver.set_window_size(500,500)
	driver.get(url)
	s('clear')
	print(driver.title)
	while True:
		for i in range(20):
			main=driver.find_element(By.XPATH, f'//*[@id="words"]/div[{(i+1)}]')
			print(f'word: { main.text}')
			for letter in main.text:
				pg.write(letter)
			pg.write(' ')
			print(main.text)
	zz(10)
