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
        names=[]
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
        names=self._unfollow(followers)
        print(names)
        
    
    def _get_names(self):
        names=[]
        sleep(1)
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

    def _unfollow(self,followers):
        num=0
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
        links = scroll_box.find_elements_by_class_name('uu6c_')
        for link in links:
            if num>=20:
                break
            name = link.find_elements_by_tag_name('a')
            lenght=len(name)
            for i in range(lenght):
                if name[i].text!='':
                    if name[i].text not in followers:
                        names.append(name[i].text)
                        num=num+1
                        button = link.find_element_by_tag_name('button')
                        button.click()
                        try:
                            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
                        except:
                           pass
                        sleep(1)
        #close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
        return names

my_bot = InstaBot('gym_fits1','Boavista192001')

my_bot.get_unfollowers()