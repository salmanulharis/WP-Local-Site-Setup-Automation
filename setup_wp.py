from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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