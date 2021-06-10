# A short script to crawl SET50 index from the SET website
This script uses `urllib3` to fetch HTML file from the SET's webpage and parse it with BeautifulSoup library to find the value within the specified location where SET50 value is located. The script can be applied to extract other values too. 

## Installation
`pip install -r requirements.txt`

## Run 
`python main.py`