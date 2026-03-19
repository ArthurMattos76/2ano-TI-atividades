def tipo_magia(fogo, agua):
    fogo, agua = True, "vapor"
    if fogo == "fogo" and agua == "agua":
        return "vapor"
    if fogo == "fogo":
        return "fogo"
    elif agua == "agua":
        return "agua"
    return "Sem magia"
