from selenium import webdriver
from behave import fixture

url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

def before_scenario(context,driver):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get(url)


def after_scenario(context, driver):
    context.driver.quit()





