# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:48:12 2017

@author: Tuyen
"""

# Pandas Introduction 

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

# Import data

## Lung Capacity dataset 

lungcap=pd.read_csv("https://raw.githubusercontent.com/tuyenhavan/Statistics/Dataset/LungCapData.csv",sep=";")

## Movie ranking dataset

movie=pd.read_csv("https://raw.githubusercontent.com/tuyenhavan/Statistics/Dataset/Movie-Ratings.csv",sep=",")

## Flight dataset

flight=pd.read_csv("https://raw.githubusercontent.com/tuyenhavan/Statistics/Dataset/flights.csv",sep=",")
# Check the data : moview

movie.head()

movie.shape

movie.dtypes

movie.info()

movie.mean() # Calculate only numeric variables

# Due to space in column names

movie.columns # space between words and % contained

# Remove those spaces

movie.columns=movie.columns.str.replace(" ","_")

movie.head() # This is still a lot of typing 

# Another way to rename columns

movie=movie.rename(columns={"Rotten_Tomatoes_Ratings_%":"Rotten_Ratings",
                      "Audience_Ratings_%":"Audience_Ratings",
                      "Budget_(million_$)":"Budget","Year_of_release":"Year"})

movie.head()

# Calculate some descritive statistics

movie.mean()

movie.describe() # provide only numeric statistics

movie.describe(include=["object"]) # Provide only object statistics (categorical)

movie.Genre.value_counts(dropna=False) # counts by Genre including Missing values if represent

# flight dataset

flight.head()

flight.shape

flight.describe(include=["object"])

flight.CancellationCode.value_counts(dropna=False) # We see the missing data

# Identify missing data

flight[flight.CancellationCode=="A"].head()

flight.describe()

# Get all 'distance>2000'

flight[flight.Distance>2000].head()

sns.boxplot(x=flight.UniqueCarrier,y=flight.Distance)

flight.CancellationCode.unique()

# ungcap dataset

sns.boxplot(x="Gender",y="LungCap",data=lungcap,hue="Gender") # Using seaborn package

lungcap.boxplot(column="LungCap",by="Gender",rot=70) # using matplotlib package

# Scatter plot

plt.scatter(x=lungcap.Age[lungcap.Gender=="male"],y=lungcap.LungCap[lungcap.Gender=="male"],c="blue",label="Male")

plt.scatter(x=lungcap.Age[lungcap.Gender=="female"],y=lungcap.LungCap[lungcap.Gender=="female"],c="red",label="Female")

plt.xlabel("Age")

plt.ylabel("Lung Capacity")

plt.title("Scatter Plot")

plt.legend(loc="lower right")

## Tidying data for analysis

df={"Name":["Ha","Van","Tuyen"],"Type A":[12,13,14],"Type B":[23,24,25]}

df=pd.DataFrame(df) # wide data

df.head()

# Tidy this data as follow 

## wide data to long data

df_wide=pd.melt(frame=df,id_vars="Name",value_vars=["Type A","Type B"],var_name="Type",value_name="Result")

df_wide.head()
## long data to wide data

df_pivot=df_wide.pivot(index="Name",columns="Type",values="Result") # Without duplicates

df_pivot.head()

df_long=df_wide.pivot_table(columns="Type",values="Result",aggfunc=np.mean,index="Name") # with duplicates


df_long

## Another example

df={"Name":["Van","Na","Ha","Ka"],"Year":[2000,2000,2000,2000],"m012":[0,2,52,12],"m1524":[0,4,12,15]}

df=pd.DataFrame(df)

df.head() # create a new column from existing data

df=df.melt(id_vars=["Name","Year"])

df.head() # variable contains both "male" and age range, so seperate them apart

df["Sex"]=df.variable.str[0] # get the first value from ` variable` column

df.head()

df["Age_Group"]=df.variable.str[1:] # get all values after the first value

df.head()

df["Range"]=df.Age_Group.str.split("-")

df.head()

df["Get"]=df.Age_Group.str.get(2)

df.head()

# Concate data 

a={"Name":["Ha","Van","Tuyen"],"Age":[23,24,26]}

a=pd.DataFrame(a)

a

b={"Name":["Tri","Tuong","Ha"],"Age":[12,13,14]}

b=pd.DataFrame(b)

b

# Concat two seperate dataset by rows

my_df=pd.concat([a,b],ignore_index=True)

my_df

# Concat two seperate dataset by columns

c={"Name":["Ha","Van","Tuyen"],"Age":[23,24,26]}

c=pd.DataFrame(c)

c

d={"Call":["Tri","Tuong","Ha"],"ID":[12,13,14]}

d=pd.DataFrame(d)

my_newdf=pd.concat([c,d],axis=1)

my_newdf

# Read multiple `csv` files using glob package

import glob as glob

csv_files=glob.glob("*.csv")


print(csv_files)

