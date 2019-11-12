from selenium import webdriver

class application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        # login
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_group_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # filling group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        # return groups page
        wd.find_element_by_link_text("groups").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
















