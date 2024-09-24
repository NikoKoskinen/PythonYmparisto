# MODUULI OPISKELIJANUMERON JA HENKILÖTUNNUKSEN TARKISTUKSEEN
# ===========================================================
"""Module makes sanitu checks for Raseko student id and the Finnish Social Security Number
    """

# KIRJASTOT JA MODUULIT
# ---------------------

# FUNKTIOT
# ---------------------

# opiskelijatunnuksen oikea muoto

def opiskelijanumeroOK(opiskelijanumero: str) -> bool:
    """Checks if student number is 5 or 6 digits and does not contain any chararacters other than numerics

    Args:
        opiskelijanumero (str): Raseko's student id

    Returns:
        bool: True if correct otherwise False
    """
    result: bool = False
    pituus = len(opiskelijanumero)
    if pituus == 5 or pituus == 6:
        result = True
    #else:
    #    False
    return result
