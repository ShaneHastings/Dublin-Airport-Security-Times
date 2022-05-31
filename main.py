# Scraping security wait times from dublinairport.com

import re
import requests
from bs4 import BeautifulSoup

# Request the page
URL = "https://www.dublinairport.com/flight-information/live-departures"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find security times within page HTML
results = soup.find(id="main-content")
security_times = results.find_all("div", class_="sec-times")
strongtag = soup.find_all("strong", {"style": ""})

# Get both terminal security times
terminal1time = strongtag[-3]
terminal2time = strongtag[-2]

# Remove HTML tags
terminal1halfstrip = re.sub(r'.', '', str(terminal1time), count = 11)
terminal1clean = terminal1halfstrip[:-9]

terminal2halfstrip = re.sub(r'.', '', str(terminal2time), count = 11)
terminal2clean = terminal2halfstrip[:-9]

# Output to console
print("[Dublin Airport - DUB] [Security Waiting Times]")
print("Terminal 1: " + terminal1clean)
print("Terminal 2: " + terminal2clean)

