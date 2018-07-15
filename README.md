Solar Scrapy
===============
A REST API that allows users to search for information on solar objects.

Setting up the project
-----------------------
Solar Scrappy runs on python3, please make sure you are using the latest.
For Scrappy, you will need these dependencies:
```bash
sudo apt-get install python3 python3-dev
```

Setup Virtual Environment (venv)
----------------------------------
Create the project directiory:
```bach
mkdir solaryscrapy
cd solarscrapy
```

Setup the virtual environment. We use Python3:
```bash
virtualenv -p python3 venv
```

Install Required PIP packages
----------------
Intsall all the required packages including the web scraping tool.
```bash
cd solar_scrapy
pip install -r requirements.txt
```

Using the Scrapy Tool
-----------------------
To web scrape the Wikipedia page, use:
```bash
scrapy crawl planets
```
This will execute the planets spider python file
