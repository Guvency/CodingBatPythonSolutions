CodingBat Python Solutions

== Warmup-1 ==


sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

monkey_trouble 
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  return False

sum_double 
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
  if a != b:
    return a + b
  else:
    return (a+b)*2

diff21 
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n-21)*2

parrot_trouble
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
    else:
      return False
  else:
    return False

makes10 
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
  if a == 10 or b == 10 or a+b == 10:
    return True
  else:
    return False

near_hundred 
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n) <= 10

pos_neg 	 
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if (a < 0 and b > 0) or (a > 0 and b < 0):
      return True
    else:
      return False

not_string 
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str

missing_char 
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  spam = ""
  for egg in range(len(str)):
    if egg == n:
      continue
    else:
      spam += str[egg]
  return spam

front_back 	
Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) >= 2:
    spam = str[1:len(str)-1]
    return str[len(str)-1] + spam + str[0]
  else:
    return str

front3 
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
  spam = str[:3]
  return spam + spam + spam


== Warmup-2 ==


string_times  
Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  spam = ""
  for i in range(n):
    spam += str
  return spam

front_times 
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  spam = len(str)
  egg = ""
  
  if spam < 3:
    
    for i in range(n):
      egg += str
      
  else:
    
    for i in range(n):
      egg += str[:3]
    
  return egg

string_bits
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  eggs = len(str)
  spam = ""
  for egg in range(eggs):
    
    if egg % 2 == 0:
      spam += str[egg]
  
  return spam
    
string_splosion
Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  eggs = len(str)
  spam = ""
  
  for egg in range(eggs):
    
    for pol in range(egg+1):
      
      spam += str[pol]
  
  return spam
   
last2
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  
  eggs = len(str)
  
  spam = str[-2:]
  
  count = 0
  
  for egg in range(1,eggs-1):
    
    if spam == str[egg-1:egg+1]:
      count += 1
      
  return count

array_count9
Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  
  count = 0
  
  for egg in range(len(nums)):
    
    if 9 == nums[egg]:
      
      count += 1
      
  return count

array_front9
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  eggs = len(nums)
  
  if eggs <= 4:
    
    return 9 in nums
    
  else:
    
    return 9 in nums[:4]
  
array123
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  for x in range(len(nums)-2):
    if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3:
      return True
  return False
  
string_match 
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  
  eggs = min(len(a),len(b))
  
  count = 0
  
  spam_a = ""
  spam_b = ""
  
  for i in range(eggs-1):
    
    spam_a = a[i:i+2]
    spam_b = b[i:i+2]
    
    if spam_a == spam_b:
      
      count += 1
  
  return count


== String-1 ==


hello_name
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
  
  return "Hello " + name + "!"

make_abba
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

def make_abba(a, b):
  return a + b + b + a

make_tags
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

make_out_word
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  return out[:2] + word + out[2:]

extra_end	
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
  return str[-2:]*3

first_two
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[:2]

first_half
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
  half = len(str) / 2
  return str[:half]

without_end	
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
  last = len(str) - 1
  return str[1:last]

combo_string
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  return a + b + a

non_start
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
  return a[1:] + b[1:]

left2
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
  return str[2:] + str[:2]


== List-1 ==


first_last6 
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  return 6 == nums[0] or 6 == nums[len(nums)-1]

same_first_last
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

make_pi
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

def make_pi():
  return [3,1,4]

common_end
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

sum3	 
Given an array of ints length 3, return the sum of all the elements.

def sum3(nums):
  return sum(nums)

rotate_left3
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  temp = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = temp
  return nums
#return nums[1:] + nums[:1]

reverse3
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
  return nums[::-1]

max_end3
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

def max_end3(nums):
  spam = max(nums[0],nums[2])
  return [spam,spam,spam]

sum2
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  if len(nums) <= 2:
    return sum(nums)
  else:
    return sum(nums[:2])

middle_way	 
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
  return [a[1],b[1]]

make_ends
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

def make_ends(nums):
    return [nums[0],nums[-1]]


has23
Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False


== Logic-1 ==


cigar_party  
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60
     
date_fashion 
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
  if you < 3 or date < 3:
    return 0
  elif you > 7 or date > 7:
    return 2
  else:
    return 1

squirrel_play
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
  if is_summer:
    if temp > 59 and temp < 101:
      return True
    else:
      return False
  else:
    if temp > 59 and temp < 91:
      return True
    else:
      return False

