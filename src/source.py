import pandas as pd

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
            getAnnEIA(ID, key)
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
            print("ERROR: The last character of your ID is not one of the possible sampling frequencies (A, Q, M, W, D, or H)"))

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

  doc <- httr::GET(url)

  date <- fromJSON(content(doc, "text"))$response$data$period
  values <- as.numeric(fromJSON(content(doc, "text"))$response$data$value)
  if(length(values) == 0)
  {
  values <- as.numeric(fromJSON(content(doc, "text"))$response$data$price)
  }

  date <- as.Date(paste(as.character(date), "-12-31", sep=""), "%Y-%m-%d")

  xts_data <- xts(values, order.by=date)
  names(xts_data) <- sapply(strsplit(ID, "-"), paste, collapse = ".")

  temp <- assign(sapply(strsplit(ID, "-"), paste, collapse = "."), xts_data)
  return(temp)
}

