import re
import threading
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def get_input_with_timeout(x, default_value):
    input_value = None

    def input_thread():
        nonlocal input_value
        input_value = input()

    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    # Use the time module to wait for the input thread to finish executing.
    input_thread.join(x)

    if input_value is None:
        return default_value
    else:
        return input_value


MOVIE_URL = input("please enter the link of the movie: ")

# MOVIE_URL = input("enter link :  ")

# Setting up our browser options
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 '
    'Safari/537'
)

# Creating browser instance
driver = webdriver.Edge(options=options)
# setting the timeout as 15 seconds
wait = WebDriverWait(driver, timeout=15)

driver.get(MOVIE_URL)
# links = driver.find_elements(By.CLASS_NAME, "maxbutton-download-links")
# links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "maxbutton-download-links")))


# main page download button (has quality we are taking last link by default)
links = wait.until(lambda d: d.find_elements(By.CLASS_NAME, "maxbutton-download-links"))
driver.get(links[-1].get_attribute('href'))

# modlinkz page opens and we select the first option
gdrive_link = wait.until(lambda d: d.find_element(By.CLASS_NAME, "maxbutton-1"))
driver.get(gdrive_link.get_attribute('href'))
sleep(2)

# Page 1
# We just skip the clicking , by directly executing the javascript function which was in the button
# Click to verify Button
driver.execute_script("if(document.getElementById('landing')) { document.getElementById('landing').submit(); } else { "
                      "console.log('Element landing does not exist'); }")
print("verification started")

# Page 2
# goes to a different page where it says verify to continue
sleep(5)

# New Way
script_tag = driver.find_element(By.XPATH, "/html/body/section/article/script")
# Assuming 'element' is your script tag
content = script_tag.get_attribute('innerHTML')
gdrive_page = re.findall(r'https://tech.unblockedgames.world/\?go=pepe-\w+', content)
driver.get(gdrive_page[0])

# Main download page
# ########################### assuming we are choosing an instant download button #####################################
card = driver.find_element(By.CLASS_NAME, "card-body")
a_tag_texts = [i.text for i in card.find_elements(By.TAG_NAME, 'a')]

# print('Download Options : ', a_tag_texts)
# print("enter download option")
# download_option = get_input_with_timeout(10, "instant")

download_option = 'instant'
link_elements = [link.get_attribute('href') for link in card.find_elements(By.TAG_NAME, 'a')]
for _ in range(len(link_elements)):
    if download_option.lower() in a_tag_texts[_].lower():
        driver.get(link_elements[_])
        sleep(3)
try:
    sleep(3)
    driver.find_element(By.CLASS_NAME,"btn-danger").click()
except:
    try:
        driver.find_element(By.XPATH,"/html/body/div/div/div/img").click()
        sleep(1)
        driver.find_element(By.CLASS_NAME, "btn-danger").click()
    except:
        print('Sorry bro')