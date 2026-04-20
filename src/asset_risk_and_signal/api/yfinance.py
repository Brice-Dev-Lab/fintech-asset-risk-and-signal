"""A module for interacting with Yahoo Finance API for asset risk and signal analysis."""
from jedi.inference.helpers import is_string
from lib2to3.fixer_util import is_list
from typing import List

import yfinance as yf
from IPython.utils.wildcard import is_type
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
    if not isinstance(tickers,list):
        raise TypeError("tickers must be passed as a list")
    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise TypeError("Start and end dates must be a string")
    if len(tickers) == 0:
        raise ValueError("List of tickers must not be empty")
    for item in tickers:
        if not isinstance(item, str):
            raise TypeError("All tickers must be a string")


    data: DataFrame = yf.download(tickers, start=start_date, end=end_date)
    return data
