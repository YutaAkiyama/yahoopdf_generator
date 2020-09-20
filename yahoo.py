from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
import json
import sys
 
username= "***"
password="***"

def main():

    driver.get('https://login.yahoo.co.jp/config/login?.src=auc&.done=https%3A%2F%2Fauctions.yahoo.co.jp%2F' ) 
 
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("btnNext").click()
    time.sleep(1)
    driver.find_element_by_id("passwd").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
    # driver.find_element_by_id("js-prMdl-close").click()
    time.sleep(10)
    driver.find_element_by_class_name("Close-mDrpk").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[1]/a').click()
    time.sleep(1)

    
    
    while True:
      try:
         if len(driver.find_elements_by_xpath("//img[@src='https://s.yimg.jp/images/auct/template/ui/search/arrow_next.gif']")) > -1:
                print("start PDF")
                item_list= []
                for item in driver.find_elements_by_css_selector('p.decTxt01'):
                    try:
                        link = item.find_element_by_tag_name("a").get_attribute("href")
                    except:
                        link = "skip"    
                    item_list.append(link)

                for link in item_list:
                    try:
                            driver.get(link)
                            time.sleep(2)
                            driver.find_element_by_class_name('decIcoArw').click()
                            time.sleep(2)
                            driver.execute_script('return window.print()')
                            driver.back()
                    except :
                            print("None")
                btn = driver.find_element_by_link_text("次の50件").get_attribute("href")
                print(btn)
                print("next url:{}".format(btn))
                driver.get(btn)
                print("Next page")

      except:
            sys.exit()

chopt=webdriver.ChromeOptions()
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account":""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

prefs = {'printing.print_preview_sticky_settings.appState': 
json.dumps(appState)}
chopt.add_experimental_option('prefs', prefs)
chopt.add_argument('--kiosk-printing')
driver = webdriver.Chrome(executable_path='***',options=chopt)




if __name__ == '__main__':
    main()
   