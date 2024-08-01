# from selenium.webdriver.common.by import By
import os

class CheckWPFolder():

	# def __init__(self, driver):
	# 	self.driver = driver

	def check_folder(self, site_name):
		while True:
			print(f"\nDownload wordpress and put in 'Applications/MAMP/htdocs' and rename the wordpress folder as '{site_name}'.")
			created_wp = input("\nEnter 'y' after you finished :")
			if created_wp == 'y':
				# home_directory = os.path.expanduser( '~' )
				mamp_directory = '/Applications/MAMP/'
				path = os.path.join( mamp_directory, 'htdocs', site_name )
				if os.path.isdir(path):
					break
				else:
					print("\nFile not found.")
					continue
			elif(created_wp == 'exit'):
				exit()
		print("\nWordpress folder successfully created")