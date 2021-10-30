from selenium import webdriver

driver = webdriver.Chrome('/Users/won/Project/study/lieklion-seoul-6th/week11/chromedriver')
# 웹 브라우저를 제어하는 방식으로 크롤링을 하기 때문에 여기에 앞서 설치했던 크롬 웹드라이버를 driver 변수에 담아줍니다. 

driver.get('https://www.nate.com/')
# 그리고 driver에 띄워줄 페이지의 링크를 담아줍니다. 
issue_keyword = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]')
keyword_list = issue_keyword.find_elements_by_tag_name('li')
# titleEles = keyword_list.find_elements_by_css_selector(".txt_rank")

for keyword in keyword_list :
    print(keyword.text)

# driver.close()