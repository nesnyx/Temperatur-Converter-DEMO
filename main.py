import tkinter
from celcius import Celcius
from kelvin import Kelvin
from fahrenheit import Fahrenheit

print("Welcome to my program")

print("""
        Select program
        
        1. celcius
        2. fahrenheit
        3. kelvin
      """)

choose = int(input("Choose a program : "))
cel = Celcius()
fah = Fahrenheit()
kel = Kelvin()


if choose == 1:
  
  print("""
        1. Celcius to kelvin
        2. Celcius to Fahrenheit
        """)
  
  choose = int(input("Choose a conversion : "))
  
  if choose == 1:
    inputvalue = int(input("Enter a value Kelvin : "))
    
    print("The result is : ", cel.get_c_k(inputvalue))
  elif choose == 2:
    inputvalue = int(input("Enter a value Fahrenheit : "))
    print("The result is : ", cel.get_c_f(inputvalue))

  else:
    print("eror") 

elif choose == 2:
  print("""
        1. Fahrenheit to Celcius
        2. Fahrenheit to Kelvin
        """)
  
  choose = int(input("Choose a conversion : "))
  
  if choose == 1:
    inputvalue = int(input("Enter a value  : "))
    
    print("The result is : ", fah.get_f_c(inputvalue))
  elif choose == 2:
    inputvalue = int(input("Enter a value  : "))
    print("The result is : ", fah.get_f_k(inputvalue))
  else:
    print("eror")
  
elif choose == 3:
  print("""
        1. Kelvin to Celcius
        2. Kelvin to Fahrenheit
        """)
  
  choose = int(input("Choose a conversion : "))
  
  if choose == 1:
    inputvalue = int(input("Enter a value  : "))
    
    print("The result is : ", kel.get_k_c(inputvalue))
  elif choose == 2:
    inputvalue = int(input("Enter a value  : "))
    print("The result is : ", kel.get_k_f(inputvalue))
  else:
    print("eror")

else:
  print("error")