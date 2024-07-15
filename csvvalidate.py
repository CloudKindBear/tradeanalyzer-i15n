#! /usr/bin/env python3

import csv
import sys


def validate_int(val):
    return int(val)

def validate_float(val):
    return float(val)

def validate_kontragent(val):
    ## Example:
    if val == 'BBB':
        ## Don't use this row in result dataset:
        raise Exception("Wrong value")
    ## Example:
    val += ' AAA'
    return val



def validate_kontragent_id(val):
    ## Example:
    if val is None or len(val.strip()) == 0:
        ## Don't use this row in result dataset:
        raise Exception("Can not be empty")
    return val


def validate(row_src, header):
    is_empty = True
    row = []
    for col in row_src:
        if col is not None and len(col.strip()) > 0:
            is_empty = False
        col_clear = col.strip()
        row.append(col_clear)

    ## Don't use this row in result dataset:
    if is_empty:
        return None


    ##row[1] = validate_kontragent(row[1])
    ##row[2] = validate_kontragent_id(row[2])
    row[7] = validate_float(row[7])
    row[8] = validate_float(row[8])

    return row


def usage(mesg=None):
    print ("Usage: ")
    print ("	{0} CSV_SOURCE CSV_RESULT".format(sys.argv[0]))
    print ("Where:")
    print ("	CSV_SOURCE - source csv file to validate")
    print ("	CSV_RESULT - new correct validated CSV file")
    if mesg is not None:
        print()
        print(mesg)
    sys.exit(1)
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()

    with open(sys.argv[1], newline='') as csvsrc:
        csv_r = csv.reader(csvsrc, delimiter=',', quotechar='"')

        with open(sys.argv[2], 'w', newline='') as csvswc:
            csv_w = csv.writer(csvswc, delimiter=',', quotechar='"')

            header = None
            for row in csv_r:
                if header is None:
                    header = row
                    csv_w.writerow(row)
                    continue
                try:
                    row = validate(row, header)
                except Exception as err:
                    row = None
                if row is None:
                    continue
                csv_w.writerow(row)
    sys.exit(0)
