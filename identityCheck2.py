# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MOODUULIT
# ----------------------

# LUOKAT
# ------

# Henkilötunuksen käsittely
class NationalSSN:
    """Various methods to access and validate Finnish Social Security Number properties """

    def __init__(self, ssn: str) -> None:
        """Generates a finnish SSN object
        args:
            ssn (str): 11 character SSN to process
        """
        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodi eri osien laskentaan ja järkevyystarkistuksiin

# tarkistetaan että Hetun pituus on 11 merkkiä
    def checkSsnLengthOk(self) -> bool:
        """Check correct length od the SSN
        """
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
            # TODO: mieti pitäisikö tässä generoida virheilmoitus (raise)
        else:
            return True
        
# pilkotaan hemkilötunnus osiin
    def splitSsn(self) -> dict:
        """Splits the SSN to functional parts ie. birthdate, century etc

        Returns:
            dict: parts as strings
        """
        #Tehdään pilkkominen vain jos pituus on oikein
        if self.checkSsnLengthOk(): # jos True pilkotaan, HUOM! self.(metodin nimi)
            dayPart = self.ssn[0:2]
            monthPart = self.ssn[2:4]
            yearPart = self.ssn[4:6]
            centuryPart = self.ssn[6]
            birthNumberPart = self.ssn[7:10]
            checksumPart = self.ssn[10]
            return{
                'days': dayPart,
                'month': monthPart,
                'year': yearPart,
                'century': centuryPart,
                'birthNumber': birthNumberPart,
                'checksum': checksumPart,
                }
        else:
            return {'status': "error"}
            # TODO: mieti pitäisikö  antaa virhetilanne

    def getDateOfBirth(self, arg):
        pass

# lasketaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass

# Selvitetään varmistussumman avulla onko Hetu syötety oikein
    def isValidSsn(self, arg):
        pass

# main kokeiluja varten  ( poista kun ei enää tarvita)
#=====================================================
if __name__ == "__main__":
    hetu1 = NationalSSN("130728-478N")
    print("oli oikein", hetu1.checkSsnLengthOk())
    print("HeTun osat ovat: ", hetu1.splitSsn())