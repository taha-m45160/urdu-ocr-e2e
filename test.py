from googleapiclient.discovery import build

text1 = 'زمانہتھافرحون و خص کہ جوخدائی کاعویٰ کرتاتھا فرحون کو جب یخبر ہوئی کہ میری سلطنت کو برباد'

text2 = 'غیر سر کار ی نتائج کے ممطابق مر کز او ر صوبہ خنبیر پپختون خواہ میں نتحریک انصاف نے میر ان مار'

my_api_key = 'AIzaSyDEA_5cYFu0H2taoD2A1Md8m1iUq1Xd7Pk'
my_cse_id = '21cab7e1a89ce2c6d'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['spelling']['htmlCorrectedQuery']


results = google_search('زمانہتھافرحون و خص کہ جوخدائی', my_api_key, my_cse_id, num=0)
output = ''
html_tags = ['<', '>', 'b', 'i', '/' ]
for result in results:
    if result in html_tags:
        continue
    output += result
print(output)