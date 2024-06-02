import time
import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import fake_useragent
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class UndetectedChromeDriver:
    def __init__(self, username, password, date, **kwargs):
        init_driver = uc.Chrome(headless='new')

        if kwargs.get('random_agent', False):
            user_agent = fake_useragent.UserAgent.random
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
        self.date = date

    def run(self):


    def login(self):
        self.driver.get('https://foreupsoftware.com/index.php/booking/19765/2431#teetimes')

        WebDriverWait(self.driver, 20)\
            .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/button[1]')))\
            .click()

        WebDriverWait(self.driver, 20) \
            .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="teetime-login"]/div/p[1]/button'))) \
            .click()

        WebDriverWait(self.driver, 20)\
            .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_email"]')))\
            .send_keys(self.username)

        WebDriverWait(self.driver, 20)\
            .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_password"]')))\
            .send_keys(self.password)

        WebDriverWait(self.driver, 20)\
            .until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login"]/div/div[3]/div/button[1]')))\
            .click()


if __name__ == '__main__':
    UndetectedChromeDriver('kahandaniel39@gmail.com', 'Dkgolfpass39$', ['2024-06-01', '2024-06-02', '2024-06-02'], headless=False).login()
