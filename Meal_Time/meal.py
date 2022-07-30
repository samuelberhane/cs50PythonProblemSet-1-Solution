def main():
    time_input = input('What time is it? ')
    time = convert(time_input)
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')


def convert(time):
    hr, min = time.split(':')
    min = float(min) / 60
    min = round(min,2)
    hr = float(hr)
    hr_fraction = hr + min
    return hr_fraction
