#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import system as s
from time import sleep as zz
import pyautogui as pg

# ------------
url="https://www.typer.io/"
# ------------


with webdriver.Chrome('required/chromedriver') as driver:
	driver.set_window_size(500,500)
	driver.get(url)
	s('clear')
	print(driver.title)
	while True:
		for i in range(20):
			main=driver.find_element(By.XPATH, f'//*[@id="word-0"]/span')
			print(f'word: { main.text}')
			for letter in main.text:
				pg.write(letter)
			pg.write(' ')
			print(main.text)
	zz(10)
