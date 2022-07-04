from googleapiclient.discovery import build
from requests import get
from bs4 import BeautifulSoup

class MaskingEngine():
    def __init__(self) -> None:
        with open('dictionary/words.txt') as ur:
            temp = ur.read().strip().split('\n')
        self.urd_dict = set(temp)
        self.my_api_key = 'AIzaSyDEA_5cYFu0H2taoD2A1Md8m1iUq1Xd7Pk'
        self.my_cse_id = '21cab7e1a89ce2c6d'
        self.block_len = 6

    def googleSpellCheckAPI(self, search_term):
        service = build("customsearch", "v1", developerKey=self.my_api_key)
        res = service.cse().list(q=search_term, cx=self.my_cse_id, num=0).execute()
        if res.get('spelling') == None:
            return search_term
        results = res['spelling']['htmlCorrectedQuery']
        output = ''
        html_tags = ['<', '>', 'b', 'i', '/' ]
        for result in results:
            if result in html_tags:
                continue
            output += result
        return output

    def googleSpellCheckFree(self, keyword):
        url = "https://google.com.pk/search?q="+keyword
        raw = get(url).text
        soap = BeautifulSoup(raw, features='lxml')
        if soap.find('a', {'id': 'scl'}):
            return soap.find('a', {'id': 'scl'}).text
        else:
            print(keyword)
            return keyword

    def mask(self, doc):
        google_corrected_words = []
        lines = doc.split('\n')
        for l in lines:
            words = l.split(' ')
            start_word = 0
            end_word = self.block_len
            while True:
                search_term = ' '.join(words[start_word: end_word])
                # Without API
                output = self.googleSpellCheckFree(search_term)
                # With API
                # output = self.googleSpellCheckAPI(search_term)
                corrected_words = output.split(' ')
                for cw in corrected_words:
                    google_corrected_words.append(cw)
                if end_word == len(words):
                    break
                start_word += self.block_len
                end_word += self.block_len
                if end_word > len(words):
                    end_word = len(words)
    
        masked = []
        indices = []
        for idx, word in enumerate(google_corrected_words):
            if word in self.urd_dict:
                masked.append(word)
            else:
                indices.append(idx)
                masked.append('<mask>')

        masked_doc = ' '.join(masked)
        return google_corrected_words, masked_doc, indices


text1 = 'کرنے والامویٰ ہوگا اوراسی سال پیداہوگا تو اس نے حکم دیا با کہاس سال جولڑ کا پیداہوا اس ختل کردیا'

text2 = 'غیر سر کار ی نتائج کے ممطابق مر کز او ر صوبہ خنبیر پپختون خواہ میں نتحریک انصاف نے میر ان مار'

en = MaskingEngine()
google_corrected_words, masked_doc, indices = en.mask(text2)
print(google_corrected_words)