from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleHomePage():

    def __init__(self, app):
        self.driver = app.driver

    def getHomePageItens(self):
        self.SEARCH_INPUT = self.driver.find_element(By.CSS_SELECTOR, 
        "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")   
   
    def goToGoogleSearchPage(self):
        self.driver.get("https://www.google.ro/")
        time.sleep(3)
        self.getHomePageItens()
        SEARCH_BUTTON = self.driver.find_element(By.CSS_SELECTOR, 'input[value="Căutare Google"]')
        value = SEARCH_BUTTON.get_attribute('value')
        
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://consent.google.com']")))
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='introAgreeButton']"))).click() 
        return "Căutare Google" in value


    def putTextOnSearchInput(self, text):
        self.SEARCH_INPUT.send_keys(text)

    def pressEnterToSearch(self):
        self.SEARCH_INPUT.send_keys(Keys.RETURN)
        
    def seeResults(self, txtResult):
        return txtResult in self.driver.page_source 
        