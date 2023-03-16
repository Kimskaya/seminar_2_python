#Задача 14: Требуется вывести все целые степени двойки 
#(т.е. числа вида 2k), не превосходящие числа N.
maxNumber = int(input("Input the max number, which is a multiple of 2  "))
firstNumber =1 
if maxNumber%2!=0:
    print("You have imput the wrong number")
else:
    while 2*firstNumber <= maxNumber:
      print(2*firstNumber," ")
      firstNumber+=1

