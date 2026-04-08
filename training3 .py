
import os
import json

data_text = "This is a text file created by Python"
file_path = "output.json"


try:
    with open(file_path,'r') as file:
            content = json.load(file)
            print(content["job"]) 
       
        

except FileNotFoundError:
    print(f"File '{file_path}' not found. Creating the file and writing data to it.")