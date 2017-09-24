from urllib.request import urlopen as uReq
import requests

from bs4 import BeautifulSoup as soup


def main(comments_link_array, name):

    print("Creating file with hotel name: " + name)
    filename = name + ".csv"
    f = open(filename, "w", encoding="utf-8")

    headers = "Comment Title, Comment\n"

    f.write(headers)
    # comment_url = "https://www.tripadvisor.com/ShowUserReviews-g298342-d2554952-r237556936-Maritim_Crystals_Beach_Hotel_Mauritius-Belle_Mare.html#CHECK_RATES_CONT"

    for comment_url in comments_link_array:
        uClient = uReq(comment_url[1])

        # Storing html page in page_html
        comment_html = uClient.read()

        uClient.close()

        # call soup function

        # html parser
        comment_soup = soup(comment_html, "html.parser")
        # print(page_soup.h1)
        # Grabs each hotel listed

        title = comment_soup.find("span", {"class": "noQuotes"})
        comment = comment_soup.find("p", {"class": "partial_entry"})

        cmm = comment.text.replace(",", "|")

        f.write(title.text + "," + cmm + "\n")

        # print(title.text)
        # print(comment.text)

    # print("Closing file with hotel name: " + name)
    f.close()