caught_speeding	 
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed < 66:
      return 0
    elif speed < 86:
      return 1
    else:
      return 2
  else:
    if speed < 61:
      return 0
    elif speed < 81:
      return 1
    else:
      return 2

sorta_sum	 
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
  egg = a + b
  if egg >= 10 and egg <= 19:
    return 20
  else:
    return egg

alarm_clock
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
  if vacation:
    if day % 6 == 0:
      return "off"
    else:
      return "10:00"
  else:
    if day % 6 == 0:
      return "10:00"
    else:
      return "7:00"
     

love6	 
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

def love6(a, b):
  if a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6:
    return True
  else:
    return False

in1to10	 
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return n >= 1 and n <= 10

near_ten
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

def near_ten(num):
  if num%10 <= 2 or num%10 >= 8 :
    return True
  else:
    return False


== Logic-2 ==


make_bricks	 
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
  
  spam = goal // 5
  
  if spam > big:
    spam = big
    
  newGoal = goal - spam * 5
  
  return small >= newGoal

lone_sum	
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  sum = 0
  
  if a != b and a != c: 
    sum += a
  if a != b and b != c: 
    sum += b
  if c != b and a != c: 
    sum += c
  
  return sum
  
lucky_sum
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  else:
    return a + b + c

no_teen_sum	
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


def fix_teen(n):
  if 12 < n < 20 and (n != 15 and n != 16):
      n = 0
  return n

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

round_sum	 
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

def round10(num):
  if num % 10 < 5:
    return num - (num%10)
  else:
    return ((num // 10) + 1) * 10
    
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

close_far
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  ab = abs(a - b)
  bc = abs(b - c)
  ac = abs(a - c)
  
  if bc > 1:
    if (ab <= 1 and ac != 1) or (ab != 1 and ac <= 1):
      return True
  
  return False

make_chocolate
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  
  spam = goal // 5
  
  if big < spam:
    spam = big
    
  newGoal = goal - spam * 5
  
  if small < newGoal:
    return -1
  
  return newGoal


== String-2 ==


double_char
Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  spam = ""
  for i in range(len(str)):
    spam += str[i] * 2
  return spam

count_hi 	
Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if "hi" == str[i:i+2]:
      count += 1
  return count

cat_dog
Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  
  countCat = 0
  countDog = 0

  for i in range(len(str)-2):
    
    if "cat" == str[i:i+3]:
       countCat += 1
    if "dog" == str[i:i+3]:
       countDog += 1
  
  if countDog == countCat:
    return True
  
  return False

count_code	
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  
  count = 0
  
  for i in range(len(str)-3):
    
    if str[i:i+2] == "co" and str[i+3] == "e":
      count += 1
      
  return count
      
end_other
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  
   newA = a.lower()
   newB = b.lower()
  
   
   la = len(a)
   lb = len(b)
   
   spam = min(la,lb)
   
   if spam == la:
     return newB.endswith(newA)
   return newA.endswith(newB)

xyz_there
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  
  return str.count("xyz") > str.count(".xyz") 
  
  """
  
  def xyz_there(str):
    for i in range(len(str)):
       if str[i] != '.' and str[i+1:i+4] == 'xyz':
         return True
       if str[0:3] == 'xyz':
         return True
    return False
  
  """


== List-2 ==


count_evens
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  
  count = 0
  
  for i in range(len(nums)):
    
    if nums[i] % 2 == 0:
      count += 1
      
  return count

big_diff	
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
    
  x = 0
  
  y = nums[0]
  
  for i in range(len(nums)):
    
    x = max(x, nums[i])
    
    y = min(y, nums[i])
    
  return x - y
    
centered_average
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
  maxL = max(nums)
  minL = min(nums)
  
  eggs = sum(nums) - maxL - minL
  return eggs / (len(nums)-2)

sum13
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  egg = 0
  pol = 0
  spam = len(nums)
  if spam <= 0:
    return pol
  else:
    while egg < spam:
      if nums[egg] != 13:
        pol = pol + nums[egg]
        egg += 1
      else:
        egg += 2
    return pol

sum67
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(nums):
  res = 0
  pol = True
  spam = len(nums)
  
  for egg in nums:
    
    if egg == 6:
      pol = False
    if pol:
      res += egg
    if egg == 7:
      pol = True
    
  return res 
      
has22
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  spam = len(nums)
  egg = 0
  
  for egg in range(spam-1):
    if nums[egg] == 2 and nums[egg+1] == 2:
      return True
  
  return False


