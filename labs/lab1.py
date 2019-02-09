# reads the contents of the file and returns a list of lines
def read_numbers(filename):
    number_lst = []
    file = open(filename)
    for line in file:
        number_lst.append(line[:-1])
    
    return number_lst

# takes a number in a free format and returns the standard form xxx-xxx-xxxx
def standardize(phone_number):
    phone_number = phone_number.replace('-','')
    standard_phone_number = ""
    for digit in phone_number:
        if digit.isdigit() == False:
            digit = key_map[digit]
        standard_phone_number = standard_phone_number + digit
    standard_phone_number = standard_phone_number[:3] + "-" + standard_phone_number[3:6] + "-" + standard_phone_number[6:10]
    
    return standard_phone_number

# takes a phone number in the standard form and returns the sum of its digits
def sum_of_digits(phone_number):
    sum_val = 0
    for num in phone_number:
        if num.isdigit() == True:
            sum_val = sum_val + int(num)
    
    return sum_val

# takes a list of phone numbers and returns the highest sum of digits
def find_highest_sum(phone_list):
    sum_of_all_numbers = []
    for elem in phone_list:
        sum_of_all_numbers.append(sum_of_digits(elem))
    highest = max(sum_of_all_numbers)
    return highest

key_map = {'A':'2', 'B':'2', 'C':'2',
           'D':'3', 'E':'3', 'F':'3',
           'G':'4', 'H':'4', 'I':'4',
           'J':'5', 'K':'5', 'L':'5',
           'M':'6', 'N':'6', 'O':'6',
           'P':'7', 'Q':'7', 'R':'7', 'S':'7',
           'T':'8', 'U':'8', 'V':'8',
           'W':'9', 'X':'9', 'Y':'9', 'Z':'9',
           }

# main program

phone_list = read_numbers("phones.txt")

phone_list = [ standardize(x) for x in phone_list ]
  
highest_sum = find_highest_sum(phone_list)

for number in phone_list:
    if sum_of_digits(number) == highest_sum:
        print(number, '*')
    else:
        print(number)

