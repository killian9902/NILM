from msilib import Directory
import os
import datetime
import pandas as pd






# FUNCITON: Convert Unix timestamp to UTC datetime
def convert_unix_to_utc_datetime(unix_time):
    return datetime.datetime.utcfromtimestamp(float(unix_time))



#FUNCTION: Convert Watts per x time to kWh
def kWh(df):

    # Find kW & how long readings represent (6-8 secs)
    df['kW'] = df['Watts']/1000
    df['Elapsed Time'] = df['DateTime'].diff()

    # Handle null values
    default_timedelta = pd.to_timedelta('0 days 00:00:06')
    df['Elapsed Time'].fillna(default_timedelta, inplace=True)

    # Convert seconds to int & find kWh
    df['Elapsed Time'] = df['Elapsed Time'].dt.total_seconds().astype(int)
    df['sec/hour'] = df['Elapsed Time'] / 3600
    df['kWh'] = df['kW'] * df['sec/hour']

    # Add column for Wh
    df['Wh'] = df['kWh'] * 1000

    
    return df


def clean_data(input_file, output_file):
    
    # INGEST DATA: Change house & type below
    file_path = input_file

    column_names = ["DateTime", "Watts"]
    df = pd.read_csv(file_path, delimiter=' ', usecols=[0,1], converters={0: convert_unix_to_utc_datetime}, header=None, names=column_names)


    # SELECT TIMEFRAME
    start_date = pd.Timestamp('2013-04-12')
    end_date = pd.Timestamp('2015-01-05')
    df = df[(df['DateTime'] >= start_date) & (df['DateTime'] <= end_date)]

    # Watt to kWh
    df = kWh(df)

    # CHANGE TO 15 MIN READINGS
    df.set_index('DateTime', inplace=True)
    df = df.resample('15T').sum()


    # EXPORT DATA: Change house & type below
    file_path = output_file
    df.to_csv(file_path, index=True)




# Change directory below
input_directory = "INPUT DIRECTORY HERE/NILM AI/UK-DALE DB/house_1"
output_directory = "INPUT DIRECTORY HERE/NILM AI/UK-DALE CLEAN/H1"

for filename in os.listdir(input_directory):
    

    if filename.endswith(".dat"):

        if ('button_press' not in filename) and (filename != 'labels.dat'):

            
            # OUTPUT FILE
            input_file = input_directory + '/' + filename

            # INPUT FILE: change .dat to .csv
            file_root, file_extension = os.path.splitext(filename)
            out_filename = file_root + '.csv'
            output_file = output_directory + '/' + out_filename

    
            clean_data(input_file,output_file)