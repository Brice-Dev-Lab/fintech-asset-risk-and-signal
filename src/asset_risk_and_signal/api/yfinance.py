"""A module for interacting with Yahoo Finance API for asset risk and signal analysis."""
from typing import List

import yfinance as yf
from pandas import DataFrame


def multi_yfinance(tickers:list[str], start_date:str, end_date:str) -> DataFrame:
    """
    API call for multiple tickers

    Inputs
    ------
        tickers: list of strings with stock symbols
        start_date: string for the start date in the format 'YYYY-MM-DD'
        end_date: string for the end date in the format 'YYYY-MM-DD'

    Output:
        data: returns a pandas DataFrame

    Example:
        >>> multi_yfinance(['MSFT', 'GOOG', 'AAPL'], '2020-01-01', '2026-01-01')
    """
    # TODO: Create error validation
    #   Layer 1 (input validation):
    #       - is tickers a list
    #       - are all elements strings
    #       - is the list empty
    #       - bad format with date entry
    #   Layer 2 (try/except - external risk):
    #       - what to do if an invalid ticker is passed
    #       - API outages
    #       - empty dataframe (API worked but returned nothing
    #       - unexpected library behavior
    
    data: DataFrame = yf.download(tickers, start=start_date, end=end_date)
    return data
