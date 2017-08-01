import os
import unittest
import vocabulary

class vocabularyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            os.remove('test.pkl')
        except OSError, e:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('test.pkl')
        except OSError, e:
            pass
    
    def testWriteOnce(self):
        vocabulary.updateVocabulary(['the','quick','brown','fox','jumped',
                                     'over','the','lazy','dog'], 'test.pkl')
        freqs = vocabulary.queryVocabulary(['the','brown'], 'test.pkl')
        self.assertEqual(freqs, [2,1])

    def testWriteTwice(self):
        vocabulary.updateVocabulary(['the','quick','brown','fox','jumped',
                                     'over','the','lazy','dog'], 'test.pkl')
        freqs = vocabulary.queryVocabulary(['the','brown'], 'test.pkl')
        self.assertEqual(freqs, [4,2])

if __name__ == '__main__':
    unittest.main()
