from selenium import webdriver
from typing import List, Callable, TypeVar
from linkedin_selenium.job_page import JobPage
from services.config_service import get_selenium_url

T = TypeVar("T")  # Generic return type for functions that use WebDriver

def with_driver(func: Callable[[webdriver.Chrome], T]) -> T:
    """Handles WebDriver setup, execution, and teardown."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Run in headless mode
    driver = webdriver.Remote(command_executor=get_selenium_url(), options=options)
    try:
        return func(driver)
    finally:
        # print("Tear down")
        driver.quit()

def get_job_data(job_link: str):
    """Fetches date event links from the homepage."""
    def fetch_links(driver: webdriver.Chrome) -> List[str]:
        driver.get(job_link)
        job_page = JobPage(driver)
        return job_page.get_job_data()
    
    return with_driver(fetch_links)


