import random


# size of the space is 100*100 and presented in integer form.

def initializing_points():
    initializing_points_file = open('initializing_points.txt', 'w')
    initializing_points_file.write("")
    for i in range(1, 31):  # number of point is 30 point.
        num_1 = random.sample(range(0, 100), 1)
        num_1_1 = "".join(map(str, num_1))
        num_2 = random.sample(range(0, 100), 1)
        num_2_2 = "".join(map(str, num_2))
        initializing_points_file = open('initializing_points.txt', 'a')
        initializing_points_file.write("{}_{}_{}\n".format(i, num_1_1, num_2_2))
    print("*** done ***")


def show_points():
    initializing_points_file = open('initializing_points.txt', 'r')
    data_set = initializing_points_file.read()
    print("***\n" + data_set + "***")


def initializing_paths():
    initializing_paths_file = open('initializing_paths.txt', 'w')
    initializing_paths_file.write("")
    print("please wait...")
    for i in range(1, 1001):
        data_set = []
        while len(data_set) < 30:
            num_1 = random.sample(range(1, 31), 1)
            if num_1 in data_set:
                pass
            else:
                data_set.append(num_1)
        initializing_paths_file = open('initializing_paths.txt', 'a')
        initializing_paths_file.write("{}){}\n".format(i, data_set))
    print("*** done ***")


def show_paths():
    initializing_paths_file = open('initializing_paths.txt', 'r')
    data_set = initializing_paths_file.read()
    print("***\n" + data_set + "***")


if __name__ == '__main__':
    while True:
        chose_number = int(input("1)set points\n2)show points\n3)set path\n4)show paths\n==>"))
        if chose_number == 1:
            initializing_points()
        elif chose_number == 2:
            show_points()
        elif chose_number == 3:
            initializing_paths()
        elif chose_number == 4:
            show_paths()
