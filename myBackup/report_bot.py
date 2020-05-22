import getpass
import selenium.common.exceptions as selenium_except
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class my_bot():
    def __init__(self):
        self.bin_browser = 'bin_driver/geckodriver.exe',
        self.url = 'https://mega.nz/'
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options, executable_path=self.bin_browser)

    def megaBot(self):
        def basic_auth():
            # send email
            browser.find_element_by_xpath('//*[@id="login-name"]').send_keys(input('Your e-mail:\n\t>> '))
            # send pass
            browser.find_element_by_xpath('//*[@id="login-password"]').send_keys(getpass.getpass('Your pass:\n\t>> '))
            # send login
            browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div[26]/div[2]/form/div[5]').click()
            return

        browser = self.driver
        #open the browser
        browser.get(self.url)
        #time to load the page
        browser.implicitly_wait(10)
        # #choose sign in
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div[17]/a[2]').click()
        basic_auth()
        print('Wait..')
        #time to load the page
        browser.implicitly_wait(15)
        try:
            browser.find_element_by_class_name('nw-tree-panel-header')
        except selenium_except.TimeoutException:
            print('printar log de erro')
        except selenium_except.NoSuchElementException:
            browser.save_screenshot('home.png')
            message = browser.find_element_by_class_name('top-login-pad login')
            print(message.parent)





        browser.save_screenshot('home.png')
        browser.quit()
        return

