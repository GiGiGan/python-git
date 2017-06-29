# """This is the "P30.py" module,and it provides one function called
# print_lol() which prints lists that may or may not include nested lists."""
def print_lol(the_list, level):
# # This function takes a postional argument called "the_list", which is any
# # Python list(of, possibly, nested list.). Each data item in the provided list 
# # is (recursively) printed to the screen on its owe line
# A second argument called "level" is used to insert tab-stops when a nested list is 
# encountered.
# #選擇多行然後 command + / 就可以幫多行加＃ 
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, leve+l)
        else:
            for tab_stop in range(level):
                #通過LEVEL的值來控制使用的跳格數
                    print("t", end=")
                    #為縮排的美一層顯示一個TAB字母
            print(each_item)