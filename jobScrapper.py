import requests
from bs4 import BeautifulSoup


def __main__():

  print()
  print()
  print('Techs you are not familiar with')
  unfamiliar_techs = input('>')
  print(f"Filtering out {unfamiliar_techs}")
  print()
  print('-------------------------------------------------------------------')

  JOB_PORTAL_URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
  
  html_text = requests.get(JOB_PORTAL_URL).text
  soup = BeautifulSoup(html_text, 'lxml')

  older = 4

  jobs_list = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")

  for job in jobs_list:
    
    updated = job.find('span', class_ = "sim-posted").find('span').text.split()[1]
    
    if updated == 'few' or updated == 'today' or int(updated) <= older:
      company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ', '').strip()
      skills = job.find('span', class_ = "srp-skills").text.replace(' ', '').strip().split (",")
      if unfamiliar_techs not in skills:
        link = job.find('h2').a['href']

        # visiting to the job 
        job_soup = BeautifulSoup(requests.get(link).text, 'lxml')
        job_description = job_soup.find('div', class_ = "jd-desc job-description-main").text

        

        print()
        print(f"COMPANY : {company_name}")
        print(f"SKILLS REQUIREMENT : {skills}")
        #print(job_description)
        print(f"JOB LINK : {link}")
        print()
        print('-------------------------------------------------------------------')

__main__()