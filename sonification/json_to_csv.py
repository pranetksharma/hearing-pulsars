#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 17:28:54 2023
@author: sanjanaiyer

"""

import json 
import csv
#import plotly.graph_objects as go
#import plotly.io as pio

data_entries = []

#1
file_path = "1-GBT820drift_57561_100626+2000_DM115.90_Z0_ACCEL_Cand_3.pfd.json"

my_dict1 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list
def convert_to_float(nested_list):
    if isinstance(nested_list, list):
        return [convert_to_float(item) for item in nested_list]
    else:
        return float(nested_list)

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict1["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers
def convert_to_float(nested_list):
    if isinstance(nested_list, list):
        return [convert_to_float(item) for item in nested_list]
    else:
        return float(nested_list)
    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict1["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict1["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict1["DMc"] = DMc

#print(my_dict1)
data_entries.append(my_dict1)



#2
file_path = "2-GBT820drift_57561_100626+2000_DM12.50_Z0_ACCEL_Cand_1.pfd.json"

my_dict2 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict2["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict2["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict2["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict2["DMc"] = DMc

#print(my_dict2)
data_entries.append(my_dict2)


#3
file_path = "3-GBT820drift_57561_100626+2000_DM122.60_Z0_ACCEL_Cand_2.pfd.json"

my_dict3 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict3["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict3["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict2["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict3["DMc"] = DMc

#print(my_dict3)
data_entries.append(my_dict3)

#4
file_path = "4-GBT820drift_57561_100626+2000_DM138.40_Z0_ACCEL_Cand_2.pfd.json"

my_dict4 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict4["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict4["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict4["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict4["DMc"] = DMc

#print(my_dict4)
data_entries.append(my_dict4)



#5
file_path = "5-GBT820drift_57561_100626+2000_DM138.50_Z0_ACCEL_Cand_3.pfd.json"

my_dict5 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict5["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict5["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict5["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict5["DMc"] = DMc

#print(my_dict5)
data_entries.append(my_dict5)


#6
file_path = "6-GBT820drift_57561_100626+2000_DM14.10_Z0_ACCEL_Cand_1.pfd.json"

my_dict6 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict6["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict6["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict6["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict5["DMc"] = DMc

#print(my_dict6)
data_entries.append(my_dict6)


#7
file_path = "7-GBT820drift_57561_100626+2000_DM148.40_Z0_ACCEL_Cand_1.pfd.json"

my_dict7 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict7["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict7["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict7["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict7["DMc"] = DMc

#print(my_dict7)
data_entries.append(my_dict7)


#8
file_path = "8-GBT820drift_57561_100626+2000_DM155.90_Z0_ACCEL_Cand_1.pfd.json"

my_dict8 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict8["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict8["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict8["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict8["DMc"] = DMc

#print(my_dict8)
data_entries.append(my_dict8)


#9
file_path = "9-GBT820drift_57561_100626+2000_DM156.50_Z0_ACCEL_Cand_1.pfd.json"

my_dict9 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict9["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict9["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict9["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict9["DMc"] = DMc

#print(my_dict9)
data_entries.append(my_dict9)


#10
file_path = "10-GBT820drift_57561_100626+2000_DM186.30_Z0_ACCEL_Cand_1.pfd.json"

my_dict10 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict10["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict10["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict10["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict10["DMc"] = DMc

#print(my_dict10)
data_entries.append(my_dict10)


#11
file_path = "11-GBT820drift_57561_100626+2000_DM239.30_Z0_ACCEL_Cand_1.pfd.json"

my_dict11 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict11["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict11["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict11["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict11["DMc"] = DMc

#print(my_dict11)
data_entries.append(my_dict11)



#12
file_path = "12-GBT820drift_57561_100626+2000_DM243.70_Z0_ACCEL_Cand_2.pfd.json"

my_dict12 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict12["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict12["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict12["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict12["DMc"] = DMc

#print(my_dict12)
data_entries.append(my_dict12)


#13
file_path = "13-GBT820drift_57561_100626+2000_DM248.50_Z0_ACCEL_Cand_1.pfd.json"

my_dict13 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict13["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers
  
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict13["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict13["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict13["DMc"] = DMc

#print(my_dict13)
data_entries.append(my_dict13)


#14
file_path = "14-GBT820drift_57561_100626+2000_DM27.60_Z0_ACCEL_Cand_1.pfd.json"

my_dict14 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict14["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict14["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict14["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict14["DMc"] = DMc

#print(my_dict14)
data_entries.append(my_dict14)


#15
file_path = "15-GBT820drift_57561_100626+2000_DM3.00_Z0_ACCEL_Cand_6.pfd.json"

my_dict15 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict15["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict15["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict15["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict15["DMc"] = DMc

#print(my_dict15)
data_entries.append(my_dict15)


#16
file_path = "16-GBT820drift_57561_100626+2000_DM3.40_Z0_ACCEL_Cand_5.pfd.json"

my_dict16 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict16["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict16["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict16["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict16["DMc"] = DMc

#print(my_dict16)
data_entries.append(my_dict16)


#17
file_path = "17-GBT820drift_57561_100626+2000_DM3.60_Z0_ACCEL_Cand_4.pfd.json"

my_dict17 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict17["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict17["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict17["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict17["DMc"] = DMc

#print(my_dict17)
data_entries.append(my_dict17)


#18
file_path = "18-GBT820drift_57561_100626+2000_DM3.70_Z0_ACCEL_Cand_1.pfd.json"

my_dict18 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict18["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict18["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict18["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict18["DMc"] = DMc

#print(my_dict18)
data_entries.append(my_dict18)


#19
file_path = "19-GBT820drift_57561_100626+2000_DM306.20_Z0_ACCEL_Cand_2.pfd.json"

my_dict19 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict19["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict19["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict19["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict19["DMc"] = DMc

#print(my_dict19)
data_entries.append(my_dict19)


#20
file_path = "20-GBT820drift_57561_100626+2000_DM307.70_Z0_ACCEL_Cand_1.pfd.json"

my_dict20 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict20["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict20["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict20["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict20["DMc"] = DMc

#print(my_dict20)
data_entries.append(my_dict20)

#21
file_path = "21-GBT820drift_57561_100626+2000_DM327.10_Z0_ACCEL_Cand_2.pfd.json"

my_dict21 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict21["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict21["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict21["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict21["DMc"] = DMc

#print(my_dict21)
data_entries.append(my_dict21)



#22
file_path = "22-GBT820drift_57561_100626+2000_DM356.30_Z0_ACCEL_Cand_3.pfd.json"

my_dict22 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict22["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict22["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict22["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict22["DMc"] = DMc

#print(my_dict22)
data_entries.append(my_dict22)

#23
file_path = "23-GBT820drift_57561_100626+2000_DM356.80_Z0_ACCEL_Cand_1.pfd.json"

my_dict23 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict23["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers
  
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict23["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict23["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict23["DMc"] = DMc

#print(my_dict23)
data_entries.append(my_dict23)

#24
file_path = "24-GBT820drift_57561_100626+2000_DM37.90_Z0_ACCEL_Cand_3.pfd.json"

my_dict24 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict24["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers
  
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict24["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict24["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict24["DMc"] = DMc

#print(my_dict24)
data_entries.append(my_dict24)

#25
file_path = "25-GBT820drift_57561_100626+2000_DM374.20_Z0_ACCEL_Cand_1.pfd.json"

my_dict25 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict25["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict25["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict25["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict25["DMc"] = DMc

#print(my_dict25)
data_entries.append(my_dict25)

#26
file_path = "26-GBT820drift_57561_100626+2000_DM5.80_Z0_ACCEL_Cand_6.pfd.json"

my_dict26 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict26["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict26["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict26["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict26["DMc"] = DMc

#print(my_dict26)
data_entries.append(my_dict26)

#27
file_path = "27-GBT820drift_57561_100626+2000_DM586.00_Z0_ACCEL_Cand_3.pfd.json"

my_dict27 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict27["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

    
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict27["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict27["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict27["DMc"] = DMc

#print(my_dict27)
data_entries.append(my_dict27)

#28
file_path = "28-GBT820drift_57561_100626+2000_DM677.40_Z0_ACCEL_Cand_2.pfd.json"

my_dict28 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict28["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict28["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict28["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict28["DMc"] = DMc

#print(my_dict28)
data_entries.append(my_dict28)

#29
file_path = "29-GBT820drift_57561_100626+2000_DM76.70_Z0_ACCEL_Cand_1.pfd.json"

my_dict29 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list


nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict29["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers

# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict29["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict29["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict29["DMc"] = DMc

#print(my_dict29)
data_entries.append(my_dict29)


#30
file_path = "30-GBT820drift_57561_100626+2000_DM88.20_Z0_ACCEL_Cand_1.pfd.json"

my_dict30 = {}

#TVP!!
#extracting TvP from the nested list
with open(file_path) as file:
    nested_list = json.load(file)
TvP_list = nested_list.get("TvP")

#aggregating the values in the nested TvP list

nested_list = convert_to_float(TvP_list)

# making a new list to store those summed values
summed_TvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    summed_TvP.append(list_sum)

# adding the summed TvP list to the dictionary
my_dict30["TvP"] = summed_TvP

# FVP!!
with open(file_path) as file:
    data = json.load(file)
nested_list = data["FvP"]

# convert nested list file elements to integers
 
     
# nested list with float values 
nested_list = convert_to_float(nested_list)

# new list to store the summed values
FvP = []

# iterate, calculate, and add the sum of each inner list to the new lists
for inner_list in nested_list:
    list_sum = sum(inner_list)
    FvP.append(list_sum)

my_dict30["FvP"] = FvP

#PROFILE!!
# extracting profile from the nested list
key_to_extract = "profile"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("profile")

profile = nested_list["profile"]
my_dict30["profile"] = profile

#DMC!!
# extracting DMc from the nested_list
key_to_extract = "DMc"
with open(file_path) as file:
    nested_list = json.load(file)
selected_list = nested_list.get("DMc")

DMc = nested_list["DMc"]
my_dict30["DMc"] = DMc

#print(my_dict30)
data_entries.append(my_dict30)




#make csv file
filename = 'my_dicts.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data_entries[0].keys())  # Write the header row
    for entry in data_entries:
        writer.writerow(entry.values())  # Write the values of each entry
        
print(f'{filename} created successfully.')
