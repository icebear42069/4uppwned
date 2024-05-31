import time
import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By



class UndetectedChromeDriver:
    def __init__(self, username, password, **kwargs):
        init_driver = uc.Chrome(headless='new')

        if kwargs.get('random_agent', False):
            user_agent = uc.random
        else:
            user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         f'Chrome/{init_driver.capabilities["browserVersion"]} Safari/537.36'
        init_driver.close()

        chrome_options = ChromeOptions()
        chrome_options.add_argument(f'--user-agent={kwargs.get("user_agent", user_agent)}')

        if 'proxy_server_url' in kwargs:
            chrome_options.add_argument(f'--proxy-server={kwargs["proxy_server_url"]}')

        self.driver = uc.Chrome(headless=kwargs.get('headless', 'new'), options=chrome_options)
        self.username = username
        self.password = password

    def run(self):

        self.driver.get('https://foreupsoftware.com/')

        user_field = self.driver.find_element(By.ID, 'form_field_username')
        pass_field = self.driver.find_element(By.ID, 'form_field_password')

        time.sleep(10)


if __name__ == '__main__':
    UndetectedChromeDriver(headless=False)
