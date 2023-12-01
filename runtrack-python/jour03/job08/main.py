def the_food(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    
    if type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

the_food("fruits", "hiver")
the_food("fruits", "ete")
the_food("legume", "hiver")
the_food("legume", "ete")
