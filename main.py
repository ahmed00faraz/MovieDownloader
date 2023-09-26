import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from custom import get_input_with_timeout

# MOVIE_URL = "https://moviesmod.mobi/download-blue-beetle-2023-english-480p-720p-1080p/"

MOVIE_URL = input("enter link :  ")

# Setting up our browser options
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537'
)

# Creating browser instance
driver = webdriver.Edge(options=options)
# setting the timeout as 15 seconds
wait = WebDriverWait(driver, timeout=15)

driver.get(MOVIE_URL)
# links = driver.find_elements(By.CLASS_NAME, "maxbutton-download-links")
# links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "maxbutton-download-links")))


# main page download button (has quality we are taking 1080p by default)
links = wait.until(lambda d: d.find_elements(By.CLASS_NAME, "maxbutton-download-links"))
driver.get(links[-1].get_attribute('href'))


# modlinkz page opens and we select the first option
grdive_link = wait.until(lambda d: d.find_element(By.CLASS_NAME, "maxbutton-1"))
driver.get(grdive_link.get_attribute('href'))

# we have opened a blog , and clicking the start verification button
start_verification_button = wait.until(lambda d: d.find_element(By.TAG_NAME, 'form').find_element(By.TAG_NAME, 'a'))
start_verification_button.click()
print("verification started")
# goes to a different page where it says verify to continue

sleep(5)

verify_to_continue = driver.find_element(By.ID, "verify_button2")
verify_to_continue.click()
print("verified")
# waiting period of 10 seconds
sleep(11)
print("waiting 10 sec completed")
clicker_here_to_continue = driver.find_element(By.ID, "verify_button")
clicker_here_to_continue.click()
# wait for that element to generate links
print("wait for final link started")
sleep(10)
print("wait for final link ended")
grdive_page = driver.find_element(By.ID, "two_steps_btn").get_attribute('href')
driver.get(grdive_page)

# ########################### assuming we are choosing an instant download button#####################################
card = driver.find_element(By.CLASS_NAME, "card-body")
i_elements = [i.text for i in card.find_elements(By.TAG_NAME, 'i')]
print('Download Options : ', i_elements)
print("enter download option")
download_option = get_input_with_timeout(20, "instant")
link_elements = [link.get_attribute('href') for link in card.find_elements(By.TAG_NAME, 'a')]
for _ in range(len(link_elements)):
    if download_option in i_elements[_]:
        driver.get(link_elements[_])
        sleep(3)
        sys.exit()
driver.get(link_elements[0])
