from datetime import date as d, datetime as dt


# Objeto date

print ("Fecha actual:", d.today())
print ("Día del mes:", d.today().day)
print ("Mes:", d.today().month)
print ("Año:", d.today().year)
print ("Día de la semana:", d.today().weekday())

mes = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

dia_semana = {
    0:"Lunes",
    1:"Martes",
    2:"Miercoles",
    3:"Jueves",
    4:"Viernes",
    5:"Sábado",
    6:"Domingo"
}

fecha = "Hoy " + dia_semana[d.today().weekday()] + " " + str(d.today().day) + " de " + mes[d.today().month] + " del " + str(d.today().year)


print ("\n\n")

# Objeto datetime

print ("Fecha y hora actual:", dt.now())
print ("Segundos actuales:", dt.now().second)
print ("Minutos actuales:", dt.now().minute)
print ("Hora actual", dt.now().hour)
print ("Microsegundos actuales:", dt.now().microsecond)


# strftime(string)
# Formato de hora personalizado

#Fecha
"""
%Y : año con 4 dígitos
%m : mes con 2 dígitos
%d : dia con 2 dígitos
"""

# Hora
"""
%H : hora con formato 24 horas y dos dígitos
%M : minutos con 2 dígitos
%S : segundos con 2 dígitos
"""

print (dt.now().strftime("%d-%m-%Y %H:%M:%S"))