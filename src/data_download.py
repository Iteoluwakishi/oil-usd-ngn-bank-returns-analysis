import yfinance as yf
import pandas as pd

def download_data():
    start_date = "2014-01-01"
    end_date = "2024-12-31"

    oil = yf.download("BZ=F", start=start_date, end=end_date)
    usdngn = yf.download("NGN=X", start=start_date, end=end_date)

    oil.to_csv("data/oil_prices.csv")
    usdngn.to_csv("data/usd_ngn.csv")

    print("Data downloaded successfully.")

if __name__ == "__main__":
    download_data()
