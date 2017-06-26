movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
              ["Graham Chapman", ["Michael Palin", "John Cleese",
                    "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)
#["The Holy Grail", 1975, "Terry Jones & Terry Gilliam",
#91,["Graham Chapman", ["Michael Palin", "John Cleese",
#"Terry Gilliam", "Eric Idle", "Terry Jones"]]] 
#選擇多行然後 command + / 就可以幫多行加＃

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)


print_lol(movies)
