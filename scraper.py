import requests
import csv
from bs4 import BeautifulSoup


def write_to_csv(list_input):
    try:
        with open("allMovies.csv", "a") as fopen:
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False


with open("Templates/imdb_most_popular_movies_dump.html") as log_file:
    html = log_file.read()
    soup = BeautifulSoup(html, "html.parser")


for tr in soup.find_all("tr")[1:]:
    gdp_table = tr.find("td", attrs={"class": "titleColumn"})
    tds_title = gdp_table.find('a').text.strip()
    tds_year = tr.find('span', class_='secondaryInfo').text.strip()
    tds_rate = tr.find('td', class_='ratingColumn imdbRating').text.strip().encode("ascii", "ignore").decode("ascii")
    print("title:", tds_title)
    print("year:", tds_year)
    print("rating:", tds_rate)

    write_to_csv([tds_title, tds_year, tds_rate])

