from page_object_pattern.locators.locators import SearchHomeLocators
import logging
import allure
from allure_commons.types import AttachmentType


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        # self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        # self.location_match_xpath = "//span[@class='select2-match']"
        # self.check_in_input_name = 'checkin'
        # self.check_out_input_name = 'checkout'
        # self.travellers_input_id = 'travellersInput'
        # self.adult_input_id = 'adultInput'
        # self.child_input_id = 'childInput'
        # self.search_button_xpath = "//button[text()=' Search']"

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(SearchHomeLocators.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(SearchHomeLocators.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(SearchHomeLocators.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="Set city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting data range from '{1}' to '{2}'")
    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} and {checkout} dates".format(checkin=check_in, checkout=check_out))
        self.driver.find_element_by_name(SearchHomeLocators.check_in_input_name).send_keys(check_in)
        self.driver.find_element_by_name(SearchHomeLocators.check_out_input_name).send_keys(check_out)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set data range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers adults- '{1}' and children- '{2}'")
    def set_travellers(self, adult, child):
        self.logger.info(
            "Setting travellers adults- {adults} and children- {kids} dates".format(adults=adult, kids=child))
        self.driver.find_element_by_id(SearchHomeLocators.travellers_input_id).click()
        self.driver.find_element_by_id(SearchHomeLocators.adult_input_id).clear()
        self.driver.find_element_by_id(SearchHomeLocators.adult_input_id).send_keys(adult)
        self.driver.find_element_by_id(SearchHomeLocators.child_input_id).clear()
        self.driver.find_element_by_id(SearchHomeLocators.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set  travellers", attachment_type=AttachmentType.PNG)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element_by_xpath(SearchHomeLocators.search_button_xpath).click()


'''
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
'''
