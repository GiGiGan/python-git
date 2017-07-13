try:
    with open('man_data.txt, 'w') as man_file:
        print(man, file=man_file)
    with open('other_data.txt, 'w') as other_file:
        print(other, file=other_file)
    except IOError as err:
        print('File Error:' + str(err))

    # with open('man_data.txt, 'w') as man_file, open('other_data.txt, 'w') as other_file:
    #     print(man, file=man_file)
    #     print(other, file=other_file)