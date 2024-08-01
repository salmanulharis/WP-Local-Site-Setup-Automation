from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

from create_wp_db import CreateWpDb
from check_wp_folder import CheckWPFolder
from setup_wp import SetUpWP

# name for the site
while True:
	print("Name should not contain space or special characters.")
	site_name = input("Enter the site name:")
	if not site_name.isalnum():
		print("Error: Name should not contain space or special characters.")
		continue
	elif site_name == 'exit':
		exit()
	else:
		break

need_backup = input("Did you need to create backup(y/n)?: ")

# create wordpress folder
check_folder = CheckWPFolder()
check_folder.check_folder(site_name)

# # initialise driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

# create database
create_db = CreateWpDb(driver)
create_db.create_db(site_name)

# setup wordpress site and backup
setup_wp = SetUpWP(driver)
setup_wp.setup_wp(site_name)
if need_backup == 'y':
	setup_wp.delete_all_plugin(site_name)
	setup_wp.add_updraft(site_name)
	setup_wp.create_backup(site_name)

# wait and quit
time.sleep(4)
driver.quit()
print("\nsuccess")