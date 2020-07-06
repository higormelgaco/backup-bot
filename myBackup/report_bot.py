import getpass, platform, logging, time, zipfile, os
import selenium.common.exceptions as selenium_except
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

class my_bot():
    def __init__(self):
        self.win_browser = 'bin_driver/geckodriver.exe'
        self.unix_browser = 'bin_driver/geckodriver'
        self.url = 'https://mega.nz/'
        self.options = Options()
        self.options.headless = True

    def file_prepare(self, path_target):
        compact_file = str(input('\t[+] - Insert the zip name:\n\t\t>> '))
        my_zip = zipfile.ZipFile(compact_file, 'w')
        path = os.listdir(path_target)
        print('\t[+] - Compacting target...')
        for item in range(len(path)):
            my_zip.write(path[item], compress_type=zipfile.ZIP_DEFLATED)
            time.sleep(1)
            print(f'\t\t[{item}] - {path[item]} ok')
        my_zip.close()
        print(f'\t[+] - Compactation successfully!\n\t\t[1] - Name: {compact_file}\n\t\t[2] - Path: {os.path.abspath(compact_file)}')

    def megaBot(self):
        def basic_auth():
            # send email
            browser.find_element_by_xpath('//*[@id="login-name"]').send_keys(input('\t[+] - Your e-mail:\n\t\t>> '))
            # send pass
            browser.find_element_by_xpath('//*[@id="login-password"]').send_keys(getpass.getpass('\t[+] - Your pass:\n\t\t>> '))
            # send login
            browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div[26]/div[2]/form/div[5]').click()
            return

        def check_bin():
            if platform.system() == 'Linux':
                return 'Linux',webdriver.Firefox(options=self.options, executable_path=self.unix_browser)
            elif platform.system() == 'Windows':
                return 'Windows',webdriver.Firefox(options=self.options, executable_path=self.win_browser)
            else:
                return '','Not found'

        def upload(file):
            browser.find_element_by_xpath('/html/body/div[7]/div[4]/div[2]/div[6]/div[7]/div[1]/div[2]/input').send_keys(file)
            print('\t[+] - Uploading file...')
            time.sleep(3)
            print('\t[+] - Upload status:',end=' ')
            progress = browser.find_element_by_xpath('/html/body/div[7]/div[4]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]').text
            while progress != '100%':
                progress = browser.find_element_by_xpath('/html/body/div[7]/div[4]/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]').text
            print(progress)
            time.sleep(3)
            browser.save_screenshot('upload-evidence.png')
            return

        print('\n\t[+] - Checking operational system: ',end='')
        syst,browser = check_bin()
        if browser == 'Not found':
            return logging.error("[*] - ERROR: Operational system incompatible")
        print(syst)

        #open the browser
        print('\t[+] - Starting Firefox')
        browser.get(self.url)
        print('\t[+] - Opening Mega')
        #time to load the page
        browser.implicitly_wait(10)
        # #choose sign in
        browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[1]/div[1]/div/div[17]/a[2]').click()
        basic_auth()
        print('\t[+] - Authenticating...')
        #time to load the page
        browser.implicitly_wait(15)

        try:
            browser.find_element_by_class_name('nw-tree-panel-header')
        except selenium_except.TimeoutException:
            logging.error('[*] - Timeout error. Check your connection and try again later.')
        except selenium_except.NoSuchElementException:
            browser.save_screenshot('home.png')
            message = browser.find_element_by_class_name('top-login-pad login')
            logging.info(message.parent)

        print('\t[+] - Loading page...')
        time.sleep(10)

        try:
            target = str(input('\t[+] - Insert the absolute path of file or directory that you want save in Mega:\n\t\t>> '))
            if os.path.isdir(target) == True:
                file_upld = my_bot.file_prepare(self, target)
                upload(file_upld)
            else:
                upload(target)
        except Exception as error:
            browser.quit()
            return error

        browser.quit()
        return print('\t[+] - End of operations')


