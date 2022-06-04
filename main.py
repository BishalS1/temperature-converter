

text='''
*************** Operators ********************
press (A) to convert celsius to fahrenheit
press (B) to convert fahrenheit to celsius
press (C) to convert celsius to kelvin 
press (D) to convert kelvin  to celsius
press (E) to convert fahrenheit to kelvin
press (F) to convert kelvin to fahrenheit
///////////////////////////////////////////////
'''

while True:

    ip1 = input(text +'\n Your input:- ')

    if ip1.upper() == 'A':
        celsius=int(input("Enter value of celsius(°C):"))
        fahrenheit = (celsius*9/5)+32
        result = f'{fahrenheit} °F'


    elif ip1.upper() == 'B':
        fahrenheit=int(input("Enter value of fahrenheit(°F):"))
        celsius= (fahrenheit-32)*5/9
        result = f'{celsius} °C'

    elif ip1.upper() == 'C':
        celsius=int(input("Enter value of celsius(°C):"))
        kelvin = celsius + 273.15
        result = f'{kelvin} °K'

    elif ip1.upper() == 'D':
        kelvin=int(input("Enter value of kelvin(°K):"))
        celsius = kelvin - 273.15 
        result = f'{celsius} °C'


    elif ip1.upper() == 'E':
        fahrenheit=int(input("Enter value of fahrenheit(°F):"))
        kelvin = ((fahrenheit-32)*5/9)+273.15
        result = f'{kelvin} °K'

    elif ip1.upper() == 'F':
        kelvin=int(input("Enter value of kelvin(°K):"))
        fahrenheit = (kelvin - 273.15)*9/5 + 32
        result = f'{fahrenheit} °F'

    else:
        # result=NonZe
        result="Invalid letter! try again"


    print(result)




