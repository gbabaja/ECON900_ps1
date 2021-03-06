from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")


cdriver = "/Users/guncha/Documents/machine_learning/ECON900_ps1/chromedriver" #must include the proper path to the driver
driver = webdriver.Chrome(cdriver) #need driver for selenium to work.  Default is mozilla firefox

for i in range(1062):
	driver.get("https://boardgamegeek.com/browse/boardgame/page/" +str(i+1)) #launching the URL
	time.sleep(60) #give the page time to load (otherwise prices do not load properly)
	page = driver.page_source #get the html
	file_ = open("html_files/boardgamegeek_page_no_" + str(i+1)+".html", "w") #save the html files in the folder
	file_.write(page)
	file_.close()
	time.sleep(60)

driver.close()



