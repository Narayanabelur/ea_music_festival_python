import pytest
import requests

@pytest.fixture
def myget():
     response = requests.get("https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals")
     if (response.status_code == 200):
         print("Response code is 200")
     elif (response.status_code == 429):
         print("Request Throttled")
     
 
     return(response)
