import random


# size of the space is 100*100 and presented in integer form.

def initializing_points():
    paths_length_file = open('paths_length.txt', 'w')
    paths_length_file.write("")
    initializing_points_file = open('initializing_points.txt', 'w')
    initializing_points_file.write("")
    for i in range(1, 31):  # number of point is 30 point.
        num_1 = random.sample(range(1, 100), 1)
        num_2 = random.sample(range(0, 100), 1)
        data_set = {'id': i, "x": num_1[0], "y": num_2[0]}
        initializing_points_file = open('initializing_points.txt', 'a')
        initializing_points_file.write(str(data_set) + '\n')
    input("*** done ***")


def show_points():
    initializing_points_file = open('initializing_points.txt', 'r')
    data_set = initializing_points_file.read()
    print(data_set)
    return 1


def initializing_paths():
    paths_length_file = open('paths_length.txt', 'w')
    paths_length_file.write("")
    initializing_paths_file = open('initializing_paths.txt', 'w')
    initializing_paths_file.write("")
    print("please wait...")
    for i in range(0, 1001):
        data_set = []
        while len(data_set) < 30:
            num_1 = random.sample(range(1, 31), 1)
            if num_1 in data_set:
                pass
            else:
                data_set.append(num_1)
        initializing_paths_file = open('initializing_paths.txt', 'a')
        initializing_paths_file.write("{}){}\n".format(i + 1, data_set))
    input("*** done ***")


def show_paths():
    initializing_paths_file = open('initializing_paths.txt', 'r')
    data_set = initializing_paths_file.read()
    print("***\n" + data_set + "***")


def return_data(id_get):
    initializing_points_file = open('initializing_points.txt', 'r')
    for i in range(1, 31):
        data_set = initializing_points_file.readline()
        p_1, p_2, p_3 = data_set.split(",")
        p_1 = p_1.split(":")[1]
        if int(p_1) == id_get:
            p_2 = p_2.split(":")[1][1:]
            p_3 = p_3.split(":")[1]
            if len(p_3) == 5:
                p_3 = p_3[1:][:2]
            else:
                p_3 = p_3[1:][:1]
            return "{},{}".format(p_2, p_3)


def set_length(point_1, point_2):
    p_1 = return_data(point_1)
    p_2 = return_data(point_2)
    p_1_x, p_1_y = p_1.split(",")
    p_2_x, p_2_y = p_2.split(",")
    l = ((((int(p_1_x) - int(p_2_x)) ** 2) + ((int(p_1_y) - int(p_2_y)) ** 2)) ** (1 / 2))
    return l


def set_path_length():
    paths_length_file = open('paths_length.txt', 'w')
    paths_length_file.write("")
    initializing_paths_file = open('initializing_paths.txt', 'r')
    data_set = initializing_paths_file.read()
    for i in range(0, 1001):
        data = data_set.split("\n")[i]
        b = data.split(")")[1][2:]
        b = b[:(len(b) - 1)]
        l = 0
        for j in range(0, 29):
            c_1 = b.split(",")[j]
            if len(c_1) == 2:
                c_1 = c_1[:1]
            elif len(c_1) == 3:
                c_1 = c_1[:2]
            elif len(c_1) == 4:
                c_1 = c_1[2:][:1]
            elif len(c_1) == 5:
                c_1 = c_1[2:][:2]
            c_2 = b.split(",")[j + 1][2:]
            if len(c_2) == 2:
                c_2 = c_2[:1]
            elif len(c_2) == 3:
                c_2 = c_2[:2]
            l = l + set_length(int(c_1), int(c_2))
        paths_length_file = open('paths_length.txt', 'a')
        paths_length_file.write(str(i + 1) + ":" + str(l) + "\n")


test_path = [[7], [26], [8], [19], [16], [1], [10], [23], [13], [27], [30], [17], [12], [2], [9], [18], [25], [28],
             [11], [29], [24], [4], [22], [21], [20], [5], [6], [15], [3], [14]]


def test_length():
    paths_length_file = open('paths_length.txt', 'w')
    paths_length_file.write("")
    b = str(test_path[:(len(test_path))])
    b = b[:len(b) - 1]
    l = 0
    for i in range(0, 29):
        c_1 = b.split(",")[i]
        if len(c_1) == 2:
            c_1 = c_1[:1]
        elif len(c_1) == 3:
            c_1 = c_1[:2]
        elif len(c_1) == 4:
            c_1 = c_1[2:][:1]
        elif len(c_1) == 5:
            c_1 = c_1[2:][:2]
        c_2 = b.split(",")[i + 1][2:]
        if len(c_2) == 2:
            c_2 = c_2[:1]
        elif len(c_2) == 3:
            c_2 = c_2[:2]
        l = l + set_length(int(c_1), int(c_2))
    input(l)


def sort_clean_up():
    cleaned_paths_file = open('cleaned_paths.txt', 'w')
    cleaned_paths_file.write("")
    paths_length_file = open('paths_length.txt', 'r')
    top_path_founded_file = open('top_path_founded.txt', 'a')
    cleaned_paths_file = open('cleaned_paths.txt', 'a')
    data_set = paths_length_file.read()
    data_dict = {}
    data_list = []
    for i in range(0, 1000):
        data_id, data_length = (data_set.split("\n")[i]).split(":")
        data_dict[data_length] = data_id
    for key in sorted(data_dict):
        data_list.append("%s:%s" % (key, data_dict[key]))
    for i in range(0, 502):
        cleaned_paths_file.writelines(str(data_list[i]) + "\n")
    top_path_founded_file.writelines(str(data_list[0]))


