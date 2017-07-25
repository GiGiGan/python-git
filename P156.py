mins = [1, 2, 3]
secs = [m * 60 for m in mins]
secs

meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
feet

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
upper

dirty = ["2-22", "2:22", "2.22"]
clean = [ [sanitize(t) for t in dirty]
clean

clean = [float(s) for s in clean]
clean

clean = [float(sanitize(t)) for t in ["2-22", "3:33", "4.44"]]
clean