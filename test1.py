#! /usr/bin/env python3

import pandas as pd


class DataProcessing:
    
    def __init__(self, datafile, ftype='csv'):
        self.fl = datafile

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
        True

    def process(self):
        filter_ = self.df.apply(self.filter, axis='columns')
        ##df_filtered = self.df[filter_]
        df_filtered = self.df
        
        for row_ in df_filtered:
            yield row_
        
    





def usage(error=None):
    if error is not None:
        print ("Failed: {0}\n".format(error))
    print ("Usage:\n	{0} DATAFILE".format(sys.argv[0]))
    print ("Where:")
    print ("  DATAFILE: file in any of supported formats, such as: xlsx, csv")
    sys.exit(1)

if __name__ == "__main__":
    import sys

    ## Check for arguments:
    if len(sys.argv) == 1:
        usage()

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
        print(row_)

    ## 2. output result
