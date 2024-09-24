# YKSIKKÖTESTIT MODUULILLE identityCheck.py
import identityCheck

def test_opiskelijanumeroOK_5():
    assert identityCheck.opiskelijanumeroOK('12345') == True

def test_opiskelijanumeroOK_6():
    assert identityCheck.opiskelijanumeroOK('123456') == True

def test_opiskelijanumeroOK_4():
    assert identityCheck.opiskelijanumeroOK('1234') == False

def test_opiskelijanumeroOK_7():
    assert identityCheck.opiskelijanumeroOK('1234567') == False

def test_opiskelijanumeroOK_x():
    assert identityCheck.opiskelijanumeroOK('12X45') == False