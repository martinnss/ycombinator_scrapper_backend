from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import json

def load_all_companies():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for content to load

        # Calculate new scroll height and compare with the last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def get_company_links(driver, base_selector="a._company_1pgsr_355", max_elements=20):
    """
    Extract all company href links for different nth-child values
    
    Args:
        driver: Selenium WebDriver instance
        base_selector: Base CSS selector without nth-child
        max_elements: Maximum number of elements to check
        
    Returns:
        list: List of unique company URLs
    """
    companies = set()  # Using set to avoid duplicates
    
    try:
        # Wait for at least one element to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, base_selector))
        )
        
        # Try each nth-child value
        for i in range(1, max_elements + 1):
            selector = f"{base_selector}:nth-child({i})"
            try:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                for element in elements:
                    href = element.get_attribute('href')
                    if href:  # Only add non-None values
                        companies.add(href)
                        logging.info(f"Found company link: {href}")
            except Exception as e:
                logging.debug(f"No elements found for nth-child({i}): {str(e)}")
                continue
                
    except TimeoutException:
        logging.error("Timeout waiting for company elements to load")
    except Exception as e:
        logging.error(f"Error extracting company links: {str(e)}")
    
    return list(companies)


try:
    # Create an Options object to configure Firefox
    options = Options()
    options.headless = False  # Ensure headless is False for GUI
    
    print("Setting up Firefox driver...")
    
    # Initialize the Firefox WebDriver with the configured options
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    print("Driver initialized successfully")
    
    url = "https://www.ycombinator.com/companies?batch=F24&batch=W25&batch=S24&batch=W24"
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)



    load_all_companies()
    
    
    company_elements = driver.find_elements(By.CSS_SELECTOR, "a._company_1pgsr_355")
    num_companies = len(company_elements)
    print(f"Number of companies found: {num_companies}")

    
    companies = get_company_links(driver, max_elements=(num_companies+1))

    companies_json = [{"url": company} for company in companies]

    # Export to a JSON file
    with open('events.json', 'w') as file:
        json.dump(companies_json, file, indent=4)

    # 8Close the driver
    #driver.quit()

    # Output the result
    for i, company in enumerate(companies, start=1):
        print(f"{i}: {company}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    print('end')
