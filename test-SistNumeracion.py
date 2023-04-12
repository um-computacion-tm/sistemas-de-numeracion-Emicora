import unittest

from sistNumeracion import decimal2binario 
from sistNumeracion import binario2decimal
from sistNumeracion import decimal2octal
from sistNumeracion import octal2decimal
from sistNumeracion import decimal2hexa
from sistNumeracion import hexa2decimal
from sistNumeracion import binario2octal
from sistNumeracion import binario2hexa

class Test_sistNumeracion(unittest.TestCase):
    def testDecimal2Binario(self):
        self.assertEqual(decimal2binario(97),'01100001')

    def testBinario2Decimal(self):
        self.assertEqual(binario2decimal('01011100'),92)

    def testDecimal2octal(self):
        self.assertEqual(decimal2octal(55),'67')

    def testDecimal2octal2(self):
        self.assertEqual(decimal2octal(641),'1201')

    def testOctal2decimal(self):
        self.assertEqual(octal2decimal('154'),108)

    def testDecimal2hexa(self):
        self.assertEqual(decimal2hexa(196),'C4')

    def testDecimal2hexa2(self):
        self.assertEqual(decimal2hexa(154),'9A')

    def testHexa2decimal(self):
        self.assertEqual(hexa2decimal('A45'),2629)

    def testBinario2octal(self):
        self.assertEqual(binario2octal('1001011'),113)

    def testBinario2hexa(self):
        self.assertEqual(binario2hexa('1110110'),76)

    
if __name__=="__main__":
    unittest.main()