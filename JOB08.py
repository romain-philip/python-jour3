def année(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange,mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire,fraise,cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte,topinambour,endive")
    elif type == "legume" and saison == "ete":
        print("artichaut,aubergine,navet")
année("fruits","hiver")