
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Navigate to the login page
    driver.get("http://127.0.0.1:8000/admin-login/")
    print("Page loaded successfully.")

    # Find login form elements
    login_username = driver.find_element(By.ID, "username")
    login_password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "form[action*='admin_login'] button.btn")

    # Fill in the login form
    login_username.send_keys("testt_user1")  # Replace with valid username
    login_password.send_keys("securepassword56123")  # Replace with valid password
    print("Login form filled successfully.")

    # Submit the login form
    login_button.click()
    print("Login button clicked.")

    # Check if login is successful by verifying the current URL or looking for a specific element on the dashboard
    WebDriverWait(driver, 10).until(lambda d: d.current_url != "http://127.0.0.1:8000/admin-login/")
    print("Login test passed! Redirected to:", driver.current_url)

except Exception as e:
    print(f"Login test failed: {e}")

finally:
    # Quit the browser
    driver.quit()
