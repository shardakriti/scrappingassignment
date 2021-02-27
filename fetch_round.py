from selenium import webdriver
import os
import time
import sys
number=str(sys.argv[1])

PATH= 'C:\Program Files (x86)\chromedriver.exe'
driver=webdriver.Chrome(PATH)
alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
os.mkdir('./'+number)
for i in range(26):
    driver.get('https://codeforces.com/problemset/problem/'+number+'/'+alphabets[i])
    title = driver.find_element_by_class_name('title').text
    if title[0] == alphabets[i]:
        os.mkdir('./'+number+'/'+alphabets[i])
        problem = driver.find_element_by_class_name('problem-statement')
        time.sleep(1)
        y='./'+number+'/'+alphabets[i]+'/problem.png'
        problem.screenshot(y)
        inputs=driver.find_elements_by_class_name('input')
        for k in inputs:
            f= open('./'+number+'/'+alphabets[i]+'/input'+str(inputs.index(k)+1)+'.txt','x')
            print(k.find_element_by_tag_name('pre').text,file=f)
        outputs=driver.find_elements_by_class_name('output')
        for k in outputs:
            f= open('./'+number+'/'+alphabets[i]+'/output'+str(outputs.index(k)+1)+'.txt','x')
            print(k.find_element_by_tag_name('pre').text,file=f)
    else:
        driver.close()
        break
