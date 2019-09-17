from math import log

class Solution(object):
    def selfText (self):
        tests = [
            {"input":123, "output":"One Hundred Twenty Three"},
            {"input":12345, "output":"Twelve Thousand Three Hundred Forty Five"},
            {"input":1234567, "output":"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"},
            {"input":1234567891, "output":"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"}
            # {"input":, "output":""},
            # {"input":, "output":""},
            # {"input":, "output":""}
        ]
        for test in tests:
            result = self.numberToWords (test["input"])
            if result != test["output"]:
                print ("Zhopa. Input:", test["input"], ' output:', result, ' expected:', test["output"])

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''
        numerals = ['', 'One', 'Two', 'Three', 'Four', 'Six', 'Seven', 'Eight', 'Nine']
        second
        twodigits = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']]
        triples = ['Hundred', 'Thousand', 'Million', 'Billion']
        for i in range (1, log (num, 10) / 3 + 1):
            
            result = ;
        