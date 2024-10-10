# testataan Moduulin identitycheck2.py luokkien toimintaa
# ----------------------------------------------------------

import identityCheck2

testSsnOk = identityCheck2.NationalSSN('130728-478N')
testSsnShort = identityCheck2.NationalSSN('130728-78N')
testSsnLong = identityCheck2.NationalSSN('130728-4478N')


def test_checkSsnLengthOk():
    assert testSsnOk.checkSsnLengthOk() == True
    assert testSsnShort.checkSsnLengthOk() == False
    assert testSsnLong.checkSsnLengthOk() == False
    
