from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver')
# win = r'/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver.exe'

driver.get('https://www.nate.com/')

issue_title = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/h4')
print(issue_title)
print(issue_title.text)

img = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/ul[1]/li[1]/a/span[1]')
print(img)
print(img.text)

txt_rank_list = driver.find_elements_by_class_name('txt_rank')
for txt_rank in txt_rank_list:
    print(txt_rank.text)

# time.sleep(10)

# txt_rank_list = driver.find_elements_by_class_name('txt_rank')
# for txt_rank in txt_rank_list:
#     print(txt_rank.text)

h4_tag = driver.find_element_by_tag_name('h4')
print(h4_tag.text)

# h4_tag_list = driver.find_elements_by_tag_name('h4')
# for h4_tag in h4_tag_list:
#     print(h4_tag.text)

news_btn = driver.find_element_by_class_name('news')
news_btn.click()

# driver.close()