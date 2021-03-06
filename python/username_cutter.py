# For USF SAIL
# ~Mihir

import pandas as pd
import glob
import os

#read the multiple csv file where only first one keeps the header, rest are pushed below, -1 header

interesting_files = glob.glob("RawCSV_firstBatch/*.csv") #please update the path accordingly! eg. folder/*.csv

# make a list of files names
df_list = []

#parse each file, but only select the username columns, and keep stacking them (much effiecient)
for filename in sorted(interesting_files):
    df_list.append(pd.read_csv(filename, usecols=['user_screen_name', 'lang']))

#join all the list
full_df = pd.concat(df_list)

#Modify the full_df to only keep en lang account
full_df= full_df.loc[full_df['lang'] == 'en']

#drop the lang column from full_df
full_df= full_df.drop('lang', 1)

#-------------------------------

#we will clear the file where we only keep the unique entries

#print('pre-clean: ')
#print(full_df.shape) #check pre clean rows output: (rows, column)

# keep only unique usernames
full_df = full_df.drop_duplicates('user_screen_name')

full_df.to_csv('mihir_output_NEW.csv', sep=',', index= False) #you can name your file whatever you want

##now very important to release the RAM mem back (do this only if you uncommented 52-58)
##del full_df

## print('post-clean: ')
## print(full_df.shape) #check post clean rows output: (rows, column)

#------------------------------

#now we will cut the final file by rows until last row is reached
#
# file_dir = os.path.dirname(os.path.abspath(__file__))
# csv_folder = 'cleanusrnms_firstbatch'
# os.makedirs(csv_folder) #creates a folder for you automatically
# csv_folder = csv_folder + '/'
#
# for i,chunk in enumerate(pd.read_csv('output.csv', chunksize= 17200)):
#     chunk.to_csv(csv_folder+'chunk{}.csv'.format(i), index=False)