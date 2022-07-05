from selenium import webdriver
import random 
import time

def autorun():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")

    #option.add_argument("--headless")
   #option.add_argument("disable-gpu")

    q1 = random.randint(0,4)

 

    web = webdriver.Chrome(executable_path="C:\\Users\\Ashwin\\Downloads\\chromedriver_win32\\chromedriver.exe", options=option)
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfRUOszn4dU5uLPHei-Mv14ujTHT0ODr7Uq7PyevEls7aXX2g/viewform')

    radio_buttons = web.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    submit = web.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span")
    time.sleep(1)

    radio_buttons[1].click()



    submit.click()
    time.sleep(3)
    web.close()

for i in range(2):
    autorun()