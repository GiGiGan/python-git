class NamedList(list):
    def __inint__(self, a_name):
        list.__inint__([])
        self.name = a_name

johnny = NamedList("John Paul Jones")
type(johnny)

dir(johnny)

johnny.appen("Bass Player")
johnny.extend(["Composer", "Arrange", "Musician"])
johnny

johnny.name

for attr in johnny:
    print(johnny.name + " is a " + attr + ".")