# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(8)

assert "Amazon.ca" in driver.title



# Clicking on the "All" tab
all_tab = driver.find_element("id", "nav-hamburger-menu")
all_tab.click()
time.sleep(5)

# Clicking on "Best Sellers"
best_seller = driver.find_element("xpath", "//body/div[@id='hmenu-container']/div[@id='hmenu-canvas']/div[@id='hmenu-content']/ul[1]/li[2]/a[1]")
best_seller.click()
time.sleep(5)

assert "Best Sellers" in driver.title

# Clicking on the logo to go to the home page
back_home = driver.find_element("xpath", "//a[@id='nav-logo-sprites']")
back_home.click()
time.sleep(5)

# Hovering over "Sign in"
hover_check = driver.find_element("xpath", "//header/div[@id='navbar']/div[@id='nav-belt']/div[3]/div[1]/a[2]/span[1]/span[1]")
action = ActionChains(driver)
action.move_to_element(hover_check).perform()
time.sleep(5)

# Selecting an option from the hover menu
select_choice = driver.find_element("xpath", "//span[contains(text(),'Find a Gift')]")
select_choice.click()
time.sleep(5)

# Update location
update_location = driver.find_element("xpath", "//a[@id='nav-global-location-popover-link']")
update_location.click()
time.sleep(5)

# Inputting location in the first input box
update_location_input = driver.find_element("xpath", "//input[@id='GLUXZipUpdateInput_0']")
update_location_input.send_keys("n2j")
update_location_input.send_keys(Keys.RETURN)
time.sleep(5)

# Inputting location in the second input box
update_location_input1 = driver.find_element("xpath", "//input[@id='GLUXZipUpdateInput_1']")
update_location_input1.send_keys("4y3")
update_location_input1.send_keys(Keys.RETURN)
time.sleep(5)



# Close the browser
driver.close()
