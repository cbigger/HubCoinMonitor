#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import csv
import discord.py
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# HubCoinMonitor jupyter notebook

#******************************************************************************
# Setting up the two files and importing them as dataframes


# REMEMBER THAT YOU MANUALLY CLEANED THE ONE **Holders** FILE AKA 'Address Book'
# For you guys that means you need to remove everything from the first file that isn't a 
# valid entry (the titles that are in the spreadsheet need to be deleted)
# DON'T DELETE THE COLUMN NAMES, JUST THE OTHER THINGS

# Holders is our manually created record of addresses and names
# Import **** <<<<< THIS FILENAME SHOULDN'T NEED CHANGING BUT DOUBLE-CHECK >>>>>  
Holders=pd.read_csv('HubCoin Address Book & Achievement List - Address Book.csv', thousands=',')
# Make sure the hex addresses are lowercase (for some reason they aren't universal in case -_-)
Holders['ADDRESSES'] = Holders['ADDRESSES'].str.lower()
# Line up the addresses (this may be redundant as I iterate through to find the right address...may change later)
Holders = Holders.sort_values(by='ADDRESSES')
# Useless Column
Holders.drop('Achievements',axis=1,inplace=True)
# Take a loook-seeeee:
#Holders.head(5)


# AddressBook is actually our downloaded csv from etherscan containing balances and hex addresses
# Import 2 ***** <<<<< THIS FILENAME ALMOST CERTAINLY NEEDS CHANGING >>>>
Records = pd.read_csv('tokenholders32022.csv')
Records['HolderAddress'] = Records['HolderAddress'].str.lower()
Records.drop('PendingBalanceUpdate',axis=1,inplace=True)
#ESRecords.head(5)

# ******************************************************************************

# Let's just make everything into lists LOL
# We are creating two dictionaries: one of name:address pairs, and one of address:balance pairs
# List of names
namlist = Holders['Player Name'].tolist()
addlist = Holders['ADDRESSES'].tolist()
logBook = {}
logBook = dict(zip(namlist, addlist))
invlogBook = {v: k for k, v in logBook.items()}
# Same thing but on the other side with a one liner because fuck you
addressBalance = list(zip(Records.HolderAddress, Records.Balance.apply(str)))


# Create a dictionary to put our name:balance pairs into
nameBalance = {}

# The following function prints the name, balance, and hex address of all accounts, and populates the nameBalance dict
for key,value in addressBalance:
        for x in logBook:
            if key == logBook[x]:
                #d1 = (x,value)
                #print(d1)
                nameBalance[x]= value
            
                #print(x)
                #print("BALANCE:    " + value + '\r\nADDRESS:    ' + key + '\r\n')
            
            else:
                pass

def PrintAll():

    for key,value in addressBalance:
        for x in logBook:
            if key == logBook[x]:
                #d1 = (x,value)
                #print(d1)
                nameBalance[x]= value
            
                print(x)
                print("BALANCE:    " + value + '\r\nADDRESS:    ' + key + '\r\n')
            
            else:
                pass

# run once to populate nameBalance dict   
#PrintAll()
# create and populate a reverse dict (fuk u I like dictionaries)
invNameBalance = {}
invNameBalance = {v: k for k, v in nameBalance.items()}


# In[3]:


# The following function takes a name and returns the balance in their address
def GetBalanceByName():
    name = input(">name? ")
    for x in nameBalance:
        if x == name:
            print(nameBalance[x])
        else:
            pass
GetBalanceByName()


# In[4]:


def GetBalanceByAddress():
    address = input(">address? ")
    for key in logBook:
        if address == logBook[key]:
            print(nameBalance[key])


# In[5]:


GetBalanceByAddress()


# In[6]:


def GetAccountInfo():
    search = input(">Enter a name or hex address: ")
    for x in logBook:
        if x == search:
            print(x + "\r\nBALANCE:    " + nameBalance[x] + "\r\nADDRESS:    " + logBook[search]  )
        else:
            pass
    for x in invlogBook:
        if x == search:
            name = invlogBook[search]
            print(name + "\r\nBALANCE:    " + nameBalance[name] + "\r\nADDRESS:    " + logBook[name] )
        else:
            pass


# In[7]:


GetAccountInfo()


# In[ ]:





# In[ ]:




