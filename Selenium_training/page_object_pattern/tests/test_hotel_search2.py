import pytest
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure

from page_object_pattern.tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestHotelSearch(BaseTest):

    @allure.title("This is title")
    @allure.description("Test description")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("15/02/2020", '15/03/2020')
        search_hotel_page.set_travellers('2', '2')
        search_hotel_page.perform_search()
        result_page = SearchResultsPage(self.driver)
        hotel_name = result_page.get_hotel_names()
        hotel_prices = result_page.get_hotel_prices()

        assert hotel_name[0] == 'Jumeirah Beach Hotel'
        assert hotel_name[1] == 'Oasis Beach Tower'
        assert hotel_name[2] == 'Rose Rayhaan Rotana'
        assert hotel_name[3] == 'Hyatt Regency Perth'

        assert hotel_prices[0] == '€20.24'
        assert hotel_prices[1] == '€46'
        assert hotel_prices[2] == '€73.60'
        assert hotel_prices[3] == '€138'




