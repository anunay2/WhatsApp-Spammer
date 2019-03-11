from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string
import random
#Function to generate random text
def random_generator(size=75,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

driver=webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

#waiting time to scan the QR code
driver.implicitly_wait(60)

#Xpath of the text box is given
element=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input")

#Enter the friend's name.Write in correct spelling
element.send_keys("Enter Name Here ",Keys.RETURN)

#Xpath of the text box
spam=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")



#number of times you would like to send the random text
num=100
for i in range(num):
    spam.send_keys(random_generator(),Keys.RETURN)
    driver.implicitly_wait(120)




