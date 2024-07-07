import os.path


def get_cats_info(path):
    list_dict_cat = []
    if os.path.exists(path):
        with open(path) as fh:
            list_unit = fh.readlines()
            for row in list_unit:
                dict_cat = {}
                row = (row.split(','))
                try:
                    dict_cat['id'] = row[0]
                    dict_cat['name'] = row[1]
                    if row[2].isdigit():
                        dict_cat['age'] = row[2]
                    else:
                        dict_cat['age'] = row[2][:-1]
                except IndexError:
                    print(f'{path} List is out of range')
                list_dict_cat.append(dict_cat)
        return list_dict_cat
    print(f'{path} to file is not found.')
    exit()


if __name__ == '__main__':
    cats_info = get_cats_info('second_example.txt')
    print(cats_info)
