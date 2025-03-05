import time
import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ica_aep_team_engager(Array_URLs):
    
    ### IBM CREDENTIALS ###
    ### IMPORTANT ###

    # Open credentials.json file and input your IBM email address and password
    with open('credentials.json', 'r') as file:
        user_credentials = json.load(file)
    ibm_credentials = {
        "IBM_email_address": user_credentials["IBM_email_address"],
        "password": user_credentials["password"]
    }

    if ibm_credentials["password"] != '':

        # Initialize the WebDriver (this example uses Chrome)
        driver = webdriver.Chrome()  # You can specify the path to chromedriver if not in PATH

        # Open the login page
        driver.get('https://servicesessentials.ibm.com/curatorai/apps/ui/?teamName=AEP%20PH%20Team&teamId=664de36238fbda6f54c89677')

        # Input initial ibm email address credentials
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/form/div[2]/div/div/div/div/input').send_keys(ibm_credentials["IBM_email_address"])
        driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div/form/div[3]/div/div/button').click()

        # Wait for the page to load and the username field to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        time.sleep(2)
        # driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/span[3]').click()
        driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[1]/input').send_keys(ibm_credentials["IBM_email_address"])
        driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/input').send_keys(ibm_credentials["password"])
        driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[4]/button').click()

        # Wait for the ICA AEP TEAM page to load after login
        time.sleep(10)

        driver.get('https://servicesessentials.ibm.com/curatorai/apps/ui/new-chat')
        time.sleep(2)

        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/span/span/span[1]/button').click()

        # send keys to ICA chat prompt
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/textarea').send_keys(f"Hello there! Greetings from AEP Team!")
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[5]/div/div/div[2]/div/div[2]/div/div/div[2]/span/div/button').click()


Array_URLs,ask_try,URL = [],'n','https://servicesessentials.ibm.com/'

while True:
    if ask_try == 'n':
        break
    URL = input('Input ICA URL: ').strip()
    Array_URLs.append(URL)
    while True:
        ask_try = input('Input another URL? (y/n): ').strip().lower()
        if ask_try == 'n':
            break
        elif ask_try == 'y':
            break
        else:
            print('Not a valid input.')

print("\nHere's the ICA URL we're going to engage:\n")
print(f"\t{URL}")

continue_or_exit_program = input("\n***Please read the following carefully:***\n\n"
    "This program will open your \n"
    "Chrome browser to work with IBM's SSO.\n"
    "Then will open the ICA URL you provided.\n"
    "It will engage the ICA chat with a message.\n"
    "Then it will chat 'Hello there! Greetings from AEP Team!'\n\n"
    "If you're ready, press Enter to continue.\n")

ica_aep_team_engager(Array_URLs)

time.sleep(10) # Wait for 10 seconds before closing the browser