'''
Random Split for Control-Test Group Division

Equal number of uniqueodd and even participant IDs are 
randomly generated to split a group of participants into
control and test groups perfectly.
'''

import os
import random
import argparse
from getpass import getpass

# Key is the password required to generate a new participant ID
key = "kronos"

# If participant ID's have already been generated, generation step is skipped
if not os.path.exists("./cache.txt"):

  # Parsing argument
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", nargs="?", help="Enter the number of total participants in the study")
  args = parser.parse_args()
  try :
    n = int(args.n)
  except TypeError:
    print("Enter number of participants using flag -n <number> and try again.")
    quit()

  # Cache created for participant IDs -- equally even and odd
  cache = open("./cache.txt","a")

  # Generation of 5 digit IDs
  while(True):
    final_list = []
    for i in range(0,int(n/2)):
      final_list.append(random.randrange(10001,99999,2))
    for i in range(0,int(n/2)):
      final_list.append(random.randrange(10000,99998,2))
    if len(final_list) > len(set(final_list)):
      final_list.clear()
    else:
      break
  for i in final_list:  
    cache.write(str(i)+'\n')
  cache.close()
  print (str(n) + " random numbers generated, evenly split and saved in cache.txt")

# Checking for password
while(True):
  while(True):
    password = getpass()
    if(password == key):
      break
    else:
      print("Wrong password")

  # Reading new ID from cache and updating cache
  numbers = [int(line.rstrip('\n')) for line in open("./cache.txt")]
  os.system("clear")
  print("Current total is : {0}".format(len(numbers)))
  random.shuffle(numbers)
  try :
    print("Your participation id is : {0}".format(numbers[0]))
  except IndexError:
    print("You've run out of participation IDs.\nGenerate new ones using -n <number>")
    os.system("rm cache.txt")
    quit()
  numbers.pop(0)
  cache = open("./cache.txt","w+")
  for i in numbers:  
    cache.write(str(i)+'\n')
  cache.close()
