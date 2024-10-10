# kokeillaan luokkia ja olioita
#-------------------------------

# LUOKKIA JA OLIOITA
#-----------------------------------

#Yliluokka(parent class, mother class, superclass)
class henkilo:

    # Konstruktori(metodi), jonka avulla luodaan uusi Henkilö-olio
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.ika = 0
        self.kaupunki = "Raisio"
        self.harrastukset = ['koripallo', 'nukkuminen', 'kokkaus']

#Aliluokka (child class, daugter class, subclass) PERII ( inherit ) henkilö-luokan
class Opiskelija(henkilo):
    def __init__(self, etunimi, sukunimi, ryhma):
        super().__init__(etunimi, sukunimi)
        self.ryhma = ryhma

#Aliluokka (child class, daugter class, subclass) PERII ( inherit ) henkilö-luokan
class Opettaja(henkilo):
    def __init__(self, etunimi, sukunimi, aine):
        super().__init__(etunimi, sukunimi)
        self.aine = aine

#Aliluokka (child class, daugter class, subclass) PERII ( inherit ) henkilö-luokan
class Oppivelvollinen(Opiskelija):
    def __init__(self, etunimi, sukunimi, ryhma, paattyy):
        super().__init__(etunimi, sukunimi, ryhma)
        self.paattyy = paattyy

# Määritetään __str__-metodi, jotta olio voidaan tulostaa
#    def __str__(self):
#        return f"{self.etunimi} {self.sukunimi}, ryhmä: {self.ryhma}, oppivelvollisuus päättyy: {self.paattyy}"

if __name__ == "__main__":

    # Johdetaan (instantiate) luokasta Henkilö olio rehtori
    rehtori = henkilo("Reijo" , "Rantanen")

    # Luodaan olio opiskelija
    opiskelija = Opiskelija("Saana" , "Saamaton" ,"TiVi20OA")
    
    # luodaan olio oppivelvollinne
    oppivelvollinen = Oppivelvollinen("Saana" , "Saamaton" ,"TiVi20OA" ,"2027-05-20")

#tulostetaan olion tietoja toisella tavalla
print("Koulun rehtorina toimii: ", rehtori.etunimi , rehtori.sukunimi)
print("Rehtori harrastaa", rehtori.harrastukset)
print("Jakke Jäynä harrastaa", opiskelija.harrastukset)

# Tulostetaan luodut oliot käyttäen metodia ja f-stringiä
#    print("Koulun rehtorina toimii", rehtori)
#    print("Opiskelija:", opiskelija)
#    print("Oppivelvollinen:", oppivelvollinen)