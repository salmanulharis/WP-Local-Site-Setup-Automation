from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SetUpWP():

	def __init__(self, driver):
		self.driver = driver

	def setup_wp(self, site_name):
		driver = self.driver
		url = f"http://localhost/{site_name}/wp-admin/"
		driver.get(url)

		# select language
		select = Select(driver.find_element(By.ID,"language"))
		# select by visible text
		select.select_by_visible_text('English (United States)')
		# # select by value 
		# select.select_by_value('1')
		driver.find_element(By.ID,"language-continue").click()
		driver.find_element(By.XPATH,"//a[contains(text(),'Let’s go!')]").click()

		# set database logins
		driver.find_element(By.ID,"dbname").send_keys(site_name)
		driver.find_element(By.ID,"uname").send_keys("root")
		driver.find_element(By.ID,"pwd").send_keys("root")
		driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/p[2]/input[1]").click()
		driver.find_element(By.XPATH,"/html[1]/body[1]/p[3]/a[1]").click()

		# set site credentails
		driver.find_element(By.ID,"weblog_title").send_keys(site_name.capitalize())
		driver.find_element(By.ID,"user_login").send_keys("groot")
		driver.find_element(By.ID,"pass1").clear()
		driver.find_element(By.ID,"pass1").send_keys("password")
		driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[5]/td[1]/label[1]/input[1]").click()
		driver.find_element(By.ID,"admin_email").send_keys("salman@zennode.com")
		driver.find_element(By.ID,"submit").click()

		# ready to login
		driver.find_element(By.XPATH,"/html[1]/body[1]/p[3]/a[1]").click()

		# login
		driver.find_element(By.ID,"user_login").send_keys("groot")
		driver.find_element(By.ID,"user_pass").send_keys("password")
		driver.find_element(By.ID,"wp-submit").click()
		print(f"\nWordpress site is available in the below link \n{url}")

	def delete_all_plugin(self, site_name):
		driver = self.driver
		url = f"http://localhost/{site_name}/wp-admin/plugins.php"
		driver.get(url)

		#delete all plugins
		driver.find_element(By.ID,"cb-select-all-1").click()
		select = Select(driver.find_element(By.ID,'bulk-action-selector-top'))
		select.select_by_visible_text('Delete')
		driver.find_element(By.ID,"doaction").click()
		wait = WebDriverWait(driver, 10)
		alert = wait.until(EC.alert_is_present())
		alert.accept()

		# wait to delete
		time.sleep(5)

	def add_updraft(self, site_name):
		driver = self.driver
		url = f"http://localhost/{site_name}/wp-admin/plugin-install.php"
		driver.get(url)

		#search and install updraft
		driver.find_element(By.ID,"search-plugins").send_keys("UpdraftPlus WordPress Backup Plugin")
		wait = WebDriverWait(driver, 100)

		#click install button
		install_button = wait.until(EC.presence_of_element_located((By.XPATH, "//body/div[@id='wpwrap']/div[@id='wpcontent']/div[@id='wpbody']/div[@id='wpbody-content']/div[3]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]")))
		install_button.click()

		#wait for activate button
		activate_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "activate-now")))
		activate_button.click()

		# wait to activate
		time.sleep(5)

	def create_backup(self, site_name):
		driver = self.driver
		url = f"http://localhost/{site_name}/wp-admin/options-general.php?page=updraftplus"
		driver.get(url)

		#create backup
		driver.find_element(By.ID,"updraft-backupnow-button").click()
		driver.find_element(By.CLASS_NAME,"js-tour-backup-now-button").click()

		#wait for download buttons
		wait = WebDriverWait(driver, 100)
		activate_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "updraft_download_button")))





