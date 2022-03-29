#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
'''
So, basically we want to set up a few tracking systems to measure the growth of the economy,
from as many different perspectives as possible. 
One, would be tracking the rate of growth of individual accounts. Because the ETH testnet
application doesn't allow us to pick the scope of the .csv download, this will require us to 
manually redownload the file at a specific date every time we want new information. It also 
will require the creation of a library of dataframes..
'''


# In[5]:


# Setting up the two files and importing them as dataframes

# REMEMBER THAT YOU MANUALLY CLEANED THE ONE **Holders** FILE AKA 'Address Book(1)'

# Holders is our manually created record of addresses and names
# Import
Holders=pd.read_csv('HubCoin Address Book & Achievement List - Address Book(1).csv', thousands=',')

# Make sure the hex addresses are lowercase (for some reason they aren't universal in case -_-)
Holders['ADDRESSES'] = Holders['ADDRESSES'].str.lower()

# Line up the addresses (this may be redundant as I iterate through to find the right address...may change later)
Holders = Holders.sort_values(by='ADDRESSES')

# Useless Column
Holders.drop('Achievements',axis=1,inplace=True)
# Take a loook-seeeee:
#Holders.head(5)


# AddressBook is actually our downloaded csv from etherscan containing balances and hex addresses
ESRecords = pd.read_csv('tokenholders32022.csv')
ESRecords['HolderAddress'] = ESRecords['HolderAddress'].str.lower()
ESRecords.drop('PendingBalanceUpdate',axis=1,inplace=True)
#ESRecords.head(5)


# In[6]:


Holders.head()


# In[8]:


# Let's just make everything into lists LOL
# List of names
namlist = Holders['Player Name'].tolist()
addlist = Holders['ADDRESSES'].tolist()

Logbook = dict(zip(namlist, addlist))
addressBalanceDict = list(zip(ESRecords.HolderAddress, ESRecords.Balance.apply(str)))


# In[18]:



NameBalance = {}

# The following function prints the name, balance, and hex address of all accounts
def CheckAll():

    for key,value in addressBalanceDict:
        for x in Logbook:
            if key == Logbook[x]:
                #d1 = (x,value)
                #print(d1)
                NameBalance[x]= value
            
                print(x)
                print("BALANCE:    " + value + '\r\nADDRESS:    ' + key + '\r\n')
            
            else:

                pass
# run once to populate NameBalance dict   
CheckAll()


# In[16]:




# The following function takes a name and returns the balance
def GetBalanceByName():
    name = input(">name? ")
    for x in NameBalance:
        if x == name:
            print(NameBalance[x])
        
#GetBalanceByName()


# In[ ]:




