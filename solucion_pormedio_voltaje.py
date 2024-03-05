voltaje_1 = int(input("ingrese el primer valor de voltaje"))
print(voltaje_1)
voltaje_2 = int(input("ingrese el segundo valor de voltaje"))
print(voltaje_2)
voltaje_3 = int(input("ingrese el tercer valor de voltaje"))
print(voltaje_3)
voltaje_4 = int(input("ingrese el cuarto valor de voltaje"))
print(voltaje_4)
voltaje_5 = int(input("ingrese el quinto valor de voltaje "))
print(voltaje_5)



promedio = ((voltaje_1 + voltaje_2 + voltaje_3 + voltaje_4 + voltaje_5)/5)

if promedio > 220:
    print("ALTO VOLTAJE")
else:
    if promedio < 220:
        print("VOLTAJE CORRECTO")
        