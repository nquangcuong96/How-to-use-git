import math
import pygame as pg
import time

pg.mixer.init()
pg.init()
pg.display.init()

# method function
def takeSecond(elem):
    return elem[1]

def process_text(value):
    value = str(value)
    value = value.lower()
    remove_char = '!@#$%^&*(){}:;"?/><., ' + "'"
    for i in remove_char:
        value = value.replace(i,'')
    return value

# method variable
roman_ex = [('N',0),('I',1),('IV',4),('V',5),('IX',9),('X',10),('XL',40),('L',50),('XC',90),('C',100),('CD',400),('D',500),('CM',900),('M',1000)]
roman_char = 'NIVXLCDM'
piano_char = [('A','B'),('B','C'),('C','D'),('D','E'),('E','F'),('F','G'),('G','A')]




# waypoint 1
def hello(name):
    a = name.strip()
    ans = 'Hello ' + a + '!'
    return ans

# waypoint 2
def calculate_hypotenuse(x,y):
    return math.sqrt(pow(float(x),2)+pow(float(y),2))

# waypoint 3
def are_all_conditions_true(conditions):
    if not conditions:
        return None
    arr = [i for i in conditions if i == False]
    if len(arr)%2 == 1:
        return False
    else:
        return True

# waypoint 4
def is_a_condition_true(conditions):
    if not conditions:
        return None
    for i in conditions:
        if i == True:
            return True
    return False

# waypoint 5
def filter_integers_greater_than(lst,number):
    return [i for i in lst if i > number]

# waypoint 6
def find_cheapest_hotels(lst_hotel, price):
    arr = sorted([i for i in lst_hotel if i[1] <= price], key =takeSecond)
    return [x[0] for x in arr]

# waypoint 7
def calculate_euclidean_distance_between_2_points(p1,p2):
    return math.sqrt(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2))

# waypoint 8
def calculate_euclidean_distance_between_points(array):
    if not array or len(array) == 1:
        return 'ValueError: The list MUST contain at least 2 points'
    ans = 0
    for i in range(len(array)-1):
            ans += calculate_euclidean_distance_between_2_points(array[i],array[i+1])
    return ans

# waypoint 9
def capitalize_words(string):
    if not string:
        return  None
    if isinstance(string,str) == False:
        return "TypeError: Not a string"
    arr = string.split()
    if not arr:
        return ''
    ans = arr[0]
    for x in arr[1:]:
        ans += ' ' + x
    return ans.title()

# waypoint 10
def uppercase_lowercase_words(string):
    if not string:
        return None
    if isinstance(string,str) == False:
        return "TypeError: Not a string"
    arr = string.split()
    if not arr:
        return ''
    ans = arr[0].upper()
    for i in range(1,len(arr)):
        if i%2 == 1:
            ans += ' ' + arr[i].lower()
        else:
            ans += ' ' + arr[i].upper()
    return ans

# waypoint 11
def factorial(n):
    if isinstance(n,int) == False:
        return 'TypeError: Not an integer'
    if n < 0:
        return 'ValueError: Not a positive integer'
    ans = 1
    if n >= 1:
        for i in range(1,n+1):
            ans *= i
    return ans

#waypoint 12
def char_to_int(char):
    if isinstance(char,str) == False:
        return "TypeError: Not a string"
    if len(char) > 1:
        return 'ValueError: Not a single digit'
    if ord(char) < 48 or ord(char) > 57:
        return 'ValueError: This character is not a digit'
    return int(char)

#waypoint 13
def string_to_int(string):
    if isinstance(string,str) == False:
        return "TypeError: Not a string"
    for i in string:
        if ord(i) < 48 or ord(i) > 57:
            return 'ValueError: Not a positive integer string expression'
    return int(string)

#waypoint 14
def is_palindrome(value):
    value = process_text(value)
    for i in range(len(value)//2):
        if value[i] != value[-1-i]:
            return False
    return True

#waypoint 15
def roman_numeral_to_int(string):
    if isinstance(string,str) == False:
        return "TypeError: Not a string"
    ans = 0
    string = string + 'N'
    lens = len(string)
    for i in range(lens-1):
        for x in roman_char:
            if x == string[i]:
                is_true = True
                break
            is_true = False
        if is_true == False:
            return 'ValueError: Not a Roman numeral'
        sub_string = string[i]
        if sub_string + string[i+1] == 'IV' or sub_string + string[i+1] == 'IX' or sub_string + string[i+1] == 'XL' or sub_string + string[i+1] == 'XC' or sub_string + string[i+1] == 'CD' or sub_string + string[i+1] == 'CM':
            sub_string += string[i+1]
            string = string[:i+1] + string[i+2:] + 'N'
        for j in roman_ex:
            if sub_string == j[0]:
                ans += j[1]
    return ans

#waypoint 16
def play_melody(melody,sound_basedir):
    for i in melody:
        name = i
        if i[1] == '#':
            for j in piano_char:
                if i[0] == j[0]:
                    name = j[1] + 'b' + i[2]
        address = sound_basedir + '/' + name.lower() + '.ogg'
        sound = pg.mixer.Sound(address)
        sound.play()
        pg.time.wait(400)
