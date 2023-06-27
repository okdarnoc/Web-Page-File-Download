import subprocess
import sys
import os
from urllib.parse import urljoin, urlsplit

# Check for missing libraries and install them
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install('requests')

try:
    from bs4 import BeautifulSoup
except ImportError:
    install('beautifulsoup4')

def download_files(url, exts, path):
    # Get the HTML
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the links on the webpage
    links = soup.find_all("a")

    # Filter the links to get only the specified files
    file_links = [urljoin(url, link.get('href')) for link in links if link.get('href') and any(link.get('href').endswith(ext) for ext in exts)]

    # Download the files
    for link in file_links:
        # Get the file name
        file_name = os.path.join(path, os.path.basename(urlsplit(link).path))

        # Download the file
        response = requests.get(link, stream=True)

        # Save the file
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                # Writing one chunk at a time to file
                if chunk:
                    file.write(chunk)


# Prompt the user for the url of the webpage to scrape
url = input("Enter the URL of the webpage to scrape: ")

# Prompt the user for the types of files to download
exts = input("Enter the file extensions to download, separated by commas: ").split(',')

# Prompt the user for the location to save the files
path = input("Enter the path of the directory to save the files: ")

# Use the function to download the files
download_files(url, exts, path)
