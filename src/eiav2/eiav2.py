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
            return(getQEIA(ID, key))
        case ".M":
            return(getMonEIA(ID, key))
        case ".W":
            return(getWDEIA(ID, key))
        case ".D":
            return(getWDEIA(ID, key))
        case ".H":
            return(getHEIA_UTC(ID, key))
        case "HL":
            return(getHEIA_L(ID, key))
        case _:
            print("ERROR: The last character of your ID is not one of the possible sampling frequencies (A, Q, M, W, D, or H)")

#' Download annual series data via the EIA API.  Do not use this function directly.
#' 
#' @param ID The Series Id.
#' @param key Your API key.
#' @returns pandas time series.
def getAnnEIA(ID, key):

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    ## the following line converts the year to yyyy-01-01.  
    ## it may be more appropriate to change it to yyyy-12-31.
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period'], format="%Y"), drop=True)
    return energy_data


def getQEIA(ID, key):

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    ## index below is a periodindex.  Is this OK?
    energy_data = energy_data.set_index(pd.PeriodIndex(energy_data['period'], freq='Q'), drop=True)
    energy_data = energy_data.drop(['period'], axis=1)
    return energy_data
    

def getMonEIA(ID, key):

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period'], format="%Y-%m"), drop=True)
    energy_data = energy_data.drop(['period'], axis=1)
    return energy_data

def getWDEIA(ID, key):

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period'], format="%Y-%m-%d"), drop=True)
    energy_data = energy_data.drop(['period'], axis=1)
    return energy_data

def getHEIA_UTC(ID, key):
    """
    Format of period:
    2023-03-24T08
    R version also handled the following format, but haven't seen it in .H data yet:
    UTC: 20200509T19Z
    """

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    ## looks like pandas handles the time perfectly by itself
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period']), drop=True)
    energy_data = energy_data.drop(['period'], axis=1)
    return energy_data

def getHEIA_L(ID, key):
    """
    period has a UTC offset: 2023-03-24T13-05
    looks like pandas handles it
    """

    url = "https://api.eia.gov/v2/seriesid/" + ID + "?api_key=" + key + "&out=xml"
    doc = requests.get(url)
    json_data = doc.json() 
    energy_data = pd.json_normalize(json_data['response']['data'])
    ## looks like pandas handles the time UTC offset
    energy_data = energy_data.set_index(pd.to_datetime(energy_data['period']), drop=True)
    energy_data = energy_data.drop(['period'], axis=1)
    return energy_data


