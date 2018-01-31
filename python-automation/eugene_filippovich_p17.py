from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://yahoo.com")
assert 'Yahoo' in browser.title

def yahoo_lookup():
    #yahoo
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
            break
        except:
            next_page_button = browser.find_element_by_class_name('next')
            next_page_button.click()
    else:
        browser.close()
        raise BaseException ("search request not found")

def get_followers_count():
    folowers_count = browser.find_element_by_xpath('/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a')
    folowers_count.click()

yahoo_lookup()
yahoo_search_request()
browser.implicitly_wait(3)
get_followers_count()
