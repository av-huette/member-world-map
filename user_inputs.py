import os


def get_number_of_csvs():
    num = input('How many CSVs do you need to parse?\n')
    print('')
    return int(num)


def get_file_path():
    file_name = input('Type in file name (must be located in /samples/):\n')
    print('')
    curr_dir = os.getcwd()
    file_path = os.getcwd() + '/samples/' + file_name
    return file_path


def get_delimiter():
    delimiter = input('Which delimiter does the CSV use?\n')
    print('')
    if delimiter == '':
        delimiter = ','
    return delimiter


def get_codec():
    codec = input('Which codec does the CSV use? Hit Enter for \'utf-8\'\n')
    print('')
    if codec == '':
        codec = 'utf-8'
    return codec


def get_column_indices():
    print('In the following, enter the column numbers:\nNote: first column is 0. If column doesn\'t exist, hit Enter.')
    number = input('Number: ')
    street = input('Street: ')
    postal = input('Postal Code: ')
    city = input('City: ')
    country = input('Country: ')
    print('')
    return cast_array_to_int([number, street, postal, city, country])


def cast_array_to_int(array):
    # Does not handle faulty insertion!
    newArray = []
    for x in range(0,len(array)):
        item = array[x]
        if item != '':
            newArray.append(int(item))
    return newArray


def get_geocoder_from_user():
    geocoder = input('Which geocoder? Bing or default?\n')
    print('')
    if geocoder == 'Bing' or geocoder == 'bing':
        geocoder = 'bing'
    else:
        geocoder = ''
    return geocoder
