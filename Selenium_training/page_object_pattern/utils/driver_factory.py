from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser =="chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start_maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
        raise Exception('Provider valid driver name')
