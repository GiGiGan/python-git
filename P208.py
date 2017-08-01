def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

class AthleteList(list):
    
    def __int__(self, a_name, a_dob=None, a_times=[]):
        list__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return(sorted(set([snaitize(t) for t in self]))[0:3])

  def get_coach_data(filename):
        try:
            with open(filename) as f:
                 data = f.readline()
            templ = data.strip().split(",")
            return(Athlete(templ.pop(0), templ.pop(0), templ))
        except IOError as ioerr:
            print("File error:" + str(ioerr))
            return(None)

james = get_coach_data("james2.txt")
juile = get_coach_data("juile2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

print(james["Name"] + "'s fastest times are: " + james["Times"])
print(juile["Name"] + "'s fastest times are: " + juile["Times"])
print(mikey["Name"] + "'s fastest times are: " + mikey["Times"])
print(sarah["Name"] + "'s fastest times are: " + sarah["Times"])