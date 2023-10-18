# EIAv2

Python wrapper compatible with version 2 of the EIA's API.  To pull an energy series you'll have to know the Series ID from the version 1 API.  If you don't know the Series IDs for the data you want, do the following:

1.  Go to [EIA's Opendata website](https://www.eia.gov/opendata/).
2.  Go to the "Bulk File Downloads" by scrolling down a bit and looking on the right margin.
3.  Choose the bulk download for the category that contains the series you want.  Foe example if it is a Crude Oil series download the "Petroleum" file.
4.  After the file downloads unzip it and find the Series ID you want. 

Note you only have to do the above once to get the Series ID.

This package provides programmatic access to the Energy Information Administration's (EIA) API (See http://www.eia.gov/beta/api/).  There are currently over a million unique time series available through the API.  To use the package you'll need a *free* API key from here: http://www.eia.gov/beta/api/register.cfm

This package has one function `getEIA`.  It allows you to pull a time series (given by the series ID).  The resulting object is a pandas dataframe.  For example, assume you have read your api key as a string into `key`, you can pull a series with:

`getEIA(ID = 'EBA.TVA-ALL.D.HL', key = key)`

which returns:

```
                          respondent             respondent-name type type-name  value    value-units
period                                                                                               
2023-10-18 16:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16355  megawatthours
2023-10-18 15:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16279  megawatthours
2023-10-18 14:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16281  megawatthours
2023-10-18 13:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16422  megawatthours
2023-10-18 12:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16390  megawatthours
...                              ...                         ...  ...       ...    ...            ...
2023-03-24 13:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16607  megawatthours
2023-03-24 12:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16449  megawatthours
2023-03-24 11:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16536  megawatthours
2023-03-24 10:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  16183  megawatthours
2023-03-24 09:00:00-05:00        TVA  Tennessee Valley Authority    D    Demand  15849  megawatthours

[5000 rows x 6 columns]
```
