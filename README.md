# Web Scraper for Downloading Files

This Python script allows you to scrape a webpage and automatically download all files of specified extensions. This could be useful when you need to download multiple files from a webpage, saving the hassle of manual downloads.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Mechanism](#mechanism)
- [Use Cases](#use-cases)
- [License](#license)
- [Contact](#contact)

## Prerequisites

The script requires Python 3.6 or higher. It uses the following Python libraries:

- requests
- BeautifulSoup4

The script will attempt to install these libraries if they are not found in your Python environment. However, it's generally recommended to install these manually in advance.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/okdarnoc/Web-Page-File-Download.git
    ```
2. Navigate to the repository directory:
    ```
    cd repositoryname
    ```
3. (Optional) Create a virtual environment and activate it:
    - On Windows:
      ```
      python -m venv env
      env\Scripts\activate
      ```
    - On Unix or MacOS:
      ```
      python3 -m venv env
      source env/bin/activate
      ```
4. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```
    python downloadfile.py
    ```
2. When prompted, enter the URL of the webpage to scrape.
3. Enter the file extensions to download. Multiple extensions should be separated by commas (for example: `.pdf,.jpg,.png`).
4. Enter the path of the directory where the files will be saved.

The script will then download all files of the specified types from the given webpage.

## Mechanism

The script works by sending a GET request to the specified URL to retrieve the webpage HTML. It then parses the HTML with BeautifulSoup to find all the links. The script then filters these links to get only those ending with the specified file extensions. For each of these links, the script sends a GET request to download the file, and then saves the file to the specified directory.

## Use Cases

This script can be useful in a variety of scenarios where multiple files need to be downloaded from a webpage. For example, it could be used to download all PDF documents from a webpage for offline reading, or download all image files from a webpage for data analysis.

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.

## Contact

If you have any questions, feel free to open an issue or submit a pull request.
