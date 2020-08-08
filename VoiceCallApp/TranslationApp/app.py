from googletrans import Translator
import json
translator = Translator()
translations = {
    'title':'Jan Dhan 2.0',
    'atm':'ATM',
    'branch':'Branch',
    'po':'PO',
    'csc':'CSC',
    'emitra':'E-Mitra',
    'accinfo':'Upload Account Info',
    'feedback':'Feedback',
    'missing':'Missing Bank/ATM',
    'request':'Request Bank/ATM',
    'updates':'Latest Update',
    'help':'Help',
    'version':'App Version 1.0.4',
    'name':'Name',
    'phno':'Phone Number',
    'permaddr':'Permanent Address',
    'issue':'Please Explain the Issue',
    'dob':'Date of Birth',
    'email':'Email ID',
    'aadhaar':'Aadhaar Number',
    'selbank':'Select the bank',
    'seltouch':'Select the touchpoint',
    'aadhaarimg':'Attested Aadhaar Image Here',
    'panimg':'Attested PAN Image Here',
    'signimg':'Signature Image Here',
    'passimg':'Passport Size Photo Here',
    'selprob':'Select your problem domain',
    'rating':'Please give a Rating',
    'pickloc':'Pick location of Bank/ATM',
    'disploc':'(Bank/ATM Location will appear here)',
    'comments':'Add Special Comments',
    'submit':'SUBMIT'
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
saveTranslation('mr')
saveTranslation('kn')
saveTranslation('te')
saveTranslation('ta')
saveTranslation('pa')