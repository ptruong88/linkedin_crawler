from services.config_service import get_linkedin_job_links
from services import linkedin_job_service
from datetime import datetime

def main():
    print(f'Processing LinkedIn job link: {get_linkedin_job_links()}')
    for linkedin_job_link in get_linkedin_job_links():
        job_data = linkedin_job_service.get_job_data(linkedin_job_link)
        print("HELLO")
        print(f"""{job_data['company_name']},{job_data['company_link']},{linkedin_job_link},{job_data['job_name']},{job_data['location']}, {get_current_time()}""")

def get_current_time():
    # Get current date and time
    current_time = datetime.now()

    # Format it as MM/DD/YYYY HH:mm:ss
    return current_time.strftime("%m/%d/%Y %H:%M:%S")

if __name__ == "__main__":
    main()