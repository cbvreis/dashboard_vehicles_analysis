import pandas as pd

def process_data(df):
    '''
    Convet date pandas to weekday name
    :param df: dataframe pandas
    :return: dataframe pandas
    '''
    df['Data'] = pd.to_datetime(df['Data'],format='%Y-%m-%d %H:%M:%S.%f')
    df['Weekday'] = df['Data'].dt.day_name()
    df['Month'] = df['Data'].dt.month_name()
    df['Weekyear'] = df['Data'].dt.weekofyear
    df = df[df['Diff Km'] > 20]
    return df