# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import time
    def generator():
        for i in range(100000000):
            yield i

    start_time = time.time()

    for i in generator():
        pass

    end_time = time.time()

    print(end_time - start_time)

    start_time = time.time()
    for i in list(range(100000000)):
        pass

    end_time = time.time()
    print(end_time - start_time)

    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
