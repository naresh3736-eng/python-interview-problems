def checkDistinctUppercaseEnglishCharacters(string):
    lookup = {}
    for char in string:
        if not checkUpperEnglishCharacter(char):
            return False
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1

    for key in lookup:
        if lookup[key] > 1:
            return False
    return True

def checkUpperEnglishCharacter(char):
    return char.isupper() and char.isalpha()

def checkValidYear(year):
    if not year.isdigit():
        return False
    return int(year) in set(range(1900, 2020))

def checkDenomination(denomination):
    valid_denominations = {"10", "20", "50", "100", "200", "500", "1000"}
    return denomination in valid_denominations

def checkValidSerial(serial):
    if len(serial) < 10 or len(serial) > 12:
        return "invalid"
    # if type(serial[3]) is not int:
    #     return "invalid"
    if not checkUpperEnglishCharacter(serial[-1]):
        return "invalid"
    serial = serial[0:len(serial) - 1]
    if not checkDistinctUppercaseEnglishCharacters(serial[0:3]):
        return "invalid"
    serial = serial[3:]
    if not checkValidYear(serial[0:4]):
        return "invalid"
    serial = serial[4:]
    if not checkDenomination(serial):
        return "invalid"
    if not serial.isdigit():
        return "invalid"
    return serial

def counterfietCurrency(serialNumbmer):
    total = 0
    if len(serialNumbmer) == 0:
        return "invalid"
    for serial in serialNumbmer:
        valid_serial = checkValidSerial(serial)
        if valid_serial != "invalid":
            total += int(valid_serial)
    return total



# print(checkDistinctUppercaseEnglishCharacters("ABC"))
# print(checkUpperEnglishCharacter('1'))

# test1 = ["AVG190420T", "RTF20001000Z", "QWER201850G", "AFA199620E", "ERT1947200T", "RTY20202004", "DRV1984500Y", "ETB2010400G"]
# test2 = ["A201550B", "ABB19991000Z", "XYZ200019Z", "ERF200220", "SCD203010T"]
test3 = ["ADB2012R20B", "RED190250E", "RFV201111T", "TYU20121000E", "AAA198710B", "AbC200010E"]
print counterfietCurrency(test3)