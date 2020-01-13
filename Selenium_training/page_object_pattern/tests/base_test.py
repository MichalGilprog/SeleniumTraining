import pytest
from selenium import webdriver

from page_object_pattern.utils.driver_factory import DriverFactory


class BaseTest:

    @pytest.fixture()
    def setup(self):
        self.driver = DriverFactory.get_driver("firefox")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()