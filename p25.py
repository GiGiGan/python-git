movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
              ["Graham Chapman", ["Michael Palin", "John Cleese",
                    "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
#["The Holy Grail", 1975, "Terry Jones & Terry Gilliam",
#91,["Graham Chapman", ["Michael Palin", "John Cleese",
#"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

for each_item in movies:
    if isinstance(each_item, list):
        for nasted_item in each_item:
            if isinstance(nasted_item, list):
                for deeper_item in nasted_item:
                    print(deeper_item)
            else:
                print(nasted_item)
    else:
        print(each_item)
