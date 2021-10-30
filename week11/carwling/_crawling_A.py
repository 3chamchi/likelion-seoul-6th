from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver')
# MAC : '/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver'
# WIN : r'/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver'

driver.get('https://www.nate.com/')

issue_title = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/h4')
print(issue_title)
print(issue_title.text)

issue_title2 = driver.find_element_by_tag_name('h4')
print(issue_title2)
print(issue_title2.text)

# tag_h4_list = driver.find_elements_by_tag_name('h4')
# for tag_h4 in tag_h4_list:
#     print(tag_h4.text)

txt_rank_list = driver.find_elements_by_class_name('txt_rank')
for txt_rank in txt_rank_list:
    print(txt_rank.text)

# time.sleep(15)
# txt_rank_list = driver.find_elements_by_class_name('txt_rank')
# for txt_rank in txt_rank_list:
#     print(txt_rank.text)

# tag_news = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[4]/ul/li[2]/a')
# time.sleep(3)
# tag_news.click()

newsTxt_ul_1 = driver.find_element_by_id('newsTxt_ul_1')
print(newsTxt_ul_1.text)
print(type(newsTxt_ul_1))
print(newsTxt_ul_1.parent)

driver.close()


