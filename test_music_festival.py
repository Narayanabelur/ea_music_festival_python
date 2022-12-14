import pytest
import requests
import json
from jsonschema import validate
from jsonschema import Draft6Validator
import logging


def test_ea_festivals_statuscode_200(myget, mylog):
     
     response = myget
     
     if (response.status_code == 200):
         logging.info("Response code is 200")
     elif (response.status_code == 429):
         logging.info("Request Throttled")


def test_get_music_festivals_validates_response_content_type_json(myget):

    response = myget
     
    if (response.status_code == 200):
        logging.info("Response code is 200")
    elif (response.status_code == 429):
        logging.info("Request Throttled")
        return()

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


@pytest.mark.test
def test_music_festival_has_valid_festival_names(myget):
    
    response = myget

    if (response.status_code == 200):
        logging.info("Response code is 200")
    elif (response.status_code == 429):
        logging.info("Request Throttled")
        return()
    
    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    req_content = response.content

    myjson = json.loads(req_content)

    for i in myjson:
        logging.debug ("-----------_>",i['name'])
        if (i['name'] == "LOL-palooza"):
            logging.debug("Festival Name:",i['name'],"exists")


@pytest.mark.test
def test_correct_bands_in_correct_mustic_festival(myget):

    response = myget

    if (response.status_code == 200):
        logging.info("Response code is 200")
    elif (response.status_code == 429):
        logging.info("Request Throttled")
        return()

    # Validate response content type header
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    req_content = response.content

    myjson = json.loads(req_content)

    for i in myjson:
        logging.debug ("Festival names---------->", i['name'])
        for resp_key, resp_value in i.items():
            if (resp_key == 'bands'):
                for j in resp_value:
                    for bandkey, bandname in j.items():
                        if ( bandname == "Winter Primates"):
                            logging.debug ("----------> Band name ", bandname , "is in ", i['name'])
 


