from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import logging

logging.basicConfig(filename='E:/followers.txt', level=logging.INFO)

now = datetime.datetime.now()

file = open('E:\creds.txt', 'r')

for line in file:  # question #2
    creds = {}
    creds['username'] = line.split(' ')[0]
    creds['password'] = line.split(' ')[1]

browser = webdriver.Chrome()
browser.get("http://yahoo.com")
assert 'Yahoo' in browser.title


def yahoo_lookup():
    search_field = browser.find_element_by_xpath('//*[@id="uh-search-box"]')
    search_field.send_keys('Александр Солодуха твиттер')
    search_button = browser.find_element_by_xpath('//*[@id="uh-search-button"]')
    search_button.click()
    browser.implicitly_wait(3)


def yahoo_search_request():
    for _ in range(10):
        try:
            solodukha_page = browser.find_element_by_partial_link_text('@solodukha')
            solodukha_page.click()
            browser.switch_to_window(browser.window_handles[1]) #question #1
            break
        except:
            next_page_button = browser.find_element_by_class_name('next')
            next_page_button.click()
    else:
        browser.close()
        raise BaseException("search request not found")


def log_in():
    browser.implicitly_wait(3)
    login_window = browser.find_element_by_xpath('//*[@id="signin-dropdown"]')
    if not login_window.is_displayed():
        login = browser.find_element_by_xpath('//*[@id="signin-link"]')
        login.click()

    username = browser.find_element_by_css_selector('#signin-dropdown > div.signin-dialog-body > form > div.LoginForm-input.LoginForm-username > input')
    username.send_keys(creds['username'])
    password = browser.find_element_by_xpath('//*[@id="signin-dropdown"]/div[3]/form/div[2]/input')
    password.send_keys(creds['password'])
    password.send_keys(Keys.ENTER)


def get_followers_count():
    followers_count = browser.find_element(By.XPATH, '//*[@id="page-container"]/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[3]').text
    return followers_count

yahoo_lookup()
yahoo_search_request()
log_in()
get_followers_count()

logging.info('Time when last test was executed: {}. Browser name and version: {} {}. {} followers.'.format(now.strftime("%Y-%m-%d %H:%M"), browser.capabilities['browserName'], browser.capabilities['version'], get_followers_count()))

