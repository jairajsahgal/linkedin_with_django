import pandas as pd
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import logging
import os
import re
config = os.environ
logging.basicConfig(filename='scraping.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger("scraping")

def get_followers(input_string):
    followers_match = re.search(r'(\d+,\d+)', input_string)

    if followers_match:
        # Remove commas and convert to an integer
        followers_count = int(followers_match.group(1).replace(',', ''))
        return followers_count
    else:
        return None



#function to ensure all key data fields have a value
def validate_field(field):
    if not field:
        field = "No results"
    return field

def get_values(linkedin_profile_url:str):
    opts = Options()

    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(options=opts,service=service)
    data = {}
    driver.get('https://www.linkedin.com')

    sleep(5)

    username = driver.find_element(By.ID, 'session_key')

    username.send_keys(config['EMAIL'])

    sleep(0.5)

    password = driver.find_element(By.ID, 'session_password')

    password.send_keys(config['PASSWORD'])

    sleep(0.5)

    sign_in_button = driver.find_element(By.XPATH,'//*[@type="submit"]')

    sign_in_button.click()

    #* Sign In Complete

    #* Getting all fields
    account_url = linkedin_profile_url
    driver.get(account_url)

    sleep(20)

    src = driver.page_source
    logger.info("Page source captured")

    soup = BeautifulSoup(src,'lxml')

    logging.info(soup)

    img_tag = soup.find('img', {'class': 'evi-image lazy-image ember-view org-top-card-primary-content__logo'})
    img_url = img_tag['src']
    data["image_url"] = img_url

    heading_tag = soup.find('h1',{'class':'ember-view text-display-medium-bold org-top-card-summary__title full-width'})
    heading = heading_tag['title']
    data["heading"]=heading

    follower_tag = soup.find_all('div',{'class':'org-top-card-summary-info-list__info-item'})
    # number_of_followers = follower_tag.text.split()[0]
    follower = 0
    for i in follower_tag:
        i.find('div',{'class':'artdeco-entity-lockup__caption ember-view reusable-org-card__secondary-subtitle'})
        follower = i.text
        logger.info(f"Found number of followers: {follower}")
        if "followers" in follower:
            follower = get_followers(follower)
            logger.info(f"Stripped text: {follower}")
            break
    logger.info(follower_tag)
    data["followers"]=follower

    see_more_description_button = driver.find_element(By.CLASS_NAME,"org-about-module__description")
    click_on_see_more=see_more_description_button.find_element(By.CLASS_NAME,"lt-line-clamp__more")
    click_on_see_more.click()


    logger.info("SEE MORE DESCRIPTION")
    logger.info(see_more_description_button.text)
    data["description"]=see_more_description_button.text
    sleep(15)
    driver.close()
    return data