import pandas as pd
import requests
import json

def last_two_char(x):
    return x[-2:]

#' Download series data via the EIA API.
#' 
#' @param ID The Series Id.
#' @param key Your API key.
#' @returns an pandas time series.
def getEIA(ID, key):
    match last_two_char(ID):
        case ".A":
            return(getAnnEIA(ID, key))
        case ".Q":
            getQEIA(ID, key)
        case ".M":
            getMonEIA(ID, key)
        case ".W":
            getWDEIA(ID, key)
        case ".D":
            getWDEIA(ID, key)
        case ".H":
            getHEIA_UTC(ID, key)
        case "HL":
            getHEIA_L(ID, key)
        case _:
            print("ERROR: The last character of your ID is not one of the possible sampling frequencies (A, Q, M, W, D, or H)")

#' Download annual series data via the EIA API.  Do not use this function directly.
#' 
#' @param ID The Series Id.
#' @param key Your API key.
#' @returns pandas time series.
def getAnnEIA(ID, key):

    # I don't think we need the following two lines.
  # ID <- unlist(strsplit(ID, ";"))
  # key <- unlist(strsplit(key, ";"))

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    ## the following line converts the year to yyyy-01-01.  
    ## it may be more appropriate to change it to yyyy-12-31.
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period'], format="%Y"), drop=True)
    return energy_data



## to test
with open('/home/matt/eia_api_key.txt', 'r') as f:
  key = f.read().rstrip('\n')

ID = 'ELEC.GEN.ALL-AK-99.A'

getEIA(ID = ID, key = key)
gen = getEIA(ID = ID, key = key)
gen