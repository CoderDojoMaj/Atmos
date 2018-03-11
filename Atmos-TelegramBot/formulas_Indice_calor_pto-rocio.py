def celsius_to_fahrenheit(c):
    'Degrees Celsius (C) to degrees Fahrenheit (F)'
    return (c * 1.8) + 32.0

def fahrenheit_to_celsius(f):
    'Degrees Fahrenheit (F) to degrees Celsius (C)'
    return (f - 32.0) * 0.555556



def calc_heat_index(temp, hum):
    '''
    calculates the heat index based upon temperature (in C) and humidity.
    http://www.srh.noaa.gov/bmx/tables/heat_index.html

    returns the heat index in degrees C.
    '''
    temp = celsius_to_fahrenheit(temp)

    if (temp < 80):
        return fahrenheit_to_celsius(temp)
    else:
        out = -42.379 + 2.04901523 * temp + 10.14333127 * hum - 0.22475541 * \
               temp * hum - 6.83783 * (10 ** -3) * (temp ** 2) - 5.481717 * \
               (10 ** -2) * (hum ** 2) + 1.22874 * (10 ** -3) * (temp ** 2) * \
               hum + 8.5282 * (10 ** -4) * temp * (hum ** 2) - 1.99 * \
               (10 ** -6) * (temp ** 2) * (hum ** 2)

        return fahrenheit_to_celsius(out)


def calc_dewpoint(temp, hum):
    '''
    calculates the dewpoint via the formula from weatherwise.org
    return the dewpoint in degrees C.
    '''

    x = 1 - 0.01 * hum;

    dewpoint = (14.55 + 0.114 * temp) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * temp) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * temp) * x ** 14;
    dewpoint = temp - dewpoint;

    return dewpoint