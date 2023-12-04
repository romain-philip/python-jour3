def time_to_text(minutes):
    X = minutes // 60
    Y = minutes % 60

    temps_texte = f"{X} heures et {Y} minutes"
    print(temps_texte)


nombre_entier_de_minutes = 130
time_to_text(nombre_entier_de_minutes)
