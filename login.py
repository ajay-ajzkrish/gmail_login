from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

usernameStr = 'yourGmailidHere'
passwordStr = 'yourPasswordHere'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))


# fill in username and hit the next button
username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

time.sleep(2)

# wait for transition then continue to fill items
password = browser.find_element_by_name('password')
password.send_keys(passwordStr)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
