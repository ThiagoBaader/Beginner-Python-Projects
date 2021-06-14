# Library imports
import requests
from bs4 import BeautifulSoup


def scrapeArticle(URL):
    """
    Web scraper to get news article content
    :param URL: the url of the article to be scrapped
    :return: the article html parsed and the article content
    """

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get article title
    articleTitle = soup.find('h1', class_="Article__title").get_text()
    print("Title: ", articleTitle)

    # Get article author
    articleAuthor = soup.find_all("div", class_="Article__subtitle")[0].text.split(',')[0]
    print("Author: ", articleAuthor)

    # Get article updated date
    articleUpdatedDate = soup.find_all("div", class_="Article__subtitle")[0].text.split('Updated ')[1]
    print("Updated date: ", articleUpdatedDate)

    # Get article content
    articleContent = soup.find_all("div", class_="Article__content")[0].text
    print("Content: ", articleContent)


# Article URL
URL = 'https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html'
scrapeArticle(URL)
