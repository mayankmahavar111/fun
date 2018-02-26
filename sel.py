import selenium.webdriver as webdriver



def query(key):

    url = 'https://www.startpage.com'
    browser=webdriver.PhantomJS('G:\\6th sem\\fun\\phantomjs.exe')
    #browser=webdriver.Firefox('C:/Program Files/Mozilla Firefox/firefox.exe')
    browser.get(url)
    search_box=browser.find_element_by_id("query")
    search_box.send_keys(key)
    search_box.submit()
    try:
       links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
    except:
       links=browser.find_elements_by_xpath("//h3//a")

    #print links
    results=[]
    for link in links:
       href = link.get_attribute("href")
       print href
       results.append(href)

    browser.close()
    return results


key=raw_input('Enter keyword to search : ')

query(key)
