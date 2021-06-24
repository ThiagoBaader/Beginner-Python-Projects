# Library imports
import requests
from bs4 import BeautifulSoup
import pandas


def rssFeedReader(url):
    """
    Return a Pandas dataframe containing the RSS feed contents.
    :param url: url of the rss feed to read.
    :return df: Pandas dataframe containing the RSS feed contents.
    """

    df = pandas.DataFrame(columns=['Title', 'Description', 'Link'])

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='xml')

        feed = soup.findAll('item')

        for post in feed:
            title = post.find('title').text
            link = post.find('link').text
            description = post.find('description').text

            row = {'Title': title, 'Description': description, 'Link': link}
            df = df.append(row, ignore_index=True)

        return df

    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)


urls = input("Please enter the RSS feed URL(s) (separate them using a comma): ")
urls = urls.split(",")
for url in urls:
    print(url)
    df = rssFeedReader(url)
    print(df, "\n")

#urls for test = https://practicaldatascience.co.uk/feed.xml,https://www.bikeradar.com/news/feed/,https://www.bikeradar.com/cycling-discipline/mtb/feed/
