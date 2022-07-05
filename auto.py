from selenium import webdriver
import random
from selenium.webdriver import ActionChains
import time

def selrun():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    #option.add_argument("--headless")
    #option.add_argument("disable-gpu")
    
    q1 = random.randint(0,4)
    q2 = random.randint(5,7)
    q3 = random.randint(8,10)
    q4 = random.randint(11,14)
    q5 = random.randint(15,17)
    q6 = random.randint(18,24)
    q7 = random.randint(25,29)
    q8 = random.randint(30,32)
    q9 = random.randint(33,36)
    q10 = random.randint(37,40)
    q11 = random.randint(41,44)
    q12 = random.randint(45,48)
    q13 = random.randint(49,51)
    q14 = random.randint(52,56)
    q15 = random.randint(57,60)
    q16 = random.randint(61,66)
    q17 = random.randint(67,71)
    q18 = random.randint(72,76)
    q19 = random.randint(77,81)
    q20 = random.randint(82,86)
    q21 = random.randint(87,88)
    q22 = random.randint(89,91) 

    textoptions = ["OTT is the best","OTT is easier to access","OTT can be watched from the comfort of the house","OTT is cheaper in longrun","I can watch movie whenever I want in OTT platforms","OTT is better","OTT subscription is all we need for all the movies"]
    a = random.randint(0,6)
    browser = webdriver.Chrome(executable_path="C:\\Users\\Ashwin\\Downloads\\chromedriver_win32\\chromedriver.exe", options=option)
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSdd1TK0q1ec7L3D-D46ruogCS-zpeN9BAMbQ0AUATJnUC_mYA/viewform')

    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
    radio_buttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")


    time.sleep(2)

    radio_buttons[q1].click()
    radio_buttons[q2].click()
    radio_buttons[q3].click()
    radio_buttons[q4].click()
    radio_buttons[q5].click()
    radio_buttons[q6].click()
    radio_buttons[q7].click()
    radio_buttons[q8].click()
    radio_buttons[q9].click()
    radio_buttons[q10].click()
    radio_buttons[q11].click()
    radio_buttons[q12].click()
    radio_buttons[q13].click()
    radio_buttons[q14].click()
    radio_buttons[q15].click()
    radio_buttons[q16].click()
    radio_buttons[q17].click()
    radio_buttons[q18].click()
    radio_buttons[q19].click()
    radio_buttons[q20].click()
    radio_buttons[q21].click()
    radio_buttons[q22].click()

    textboxes[0].send_keys("OTT")
    textboxes[1].send_keys(textoptions[a])



    submit = browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span")
    submit.click()
    time.sleep(3)
    browser.close()

for i in range(19):
    selrun()
