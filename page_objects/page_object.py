from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class PageObj:

    def __init__(self, link: str):
        if isinstance(link, str):
            self.link = link
        else:
            raise Exception(TypeError)


    def _driver(self):
        '''Prepear Silenium web-driver and return it.'''
        # service = Service(executable_path='/home/mephit/Downloads/')
        profile = FirefoxProfile()
        profile.set_preference('permissions.default.image', 2)
        profile.set_preference("javascript.enabled", False)
        options = Options()
        options.profile = profile
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        return webdriver.Firefox(options=options)#service=service


    def get_page(self):
        driver = self._driver()
        try:
            driver.get(self.link)
            page = driver.page_source
            return page
        except Exception:
            print("Driver can't get page!")
        finally:
            driver.quit()
