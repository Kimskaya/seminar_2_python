#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
coinNumber = int (input ("Input the number of coins  "))
headsNumber = 0
tailsNumber = 0
for i in range (coinNumber):
    tempCoins = int(input("Input 1 for heads and 0 for tails  "))
    if tempCoins == 1:
        headsNumber+=1
    else:
        tailsNumber+=1
if headsNumber>tailsNumber:
            print("You need to turn over",tailsNumber," coins showing tails")
else:
            print ("You need to turn over",headsNumber," coins showing heads")


