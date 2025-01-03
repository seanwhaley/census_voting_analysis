import os
import requests
import zipfile
import io

# Download Census Data
def download_census_data():
    ftp_url = "https://www2.census.gov/programs-surveys/acs/data/pums/2020/1-Year/csv_pus.zip"
    response = requests.get(ftp_url)
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall()
    os.rename('ss20pus.csv', 'data/census_data.csv')

# Download Voting Data
def download_voting_data():
    url = "https://raw.githubusercontent.com/openelections/openelections-data-va/master/2020/20201103__va__general__precinct.csv"
    response = requests.get(url)
    with open('data/voting_data.csv', 'wb') as file:
        file.write(response.content)

# Check if files exist, if not download them
if not os.path.exists('data/census_data.csv'):
    download_census_data()

if not os.path.exists('data/voting_data.csv'):
    download_voting_data()
