import re

def binary(test_string):
    return re.search(r"^[01]+$",test_string)


def binary_even(test_string):
    return re.search(r"^[01]*0$",test_string)


def hex(test_string):
    return re.search(r"^[0-9ABDCEF]+$",test_string)


def word(test_string):
    return re.search(r"^([0-9a-zA-z]+-)*[a-zA-Z]+$",test_string)

def words(test_string,count = None):
    words_found = re.findall(r"([0-9a-zA-z]+-)*[a-zA-Z]+",test_string)
    if count is None:
        return words_found
    else:
        return len(words_found) == count

def phone_number(test_string):
    return re.match(r"^(\D)*\d{3}(\D)*\d{3}(\D)*\d{4}",test_string)

def money(test_string):
    return re.match(r"^\$\d{1,3}(,?\d{3})*(\.\d{2})?$",test_string)

def zipcode(test_string):
    return re.match(r"\d{5}(-\d{4})?$",test_string)

def length_of_feb(year):
    if year % 4 >0:
        return 28 #regular years
    elif year %100 >0:
        return 29 #regular leap years
    elif year % 1000 >0:
        return 28 #most centuries
    else:
        return 29 #millenia

def date(test_string):
        matches = re.match(r"^(\d+)\D(\d+)\D(\d+)$",test_string)
        month_length = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        months = ['jan', 'january', 'feb', 'february', 'mar', 'march']#etc
        if matches:
            if len(matches.group(1)) ==4: #year month day ISO 8601
                month_length[2] = length_of_feb(int(matches.group(1)))
                if int(matches.group(2)) > 12:
                    return None
                elif int(matches.group(3)) >month_length[int(matches.group(2))]:
                    return None
                else:
                    return True
            elif len(matches.group(3)) ==4: # month day year
                month_length[2] = length_of_feb(int(matches.group(3)))
                if int(matches.group(1)) > 12:
                    return None
                elif int(matches.group(2)) >month_length[int(matches.group(1))]:
                    return None
                else:
                    return True
            else:
                return None
        else:
            matches = re.match(r"^(\d{4})\s([a-zA-Z]+)\s(\d{2})$",test_string) #year named-month day
            if matches:
                if matches.group(2).lower() in months:
                    return True
            matches = re.match(r"([a-zA-Z]+)\.? (\d{1,2}),? (\d{4})$",test_string)
            if matches:
                if matches.group(1).lower() in months:
                    return True
            return None

def email(test_string):
    return re.match(r"[\w\.]+@[\w]+\.[\w]+$",test_string)

def address(test_string):
    return re.match(r"(?P<address>\d+[^,\n]+)[,\n]\s*(?P<city>[a-zA-Z ]+), (?P<state>(?:MS)|(?:AK)|(?:MT)|(?:NH)) (?P<zip>\d{5})(?:-(\d{1,4}))?$",test_string)
