import math
def parabola(x):
	return x ** 2

def a_triangle(x, y) :
        return x * y / 2
def a_trapezium(x, y, z) :
        return (x+y) * z / 2
def a_rectangle(x, y) :
        return x * y
def a_square(x) :
        return x ** 2
pi = 3.1415985945
def a_circle(r) :
        return pi *  r ** 2
def p_circle(r) :
        return 2 * pi * r
def v_prism(x, y, z) :
        return a_rectangle(x, y) * z
def add(x, y):
        return x+y
print('hello \n how \n are\t you')
name = input('What is your name: ')
Phone = input('What is the brand name of your phone: ')
print(name, 'has', Phone)


def temp_phone(num):
        """(number) -> str

        Returns the comment on the temperature of phone input
        """
        if num == 24.0:
               return 'Perfect weather to carry a phone!'
        elif num > 24.0:
               return 'make sure your phone does not melt off due to the heat'
        else:
               return 'Where are you; South pole or North pole'



def convert_to_celsius(fahrenheit):
   ''' (number) -> float
   
   Return the number of Celsius degrees equivalent to fahrenheit degrees.
   
   >>> convert_to_ccelsius(32)
   0.0
   >>> convert_to_celsius(212)
   100.0
   '''
   
   return (fahrenheit - 32) * 5 / 9

def p_triangle(x, y, z):
  '''(number, number, number) -> number
  Returns the perimeter of a triangle with sides x, y, z
  >>>p_triangle(1, 2, 3)
  6
  >>>p_triangle(2, 3, 4)
  9
  '''
  return x + y + z

def semi_p_triangle(x, y, z):
  '''(number, number, number) -> float

  Returns the semiperimeter of a triangle of sides x, y, z

  >>>semi_p_triangle(1, 2, 3)
  3
  >>>semi_p_triangle(4, 5.5, 7)
  8.25
  '''
  return p_triangle(x, y, z) / 2



def a_triangle_HF(x, y, z):
        """(number, number, number) -> float

        Returns the area of a triangle with three sides: x, y, z using Heron's
        Formula
        >>>a_triangle_HF(3, 4, 5)
        6.0"""
        semi = semi_p_triangle(x, y, z)
        area = math.sqrt(semi * (semi - x) * (semi - y) * (semi - z))
        return area


def find_vowel(letter):
        """(str) -> bool

        Returns if the given letter is vowel or not

        >>> find_vowel(e)
        True
        >>> find_vowel(y)
        False"""
        return letter in 'aeiou'

def count_vowels(word):
        """ (str) -> int

        Returns the number of vowels in a given word.
        >>> count_vowels('xyz')
        0
        >>> count_vowels('hi there')
        3"""
        num_vowels = 0;
        for letter in word:
                if letter in 'aeiouAEIOU':
                        num_vowels = num_vowels + 1
        return num_vowels


def display_vowels(word):
        """ (str) -> str

        Returns the vowels inside the given word.
        >>> display_vowels('serty')
        'e'
        >>> display_vowels('xyz')
        ''
        >>> display_vowels('hi there')
        'iee'"""
        vowels = ''
        for letter in word:
                if letter in 'aeiouAEIOU':
                        vowels = vowels + letter
        return vowels
                
def up_to_vowel(word):
        """ (str) -> str

        Return all the letters before a vowel is encountered in the word.

        >>> up_to_vowel('heeelo')
        'h'
        >>> up_to_vowel('xyz')
        'xyz'
        """
        first_consonants = ''
        i = 0
        while i < len(word) and not word[i] in 'aeiouAEIOU':
                first_consonants = first_consonants + word[i]
                i = i + 1
        return first_consonants

def up_to_consonant(word):
        """ str -> str

        Return all vowels until an consonant is encountered in the word.

        >>> up_to_consonant('eeel')
        'eee'
        >>> up_to_consonant('heelo')
        ''
        """
        first_vowels = ''
        i = 0
        while i < len(word) and word[i] in 'aeiouAEIOU':
                first_vowels = first_vowels + word[i]
                i = i + 1
        return first_vowels

def first_vowel(word):
        """ (str) -> str

        Return the first vowel in the word.

        >>> first_vowel('hello')
        'e'
        >>> first_vowel('htrgrdvddnarigero')
        'a'
        """
        i = 0
        while i < len(word):
                if word[i] in 'aeiouAEIOU':
                        return word[i]
                else:
                        i = i + 1
        return None

def display_vowels_while(word):
        """ (str) -> str

        Return the vowels in a word.

        >>> display_vowels_while('hello')
        'eo'
        >>> display_vowels_while('xyz')
        ''
        """
        vowels = ''
        i = 0
        while i < len(word):
                if word[i] in 'aeiouAEIOU':
                        vowels = vowels + word[i]
                        i = i + 1
                else:
                        i = i + 1
        return vowels

def last_vowel(word):
        """ (str) -> str

        Return the last vowel in a word.

        >>> last_vowel('hello')
        'o'
        >>> last_vowel('xyaz')
        'a'
        """
        i = len(word) - 1
        while i >= 0:
                if word[i] in 'aeiouAEIOU':
                        return word[i]
                else:
                        i = i - 1
        return 'None'
                
        
#Epico!
def sum_AP(start, end, step):
        """(number, number, number) -> number
        Return the sum of all numbers between start and end inclusive
        while increasing start by step(just like arithmetic progression)
        >>> sum_AP(1, 5, 1)
        15
        """
        sum_num = 0
        while start <= end:
                sum_num = sum_num + start
                start = start + step
        return sum_num

def sum_AP_for(start, end, step):
        """(number, number, number) -> number
        Return the sum of all numbers between start and end inclusive
        while increasing start by step(just like arithmetic progression)
        >>> sum_AP_for(1, 5, 1)
        15
        """
        sum_num = 0 
        for num in range(start, end + 1, step):
                sum_num = sum_num + num
        return sum_num
def count_adjacent_repeats_while(word):
        """ (str) -> int

        Return the number of repeats of adjacent letters in word.

        >>> count_adjacent_repeats_while('abbc')
        1
        """
        repeats = 0
        i = 0
        while i < len(word) - 1:
              if word[i] == word[i + 1]:
                      repeats = repeats + 1
                      i = i + 1
              else:
                      i = i + 1
        return repeats

def display_even_char(word):
        """ (str) -> str

        Return only the even characters the list called lis.(0, 2, 4...)

        >>> display_even_char('abcsfs')
        'acf'
        """
        even_char = ''
        for i in range(len(word)):
                if i % 2 == 0:
                        even_char = even_char + word[i]
        return even_char
                
def display_even_char_list(lis):
        """ (list) -> list

         Return only the even characters the list called lis.(0, 2, 4...)

        >>> display_even_char_list([1, 2, 5, 89])
        [1, 5]
        """
        even_char_l = []
        for i in range(len(lis)):
                if i % 2 == 0:
                        even_char_l.append(lis[i])
        return even_char_l
