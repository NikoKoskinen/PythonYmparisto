# VIIVAKOODIEN TESTIT
# ===================

# MODUULIT JA KIRJASTOT
# ---------------------

import barcode
import pytest  # Tarvitaan virheiden generointiin

# YKSIKKÖTESTIT
# -------------

# Testitapaus 1 Viivakoodin "128B" varmistussumma 
def test_128BCheckSum():
    assert barcode.calculateCode128BCheksum('128B') == 56

# Testitapaus 2 Viivakoodin "128B" sisältö
def test_128BString():
    assert barcode.createCode128B('128B') == 'Ì128BXÎ'

# Luokan Code128B testit Common-variantille
# ----------------------

text1 = '128B'
barcode1 = barcode.Code128B(text1, 'Common')

def test_Common128B():
    assert barcode1.text == '128B'
    assert barcode1.variant == 'Common'

def test_Common128BValid():
    assert barcode1.checkValidityOfText() == True

# Invalid character in Common variant
text2 = '128Ö'
barcode2 = barcode.Code128B(text2, 'Common')
def test_invalidCharacterCommon():
    with pytest.raises(ValueError) as errorMessage:
        barcode2.checkValidityOfText()
    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

# Invalid variant test
text3 = '128B'
variant = 'A'
barcode3 = barcode.Code128B(text3, variant)

def test_invalidVariant():
    with pytest.raises(ValueError) as errorMessage:
        barcode3.checkValidityOfText()
    assert str(errorMessage.value) == 'Invalid variant (A), supported variants are Common, Uncommon, and Barcodesoft'

# Testit Uncommon-variantille
barcode4 = barcode.Code128B(text1, 'Uncommon')
def test_Uncommon128B():
    assert barcode4.text == '128B'
    assert barcode4.variant == 'Uncommon'

def test_Uncommon128BValid():
    assert barcode4.checkValidityOfText() == True

# Invalid character in Uncommon variant
barcode5 = barcode.Code128B(text2, 'Uncommon')
def test_invalidCharacterUncommon():
    with pytest.raises(ValueError) as errorMessage:
        barcode5.checkValidityOfText()
    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

# Testit Barcodesoft-variantille
barcode6 = barcode.Code128B(text1, 'Barcodesoft')
def test_BarcodeSoft128B():
    assert barcode6.text == '128B'
    assert barcode6.variant == 'Barcodesoft'

def test_BarcodeSoft128BValid():
    assert barcode6.checkValidityOfText() == True

# Invalid character in Barcodesoft variant
barcode7 = barcode.Code128B(text2, 'Barcodesoft')
def test_invalidCharacterBarcodeSoft():
    with pytest.raises(ValueError) as errorMessage:
        barcode7.checkValidityOfText()
    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

# Erikoismerkkitestit 

# Valid special characters for Common
text4 = '128Â'
def test_commonSpecial1():
    barcode8 = barcode.Code128B(text4, 'Common')
    assert barcode8.checkValidityOfText() == True

text5 = '128Ï'
def test_commonSpecial2():
    barcode9 = barcode.Code128B(text5, 'Common')
    assert barcode9.checkValidityOfText() == True

text6 = '128 '
def test_commonSpace():
    barcode10 = barcode.Code128B(text6, 'Common')
    assert barcode10.checkValidityOfText() == True

# Valid character for Uncommon
text7 = '128Ô'
def test_unCommonNormal():
    barcode11 = barcode.Code128B(text7, 'Uncommon')
    assert barcode11.checkValidityOfText() == True

# Valid character for Barcodesoft
text8 = '128ü'
def test_barcodeSoftNormal():
    barcode12 = barcode.Code128B(text8, 'Barcodesoft')
    assert barcode12.checkValidityOfText() == True

# Testataan oletusvariantin toiminta
def test_defaultVariant():
    barcode13 = barcode.Code128B(text1)
    assert barcode13.variant == 'Common'
    assert barcode13.checkValidityOfText() == True

# Testataan oikein muodostetun viivakoodin syntyminen
def test_validBarcode():
    assert barcode1.generateBarcodeContent() == 'Ì128BXÎ'
