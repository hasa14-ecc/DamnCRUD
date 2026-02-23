import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("BASE_URL", "http://localhost/DamnCRUD")
USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "nimda666!")

def login(driver):
    driver.get(f"{BASE_URL}/login.php")

    # Locator ini mungkin perlu kamu sesuaikan sesuai HTML repo
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(USERNAME)

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.any_of(
            EC.url_contains("index.php"),
            EC.presence_of_element_located((By.XPATH, "//*[contains(.,'Dashboard')]"))
        )
    )

@pytest.fixture
def driver():
    headless = os.getenv("HEADLESS", "1") == "1"

    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1365,768")

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(3)

    # Precondition: login
    login(drv)

    yield drv
    drv.quit()