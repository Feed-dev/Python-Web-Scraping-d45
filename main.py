import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


# url = 'https://news.ycombinator.com/'
# response = requests.get(url)
# response.raise_for_status()
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# articles = soup.find_all('tr', class_='athing')
# for article in articles:
#     # Adjusted to the correct class name and structure
#     title_tag = article.find('span', class_='titleline').find('a')
#
#     if title_tag:
#         title = title_tag.text
#         link = title_tag['href']
#     else:
#         title = 'Title not found'
#         link = 'Link not found'
#
#     score_tag = article.find_next_sibling('tr').find('span', class_='score')
#     score = score_tag.text if score_tag else 'No score'
#
#     print(f'Title: {title}\nLink: {link}\nScore: {score}\n{"-" * 40}')


# Write your code below this line 👇

# URL of the web archive containing the top 100 movies
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to fetch the page content
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Adjust the selector based on the actual structure of the webpage
# The script below assumes movie titles are within <h3> tags
movie_titles = [h3.text for h3 in soup.find_all('h3')]

# Reverse the list to have it in ascending order
movie_titles.reverse()

# Write the movie titles to a text file, omitting custom numbering
with open('movies.txt', 'w', encoding='utf-8') as f:
    for title in movie_titles:
        f.write(f"{title}\n")

print("Top 100 movies in ascending order have been written to movies.txt")

