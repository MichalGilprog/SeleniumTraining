from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()
driver.find_element_by_xpath("//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element_by_xpath("//span[@class='select2-match']").click()
driver.find_element_by_name('checkin').send_keys('15/02/2020')
driver.find_element_by_name('checkout').send_keys('15/03/2020')
driver.find_element_by_id('travellersInput').click()
driver.find_element_by_id('adultInput').clear()
driver.find_element_by_id('adultInput').send_keys('4')
driver.find_element_by_id('childInput').clear()
driver.find_element_by_id('childInput').send_keys('4')
driver.find_element_by_xpath("//button[text()=' Search']").click()
# //h4[contains(@class,"list_title")]//b
hotels = driver.find_elements_by_xpath('//h4[contains(@class,"list_title")]//b')

hotel_name = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_name:
    print(name)

prices = driver.find_elements_by_xpath("//div[contains(@class, 'price_tab')]//b")
prices_values = [price.get_attribute("textContent") for price in prices]
for next_price in prices_values:
    print("cena to: " + next_price)


assert hotel_name[0] == 'Jumeirah Beach Hotel'
assert hotel_name[1] == 'Oasis Beach Tower'
assert hotel_name[2] == 'Rose Rayhaan Rotana'
assert hotel_name[3] == 'Hyatt Regency Perth'






