from selenium import webdriver

driver = webdriver.PhantomJS('G:\\6th sem\\fun\\phantomjs.exe')
driver.get("https://stackoverflow.com/questions/28022764/python-and-how-to-get-text-from-selenium-element-webelement-object")
results = driver.find_elements_by_xpath('//div[@class="post-text"]')

print len(results)

for result in results:
    video = result.find_element_by_xpath('.//h3/div')
    title = video.get_attribute('title')
    url = video.get_attribute('href')
    print title
driver.quit()