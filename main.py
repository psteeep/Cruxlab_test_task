def main():
    numb_of_valid = 0
    f = open('passwords.txt', 'r')
    for line in f:
        num1 = line[7:].count(line[0])  # general number of the required character

        num_list = []
        num = ''
        for char in line:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    num_list.append(int(num))
                    num = ''
        if num != '':
            num_list.append(int(num))  # list of all numeric characters (first two are necessarily restriction)

        if num_list[1] >= num1 >= num_list[0]:  # check for restriction
            numb_of_valid += 1  # count of valid
    f.close()
    print(numb_of_valid)


if __name__ == "__main__":
    main()
