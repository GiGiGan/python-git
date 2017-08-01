class Athlete:
    def __int__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    def get_coach_data(filename):
        try:
            with open(filename) as f:
                 data = f.readline()
            templ = data.strip().split(",")
            return(Athlete(templ.pop(o), templ.pop(0), templ))
        except IOError as ioerr:
            print("File error:" + str(ioerr))

james = get_coach_data("james2.txt")
juile = get_coach_data("juile2.txt")
mikey = get_coach_data("mikey2.txt")
sarah = get_coach_data("sarah2.txt")

print(james["Name"] + "'s fastest times are: " + james["Times"])
print(juile["Name"] + "'s fastest times are: " + juile["Times"])
print(mikey["Name"] + "'s fastest times are: " + mikey["Times"])
print(sarah["Name"] + "'s fastest times are: " + sarah["Times"])