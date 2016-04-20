import re

def words(test_string):
    found_words = re.findall(r"((?:[0-9a-zA-z]+-)*[a-zA-Z]+)",test_string)
    if len(found_words) == 0:
        return None
    else:
        return found_words

def phone_number(test_string):
    matches = re.search(r"(\d{3})[\D]*(\d{3})[\D]*(\d{4})",test_string)
    if matches:
        return_dict = {}
        return_dict['area_code'] = matches.group(1)
        return_dict['number'] = matches.group(2)+'-'+matches.group(3)
        return return_dict
    else:
        return None

def money(test_string):
    matches = re.match(r"^(\D)(\d{1,3}(,?\d{3})*(\.\d{2})?)$",test_string)
    if matches:
        return_dict = {}
        return_dict["currency"] = matches.group(1)
        return_dict['amount'] = float(re.sub(',','',matches.group(2)))
        return return_dict
    else:
        return None

def zipcode(test_string):
    matches = re.match(r"^(\d{5})(-(\d{1,4}))?$",test_string)
    if matches:
        return_dict = {}
        return_dict["zip"] = matches.group(1)
        return_dict['plus4'] = matches.group(3)
        if return_dict["plus4"] is None or len(return_dict["plus4"]) == 4:
            return return_dict
    else:
        return None

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
    months = {'jan':1, 'january':1, 'feb':2, 'february':2, 'mar':3, 'march':3}#etc
    if matches:
        if len(matches.group(1)) ==4: #year month day ISO 8601
            return_dict = {}
            return_dict["year"] = int(matches.group(1))
            month_length[2] = length_of_feb(return_dict['year'])
            if len(matches.group(2)) <= 2:
                return_dict["month"] = int(matches.group(2))
            else:
                return None
            if len(matches.group(3)) <= 2:
                return_dict["day"] = int(matches.group(3))
            else:
                return None
            if return_dict['day'] > month_length[return_dict['month']]:
                return None
            return return_dict
        elif len(matches.group(3)) ==4: # month day year
            return_dict = {}
            if len(matches.group(1)) <= 2:
                return_dict["month"] = int(matches.group(1))
            else:
                return None
            if len(matches.group(2)) <= 2:
                return_dict["day"] = int(matches.group(2))
            else:
                return None
            return_dict["year"] = int(matches.group(3))
            month_length[2] = length_of_feb(return_dict['year'])
            if return_dict['day'] > month_length[return_dict['month']]:
                return None
            return return_dict
        else:
            return None
    else:
        matches = re.match(r"^(\d{4})\s([a-zA-Z]+)\s(\d{2})$",test_string) #year named-month day
        if matches:
            return_dict = {}
            return_dict['year'] = int(matches.group(1))
            if matches.group(2).lower() in months:
                return_dict["month"] = months[matches.group(2).lower()]
                return_dict['day'] = int(matches.group(3))
                month_length[2] = length_of_feb(return_dict['year'])
                if return_dict['day'] > month_length[return_dict['month']]:
                    return None
                return return_dict
        matches = re.match(r"([a-zA-Z]+)\.? (\d{1,2}),? (\d{4})$",test_string)
        if matches:
            return_dict = {}
            return_dict['year'] = int(matches.group(3))
            if matches.group(1).lower() in months:
                return_dict["month"] = months[matches.group(1).lower()]
                return_dict['day'] = int(matches.group(2))
                month_length[2] = length_of_feb(return_dict['year'])
                if return_dict['day'] > month_length[return_dict['month']]:
                    return None
                return return_dict
        return None

def address(test_string):
    matches = re.match(r"(?P<address>\d+[^,\n]+)[,\n]\s*(?P<city>[a-zA-Z ]+), (?P<state>(?:MS)|(?:AK)|(?:MT)|(?:NH)) (?P<zip>\d{5})(?:-(?P<plus4>\d{1,4}))?$",test_string)
    if matches:
        return matches.groupdict()
    else:
        return None

def email(test_string):
    matches = re.match(r"(?P<local>[\w\.]+)@(?P<domain>[\w]+\.[\w]+)$",test_string)
    if matches:
        return matches.groupdict()
    else:
        return None
