from selenium import webdriver
import time
import random

web = webdriver.Chrome()
web.get('https://forms.gle/nB4ushAZCivU3ND38')

# fname=["Ahmed","Mohamed","Youssef","Sayed","Amin","Emad","Ali","Abdelrahman",
#        "khaled","Saeed","Anwar","Sohaib","Abdallah","Magdi","Seif","Hossam",
#        'Salma','Nada','Hager','Aya','Nour','Amal','Anas','Soha','Khadiga',"Mostafa",
#        'Menna','Sarah','May','Hanin','Maryem','Eman',"Kareeman","Esraa","Mariam"]

fname=["Ahmed","Mohamed","Youssef","Sayed","Amin","Emad","Ali","Abdelrahman",
       "khaled","Saeed","Anwar","Sohaib","Abdallah","Magdi","Seif","Hossam",
       'Salma','Nada','Hager','Aya','Nour','Amal','Anas','Soha','Khadiga',"Mostafa",
       'Menna','Sarah','May','Hanin','Maryem','Eman',"Kareeman","Esraa","Mariam"]


lname=["Ahmed","Mohamed","Youssef","Sayed","Amin","Emad","Ali","Abdelrahman","khaled","Saeed","Anwar","Sohaib","Abdallah","Magdi","Seif","Hossam","Anas","Omar","El Sharkay","ghareeb","Hosney"]

while True:

    time.sleep(1)

    first = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first.send_keys(random.choice(fname))

    last = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    last.send_keys(random.choice(lname))


    ################################AGE##########################################
    Age=[]
    Age.append(web.find_element('xpath','//*[@id="i13"]/div[3]/div'))
    Age.append(web.find_element('xpath','//*[@id="i16"]/div[3]/div'))
    Age.append(web.find_element('xpath','//*[@id="i19"]/div[3]/div'))

    random.choice(Age).click()


    ################################Bank##########################################
    Bank=[]
    Bank.append(web.find_element('xpath','//*[@id="i26"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i29"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i32"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i35"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i38"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i41"]/div[3]/div'))
    Bank.append(web.find_element('xpath','//*[@id="i44"]/div[3]/div'))

    random.choice(Bank).click()


    ################################UX##########################################
    Ux=[]
    Ux.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'))
    Ux.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'))
    Ux.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'))
    Ux.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'))
    Ux.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'))

    random.choice(Ux).click()


    ################################HELP##########################################
    Help=[]
    Help.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'))
    Help.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'))
    Help.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'))
    Help.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'))
    Help.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'))

    random.choice(Help).click()


    ################################SECURITY##########################################
    Sec=[]
    Sec.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div'))
    Sec.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div'))
    Sec.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div'))
    Sec.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div'))
    Sec.append(web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div'))

    random.choice(Sec).click()


    ################################USE##########################################
    Use=[]
    Use.append(web.find_element('xpath','//*[@id="i63"]/div[3]/div'))
    Use.append(web.find_element('xpath','//*[@id="i66"]/div[3]/div'))
    Use.append(web.find_element('xpath','//*[@id="i69"]/div[3]/div'))

    random.choice(Use).click()

    ################################Submit##########################################
    Submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    Submit.click()

    ################################Submit##########################################
    time.sleep(1)
    ReSubmit = web.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    ReSubmit.click()




    pass


