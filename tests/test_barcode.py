# VIIVAKOODIEN TESTIT
# ===================

# MODUULIT JA KIRJASTOT
# ---------------------

import barcode


# YKSIKKÖTESTIT
# -------------

# Testitapaus 1 Viivakoodin "128B" varmistussumma 
def test_128BCheckSum():
    assert barcode.calculateCode128BCheksum('128B') == 56

# Testitapaus 2 Viivakoodin "128B" sisältö
def test_128BString():
    assert barcode.createCode128B('128B') == 'Ì128BXÎ'

# testitapaus 3 code128B luokka testit
#--------------------------------------

text1 = '128B'
barcode1 = barcode.Code128B(text1, 'Common')
def test_Common128B():
    assert barcode1.text == '128B'
    assert barcode1.variant == 'Common'

def test_Common128BValid():
    assert barcode1.checkValidityOfText() == True
# TODO: tee virheilmoituksille testit