def found_path(path_id):
    initializing_paths_file = open('initializing_paths.txt', 'r')
    for i in range(1, 1001):
        a, b = initializing_paths_file.readline().split(")")
        if int(path_id) == int(a):
            return b


def top_paths_founded():
    top_paths_founded_file = open('top_paths_founded.txt', 'w')
    top_paths_founded_file.write("")
    cleaned_paths_file = open('cleaned_paths.txt', 'r')
    for i in range(0, 502):
        path_id_1 = str(str(cleaned_paths_file.readline().split("\n")).split(",")[0].split(":")[1])
        path_id_2 = str(path_id_1)[:len(path_id_1) - 1]
        path_data = found_path(path_id_2)
        top_paths_founded_file.writelines(str(path_id_2) + ":" + str(path_data))


def syncing_edition():
    syncing_founded_file = open('syncing.txt', 'r')
    syncing_edition_write_file = open('syncing_edition.txt', 'w')
    syncing_edition_write_file.write("")
    syncing_edition_add_file = open('syncing_edition.txt', 'a')
    for i in range(0, 1000):
        data_1 = syncing_founded_file.readline().split("\n")
        data_2, data_3, data_4 = str(data_1).split("]]")
        data_21 = str(data_2).split(":[")[1]
        data_31 = str(data_3).split(":[")[1]
        data_22 = data_21 + "]"
        data_32 = data_31 + "]"
        b = data_22 + ", " + data_32
        syncing_edition_add_file.writelines(str(b) + "\n")


def syncing():
    syncing_file = open('syncing.txt', 'w')
    syncing_file.write("")
    top_paths_founded_file = open('top_paths_founded.txt', 'r')
    syncing_file = open('syncing.txt', 'a')
    a = []
    for i in range(0, 502):
        a.append(str(top_paths_founded_file.readline()))
    for j in range(0, 501):
        b = str(
            a[j].split("\n")[0] + a[j + 1].split("\n")[0] + "\n" + a[j].split("\n")[0] + a[j + 1].split("\n")[0] + "\n")
        syncing_file.write(b)
        j = j + 1


def replacement(type_id):
    if type_id == 1:
        syncing_edition_file = open('syncing_edition.txt', 'r')
        syncing_file = open('syncing.txt', 'w')
        syncing_file.write(syncing_edition_file.read())
        syncing_clear_file = open('syncing_edition.txt', 'w')
        syncing_clear_file.write("")
    elif type_id == 2:
        cleared_brackets_file = open('cleared_brackets.txt', 'r')
        syncing_file = open('syncing.txt', 'w')
        syncing_file.write(cleared_brackets_file.read())
        cleared_brackets_clear_file = open('cleared_brackets.txt', 'w')
        cleared_brackets_clear_file.write("")


def clear_brackets():
    syncing_file = open('syncing.txt', 'r')
    a = syncing_file.read()
    b = ""
    for i in range(0, len(a) - 1):
        if a[i] == "[" or a[i] == "]" or a[i] == " ":
            pass
        else:
            b = b + str(a[i])
    cleared_brackets_file = open('cleared_brackets.txt', 'w')
    cleared_brackets_file.write(b)


def gen_creation():
    second_generator_clear_file = open('second_generator.txt', 'w')
    second_generator_clear_file.write("")
    second_generator_file = open('second_generator.txt', 'a')
    syncing_file = open('syncing.txt', 'r')
    a = []
    for i_1 in range(0, 998):
        if i_1 % 2 == 1:
            pass
        else:
            a_1 = []
            a_2 = []
            line_4 = []
            line_5 = []
            line_6 = []
            line_7 = []
            for i in range(0, 502):
                a.append(syncing_file.readline().split("\n"))
            a_1.append(str(a[i_1][0]).split(","))
            a_2.append(str(a[i_1 + 2][0]).split(","))
            for j in range(0, 16):
                line_4.append(a_1[0][j])
            for k in range(0, 14):
                line_5.append(a_2[0][k])
            for l in range(16, 30):
                line_6.append(a_1[0][l])
            for m in range(14, 30):
                line_7.append(a_2[0][m])
            second_generator_file.writelines(str(i_1) + ")" + str(line_4 + line_5) + "\n")
            second_generator_file.writelines(str(i_1 + 1) + ")" + str(line_6 + line_7) + "\n")
            i_1 = i_1 + 2


if __name__ == '__main__':
    gen_creation()
    while True:
        chose_number = int(
            input("1)set points\n2)show points\n3)set path\n4)show paths\n5)start\n6)new generation\n==>"))
        if chose_number == 1:
            initializing_points()
        elif chose_number == 2:
            show_points()
        elif chose_number == 3:
            initializing_paths()
        elif chose_number == 4:
            show_paths()
        elif chose_number == 5:
            set_path_length()
            sort_clean_up()
            top_paths_founded()
            syncing()
            syncing_edition()
            replacement(1)
            clear_brackets()
            replacement(2)
        elif chose_number == 6:
            gen_creation()
