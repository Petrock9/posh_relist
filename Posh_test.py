import selenium
import winsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from tkinter import messagebox


options = Options()
# options.add_argument("user-data-dir=C:\\Users\\JC\\AppData\\Local\\Google\\Chrome\\User Data\\Profiwle 2")
driver = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver.exe", chrome_options=options)
# ## Login to Poshmark
try:
    driver.get("https://poshmark.com/login")

    user_name = driver.find_element_by_xpath('//*[@id="login_form_username_email"]')
    user_name.send_keys('pigsz')

    password = driver.find_element_by_xpath('//*[@id="login_form_password"]')
    password.send_keys('7E3yc6gr199248$')

    time.sleep(1)
    # time.sleep(60)

    login_button = driver.find_element_by_xpath('//*[@data-pa-name="login"]')
    login_button.click()

    time.sleep(5)
except:
    print('login error')

# ## Sharing

for i in range(1, 50):

    print(i)
    try:
        robot_if = driver.find_element_by_xpath('//*[@id="recaptcha-anchor-label"]/text()')
        print("test1")
        messagebox.showinfo("Robot!")
    except:
        driver.get("https://poshmark.com/closet/pigsz")
        elm = driver.find_element_by_tag_name("html")
        time.sleep(2)
        # ## Select Available items
        try:
            driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[2]/div/div/nav/div/div[9]/div/div[2]/ul/li[2]/div/label').click()
            time.sleep(2)
        except:
            print()

        try:
            for y in range(1, 2000):
                print(y)
                x = str(y)
                driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/section/div[2]/div[' + x + ']/div/div/div[3]/div[3]/i').click()
                time.sleep(1.1)
                driver.find_element_by_xpath('//*[@id="app"]/main/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[1]/a/div').click()
                time.sleep(1.9)
                elm.send_keys(Keys.DOWN)
                time.sleep(0.75)
                elm.send_keys(Keys.DOWN)
                time.sleep(0.25)
        except:
            print("oops")
            winsound.PlaySound('chaching.wav', winsound.SND_FILENAME)
        time.sleep(5)
