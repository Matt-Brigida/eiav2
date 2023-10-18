# EIAv2

Python wrapper compatible with version 2 of the EIA's API.  To pull an energy series you'll have to know the Series ID from the version 1 API.  If you don't know the Series IDs for the data you want, do the following:

1.  Go to [EIA's Opendata website](https://www.eia.gov/opendata/).
2.  Go to the "Bulk File Downloads" by scrolling down a bit and looking on the right margin.
3.  Choose the bulk download for the category that contains the series you want.  Foe example if it is a Crude Oil series download the "Petroleum" file.
4.  After the file downloads unzip it and find the Series ID you want. 

Note you only have to do the above once to get the Series ID.

This package provides programmatic access to the Energy Information Administration's (EIA) API (See http://www.eia.gov/beta/api/).  There are currently over a million unique time series available through the API.  To use the package you'll need a *free* API key from here: http://www.eia.gov/beta/api/register.cfm

This package has one function `getEIA`.  It allows you to pull a time series (given by the series ID).  The resulting object is a pandas dataframe.  For example, assume you have read your api key as a string into `key`, you can pull a series with:

`getEIA(ID = 'ELEC.GEN.ALL-AK-99.A', key = key)`



