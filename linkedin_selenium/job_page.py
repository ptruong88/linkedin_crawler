from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

class JobPage:

    def __init__(self, job_page_content_driver: WebDriver):
        self.job_page_content_driver = job_page_content_driver        

    def get_job_data(self):
        job_data = {}

        main_content = self.job_page_content_driver.find_element(By.ID, 'main-content')
        top_card_info = main_content.find_element(By.CLASS_NAME, 'top-card-layout__entity-info')
        
        top_card_title = top_card_info.find_element(By.CLASS_NAME, 'top-card-layout__title')
        job_data['job_name'] = top_card_title.text

        top_card_subline = top_card_info.find_element(By.CLASS_NAME, 'top-card-layout__second-subline')
        company_info = top_card_subline.find_element(By.CLASS_NAME, 'topcard__org-name-link')
        job_data['company_name'] = company_info.text
        job_data['company_link'] = company_info.get_attribute('href')

        location_info = top_card_subline.find_element(By.CLASS_NAME, 'topcard__flavor--bullet')
        job_data['location'] = location_info.text


        return job_data