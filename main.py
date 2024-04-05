from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(3)


sign_up_button = driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div[1]/div[1]/ul/li[4]")
sign_up_button.click()
time.sleep(5)

click_x = 10  # 10 pixels to the right of the pop-up
click_y = 300 # 10 pixels below the pop-up
print("mirinal*************************************************************************************************************")

ActionChains(driver).move_by_offset(click_x, click_y).click().perform()
time.sleep(2)
phone_number_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/input")
phone_number = "8077665932"  # Replace with your desired phone number
phone_number_field.send_keys(phone_number)
time.sleep(2)

#continue_button1 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[2]/button/span")
#continue_button1.click()
#continue_button = driver.find_element(By.CSS_SELECTOR, `[data-cy="continueBtn"]`)
#continue_button.click()
#button[class='capText font16']
'''continue_buttons = driver.find_elements(By.CSS_SELECTOR, '[data-cy="continueBtn"]')
if continue_buttons:
    continue_buttons[0].click()
else:
    print("Continue button not found.")'''
'''continue_button_xpath = '//form[@xpath="1"]//button[@data-cy="continueBtn"]'
continue_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, continue_button_xpath))
)'''
form_xpath = '//form[@xpath="1"]'
form = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, form_xpath))
)

# Now, find the "Continue" button inside the form
continue_button_xpath = './/button[@data-cy="continueBtn"]'
continue_button = WebDriverWait(form, 10).until(
    EC.element_to_be_clickable((By.XPATH, continue_button_xpath))
)
print("henfkjsnfnlkwsgnv")

time.sleep(100)
#driver.get_screenshot_as_file("D:\mmt vscode\screenshot\mmt.png")
driver.quit()


'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(10)  # Increase the wait time for implicit waits

# Click on the sign-up button
sign_up_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/ul/li[4]')
sign_up_button.click()

# Handle the pop-up by moving to a specific location and clicking
click_x = 10
click_y = 300
ActionChains(driver).move_by_offset(click_x, click_y).click().perform()

# Enter the phone number
phone_number_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/input')
phone_number = "8077665932"  # Replace with your desired phone number
phone_number_field.send_keys(phone_number)

# Click on the "Continue" button
continue_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[2]/button/span')
continue_button.click()

# Wait for some time to see the result
time.sleep(5)

# Take a screenshot (optional)
driver.save_screenshot("mmt_screenshot.png")

# Close the browser
driver.quit()'''




















