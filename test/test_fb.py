from selenium import webdriver

class Base:
    def browser(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\DELL\PycharmProjects\pyselenium\Driver\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver
    def load_url(self,url):
        self.driver.get(url)
    def set_text(self,e,data):
        e.send_keys(data)
    def btn_click(self,e):
        e.click()
    def quit_browser(self):
        self.driver.quit()