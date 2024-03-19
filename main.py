import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


url = 'https://news.ycombinator.com/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('tr', class_='athing')
for article in articles:
    # Adjusted to the correct class name and structure
    title_tag = article.find('span', class_='titleline').find('a')

    if title_tag:
        title = title_tag.text
        link = title_tag['href']
    else:
        title = 'Title not found'
        link = 'Link not found'

    score_tag = article.find_next_sibling('tr').find('span', class_='score')
    score = score_tag.text if score_tag else 'No score'

    print(f'Title: {title}\nLink: {link}\nScore: {score}\n{"-" * 40}')

