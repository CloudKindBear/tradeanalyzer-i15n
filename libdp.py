#! /usr/bin/env python3

import pandas as pd


class DataProcessing:
    
    def __init__(self, datafile, ftype='csv', dont_make_df=False):
        self.fl = datafile

        if not dont_make_df:
            self.make_dataframe(ftype)


    def make_dataframe(self, ftype):
        ## Check that used supported format of file
        ## For process file of some selected format, we should use some sutable function
        ## of pandas software framework;
        ## Let's check that the attribute is exist in our class for prepearing used format:
        attr_name = "ftype_prepare__{0}".format(ftype)
        if not hasattr(self, attr_name):
            raise Exception("Unsupported format")

        ## Dataframe object attribute: (It will calls method: ftype_prepare__{0})
        self.df = getattr(self, attr_name)()


    ## TODO:
    ## 2. make processing method
    ## 3. get filtered columns
    ## 4. make overridable methods for filtering anything we want
    ## 5. filter processing data and yield it to user

    ## Returns DataFrame by CSV format:
    def ftype_prepare__csv(self):
       return pd.read_csv(self.fl)

    ## Returns DataFrame by XLSX format:
    def ftype_prepare__xlsx(self):
       return pd.read_excel(self.fl)


    def filter(self, col):
        return col['price'] > 350

    def process(self):
        filter_ = self.df.apply(self.filter, axis='columns')
        df_filtered = self.df[filter_]

        for i, row_ in df_filtered.iterrows():
            yield row_
        
    





## WARNING!!!  Don't modify lines below! It's only example of class usage

if __name__ == "__main__":
    import sys

    ## Get the path to datafile and check it extention:
    data_file = sys.argv[1]
    ftype='csv'
    if data_file.endswith('.csv'):
        pass
    elif data_file.endswith('.xlsx'):
        ftype='xlsx'
    else:
        usage("Unsupported format!")

    print("Working with file: {0}".format(data_file))

    ## Create our dataprocessing instance:
    dp = DataProcessing(data_file, ftype=ftype)

    ## TODO:
    ## 1. process data by class iterator
    for row_ in dp.process():
        print(row_['date'], row_['price'])

