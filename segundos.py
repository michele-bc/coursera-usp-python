segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // (24*3600)
segundosRestamDias = segundos % (24*3600)
horas = segundosRestamDias // 3600
segundosRestamHoras = segundosRestamDias % 3600
minutos = segundosRestamHoras // 60
segundosRestamMinutos = segundosRestamHoras % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosRestamMinutos, "segundos.")
