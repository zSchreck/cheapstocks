import pandas as pd

if __name__ == '__main__':
    dataframe = pd.read_csv("cashmoney.csv")
    print dataframe.describe()

