from selenium import webdriver
import time


driver = webdriver.Chrome()

url="https://forms.gle/nB4ushAZCivU3ND38"

driver.get(url)

def fillform(fname,lname,age):
    inputs = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # radiobuttons = driver.find_element('xpath','//*[@id="i13"]/div[3]/div/div')

    inputs_arr=[
        fname, lname
    ]
    for i in range(2):
        inputs[i].clear()
        inputs[i].send_keys(inputs_arr[i])

    # for rad in radiobuttons:
    #     if rad.get_attribute("data-value").lower()==age:
    #         rad.click()



while(True):
    time.sleep(2)
    fillform("youss","haa","20")

#     fname = "youssef"
#     lname = "sayed"
#     name = driver.find_element('xpath',
#                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     name.send_keys(fname)
    pass



""",gender,best,ux,ava,help,ope,sec,use"""
