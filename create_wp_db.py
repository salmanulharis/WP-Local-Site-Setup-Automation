from selenium.webdriver.common.by import By

class CreateWpDb():

	def __init__(self, driver):
		self.driver = driver

	def create_db(self, site_name):
		self.driver.get('http://localhost/phpMyAdmin5/index.php')
		self.driver.find_element(By.XPATH,"//body/div[@id='floating_menubar']/div[@id='topmenucontainer']/nav[1]/div[1]/ul[1]/li[1]/a[1]").click()
		if site_name:
			self.driver.find_element(By.ID,"text_create_db").send_keys(site_name)
			self.driver.find_element(By.ID,"buttonGo").click()
			# self.driver.quit()
			print("\nDatabase Successfully created.")
		else:
			self.driver.quit()
			print("\nError: No site name, please restart")