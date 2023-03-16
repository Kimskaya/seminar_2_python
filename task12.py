#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.
#  X+Y = sum 
#  X*Y = mult 
# (X+Y) - sum = X*Y-mult  ; X+Y-X*Y = sum -mult ;  X*X - sumX + multip = 0

sum = int(input("Input the sum of two numbers which is less than 2000  "))
multiplication = int(input("Input the multiplication of two numbers, which is less than 1000000   "))
if sum >1000 and multiplication>1000000:
    print("You have input the wrong numbers")
else:
    for x in range(1000):
     tempX = x
     if (x*x-sum*x+multiplication)==0:
        tempY= sum-tempX
        break
    print ("The number are",tempX, tempY) 