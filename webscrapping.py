#installations required
# !pip install selenium
# !pip install BeautifulSoup
# !pip install pandas

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import pandas as pd

#chrome driver for selenium. It can be download from https://chromedriver.chromium.org/downloads
DRIVER_PATH = 'G:/chromedriver.exe'

#Initializing the webdriver
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

articles = [
  "https://apolitical.co/en/solution_article/how-climate-change-adds-fuel-to-the-refugee-crisis",
  "https://apolitical.co/en/solution_article/how-wigan-drove-change-by-putting-people-first",
  "https://apolitical.co/en/solution_article/what-ghana-can-teach-us-about-integrating-refugees",
  "https://apolitical.co/en/solution_article/does-free-public-transport-actually-work",
  "https://apolitical.co/en/solution_article/the-city-of-the-future-is-built-on-open-data",
  "https://apolitical.co/en/solution_article/no-city-limits-how-data-is-helping-shape-urban-health-policy",
  "https://apolitical.co/en/solution_article/syria-displaced-doctors-turkey-workforce",
  "https://apolitical.co/en/solution_article/local-councils-citizens-collaboration",
  "https://apolitical.co/en/solution_article/reasons-to-be-cheerful-about-the-future-of-local-government",
  "https://apolitical.co/en/solution_article/a-case-for-copying-brazils-refugee-policy",
  "https://apolitical.co/en/solution_article/building-safer-and-more-resilient-cities-in-the-philippines",
  "https://apolitical.co/en/solution_article/regional-australia-needs-immigrants-but-forcing-them-there-isnt-the-answer",
  "https://apolitical.co/en/solution_article/a-small-town-solution-to-digitisation",
  "https://apolitical.co/en/solution_article/smart-cities-are-nothing-without-their-citizens",
  "https://apolitical.co/en/solution_article/what-joining-local-government-feels-like-for-a-junior-public-servant",
]

articles_content = []

def scrap_data(url):
	driver.get(url)

	#sleep for 2 seconds to allow  page load
	#Change this number based on your internet speed.
	time.sleep(2)

	#download page source with selenium driver 
	html = driver.page_source

	#parse page source with beautiful soup html parser
	soup = BeautifulSoup(html, "html.parser")

	# Get text from all <p> tags.
	p_tags = soup.find_all('p')
	# Get the text from each of the “p” tags and strip surrounding whitespace.
	p_tags_text = [tag.get_text().strip() for tag in p_tags]
	#convert to string for easier manipulation
	text = " ".join([word for word in p_tags_text
	                            if '\xa0' not in word
	                 ])

	articles_content.append(text)

for url in articles:
	scrap_data(url)

#This line converts the dictionary object into a pandas DataFrame
df = pd.DataFrame(articles_content, columns =['Content'])

df.to_csv('apoliticalArticles.csv')


driver.quit()


# Section 2

#Article content analysis

