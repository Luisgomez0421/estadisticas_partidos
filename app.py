print("=== REGISTRO DE PARTIDOS DEL JUNIOR ===")

partidos_liga = int(input("Digite cuántos partidos va a registrar: "))

goles_favor = 0
goles_contra = 0
gano = 0
perdio = 0
empate = 0
total_puntos = 0


for i in range(partidos_liga):
    print("\n----- Partido", i + 1, "-----")

    equipo = input("Contra quién jugó el Junior: ")

    marcador_junior = int(input("Goles del Junior: "))
    marcador_rival = int(input(f"Goles del {equipo}: "))

    goles_favor += marcador_junior
    goles_contra += marcador_rival

    if marcador_junior > marcador_rival:
        print("Resultado: El Junior ganó 🟢")
        gano += 1
        total_puntos += 3

    elif marcador_junior == marcador_rival:
        print("Resultado: Empate 🟡")
        empate += 1
        total_puntos += 1

    else:
        print("Resultado: El Junior perdió 🔴")
        perdio += 1


diferencia_goles = goles_favor - goles_contra


print("\n========== RESUMEN TOTAL ==========")
print(f"Partidos jugados: {partidos_liga}")
print(f"Goles a favor: {goles_favor}")
print(f"Goles en contra: {goles_contra}")
print(f"Partidos ganados: {gano}")
print(f"Partidos perdidos: {perdio}")
print(f"Partidos empatados: {empate}")
print(f"Puntos totales: {total_puntos}")
print(f"Diferencia de goles: {diferencia_goles}")
print("===================================")