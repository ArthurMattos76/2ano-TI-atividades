def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    if clima != "bom":
        return "Clima desfavorável"
    if not sistema_ok:
        return "Falha no sistema"
    return "Lançamento autorizado"