import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

#main

def main():
# info 
    buyerFName = 'XXXXXX'
    buyerLName = 'XXXXXX'
    buyerMail = 'XXX@XXX.XXX'
    buyerTele = 'XXXXXXXXX'
    buyerAddress = 'XXXXX'
    buyerZIP = 'XXXXX'

#card info
    buyerCardNumber = 'XXXXXXXXXXXXXXX'
    buyerCardExpMonth = 'XX'
    buyerCardExpYear = 'XX'
    pin = 'XXX'
    
#####change url#####

#actual ps5 url:
    url =  'https://www.walmart.com/XXXXXX'
    #####################

#gecko path
    driver = webdriver.Firefox(executable_path='XXX/geckodriver')

#go to website
    driver.get(url)

    driver.implicitly_wait(1)

#wait for add to cart
    while(True):
        try:
            WebDriverWait(driver, 2.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.spin-button-children')))
#add to cart
            driver.find_element_by_css_selector('.spin-button-children').click()
            
            time.sleep(1.75)

#wait for checkout
            while(True):
                try:
                    WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.cart-pos-main-actions > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)')))
#checkout
                    driver.find_element_by_css_selector('.cart-pos-main-actions > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)').click()

                    time.sleep(3)
                    while(True):
                        try:
#wait for continue w/out acc button 
                            WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div.CXO_module_container > div > div > div > div > div.CXO_welcome-mat.ny-lite-wm-variation.borderless > div > div:nth-child(1) > div > section > section > div > button > span')))
#continue w/out account
                            driver.find_element_by_css_selector('body > div.js-content > div > div.checkout-wrapper > div > div.accordion-inner-wrapper > div.checkout-accordion > div > div > div > div.CXO_module_container > div > div > div > div > div.CXO_welcome-mat.ny-lite-wm-variation.borderless > div > div:nth-child(1) > div > section > section > div > button > span').click()
    
                     
#w8 for continue button 
                            WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.cxo-continue-btn > span:nth-child(1)')))
#continue again
                            time.sleep(1)
                            driver.find_element_by_css_selector('.cxo-continue-btn > span:nth-child(1)').click()


#Check Out Page Fill

#wait for page          
       
                            WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]')))
    
#fill out page
                            name1=driver.find_element_by_xpath('//*[@id="firstName"]')
                            name1.send_keys(buyerFName)

                            time.sleep(.25)

                            name2=driver.find_element_by_xpath('//*[@id="lastName"]')
                            name2.send_keys(buyerLName)

                            phone=driver.find_element_by_xpath('//*[@id="phone"]')
                            phone.send_keys(buyerTele)

                            time.sleep(.25)

                            email=driver.find_element_by_xpath('//*[@id="email"]')
                            email.send_keys(buyerMail)
    
                            ord_adress=driver.find_element_by_xpath('//*[@id="addressLineOne"]')
                            ord_adress.send_keys(buyerAddress)

                            time.sleep(.15)
                            ord_city=driver.find_element_by_xpath('//*[@id="city"]')
                            ord_city.clear()
                            ord_city=driver.find_element_by_xpath('//*[@id="city"]')
                            ord_city.send_keys('Chicago')

                            ord_zip=driver.find_element_by_xpath('//*[@id="postalCode"]')
                            ord_zip.clear()
                            ord_zip=driver.find_element_by_xpath('//*[@id="postalCode"]')
                            ord_zip.send_keys(buyerZIP)

                            time.sleep(3)
                            Select(driver.find_element_by_css_selector('#state')).select_by_visible_text('Illinois')
                        

#continue again
                            time.sleep(1.25)
                            driver.find_element_by_css_selector("div.arrange-fill:nth-child(2) > button:nth-child(1) > span:nth-child(1)").click()
                            time.sleep(.25)

#wait for cc page 
                               
                            WebDriverWait(driver, 85).until(EC.presence_of_element_located((By.XPATH, '//*[@id="creditCard"]')))
    
#enter cc
                            ord_cnb=driver.find_element_by_xpath('//*[@id="creditCard"]')
                            ord_cnb.send_keys(buyerCardNumber)
    
                            Select(driver.find_element_by_css_selector('#month-chooser')).select_by_visible_text(buyerCardExpMonth)
                            Select(driver.find_element_by_css_selector('#year-chooser')).select_by_visible_text(buyerCardExpYear)

                            cvv=driver.find_element_by_name('cvv')
                            cvv.send_keys(pin)

#review order
                            time.sleep(1.35)
                            driver.find_element_by_css_selector(".spin-button > span:nth-child(1)").click()
   
#place order ; uncomment these 2 lines:
                            time.sleep(1.25)
                            WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.accordion-footer:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)')))
                            driver.find_element_by_css_selector("div.accordion-footer:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)").click()
                 
                            print("checked out.")
  
                                 
                       
                        except:
                            print("waiting for button, refreshing in 2 seconds")
                            driver.implicitly_wait(2.15)
                            driver.refresh()
                            continue
                except:
                    print("waiting for continue button, refreshing in 2 seconds")
                    driver.implicitly_wait(2.15)
                    driver.refresh()
                    continue
        except:
            print("waiting for add to cart button, refreshing in 2 seconds")
            driver.implicitly_wait(2.15)
            driver.refresh()
            continue


if __name__ == "__main__":
        main()
 

# 
