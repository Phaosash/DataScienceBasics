import pandas as pd

class DataManager:
    #   This is the default constructor which loads the data from the csv file, then calls
    #   the method to clean out any bad data.
    def __init__(self, file_path="./Data/data.csv"):
        self.health_data = pd.read_csv(file_path, header = 0, sep = ",")
        self.clean_the_Data()

    #   This function is used to return the data that has been loaded.
    def get_loaded_data (self):
        return self.health_data
    
    #   This method is used to clean out invalid data entries from the data.
    def clean_the_Data (self):
        self.health_data.dropna(axis=0, inplace=True)

        for col in self.health_data.columns:
            self.health_data[col] = pd.to_numeric(self.health_data[col], errors='coerce')
        
        self.health_data.dropna(axis=0, inplace=True)

        self.health_data.reset_index(drop=True, inplace=True)
