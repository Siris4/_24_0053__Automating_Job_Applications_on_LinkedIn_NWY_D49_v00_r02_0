import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time

first_name = os.environ.get('first_name', 'first name not found')
last_name = os.environ.get('last_name', 'last name not found')
email = os.environ.get('email', 'email not found')
linkedin_password = os.environ.get('linkedin_password', 'linkedin password not found')
phone_number = os.environ.get('phone_number', 'phone number not found')
college_or_university_attended = os.environ.get('college_or_university_attended', 'college or university attended not found')
degree = os.environ.get('degree', 'degree not found')
linked_in_profile_url = os.environ.get('linked_in_profile_url', 'linked in profile url not found')
git_or_github_repo = os.environ.get('git_or_github_repo', 'git or github repo not found')

# constants:
linkedin_login_url = "https://www.linkedin.com/login"
filter_search_url = "https://www.linkedin.com/jobs/search/?currentJobId=3813109947&f_AL=true&f_E=2%2C3&f_JT=F%2CC&f_SB2=4&f_WT=2&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

def setup_chrome_driver_for_selenium():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(linkedin_login_url)
    return driver

driver = setup_chrome_driver_for_selenium()

linkedin_dictionary = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "linkedin_password": linkedin_password,
    "phone_number": phone_number,
    "college_or_university_attended": college_or_university_attended,
    "degree": degree,
    "linked_in_profile_url": linked_in_profile_url,
    "git_or_github_repo": git_or_github_repo
}

# -------------------------- beginning at the website ---------------------------#

time.sleep(2)

Email_or_phone_id = driver.find_element(By.ID, "username")
Email_or_phone_id.send_keys(linkedin_dictionary["email"])

Password_id = driver.find_element(By.ID, "password")
Password_id.send_keys(linkedin_dictionary["linkedin_password"] + Keys.ENTER)

# sign in button:
sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

time.sleep(2)

driver.get(filter_search_url)

# the easy apply button:
'''
<span class="artdeco-button__text">
    easy apply
</span>
'''

# close the browser
# driver.quit()