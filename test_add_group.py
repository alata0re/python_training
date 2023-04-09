from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestTraining(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'env\Lib\site-packages\selenium\webdriver\chrome')
        self.wd.implicitly_wait(60)

    def test_training(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)
        WebDriverWait(self.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))
        wd.find_element(By.LINK_TEXT, "groups").click()
        WebDriverWait(self.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))
        wd.find_element(By.NAME, "new").click()
        WebDriverWait(self.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys("new_group")
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("poslednyaya nervnaya kletka")
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys("good bay")
        wd.find_element(By.NAME, "submit").click()
        WebDriverWait(self.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))
        wd.find_element(By.LINK_TEXT, "group page").click()
        WebDriverWait(self.wd, 5).until(ec.visibility_of_element_located((By.ID, "footer")))
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
