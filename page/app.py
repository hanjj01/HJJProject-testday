from appium import webdriver

from UITEST.page.base_page import BasePage
from UITEST.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = 'view.WelcomeActivityAlias'

    def start(self):
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'android'
            caps['devicesName'] = '127.0.0.1:7555'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noReset'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(5)
        return self

    def main(self) -> Main:  # 定义返回类型？？？？
        return Main(self._driver)
