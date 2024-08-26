#digite dois números

first = float(input("first number: "))
second = float(input("second number: "))

#escolher a função de cálculo

function = input("choose the calculation ( + | - | x | / ) : ")

#estrutura de cálculo de cada função
if function == "+":
    result = first+second
    print(first,"+",second,"=",result)
elif function == "-":
    result = first-second
    print(first,"-",second," = ",result)
elif function == "x":
    result = first*second
    print(first,"x"+second,"=",result)
elif function == "/":
    result = first/second
    print(first,"/",second,"=",result)
else:
    print("function not found")                          