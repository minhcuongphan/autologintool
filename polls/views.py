import undetected_chromedriver as uc
import time
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def index(request):
    return render(request, "index.html")

def autologin(request):
    dataType = request.POST.get("dataType", None)
    match dataType:
        case "gmail":
            username = ""
            password = ""
            gmailLogin(username, password)
        case "linkedIn":
            username = ""
            password = ""
            linkedInLogin(username, password)
        case _:
            print('autologin_default')
    
def linkedInLogin(username, password):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
    driver.get("https://www.linkedin.com/uas/login?")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH,"//*[@id=\"organic-div\"]/form/div[3]/button").click()

def gmailLogin(username, password):
    
    options = webdriver.ChromeOptions()

    options.set_capability("detach", True)
    
    options.add_argument("--incognito")

    options.add_argument("window-size=1500,1000")
    # Removes the "This is being controlled by automation" alert / notification
    options.set_capability("excludeSwitches", ['enable-automation'])

    browser = uc.Chrome(
        options=options,
    )
    browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    browser.find_element(By.ID, 'identifierId').send_keys(username)

    browser.find_element(
        By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

    browser.find_element(
        By.CSS_SELECTOR, password_selector).send_keys(password)

    browser.find_element(
        By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

    time.sleep(1000)