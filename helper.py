import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def check_auth(url,):
    driver=webdriver.Firefox()
    driver.get(url)
    ele=driver.find_elements(By.XPATH,'//input[@type="radio"]')
    for i in ele:
        i.click()
        time.sleep(2)
    return True

def check_display(url,exp_py=None,exp_java=None,exp_PHP=None,exp_js=None):
    driver=webdriver.Firefox()
    driver.get(url)
    if exp_py:
        e=driver.find_element(By.XPATH,'//input[@value="Python"]')

        return e.is_displayed()

    elif exp_java:
        e = driver.find_element(By.XPATH, '//input[@value="Java"]')

        return e.is_displayed()
    elif exp_PHP:
        e = driver.find_element(By.XPATH, '//input[@value="PHP"]')
        return e.is_displayed()

    elif exp_js:
        e = driver.find_element(By.XPATH, '//input[@value="NODEJS"]')
        return e.is_displayed()


def check_selected(url,exp_py=None,exp_java=None,exp_PHP=None,exp_js=None):
    driver = webdriver.Firefox()
    driver.get(url)
    if exp_py:
        e = driver.find_element(By.XPATH, '//input[@value="Python"]')
        e.click()
        return e.is_selected()

    elif exp_java:
        e = driver.find_element(By.XPATH, '//input[@value="Java"]')
        e.click()
        return e.is_selected()

    elif exp_PHP:
        e = driver.find_element(By.XPATH, '//input[@value="PHP"]')
        e.click()
        return e.is_selected()

    elif exp_js:
        e = driver.find_element(By.XPATH, '//input[@value="NODEJS"]')
        e.click()
        return e.is_selected()
    else:
        return False
