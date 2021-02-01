from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.options import Options 

group_name = input('Enter ur group: ')
week_num = int(input('Enter week num(2-18): ')) + 1

link = f'https://www.polessu.by/ruz/term2/?q={group_name}'
option = webdriver.ChromeOptions()
option.add_argument('headless')
browser = webdriver.Chrome(options=option)

browser.get(link)
browser.find_element_by_xpath('/html/body/section/div/div/div[2]/div/button').click()
browser.find_element_by_xpath(f'//*[@id="weeks-menu"]/li[{week_num}]/a').click()

with open('page.html', 'w') as f:
    f.write(browser.page_source)
