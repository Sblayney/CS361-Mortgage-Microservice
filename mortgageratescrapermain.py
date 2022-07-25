"""Program represents a microservice to a mortgage product comparison tool.
The microservice provides data related to today's mortgage rates for various lengths of mortgages
for both purchases and refinancing by scraping bankrate.com."""

import urllib.request
from bs4 import BeautifulSoup
import json

def main() -> None:
    """
    Checks for request, scrapes html from wiki page, 
    and responds with the file name with item data
    """
    # Check for request
    while True:
        with open("pipe.txt", "r") as infile:
            line = infile.read()
        
        if line == "Get Rates":
            print("Received Request")
            # Get data
            rates = scrape_rates()
        
            print("Posting data")
            with open("rate_data.json", 'w') as outfile:
                json.dump(rates, outfile, indent=4)

            print('Sending Response')
            with open("pipe.txt", "w") as file:
                file.write("rate_data.json")
            print('Response Sent')

def scrape_rates():
    """Retrieves information from wiki page using
    beautiful soup library.
    https://beautiful-soup-4.readthedocs.io/en/latest/
    """
    # Open URL, read HTML, and scrape tags 
    url = 'https://www.bankrate.com/mortgages/20-year-mortgage-rates'
    html_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    # Store Weapon Data in dictionary
    rate_dict = dict()
    attrib_list = ["Interest Rate", "APR"]
    attrib_info = [""] * 2
    ignore_words = ["Product", "Interest Rate", "APR"]

    # Iterate through html tags and store relevant info
    start, end, idx, percent_count = False, False, 0, 0
    for tag in soup.find_all(['div', 'th', 'td']):
        if str(tag.get('id')) == "purchase":
            start = True
        if percent_count >= 16:
            end = True

        # If statements for handling the different html tags we are looking for
        if start and not end:

            # Gets the two categories of products: purchase and refinance
            if str(tag.name) == 'div':
                if str(tag.get('id')) == "purchase" or str(tag.get('id') == "refinance"):
                    heading = str(tag.get('id'))
                    heading = heading.capitalize()
                    rate_dict[heading] = dict()

            # Gets the product type in terms of length
            if str(tag.name) == 'th':
                rate = str(tag.get_text())
                rate = rate.strip('\n')
                if rate not in ignore_words:
                    rate_dict[heading][rate] = \
                        dict(zip(attrib_list, attrib_info))

            # Gets the actual percentage rates
            if str(tag.name) == 'td':
                rate_dict[heading][rate][attrib_list[idx]] = str(tag.get_text())
                idx = (idx + 1) % 2
                percent_count = percent_count + 1

    return rate_dict

if __name__ == "__main__":
    main()
