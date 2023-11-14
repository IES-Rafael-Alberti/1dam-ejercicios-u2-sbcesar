inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
dinero = 2400

puntos = float(input("Introduce tu puntuación obtenida: "))


if puntos == inaceptable:
    dineroTotal = dinero * inaceptable
    print(f"Tu nivel de rendimiento es inaceptable, ganas {dineroTotal}")
elif puntos == aceptable:
    dineroTotal = dinero * aceptable
    print(f"Tu nivel de rendimiento es aceptable, ganas {dineroTotal}")
elif puntos >= meritorio:
    dineroTotal = dinero * puntos
    print(f"Tu nivel de rendimiento es meritorio, ganas {dineroTotal}")
else:
    print("Puntuación errónea")