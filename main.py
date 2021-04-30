from selenium import webdriver
import time

try:

    driver = webdriver.Chrome('D://Playground//Projects//Bomb//chromedriver.exe')
    driver.get('https://web.whatsapp.com/')
    print("\n\nScan QR Code with Whatsapp web")
    time.sleep(5)

    print("\nLog In Process Complete !")

    name = input("\nEnter Name (Exact name of Your Contact ): ")
    count = int(input("\nCount (How Many Time You want To send ): "))
    msg = input("\nMessage (Say Somthing ) : ")


    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msgbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

    print("\n Sending ....")
    for i in range(count):
        msgbox.send_keys(msg)
        send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
        send_button.click()
    
    print("\n Sending Complete!")
except Exception as e:
    print("ERROR !")
    pass

