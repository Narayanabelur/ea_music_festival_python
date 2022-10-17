import pytest
import requests
import logging
import sys



@pytest.fixture
def myget():
     response = requests.get("https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals")
     if (response.status_code == 200):
         print("Response code is 200")
     elif (response.status_code == 429):
         print("Request Throttled")
     
 
     return(response)


@pytest.fixture
def mylog():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
