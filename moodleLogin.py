from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
username1=str(sys.argv[1])
password1=str(sys.argv[2])
PATH= 'C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(PATH)
driver.get('https://moodle.iitd.ac.in/login/index.php')
username=driver.find_element_by_id('username')
username.send_keys(username1)
password=driver.find_element_by_id('password')
password.send_keys(password1)
text1=driver.find_element_by_id('login').text
import re
values=re.findall('\d+', text1)
if text1.count('first')==1:
    ans=values[0]
elif text1.count('second')==1:
    ans=values[1]
elif text1.count('add')==1:
    ans=int(values[0])+int(values[1])
elif text1.count('subtract')==1:
    ans=int(values[0])-int(values[1])
captcha=driver.find_element_by_id('valuepkg3')
captcha.send_keys(Keys.BACKSPACE)
captcha.send_keys(ans)
loginbutton=driver.find_element_by_id('loginbtn')
loginbutton.click()

time.sleep(1)
driver.close()