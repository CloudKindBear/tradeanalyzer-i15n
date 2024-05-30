#! /usr/bin/env python3

from libdp import DataProcessing

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
        print(row_['date'], row_['price'])

