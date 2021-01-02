from epic_config import Epic_config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MONTHS = ['','January','February','March','April','May','June','July', 'August', 'September', 'October',
'November', 'December']

def in_wait_room(driver):
    return 'https://waitingroom.snow.com' in driver.current_url

def sign_in(driver, reservation_url, account_keys):
    # Enter email and password
    driver.get(reservation_url)
    if ('https://www.epicpass.com/waitingroom/reservations' in driver.current_url):
        driver.find_element_by_xpath('/html/body/div/div/div[2]/a[1]').click()
    # Check to see if we are in the waiting room
    # while (in_wait_room(driver)):
    #     time.sleep(5)
    #     driver.refresh()
    driver.find_element_by_xpath('//*[@id="txtUserName_3"]').send_keys(account_keys['email'])
    driver.find_element_by_xpath('//*[@id="txtPassword_3"]').send_keys(account_keys['password'])

    try:    # Wait until the accept cookies button appears
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div/div/div[5]/button').click()

    except: # If the accept cookies button doesn't appear, proceed with sign in
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div/div/div[5]/button').click()
    
    if (EC.presence_of_element_located((By.ID, 'errorMessage_3'))):
        raise Exception('Invalid login credentials!')

def select_resort(driver, reservation_keys):
    try:    # Wait until the page loads
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "passHolderReservationsSearchButton"))
        )
        driver.find_element_by_xpath(reservation_keys['resort_name']).click()
        driver.find_element_by_xpath('//*[@id="passHolderReservationsSearchButton"]').click()
    except: # If the page does not load, raise exception
        raise Exception

def move_to_next_month(driver):
    try:    # Wait until the page loads
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/button[2]'))
        )
        next_month_button = driver.find_element_by_xpath('//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/button[2]')
        next_month_button.click()
    except: # raise an exception if the page doesn't load
        raise Exception

def get_current_month(driver):
    try:    # Wait until the page loads
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span[1]'))
        )
        return driver.find_element_by_xpath('//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span[1]')
    except: # raise an exception if the page doesn't load
        raise Exception

def select_date(driver, date):
    try:    # Wait until the page loads
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/button[2]'))
        )
        month = get_current_month(driver)
        while (month.text.upper() != MONTHS[date.month].upper()):
            move_to_next_month(driver)
            month = get_current_month(driver)
        available_days = driver.find_elements_by_class_name('passholder_reservations__calendar__day')
        for i in range (len(available_days)):
            if (available_days[i].text == str(date.day)):
                available_days[i].click()
                break
    except: # If the page does not load, raise exception
        raise Exception

def select_people(driver, reservation_keys):
    try:    # Wait until the page loads
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[2]/div[1]/div[2]/div/p'))
        )
        people = driver.find_elements_by_class_name("passholder_reservations__assign_passholder_modal__name")
        for i in range (len(reservation_keys['names'])):
            for j in range(len(people)):
                print(people[j].text)
                if (people[j].text.upper() == reservation_keys['names'][i].upper()):
                    people[j].click()
                    break
        driver.find_element_by_xpath('//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[3]/button[2]').click()
    except: # If the page does not load, raise exception
        raise Exception

def confirm_reservations(driver):
    driver.find_element_by_xpath('//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[6]/div[2]/div[2]/div[2]').click()
    driver.find_element_by_xpath('//*[@id="passHolderReservations__wrapper"]/div[3]/div[2]/div[6]/div[3]/button').click()

def tear_down(driver):
    driver.quit()

class Bot():
    def __init__(self, epic_config):
        self.reservation_keys = epic_config.reservation_keys
        self.account_keys = epic_config.account_keys
        self.reservation_url = epic_config.reservation_url
    
    def run(self):
        try:
            self.driver = webdriver.Chrome('chromedriver')
            sign_in(self.driver, self.reservation_url, self.account_keys)
            select_resort(self.driver, self.reservation_keys)
            dates = self.reservation_keys['dates']

            for i in range(len(dates)):
                select_date(self.driver, dates[i])
                select_people(self.driver, self.reservation_keys)

            confirm_reservations(self.driver)

        except Exception as e:
            raise Exception from e

        finally:
            tear_down(driver)    # Quit the driver and end the program

