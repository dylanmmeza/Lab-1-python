# Author: Dylan Meza dmm7036@psu.edu
# Collaborator: Soham Mishra svm6422@psu.edu
# Collaborator: Adnan Traore aqt5519@psu.edu
# Collaborator: Sydney Wetzel skw5571@psu.edu

temp = input("Enter temperature: ")
sign = input("Enter unit in F/f or C/c: ")
temp = float (temp)
if sign == 'F' or sign == 'f' :
  Celsius  = (temp-32)/1.8
  print(f"{temp}\N{degree sign} in Fahrenheit is equivalent to {Celsius }\N{degree sign} Celsius.")
  
elif sign == 'C'or sign == 'c' :
  fahrenheit  = (temp *1.8)+32
  print(f"{temp}\N{degree sign} in Celsius is equivalent to {fahrenheit }\N{degree sign} Fahrenheit.")

else :
   print(f"Invalid unit({sign}).") 






