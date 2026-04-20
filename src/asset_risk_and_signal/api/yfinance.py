"""A module for interacting with Yahoo Finance API for asset risk and signal analysis."""
import pandas as pd
import yfinance as yf
import datetime
from pandas import DataFrame


def load_yfinance(tickers:list[str], start_date:str, end_date:str) -> DataFrame:
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
        >>> load_yfinance(['MSFT', 'GOOG', 'AAPL'], '2020-01-01', '2026-01-01')
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
    #       - empty dataframe (API worked but returned nothing)
    #       - unexpected library behavior

    # NOTE: Layer 1 validation checks
    if not isinstance(tickers,list):
        raise TypeError("tickers must be passed as a list")
    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise TypeError("Start and end dates must be a string")
    if not tickers:
        raise ValueError("List of tickers must not be empty")
    for item in tickers:
        if not isinstance(item, str):
            raise TypeError("All tickers must be strings")
    # parse date strings
    date_format:str = '%Y-%m-%d' # %Y -> 4-digit year, %y -> 2-digit year

    try:
        s_date = datetime.datetime.strptime(start_date, date_format)
        e_date = datetime.datetime.strptime(end_date, date_format)
    except ValueError:
        raise ValueError("Invalid date or incorrect format. Format to be YYYY-MM-DD")

    # validation that start and end dates are not flipped
    if s_date > e_date:
        raise ValueError("Start date must be before end date")

    # NOTE: Layer 2 validation checks & API logic
    try:
        data: DataFrame = yf.download(tickers, start=s_date, end=e_date)
    except Exception as e:
        raise RuntimeError("Failed to fetch market data") from e

    # validate dataframe content
    if data.empty:
        raise ValueError("API returned no data")

    return data
