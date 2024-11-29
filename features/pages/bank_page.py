from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BankPage:

    def __init__(self, driver):
        self.driver = driver

    def select_option(self, option):
        option = self.driver.find_element(By.XPATH,f"//button[contains(text(),'{option}')]")
        option.click()

    def provide_value(self, field, value):
        self.driver.find_element(By.XPATH,f"//input[@placeholder='{field}']").send_keys(value)

    def click_button(self,button):
        option = self.driver.find_element(By.XPATH,f"//button[@type='submit' and contains(text(),'{button}')]")
        option.click()

    def select_dropdown_value(self,parameter,value):
        select_element = self.driver.find_element(By.XPATH,f"//label[contains(text(),'{parameter}')]/../select")
        select = Select(select_element)
        select.select_by_visible_text(value)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def get_transaction_message(self):
        message = self.driver.find_element(By.XPATH,"//span[@ng-show='message']").text
        return message



