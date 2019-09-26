from math import log

class Solution(object):
    def selfTest (self):
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
                print ("Zhopa. Input:", test["input"], ' output:"', result, '" expected:"', test["output"], '"')

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = ''
        numerals = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        triples = ['', 'Thousand', 'Million', 'Billion']
        for i in range (int(log (num, 10) / 3 + 1) + 1):
            n = (int)((num % pow (10, (i + 1) * 3) / pow (10, i * 3)))
            print ('i=%i n=%i' % (i, n))
            t = ''
            if n > 0:
                # if n % 100 != 0:
                if n % 100 in range (10, 20):
                    t = teens [n % 100 - 10]
                else:
                    if n % 10 > 0:
                        t = numerals [n % 10]
                    if n % 100 in range (20, 100):
                        if len (t) > 0:
                            t = ' ' + t 
                        t = tens [(int)((n % 100) / 10)] + t
                if n >= 100:
                    if len (t) > 0:
                        t = ' ' + t 
                    t = numerals [(int)(n / 100)] + ' Hundred' + t
                result = t + ' ' + triples [i] + ' ' + result.strip()
        return result.strip()
        
z = Solution()
# z.selfTest()
print (z.numberToWords (100000))