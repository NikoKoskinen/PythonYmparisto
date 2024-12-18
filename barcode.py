# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# FUNKTIOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation"""
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculateCode128BChecksum(text: str) -> int:
    """Calculates a checksum for a given string"""
    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum += weightedValue
    weightedSum += 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum


def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code128 font"""
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculateCode128BChecksum(text)
    checkSumSymbol = chr(checkSum + 32)
    code128BarcodeString = startChar + text + checkSumSymbol + stopChar
    return code128BarcodeString

# LUOKKA VIIVAKOODEILLE
# =====================

class Code128B:
    """Generates Code128B barcodes. Supports variants common, uncommon and Barcodesoft"""
    
    def __init__(self, text: str, variant: str = 'Common') -> None:
        """Constructor for creating Code128B barcodes"""
        self.text = text
        self.variant = variant
        self.validRangeAll = range(33, 126)
        self.validRangeCommon = range(195, 202)
        self.validRangeUncommon = range(200, 207)
        self.validRangeBarcodesoft = range(240, 247)
        self.commonSpecialChar = (32, 194, 207)
        self.uncommonSpecialChar = 212
        self.barcodesoftSpecialChar = 252

    def checkValidityOfText(self) -> bool:
        """Checks the validity of text for the given variant"""
        for character in self.text:
            characterValue = ord(character)
            if self.variant == 'Common':
                if not (characterValue in self.validRangeAll or characterValue in self.validRangeCommon or characterValue in self.commonSpecialChar):
                    raise ValueError(f'Text string contains invalid characters ({character})')
            elif self.variant == 'Uncommon':
                if not (characterValue in self.validRangeAll or characterValue in self.validRangeUncommon or characterValue == self.uncommonSpecialChar):
                    raise ValueError(f'Text string contains invalid characters ({character})')
            elif self.variant == 'Barcodesoft':
                if not (characterValue in self.validRangeAll or characterValue in self.validRangeBarcodesoft or characterValue == self.barcodesoftSpecialChar):
                    raise ValueError(f'Text string contains invalid characters ({character})')
            else:
                raise ValueError(f'Invalid variant ({self.variant}), supported variants are Common, Uncommon, and Barcodesoft')
        return True

    def generateBarcodeContent(self) -> str:
        """Generates the full barcode content for the text based on the variant"""
        self.checkValidityOfText()  # Ensure text is valid before generation
        return createCode128B(self.text)


# Main Testing
if __name__ == "__main__":
    barcode_instance = Code128B('128Ö', 'Common')
    try:
        result = barcode_instance.checkValidityOfText()
        print(f'{barcode_instance.text} on kelvollinen viivakoodiksi:', result)
        print('Generated barcode content:', barcode_instance.generateBarcodeContent())
    except Exception as e:
        print('Tapahtui virhe:', barcode_instance.text, e)