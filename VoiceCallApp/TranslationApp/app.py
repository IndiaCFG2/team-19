from googletrans import Translator
import json
translator = Translator()
translations = {
    'message0': 'Welcome to Civis Customer Helpline',
    'message1':'Please enter your pincode.',
    'message2':'Press one to comment on Financial Policy. Press two to comment on Agricultural Policy. Press three to comment on Health Policies. Press four to comment on Defence Policies. Press five to know about various schemes',
    'message3': 'Press one to know about Financial schemes. Press two to know about Health schemes.',
    'message4': 'Thank you for choosing financial schemes.',
    'message5': 'Thank you for choosing health schemes',
    'message6': 'If you are from rural india and your gender is male, press one',
    'message7': 'If you are from rural india and your gender is female press two',
    'message8': 'If you are from urban india and you gender is male press three',
    'message9': 'If you are from urban india and your gender is female press four',
    'message10': 'Sorry, I did not understand your choice.',
    'message11': 'Thank you for your selection.',
    'message12': 'How old are you?',
    'message13': 'Thank you for telling us your age.',
    'message19': 'Annapurna Yojna',
    'message20': 'Central welfare scheme',
    'message21':'Prime Minister Currency Scheme',
    'message22': 'Prime Minister Jeevan Jyoti Insurance Scheme',
    'message14': 'Please tell your PINCODE',
    'message15': 'Thank you for telling the PINCODE',
    'message16': 'Pradhan Mantri Jan Dhan Yojana.',
    'message17':'National secondary education campaign',
    'message18': 'Atal Pension Yojna.',
    'message23': 'Indira Gandhi National Old Age Pension Scheme',
    'message24': 'Prime Minister Kisan Pension Scheme',
    'message25': 'Pradhan Mantri Jan Arogya Yojana',
    'message26': 'National Health Insurance Scheme',
    'message27': 'Aam Aadmi Insurance Scheme',
    'message28': 'National Health Insurance Scheme',
    'message29': 'Prime Minister Jan Aushadhi Yojna',
    'message31': 'two',
    'message32': 'three',
    'message30': 'one',
    'message31': 'Thank you for choosing Financial Policy',
    'message32': 'Thank you for choosing Agricultural Policy',
    'message33': 'Thank you for choosing Health Policy',
    'message34': 'Thank you for choosing Defence Policy',
    'message35': 'Thank you for choosing Scheme information',
    'message40': 'These three schemes will be benefical for you to comment on',
    'message41': 'Thank you for contacting us. We hope to serve you in future!',
    'message42': 'Give us a minute...',
    'message43': 'Here are the services nearest to you.',
    'message44':'Press 1 if you like this policy, Press 2 if you dislike this policy, and Press 3 if neutral',
    'message45':'Press 1 if you think it can be improved, Press 2 if you want it to be discarded',
    'message46':'Please give a rating from 1 to 5'
}

def saveTranslation(language):
    translated = dict()
    translationKeys = list(translations.keys())
    translationValues = list(translations.values())
    translationsToLanguage = translator.translate(translationValues, dest=language)
    print(translationsToLanguage,type(translationsToLanguage))
    for trans in range(0,len(translationKeys)):
        translated[translationKeys[trans]] = translationsToLanguage[trans].text
    print(translated)
    json_object = json.dumps(translated, indent = 4) 
    filename = language + '.json'
    with open(filename, "w") as outfile: 
        outfile.write(json_object) 
    return

saveTranslation('hi')
saveTranslation('kn')
saveTranslation('ta')
