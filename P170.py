def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)
    
with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split('.')

with open('juile.txt') as juf:
    data = juf.readline()
juile = data.strip().split('.')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split('.')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split('.')

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip(.).split(","))
    except IOError as ioerr:
        print("File error:" + str(error))
        return(name)

sarah = get_coach_data("sarah.txt")
#指定所要處理檔案名稱