# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT 
# ---------------------
# MODUULIT
#-------------------------
import avtools.sound as sound # Äänimoduuli
import avtools.video as video # video moduuli

# ASETUKSET
# ---------
kameraIndeksi = 1 # Ensimmäinen kamera on aina 0

# Käynnistetään viedokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
sound.parametricBeep(425,500)

# TESTIT KOODAUKSEN AIKANA
#----------------------------
if __name__ == "__main__":
    pass