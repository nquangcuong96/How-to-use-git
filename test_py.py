import unittest
import python_basics as main

class MyTest(unittest.TestCase):
    def test_waypoint1(self):
        name = '        world             '
        self.assertEqual(main.hello(name),"Hello world!")
    def test_waypoint1a(self):
        name = '        world                                                               a'
        self.assertRaises(ValueError,main.hello,name)
    def test_waypoint2(self):
        a = 3
        b = 4
        self.assertEqual(main.calculate_hypotenuse(a,b),5.0)
    def test_waypoint3(self):
        condition = [[True, True, False, True, False, False, True],[True, True,True],[],None]
        ans = [False,True,None,None]
        for i in range(len(ans)):
            self.assertEqual(main.are_all_conditions_true(condition[i]),ans[i])
    def test_waypoint4(self):
        condition = [[],[False,False,False,False],[False,True,False,False,False,True]]
        ans = [None,False,True]
        for i in range(len(ans)):
            self.assertEqual(main.is_a_condition_true(condition[i]),ans[i])
    def test_waypoint5(self):
        l = [[0, 3, 5, -2, 9, 8],[0, 3, 5, -2, 9, 8]]
        a = [4,6]
        ans = [[5, 9, 8],[9, 8]]
        for i in range(len(a)):
            self.assertEqual(main.filter_integers_greater_than(l[i],a[i]),ans[i])
    def test_waypoint6(self):
        hotel_daily_rates = [[
            ('Majestic Saigon Hotel', 93),
            ('Hotel Grand Saigon', 80),
            ('Sofitel Saigon Plaza', 123),
            ('Hotel Continental', 62),
            ('Caravelle Hotel', 180),
            ('Sheraton Saigon Hotel', 216),
            ('Park Hyatt Saigon', 209)],
            [
                ('Majestic Saigon Hotel', 93),
                ('Hotel Grand Saigon', 80),
                ('Sofitel Saigon Plaza', 123),
                ('Hotel Continental', 62),
                ('Caravelle Hotel', 180),
                ('Sheraton Saigon Hotel', 216),
                ('Park Hyatt Saigon', 209)],
            [
                ('Majestic Saigon Hotel', 93),
                ('Hotel Grand Saigon', 80),
                ('Sofitel Saigon Plaza', 123),
                ('Hotel Continental', 62),
                ('Caravelle Hotel', 180),
                ('Sheraton Saigon Hotel', 216),
                ('Park Hyatt Saigon', 209)],
            [
                ('Majestic Saigon Hotel', 93.55),
                ('Hotel Grand Saigon', 93.56),
                ('Sofitel Saigon Plaza', 100),
                ('Hotel Continental', 93.55),
                ('Caravelle Hotel', 110),
                ('Sheraton Saigon Hotel', 93),
                ('Park Hyatt Saigon', 120)]
        ]
        price = [50,80,150,100]
        ans = [[],['Hotel Continental', 'Hotel Grand Saigon'],['Hotel Continental', 'Hotel Grand Saigon', 'Majestic Saigon Hotel', 'Sofitel Saigon Plaza'],['Sheraton Saigon Hotel','Majestic Saigon Hotel','Hotel Continental','Hotel Grand Saigon','Sofitel Saigon Plaza']]
        for i in range(len(price)):
            self.assertEqual(main.find_cheapest_hotels(hotel_daily_rates[i],price[i]),ans[i])
    def test_waypoint7(self):
        p1 = (1,1)
        p2 = (2,2)
        self.assertEqual(main.calculate_euclidean_distance_between_2_points(p1,p2),1.4142135623730951)
    def test_waypoint8(self):
        arr = [[(0, 0), (3, 4), (-1, -1)],[(0,0.5),(3.5,4.5),(-2.5,-3.5)]]
        ans = [11.403124237432849,15.315072906367325]
        for i in range(len(ans)):
            self.assertEqual(main.calculate_euclidean_distance_between_points(arr[i]),ans[i])
    def test_waypoint9(self):
        string = '       khong           co           gi quy hon        doc    lap   tu  do'
        self.assertEqual(main.capitalize_words(string),'Khong Co Gi Quy Hon Doc Lap Tu Do')
    def test_waypoint10(self):
        string = ['1 one two 2 3 three four 4 five six','   ',None]
        ans = ['1 one TWO 2 3 three FOUR 4 FIVE six','',None]
        for i in range(len(string)):
            self.assertEqual(main.uppercase_lowercase_words(string[i]),ans[i])
    def test_waypoint11(self):
        n = [5,0]
        ans = [120,1]
        for i in range(len(n)):
            self.assertEqual(main.factorial(n[i]),ans[i])
    def test_waypoint12(self):
        char = ['0','1','2','3','4','5','6','7','8','9']
        ans = [0,1,2,3,4,5,6,7,8,9]
        for i in range(len(char)):
            self.assertEqual(main.char_to_int(char[i]),ans[i])
    def test_waypoint13(self):
        string = ['17049171','123456789','987123654']
        ans = [17049171,123456789,987123654]
        for i in range(len(string)):
            self.assertEqual(main.string_to_int(string[i]),ans[i])
    def test_waypoint14a(self):
        value = ['madam','racecar',10801,1.947491,'A man, a plan, a canal, Panama!',"No 'x' in Nixon"]
        for i in value:
            self.assertEqual(main.is_palindrome(i),True)
    def test_waypoint14b(self):
        value = [" !!!!@@%$^$%&^**&)([],><!!!  ","   ","",'Hello, word!',1234,None]
        for i in value:
            self.assertEqual(main.is_palindrome(i),False)
    def test_waypoint15(self):
        value = ['XXXIX','CCXLVI','DCCLXXXIX','MMCDXXI','CLX','CCVII','MIX','MLXVI','MDCCLXXVI','MCMLIV','MMXIV','MMMCMXCIX']
        ans = [39,246,789,2421,160,207,1009,1066,1776,1954,2014,3999]
        for i in range(len(value)):
            self.assertEqual(main.roman_numeral_to_int(value[i]),ans[i])
    def test_waypoint15a(self):
        value = ['a','MXM','IXC','IIIIIIIIII','XXXXXXXXXX','DD','VV','LL','CCCCCCCCCC','LC','MLM','MIM','IVX','VX','IL','IC','IXI','IVIIIIII','IXABCD']
        for i in value:
            self.assertRaises(ValueError,main.roman_numeral_to_int,i)
    def test_waypoint15b(self):
        value = [[],12321321,21321.12321,None]
        for i in value:
            self.assertRaises(TypeError,main.roman_numeral_to_int,i)
    def test_waypoint16(self):
        MELODY_HAPPY_BIRTHDAY_TO_YOU = (
            'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
            'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
            'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
            'A#4', 'A#4', 'A4', 'F4', 'G4', 'F4',
        )
        addres = './sounds/piano'
        self.assertEqual(main.play_melody(MELODY_HAPPY_BIRTHDAY_TO_YOU,addres),['./sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/d4.ogg', './sounds/piano/c4.ogg', './sounds/piano/f4.ogg', './sounds/piano/e4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/d4.ogg', './sounds/piano/c4.ogg', './sounds/piano/g4.ogg', './sounds/piano/f4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c4.ogg', './sounds/piano/c5.ogg', './sounds/piano/a4.ogg', './sounds/piano/f4.ogg', './sounds/piano/e4.ogg', './sounds/piano/d4.ogg', './sounds/piano/bb4.ogg', './sounds/piano/bb4.ogg', './sounds/piano/a4.ogg', './sounds/piano/f4.ogg', './sounds/piano/g4.ogg', './sounds/piano/f4.ogg']
)

