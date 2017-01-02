# You must clear every notification before Running this Script 
 
# Import What We need 
from selenium import webdriver
import time
 
# The driver to control Chrome Browser 
driver = webdriver.Chrome('/home/sandeep/Downloads/chromedriver')
 
# Open LinkedIn 
driver.get('https://www.linkedin.com/')
 
# Load and WAIT for 3 seconds 
time.sleep(3)
 
# Find the email or username input  
email = driver.find_element_by_id("login-email")
 
# Find password input 
password = driver.find_element_by_id("login-password")
 
# Set your login Credentials  
email.send_keys('<YOUR_EMAIL_ADDRESS>')
password.send_keys('<YOUR_PASSWORD>')
 
 
# Find and Click upon the Login Button 
driver.find_element_by_xpath('//*[@id="pagekey-uno-reg-guest-home"]/div[1]/div/form/input[6]').click()
 
# Logging In happens here and wait 
time.sleep(10)
 
# Find the first "connect" button on the Homepage and Click
 
driver.find_element_by_xpath('//*[@id="pymk"]/ul[2]/li[1]/div/ul/li[1]/button').click()
 
# Counter for counting sent requests 
num = 0
 
while True:
	# Incraese the counter
    num = num + 1
 
	# Keep finding the next "connect" button and Click
    driver.find_element_by_xpath('//*[@id="pymk"]/ul[2]/li['+str(num)+']/div/ul/li[1]/button').click()
    print 'Clicked'
	# Wait to load the next Connection Suggestion 
    time.sleep(8)
    print num
