# When we scrape data from a website, we use the requests library to get the HTML content of the website.
# But the data we get through this is not nicely formatted like the JSON data we get from an API. (in the previous program)

# Thus, to extract the data we need to "parse" the HTML content, which means to extract the data we need from the HTML content.
# We can use the BeautifulSoup library to parse the HTML content and extract the data we need.

# To run the venv virutal environment, use the command: .\venv\Scripts\activate`
# To install the BeautifulSoup library, use the command: pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Headers are used to tell the website that we are a browser and not a bot so that we can access the website without any issues. (like most websites block bots)
# We can get the headers by searching "my user agent" on google.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers) 
# We are passing headers as a parameter to the get function so that the website thinks that we are a browser and not a bot. (named argument) 

# to extract the text from the HTML content, we can use the text attribute. --> tag.text
# to extract the attributes of a tag, we can use the get function. --> tag.get('attribute_name') or tag['attribute']
soup = BeautifulSoup(data.text, 'html.parser')
movies = soup.select("div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul")

print(movies)

for movie in movies:
    movieTitle = movie.select_one('.sc-b189961a-9 > a > h3').text
    print(movieTitle)
    
    