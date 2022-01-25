from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.keys import Keys

class TinderBot(): 
    def __init__(self): 
        self.driver = webdriver.Chrome()

    def hasXpath(self,xpath):
            try:
                self.driver.find_element_by_xpath(xpath)
                return True
            except:
                return False
    


    def login(self): 
        
        self.driver.get('https://tinder.com')
        sleep(2)
        cc= self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/button ') 
        cc.click()
        sleep(3)

        # way 1                  

        Gmail_bt = self.driver.find_element_by_xpath(' //*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        # way 2
        # Gmail_bt = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[1]/div/button') 
        Gmail_bt.click()
        #saving og window not pop up 
        
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"] ')
        email_in.send_keys('Add your own email')

        next_bt = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span ')
        next_bt.click()

        sleep(3)
        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input ')
        pw_in.send_keys(' add password to email') 

        next_bt2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span ')
        next_bt2.click() 

        sleep(5)

        self.driver.switch_to_window(base_window)
        
        sleep(1)
                                                
        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()

        sleep(2)

        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()

        sleep(3)

        passport_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button ')
        passport_popup.click()

        sleep(2)
        
    def like2(self):
        print("Test")           
        swipe_right = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body')
        swipe_right.send_keys(Keys.ARROW_RIGHT)
        sleep(0.5)
        esc = self.driver.find_element_by_xpath('//*[@id="Tinder"]/body') 
        esc.send_keys(Keys.ESCAPE)

    def dislike(self):
        swipe_left = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button ')
        swipe_left.click()

    def auto_swipe(self):
        
        while True: 
            sleep(1)
            self.like2()
            
# python -i Tinder_bot1.py
bot = TinderBot()
bot.login()
#bot.auto_swipe() 




   
        
 
#commands to run 
# python -i Tinder_bot1.py
# bot = TinderBot()
# bot.login()


 
