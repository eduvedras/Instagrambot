from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get('https://instagram.com')
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name = \"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name = \"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[@href='/{}/']".format(self.username)).click()
        sleep(2)
        #self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        #sleep(2)
        #following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        sleep(2)
        following = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    
    def _get_names(self):
        names=[]
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        for name in links:
            if name.text != '':
                names.append(name.text)
        #close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names
my_bot = InstaBot('wholesome_art1','mariana52008')

my_bot.get_unfollowers()