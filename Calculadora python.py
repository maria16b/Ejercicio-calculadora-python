
0=0

while 0!=5:

print("Calculadora")

print("----------------")

prit("Menu")

print("1. Suma")

print("2. Resta")

print("3. Multiplicacion")

print("4. Division")

print("5. Salir")

    0=int(input("seleccione una opcion:"))

      if 0==1:

        suma()

      elif 0==2:
    
        resta()

      elif 0==3:

        multiplicacion()

      elif 0==4:

        division

      elif 0==5:
        
        break

def suma ():

    n1=int(input("introduce un numero:"))
    n2=int(input("introduce un numero:"))

      suma = n1+n2
      print("el resultado de la suma es:", suma)
     
def resta ():

    n1=int(input("introduce un numero:"))
    n2=int(input("introduce un numero:"))

      resta = n1-n2
      print("el resultado de la resta es:", resta)
      
def multiplicacion ():

    n1=int(input("introduce un numero:"))
    n2=int(input("introduce un numero:"))

      multiplicacion = n1*n2
      print("el resultado de la multiplicacion es:", multiplicacion)
    
def division ():

    n1=int(input("introduce un numero:"))
    n2=int(input("introduce un numero:"))

      division = n1/n2
      print("el resultado de la division es:", division)
     
