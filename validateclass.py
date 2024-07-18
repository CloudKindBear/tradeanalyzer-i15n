import datetime

class Validator:
    DATETIME_FORMATS = [
        "%Y/%m/%d %H:%M",
        "%Y-%m-%d %H:%M",
        "%d/%m/%Y %H:%M",
        "%d-%m-%Y %H:%M",
        "%d-%m-%y %H:%M",
        "%Y/%m/%d",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%d-%m-%y",
    ]

    def __init__(self):
        self.attrs = []
        for attr in dir(self):
            if attr.startswith("validate_"):
                self.attrs.append(attr)
        

    def validate_datetime(self, data):
        for fmt in self.DATETIME_FORMATS:
            try:
                return datetime.datetime.strptime(data, fmt)
            except Exception as err:
                continue
        raise Exception("not a date field")



    def validate_int(self, data):
        return int(data)


    def validate_float(self, data):
        data = data.replace(",", ".")
        if not "." in data:
            raise Exception("no point in data")
        return float(data)


    def validate(self, data):

        for attr in self.attrs:
            try:
                return getattr(self, attr)(data)
            except Exception as err:
                ## print("Validate error: {0}".format(err))
                continue
        return data




class CustomObjects:

    def __init__(self):
        self.params = []
        self.validator = Validator()

    ## Store some data with validation:
    def store(self, data):
        data = self.validator.validate(data)
        self.params.append(data)



    ## Return human readable list of values:
    def _to_string_iter(self):
        for i in self.params:
           yield "    {0}:	{1}".format(i, type(i))

    ## Return human readable list of values:
    def to_string(self):
        return "\n".join( self._to_string_iter() )


if __name__ == "__main__":
    pass
