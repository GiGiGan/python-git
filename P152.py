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

clean_james ＝ []
clean_juile = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in juile:
    clean_juile.append(sanitize(each_t))
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print（sorted(clean_james))
print（sorted(clean_juile))
print（sorted(clean_mikey))
print（sorted(clean_sarah))