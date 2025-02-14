# Age/Gender/Area
# Financial/Health.

import os
from flask import Flask,request
from twilio.twiml.voice_response import VoiceResponse,Gather
from twilio.rest import Client
import requests
import time

app = Flask(__name__)
url1 = 'http://jandhan2.herokuapp.com/account/sendMsg'
# Make the english better for these strings so that hindi too comes better.
en = {
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

#To be changed with hindi strings.
hi = {
    "message0": "\u091c\u0928 \u0927\u0928 \u0917\u094d\u0930\u093e\u0939\u0915 \u0939\u0947\u0932\u094d\u092a\u0932\u093e\u0907\u0928 \u092e\u0947\u0902 \u0906\u092a\u0915\u093e \u0938\u094d\u0935\u093e\u0917\u0924 \u0939\u0948",
    "message1": "\u0915\u0943\u092a\u092f\u093e \u0905\u092a\u0928\u093e \u092a\u093f\u0928\u0915\u094b\u0921 \u0926\u0930\u094d\u091c \u0915\u0930\u0947\u0902\u0964",
    "message2": "\u0905\u092a\u0928\u0947 \u092a\u093e\u0938 \u0915\u0947 \u090f\u091f\u0940\u090f\u092e \u0915\u094b \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u090f\u0915 \u0926\u092c\u093e\u090f\u0902\u0964 \u0905\u092a\u0928\u0947 \u092a\u093e\u0938 \u0915\u0947 \u092c\u0948\u0902\u0915 \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0926\u094b \u0926\u092c\u093e\u090f\u0902\u0964 \u0905\u092a\u0928\u0947 \u0906\u0938-\u092a\u093e\u0938 \u0915\u0947 \u0921\u093e\u0915\u0918\u0930\u094b\u0902 \u0915\u094b \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0924\u0940\u0928 \u0926\u092c\u093e\u090f\u0902\u0964 \u0905\u092a\u0928\u0947 \u092a\u093e\u0938 \u092c\u0948\u0902\u0915 \u092e\u093f\u0924\u094d\u0930 \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u091a\u093e\u0930 \u0926\u092c\u093e\u090f\u0902\u0964 \u0935\u093f\u092d\u093f\u0928\u094d\u0928 \u092f\u094b\u091c\u0928\u093e\u0913\u0902 \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u092a\u093e\u0901\u091a \u0926\u092c\u093e\u090f\u0901",
    "message3": "\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u092f\u094b\u091c\u0928\u093e\u0913\u0902 \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u090f\u0915 \u0926\u092c\u093e\u090f\u0902\u0964 \u0938\u094d\u0935\u093e\u0938\u094d\u0925\u094d\u092f \u092f\u094b\u091c\u0928\u093e\u0913\u0902 \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u091c\u093e\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0926\u094b \u0926\u092c\u093e\u090f\u0902\u0964",
    "message4": "\u0935\u093f\u0924\u094d\u0924\u0940\u092f \u092f\u094b\u091c\u0928\u093e\u0913\u0902 \u0915\u094b \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926\u0964",
    "message5": "\u0938\u094d\u0935\u093e\u0938\u094d\u0925\u094d\u092f \u092f\u094b\u091c\u0928\u093e\u0913\u0902 \u0915\u094b \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message6": "\u092f\u0926\u093f \u0906\u092a \u0917\u094d\u0930\u093e\u092e\u0940\u0923 \u092d\u093e\u0930\u0924 \u0938\u0947 \u0939\u0948\u0902 \u0914\u0930 \u0906\u092a\u0915\u093e \u0932\u093f\u0902\u0917 \u092a\u0941\u0930\u0941\u0937 \u0939\u0948, \u0924\u094b \u090f\u0915 \u0926\u092c\u093e\u090f\u0901",
    "message7": "\u092f\u0926\u093f \u0906\u092a \u0917\u094d\u0930\u093e\u092e\u0940\u0923 \u092d\u093e\u0930\u0924 \u0938\u0947 \u0939\u0948\u0902 \u0914\u0930 \u0906\u092a\u0915\u093e \u0932\u093f\u0902\u0917 \u092e\u0939\u093f\u0932\u093e \u092a\u094d\u0930\u0947\u0938 \u0926\u094b \u0939\u0948",
    "message8": "\u092f\u0926\u093f \u0906\u092a \u0936\u0939\u0930\u0940 \u092d\u093e\u0930\u0924 \u0938\u0947 \u0939\u0948\u0902 \u0914\u0930 \u0906\u092a \u0932\u093f\u0902\u0917 \u092a\u0941\u0930\u0941\u0937 \u092a\u094d\u0930\u0947\u0938 \u0924\u0940\u0928 \u0939\u0948\u0902",
    "message9": "\u092f\u0926\u093f \u0906\u092a \u0936\u0939\u0930\u0940 \u092d\u093e\u0930\u0924 \u0938\u0947 \u0939\u0948\u0902 \u0914\u0930 \u0906\u092a\u0915\u093e \u0932\u093f\u0902\u0917 \u092e\u0939\u093f\u0932\u093e \u092a\u094d\u0930\u0947\u0938 \u091a\u093e\u0930 \u0939\u0948",
    "message10": "\u0915\u094d\u0937\u092e\u093e \u0915\u0930\u0947\u0902, \u092e\u0941\u091d\u0947 \u0906\u092a\u0915\u0940 \u092a\u0938\u0902\u0926 \u0938\u092e\u091d \u092e\u0947\u0902 \u0928\u0939\u0940\u0902 \u0906\u0908\u0964",
    "message11": "\u0906\u092a\u0915\u0947 \u091a\u092f\u0928 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926\u0964",
    "message12": "\u0906\u092a \u0915\u0940 \u0909\u092e\u094d\u0930 \u0915\u094d\u092f\u093e \u0939\u0948?",
    "message13": "\u0939\u092e\u0947\u0902 \u0905\u092a\u0928\u0940 \u0909\u092e\u094d\u0930 \u092c\u0924\u093e\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926\u0964",
    "message19": "\u0905\u0928\u094d\u0928\u092a\u0942\u0930\u094d\u0923\u093e \u092f\u094b\u091c\u0928\u093e",
    "message20": "\u0915\u0947\u0902\u0926\u094d\u0930\u0940\u092f \u0915\u0932\u094d\u092f\u093e\u0923 \u092f\u094b\u091c\u0928\u093e",
    "message21": "\u092a\u094d\u0930\u0927\u093e\u0928 \u092e\u0902\u0924\u094d\u0930\u0940 \u092e\u0941\u0926\u094d\u0930\u093e \u092f\u094b\u091c\u0928\u093e",
    "message22": "\u092a\u094d\u0930\u0927\u093e\u0928 \u092e\u0902\u0924\u094d\u0930\u0940 \u091c\u0940\u0935\u0928 \u091c\u094d\u092f\u094b\u0924\u093f \u092c\u0940\u092e\u093e \u092f\u094b\u091c\u0928\u093e",
    "message14": "\u0915\u0943\u092a\u092f\u093e \u0905\u092a\u0928\u093e \u092a\u093f\u0928\u0915\u094b\u0921 \u092c\u0924\u093e\u090f\u0902",
    "message15": "\u092a\u093f\u0928\u0915\u094b\u0921 \u092c\u0924\u093e\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message16": "\u092a\u094d\u0930\u0927\u093e\u0928 \u092e\u0902\u0924\u094d\u0930\u0940 \u091c\u0928 \u0927\u0928 \u092f\u094b\u091c\u0928\u093e.",
    "message17": "\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u092e\u093e\u0927\u094d\u092f\u092e\u093f\u0915 \u0936\u093f\u0915\u094d\u0937\u093e \u0905\u092d\u093f\u092f\u093e\u0928",
    "message18": "\u0905\u091f\u0932 \u092a\u0947\u0902\u0936\u0928 \u092f\u094b\u091c\u0928\u093e\u0964",
    "message23": "\u0907\u0902\u0926\u093f\u0930\u093e \u0917\u093e\u0902\u0927\u0940 \u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u0935\u0943\u0926\u094d\u0927\u093e\u0935\u0938\u094d\u0925\u093e \u092a\u0947\u0902\u0936\u0928 \u092f\u094b\u091c\u0928\u093e",
    "message24": "\u092a\u094d\u0930\u0927\u093e\u0928 \u092e\u0902\u0924\u094d\u0930\u0940 \u0915\u093f\u0938\u093e\u0928 \u092a\u0947\u0902\u0936\u0928 \u092f\u094b\u091c\u0928\u093e",
    "message25": "\u092a\u094d\u0930\u0927\u093e\u0928 \u092e\u0902\u0924\u094d\u0930\u0940 \u091c\u0949\u0928 \u092c\u0940\u092e\u093e\u0930\u0940 \u092f\u094b\u091c\u0928\u093e\u0915\u093e\u0930",
    "message26": "\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u0938\u094d\u0935\u093e\u0938\u094d\u0925\u094d\u092f \u092c\u0940\u092e\u093e \u092f\u094b\u091c\u0928\u093e",
    "message27": "\u0906\u092e \u0906\u0926\u092e\u0940 \u092c\u0940\u092e\u093e \u092f\u094b\u091c\u0928\u093e",
    "message28": "\u0930\u093e\u0937\u094d\u091f\u094d\u0930\u0940\u092f \u0938\u094d\u0935\u093e\u0938\u094d\u0925\u094d\u092f \u092c\u0940\u092e\u093e \u092f\u094b\u091c\u0928\u093e",
    "message29": "\u092a\u094d\u0930\u0927\u093e\u0928\u092e\u0902\u0924\u094d\u0930\u0940 \u091c\u0928\u0914\u0937\u0927\u093f \u092f\u094b\u091c\u0928\u093e",
    "message31": "ATM \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message32": "\u092c\u0948\u0902\u0915 \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message30": "\u090f\u0915",
    "message33": "\u092a\u094b\u0938\u094d\u091f \u0911\u092b\u093f\u0938 \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message34": "\u092c\u0948\u0902\u0915 \u092e\u093f\u0924\u094d\u0930 \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message35": "\u092f\u094b\u091c\u0928\u093e \u0915\u0940 \u091c\u093e\u0928\u0915\u093e\u0930\u0940 \u091a\u0941\u0928\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926",
    "message40": "\u092f\u0947 \u0924\u0940\u0928\u094b\u0902 \u092f\u094b\u091c\u0928\u093e\u090f\u0902 \u0906\u092a\u0915\u0947 \u0932\u093f\u090f \u092b\u093e\u092f\u0926\u0947\u092e\u0902\u0926 \u0939\u094b\u0902\u0917\u0940\u0964",
    "message41": "\u0939\u092e\u0938\u0947 \u0938\u0902\u092a\u0930\u094d\u0915 \u0915\u0930\u0928\u0947 \u0915\u0947 \u0932\u093f\u090f \u0927\u0928\u094d\u092f\u0935\u093e\u0926\u0964 \u0939\u092e \u092d\u0935\u093f\u0937\u094d\u092f \u092e\u0947\u0902 \u0906\u092a \u0915\u0940 \u0938\u0947\u0935\u093e \u0915\u0930\u0928\u0947 \u0915\u0940 \u0909\u092e\u094d\u092e\u0940\u0926 \u0915\u0930\u0924\u0947 \u0939\u0948\u0902!",
    "message42": "\u0939\u092e\u0947\u0902 \u090f\u0915 \u092e\u093f\u0928\u091f \u0926\u0947\u0902\u0964 \u0939\u092e \u0906\u092a\u0915\u0947 \u0932\u093f\u090f \u0928\u093f\u0915\u091f\u0924\u092e \u0938\u0947\u0935\u093e\u090f\u0901 \u0932\u093e \u0930\u0939\u0947 \u0939\u0948\u0902\u0964",
    "message43": "\u092f\u0939\u093e\u0902 \u0906\u092a\u0915\u0947 \u0932\u093f\u090f \u0928\u093f\u0915\u091f\u0924\u092e \u0938\u0947\u0935\u093e\u090f\u0901 \u0939\u0948\u0902\u0964"
}

# Change this to english tamil strings.
ta = {
    "message0": "\u0b9c\u0ba9 \u0ba4\u0ba9\u0bcd \u0bb5\u0bbe\u0b9f\u0bbf\u0b95\u0bcd\u0b95\u0bc8\u0baf\u0bbe\u0bb3\u0bb0\u0bcd \u0bb9\u0bc6\u0bb2\u0bcd\u0baa\u0bcd\u0bb2\u0bc8\u0ba9\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0bb5\u0bb0\u0bc1\u0b95",
    "message1": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0baa\u0bbf\u0ba9\u0bcd\u0b95\u0bcb\u0b9f\u0bc8 \u0b89\u0bb3\u0bcd\u0bb3\u0bbf\u0b9f\u0bb5\u0bc1\u0bae\u0bcd.",
    "message2": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0bb0\u0bc1\u0b95\u0bbf\u0bb2\u0bc1\u0bb3\u0bcd\u0bb3 \u0b8f\u0b9f\u0bbf\u0b8e\u0bae\u0bcd \u0b85\u0bb1\u0bbf\u0baf \u0b92\u0ba9\u0bcd\u0bb1\u0bc8 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd. \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0bb0\u0bc1\u0b95\u0bbf\u0bb2\u0bc1\u0bb3\u0bcd\u0bb3 \u0bb5\u0b99\u0bcd\u0b95\u0bbf\u0b95\u0bb3\u0bc8 \u0b85\u0bb1\u0bbf\u0baf \u0b87\u0bb0\u0ba3\u0bcd\u0b9f\u0bc8 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd. \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0bb0\u0bc1\u0b95\u0bbf\u0bb2\u0bc1\u0bb3\u0bcd\u0bb3 \u0ba4\u0baa\u0bbe\u0bb2\u0bcd \u0ba8\u0bbf\u0bb2\u0bc8\u0baf\u0b99\u0bcd\u0b95\u0bb3\u0bc8 \u0b85\u0bb1\u0bbf\u0baf \u0bae\u0bc2\u0ba9\u0bcd\u0bb1\u0bc1 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd. \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0b85\u0bb0\u0bc1\u0b95\u0bbf\u0bb2\u0bc1\u0bb3\u0bcd\u0bb3 \u0bb5\u0b99\u0bcd\u0b95\u0bbf \u0bae\u0bbf\u0ba4\u0bcd\u0bb0\u0bbe\u0bb8\u0bc8 \u0b85\u0bb1\u0bbf\u0baf \u0ba8\u0bbe\u0ba9\u0bcd\u0b95\u0bc1 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd. \u0baa\u0bb2\u0bcd\u0bb5\u0bc7\u0bb1\u0bc1 \u0ba8\u0bbf\u0ba4\u0bbf\u0ba4\u0bcd \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc8\u0baa\u0bcd \u0baa\u0bb1\u0bcd\u0bb1\u0bbf \u0b85\u0bb1\u0bbf\u0baf \u0b90\u0ba8\u0bcd\u0ba4\u0bc1 \u0b90 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd",
    "message3": "\u0ba8\u0bbf\u0ba4\u0bbf\u0ba4\u0bcd \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc8\u0baa\u0bcd \u0baa\u0bb1\u0bcd\u0bb1\u0bbf \u0b85\u0bb1\u0bbf\u0baf \u0b92\u0ba9\u0bcd\u0bb1\u0bc8 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd. \u0b9a\u0bc1\u0b95\u0bbe\u0ba4\u0bbe\u0bb0 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc8\u0baa\u0bcd \u0baa\u0bb1\u0bcd\u0bb1\u0bbf \u0b85\u0bb1\u0bbf\u0baf 2 \u0b90 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd.",
    "message4": "\u0ba8\u0bbf\u0ba4\u0bbf\u0ba4\u0bcd \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf.",
    "message5": "\u0b9a\u0bc1\u0b95\u0bbe\u0ba4\u0bbe\u0bb0 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message6": "\u0ba8\u0bc0\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0b95\u0bbf\u0bb0\u0bbe\u0bae\u0baa\u0bcd\u0baa\u0bc1\u0bb1 \u0b87\u0ba8\u0bcd\u0ba4\u0bbf\u0baf\u0bbe\u0bb5\u0bc8\u0b9a\u0bcd \u0b9a\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bb5\u0bb0\u0bcd \u0bae\u0bb1\u0bcd\u0bb1\u0bc1\u0bae\u0bcd \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0baa\u0bbe\u0bb2\u0bbf\u0ba9\u0bae\u0bcd \u0b86\u0ba3\u0bcd \u0b8e\u0ba9\u0bcd\u0bb1\u0bbe\u0bb2\u0bcd, 1 \u0b90 \u0b85\u0bb4\u0bc1\u0ba4\u0bcd\u0ba4\u0bb5\u0bc1\u0bae\u0bcd",
    "message7": "\u0ba8\u0bc0\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0b95\u0bbf\u0bb0\u0bbe\u0bae\u0baa\u0bcd\u0baa\u0bc1\u0bb1 \u0b87\u0ba8\u0bcd\u0ba4\u0bbf\u0baf\u0bbe\u0bb5\u0bc8\u0b9a\u0bcd \u0b9a\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bb5\u0bb0\u0bcd \u0bae\u0bb1\u0bcd\u0bb1\u0bc1\u0bae\u0bcd \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0baa\u0bbe\u0bb2\u0bbf\u0ba9\u0bae\u0bcd \u0baa\u0bc6\u0ba3\u0bcd \u0baa\u0ba4\u0bcd\u0ba4\u0bbf\u0bb0\u0bbf\u0b95\u0bc8 2 \u0b8e\u0ba9\u0bcd\u0bb1\u0bbe\u0bb2\u0bcd",
    "message8": "\u0ba8\u0bc0\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0ba8\u0b95\u0bb0\u0bcd\u0baa\u0bcd\u0baa\u0bc1\u0bb1 \u0b87\u0ba8\u0bcd\u0ba4\u0bbf\u0baf\u0bbe\u0bb5\u0bbf\u0bb2\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bc1 \u0bb5\u0ba8\u0bcd\u0ba4\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bbe\u0bb2\u0bcd, \u0ba8\u0bc0\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0baa\u0bbe\u0bb2\u0bbf\u0ba9\u0bae\u0bcd \u0b86\u0ba3\u0bcd \u0baa\u0ba4\u0bcd\u0ba4\u0bbf\u0bb0\u0bbf\u0b95\u0bc8 3",
    "message9": "\u0ba8\u0bc0\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0ba8\u0b95\u0bb0\u0bcd\u0baa\u0bcd\u0baa\u0bc1\u0bb1 \u0b87\u0ba8\u0bcd\u0ba4\u0bbf\u0baf\u0bbe\u0bb5\u0bbf\u0bb2\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bc1 \u0bb5\u0ba8\u0bcd\u0ba4\u0bbf\u0bb0\u0bc1\u0ba8\u0bcd\u0ba4\u0bbe\u0bb2\u0bcd, \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0baa\u0bbe\u0bb2\u0bbf\u0ba9\u0bae\u0bcd \u0baa\u0bc6\u0ba3\u0bcd \u0baa\u0ba4\u0bcd\u0ba4\u0bbf\u0bb0\u0bbf\u0b95\u0bc8 4 \u0b8e\u0ba9\u0bcd\u0bb1\u0bbe\u0bb2\u0bcd",
    "message10": "\u0bae\u0ba9\u0bcd\u0ba9\u0bbf\u0b95\u0bcd\u0b95\u0bb5\u0bc1\u0bae\u0bcd, \u0b8e\u0ba9\u0b95\u0bcd\u0b95\u0bc1 \u0ba4\u0bc7\u0bb0\u0bcd\u0bb5\u0bc1 \u0baa\u0bc1\u0bb0\u0bbf\u0baf\u0bb5\u0bbf\u0bb2\u0bcd\u0bb2\u0bc8.",
    "message11": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0bb5\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf.",
    "message12": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0bb5\u0baf\u0ba4\u0bc1 \u0b8e\u0ba9\u0bcd\u0ba9 ?",
    "message13": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd \u0bb5\u0baf\u0ba4\u0bc8 \u0b8e\u0b99\u0bcd\u0b95\u0bb3\u0bbf\u0b9f\u0bae\u0bcd \u0b9a\u0bca\u0ba9\u0bcd\u0ba9\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf.",
    "message19": "\u0b85\u0ba9\u0bcd\u0ba9\u0baa\u0bc2\u0bb0\u0bcd\u0ba3\u0bbe \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message20": "\u0bae\u0ba4\u0bcd\u0ba4\u0bbf\u0baf \u0ba8\u0bb2\u0ba4\u0bcd\u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message21": "\u0baa\u0bbf\u0bb0\u0ba4\u0bae\u0bb0\u0bcd \u0ba8\u0bbe\u0ba3\u0baf\u0ba4\u0bcd \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message22": "\u0baa\u0bbf\u0bb0\u0ba4\u0bae\u0bb0\u0bcd \u0b9c\u0bc0\u0bb5\u0ba9\u0bcd \u0b9c\u0bcb\u0ba4\u0bbf \u0b95\u0bbe\u0baa\u0bcd\u0baa\u0bc0\u0b9f\u0bcd\u0b9f\u0bc1 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message14": "\u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bcd PINCODE \u0b90\u0b9a\u0bcd \u0b9a\u0bca\u0bb2\u0bcd\u0bb2\u0bc1\u0b99\u0bcd\u0b95\u0bb3\u0bcd",
    "message15": "PINCODE \u0b90 \u0b9a\u0bca\u0ba9\u0bcd\u0ba9\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message16": "\u0baa\u0bbf\u0bb0\u0ba4\u0bae\u0bb0\u0bcd \u0b9c\u0bbe\u0ba9\u0bcd \u0ba4\u0ba9\u0bcd \u0baf\u0bcb\u0b9c\u0ba9\u0bbe.",
    "message17": "\u0ba4\u0bc7\u0b9a\u0bbf\u0baf \u0b87\u0b9f\u0bc8\u0ba8\u0bbf\u0bb2\u0bc8\u0b95\u0bcd \u0b95\u0bb2\u0bcd\u0bb5\u0bbf \u0baa\u0bbf\u0bb0\u0b9a\u0bcd\u0b9a\u0bbe\u0bb0\u0bae\u0bcd",
    "message18": "\u0b85\u0b9f\u0bb2\u0bcd \u0b93\u0baf\u0bcd\u0bb5\u0bc2\u0ba4\u0bbf\u0baf \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message23": "\u0b87\u0ba8\u0bcd\u0ba4\u0bbf\u0bb0\u0bbe \u0b95\u0bbe\u0ba8\u0bcd\u0ba4\u0bbf \u0ba4\u0bc7\u0b9a\u0bbf\u0baf \u0bae\u0bc1\u0ba4\u0bbf\u0baf\u0bcb\u0bb0\u0bcd \u0b93\u0baf\u0bcd\u0bb5\u0bc2\u0ba4\u0bbf\u0baf \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message24": "\u0baa\u0bbf\u0bb0\u0ba4\u0bae\u0bb0\u0bcd \u0b95\u0bbf\u0b9a\u0bbe\u0ba9\u0bcd \u0b93\u0baf\u0bcd\u0bb5\u0bc2\u0ba4\u0bbf\u0baf \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message25": "\u0baa\u0bbf\u0bb0\u0ba4\u0bbe\u0ba9\u0bcd \u0bae\u0ba8\u0bcd\u0ba4\u0bbf\u0bb0\u0bbf \u0b9c\u0bbe\u0ba9\u0bcd \u0b86\u0bb0\u0bcb\u0b95\u0bcd\u0baf \u0baf\u0bcb\u0b9c\u0ba9\u0bbe",
    "message26": "\u0ba4\u0bc7\u0b9a\u0bbf\u0baf \u0b9a\u0bc1\u0b95\u0bbe\u0ba4\u0bbe\u0bb0 \u0b95\u0bbe\u0baa\u0bcd\u0baa\u0bc0\u0b9f\u0bcd\u0b9f\u0bc1 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message27": "\u0b86\u0bae\u0bcd \u0b86\u0ba4\u0bcd\u0bae\u0bbf \u0b95\u0bbe\u0baa\u0bcd\u0baa\u0bc0\u0b9f\u0bcd\u0b9f\u0bc1 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message28": "\u0ba4\u0bc7\u0b9a\u0bbf\u0baf \u0b9a\u0bc1\u0b95\u0bbe\u0ba4\u0bbe\u0bb0 \u0b95\u0bbe\u0baa\u0bcd\u0baa\u0bc0\u0b9f\u0bcd\u0b9f\u0bc1 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0bae\u0bcd",
    "message29": "\u0baa\u0bbf\u0bb0\u0ba4\u0bae\u0bb0\u0bcd \u0b9c\u0bbe\u0ba9\u0bcd \u0b86\u0bb7\u0bbe\u0ba4\u0bbf \u0baf\u0bcb\u0b9c\u0bcd\u0ba9\u0bbe",
    "message31": "\u0b8f\u0b9f\u0bbf\u0b8e\u0bae\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0bb5\u0bc1 \u0b9a\u0bc6\u0baf\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message32": "\u0bb5\u0b99\u0bcd\u0b95\u0bbf\u0baf\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message30": "\u0b92\u0ba9\u0bcd\u0bb1\u0bc1",
    "message33": "\u0ba4\u0baa\u0bbe\u0bb2\u0bcd \u0b85\u0bb2\u0bc1\u0bb5\u0bb2\u0b95\u0ba4\u0bcd\u0ba4\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message34": "\u0bb5\u0b99\u0bcd\u0b95\u0bbf \u0bae\u0bbf\u0ba4\u0bcd\u0bb0\u0bbe\u0bb8\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message35": "\u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0ba4\u0bcd \u0ba4\u0b95\u0bb5\u0bb2\u0bc8\u0ba4\u0bcd \u0ba4\u0bc7\u0bb0\u0bcd\u0ba8\u0bcd\u0ba4\u0bc6\u0b9f\u0bc1\u0ba4\u0bcd\u0ba4\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf",
    "message40": "\u0b87\u0ba8\u0bcd\u0ba4 \u0bae\u0bc2\u0ba9\u0bcd\u0bb1\u0bc1 \u0ba4\u0bbf\u0b9f\u0bcd\u0b9f\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0bae\u0bcd \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0baa\u0baf\u0ba9\u0bb3\u0bbf\u0b95\u0bcd\u0b95\u0bc1\u0bae\u0bcd.",
    "message41": "\u0b8e\u0b99\u0bcd\u0b95\u0bb3\u0bc8 \u0ba4\u0bc6\u0bbe\u0b9f\u0bb0\u0bcd\u0baa\u0bc1 \u0b95\u0bc6\u0bbe\u0ba3\u0bcd\u0b9f\u0ba4\u0bb1\u0bcd\u0b95\u0bc1 \u0ba8\u0ba9\u0bcd\u0bb1\u0bbf. \u0b8e\u0ba4\u0bbf\u0bb0\u0bcd\u0b95\u0bbe\u0bb2\u0ba4\u0bcd\u0ba4\u0bbf\u0bb2\u0bcd \u0b89\u0b99\u0bcd\u0b95\u0bb3\u0bc1\u0b95\u0bcd\u0b95\u0bc1 \u0b9a\u0bc7\u0bb5\u0bc8 \u0b9a\u0bc6\u0baf\u0bcd\u0bb5\u0bcb\u0bae\u0bcd \u0b8e\u0ba9\u0bcd\u0bb1\u0bc1 \u0ba8\u0bae\u0bcd\u0baa\u0bc1\u0b95\u0bbf\u0bb1\u0bcb\u0bae\u0bcd",
}

# //Change this to english kannada strings/
kn = {
    "message0": "Jana dhan grāhaka sahāyavāṇige susvāgata",
    "message1": "Dayaviṭṭu nim'ma pin‌kōḍ annu namūdisi.",
    "message2": "Nim'ma hattiraviruva eṭi'eṁ tiḷiyalu ondannu ottiri. Nim'ma hattiraviruva byāṅkugaḷannu tiḷiyalu eraḍu ottiri. Nim'ma hattiraviruva an̄ce kacērigaḷannu tiḷiyalu mūru ottiri. Nim'ma hattiraviruva byāṅk mitras tiḷiyalu nālku ottiri. Vividha yōjanegaḷa bagge tiḷiyalu aidu ottiri",
    "message3": "Haṇakāsu yōjanegaḷa bagge tiḷiyalu ondannu ottiri. Ārōgya yōjanegaḷa bagge tiḷiyalu eraḍu ottiri.",
    "message4": "Haṇakāsu yōjanegaḷannu āyke māḍiddakkāgi dhan'yavādagaḷu.",
    "message5": "Ārōgya yōjanegaḷannu āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message6": "Nīvu grāmīṇa bhāratadavarāgiddare mattu nim'ma liṅga puruṣarāgiddare, ondannu ottiri",
    "message7": "Nīvu grāmīṇa bhāratadavarāgiddare mattu nim'ma liṅga strī patrikā eraḍu āgiddare",
    "message8": "If you are from urban india and you gender is male press three",
    "message9": "Nīvu nagara bhāratadinda bandiddare mattu nim'ma liṅga strī patrikā nālku āgiddare",
    "message10": "Kṣamisi, nim'ma āyke nanage arthavāgalilla.",
    "message11": "Nim'ma āykege dhan'yavādagaḷu.",
    "message12": "Ninna vayas'su eṣṭu?",
    "message13": "Nim'ma vayas'sannu namage tiḷisiddakkāgi dhan'yavādagaḷu.",
    "message19": "Annapūrṇa yōjane",
    "message20": "CKēndra kalyāṇa yōjane",
    "message21": "Pradhāni karensi yōjane",
    "message22": "Pradhāni jīvan jyōti vimā yōjane",
    "message14": "Dayaviṭṭu nim'ma pin‌kōḍ‌ge tiḷisi",
    "message15": "Pin‌kōḍ‌ge hēḷiddakkāgi dhan'yavādagaḷu",
    "message16": "Pradhān mantri jana dhan yōjane.",
    "message17": "Rāṣṭrīya mādhyamika śikṣaṇa abhiyāna",
    "message18": "Aṭal pin̄caṇi yōjane.",
    "message23": "Indirā gāndhi rāṣṭrīya vr̥d'dhāpya pin̄caṇi yōjane",
    "message24": "Pradhāni kisān pin̄caṇi yōjane",
    "message25": "Pradhān mantri jana ārōgya yōjane",
    "message26": "Rāṣṭrīya ārōgya vimā yōjane",
    "message27": "Ām ādmi vimā yōjane",
    "message28": "Rāṣṭrīya ārōgya vimā yōjane",
    "message29": "Pradhāni jana āśādi yōjane",
    "message31": "Eraḍu",
    "message32": "Mūru",
    "message30": "Ondu",
    "message31": "Eṭi'eṁ āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message32": "Byāṅk āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message33": "Pōsṭ āphīs āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message34": "Byāṅk mitravannu āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message35": "Skīm māhitiyannu āyke māḍiddakkāgi dhan'yavādagaḷu",
    "message40": "Ī mūru yōjanegaḷu nimage prayōjanakāriyāguttave.",
    "message41": "Nam'mannu samparkisiddakke dhan'yavādagaḷu. Bhaviṣyadalli nimage sēve sallisalu nāvu āśisuttēve!",
    "message42": "Namage ondu nimiṣa nīḍi. Nāvu nimagāgi hattirada sēvegaḷannu paḍeyuttiddēve.",
    "message43": "Nimage hattiraviruva sēvegaḷu illive."
}

@app.route('/')
def index():
    return "Hello World"

@app.route("/makeACall/<phoneNo>",methods=['GET'])
def makeCall(phoneNo):
    account_sid = 'AC63307fff7d6088ec61dd563aa8974597'
    auth_token = '324512a5713e65838ddd88e6f93c054e'
    client = Client(account_sid, auth_token)
    toPhoneNo = '+91'+phoneNo
    try:
        call = client.calls.create(
                                url='https://jandhan2voice.herokuapp.com/answer',
                                to=toPhoneNo,
                                from_='+12054489824'
                            )
                            
        # print(call.sid)
        return "Success"
    except:
        return "Failure"

@app.route("/answer", methods=['GET', 'POST'])
def gatherLanguage():
    print(request.values)
    resp = VoiceResponse()
    print(resp)
    resp.say('Press one for English, Press two for Hindi, Press three for Kannada and Press four for Tamil.', voice='Polly.Aditi',language="hi-IN")
  
    gather = Gather(num_digits=1, action='/gatherPincode')
    resp.append(gather)
    return str(resp)

@app.route('/gatherPincode',methods=['GET','POST'])
def gatherPincode():
    print("hi")
    resp = VoiceResponse()
    if 'Digits' in request.values:
        language = request.values['Digits']
        if language == '1':
            resp.say(en['message0'],voice='Polly.Aditi',language="hi-IN")
            resp.say(en['message1'], voice='Polly.Aditi',language="hi-IN")
            gather = Gather(num_digits=6, action='/gatherChoice/'+language)
            resp.append(gather)

        elif language == '2':
            resp.say(hi['message0'],voice='Polly.Aditi',language="hi-IN")
            resp.say(hi['message1'], voice='Polly.Aditi',language="hi-IN")
            gather = Gather(num_digits=6, action='/gatherChoice/'+language)
            resp.append(gather)

        elif language == '3':
            resp.say(kn['message0'],voice='Polly.Aditi',language="kn-IN")
            resp.say(kn['message1'], voice='Polly.Aditi',language="hi-IN")
            gather = Gather(num_digits=6, action='/gatherChoice/'+language)
            resp.append(gather)
        
        elif language == '4':
            resp.say(ta['message0'],voice='Polly.Aditi',language="hi-IN")
            resp.say(ta['message1'], voice='Polly.Aditi',language="hi-IN")
            gather = Gather(num_digits=6, action='/gatherChoice/'+language)
            resp.append(gather)
        else:
            resp.redirect('/answer')
    else:
        resp.redirect('/answer')
    print("himp")
    return str(resp)

@app.route('/gatherChoice/<language>', methods=['GET', 'POST'])
def gatherChoice(language):
    print("hola")
    resp = VoiceResponse()
    if 'Digits' in request.values:
        choice = request.values['Digits']
        if language == '1':
            gather = Gather(num_digits=1, action='/gatherData/'+language + '/'+choice)
            gather.say(en['message2'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)
        elif language == '2':

            gather = Gather(num_digits=1, action='/gatherData/'+language + '/'+choice)
            gather.say(hi['message2'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)

        elif language == '3':

            gather = Gather(num_digits=1, action='/gatherData/'+language + '/'+choice)
            gather.say(kn['message2'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)

        elif language == '4':

            gather = Gather(num_digits=1, action='/gatherData/'+language + '/'+choice)
            gather.say(ta['message2'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)

    return str(resp)



@app.route('/gatherData/<language>/<pincode>', methods=['GET', 'POST'])
def gatherData(language,pincode):
    # response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+pincode+'&sensor=true&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
    # ans = response.json()
    # lat,long = ans['results'][0]['geometry']['location']['lat'],ans['results'][0]['geometry']['location']['lng']
    # print(lat,long)
    # lat = str(lat)
    # long = str(long)
    resp = VoiceResponse()
    if 'Digits' in request.values:
        # print(request.values)
        menuItem = request.values['Digits']
        if language == '1':
            if menuItem == '1':
                resp.say(en['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=atm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(en['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message44'],voice='Polly.Aditi',language="hi-IN")
                gather = Gather(num_digits=1)
                time.sleep(5)
                resp.say(en['message45'],voice='Polly.Aditi',language="hi-IN")
                gather = Gather(num_digits=1)
                time.sleep(5)
                resp.say(en['message46'],voice='Polly.Aditi',language="hi-IN")
                gather = Gather(num_digits=1)
                time.sleep(5)
                resp.say(en['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '2':
                resp.say(en['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bank&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(en['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
                pass
            elif menuItem == '3':
                resp.say(en['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=post_office&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(en['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '4':
                resp.say(en['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(en['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message41'],voice='Polly.Aditi',language="hi-IN")
                resp.redirect('/answer')
                # message = name1+ " "+ place1 + "\n"+ name2+ " "+ place2 + "\n"+ name3+ " "+ place3 + "\n"
                # requests.post(url1,{"message":message,"caller":request.values['Caller']})
                pass
            elif menuItem == '5':
                resp.say(en['message35'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message3'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherScheme/'+language
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            resp.redirect('/answer')

        elif language == '2':
            if menuItem == '1':
                resp.say(hi['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=atm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(hi['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message41'],voice='Polly.Aditi',language="hi-IN")
                resp.redirect('/answer')
            elif menuItem == '2':
                resp.say(hi['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bank&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(hi['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message41'],voice='Polly.Aditi',language="hi-IN")
                resp.redirect('/answer')
                pass
            elif menuItem == '3':
                resp.say(hi['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=post_office&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(hi['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message41'],voice='Polly.Aditi',language="hi-IN")
                resp.redirect('/answer')
            elif menuItem == '4':
                resp.say(hi['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(hi['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
                # message = name1+ " "+ place1 + "\n"+ name2+ " "+ place2 + "\n"+ name3+ " "+ place3 + "\n"
                # requests.post(url1,{"message":message,"caller":request.values['Caller']})
                pass
            elif menuItem == '5':
                resp.say(hi['message35'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message3'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherScheme/'+language
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)

           
            
            resp.redirect('/answer')

        
        elif language == '3':
            if menuItem == '1':
                resp.say(kn['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=atm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(kn['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '2':
                resp.say(kn['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bank&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(kn['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
                pass
            elif menuItem == '3':
                resp.say(kn['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=post_office&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(kn['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '4':
                resp.say(kn['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(kn['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
                message = name1+ " "+ place1 + "\n"+ name2+ " "+ place2 + "\n"+ name3+ " "+ place3 + "\n"
                requests.post(url1,{"message":message,"caller":request.values['Caller']})
                pass
            elif menuItem == '5':
                resp.say(kn['message35'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message3'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherScheme/'+language
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            
            resp.redirect('/answer')
        
        elif language == '4':
            if menuItem == '1':
                resp.say(ta['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=atm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(ta['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '2':
                resp.say(ta['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bank&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(ta['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
                pass
            elif menuItem == '3':
                resp.say(ta['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=post_office&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(ta['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1'+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message41'],voice='Polly.Aditi',language="hi-IN")
                # resp.redirect('/answer')
            elif menuItem == '4':
                resp.say(ta['message42'],voice='Polly.Aditi',language="hi-IN")
                # response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+lat+','+long+'&type=bm&rankby=distance&fields=name,rating&key=AIzaSyCILGP87TZPkXUobQfqDp9mkPA7IXnEGXU')
                # ans = response.json()
                # name1,place1 = ans['results'][0]['name'],ans['results'][0]['vicinity']
                # name2,place2 = ans['results'][1]['name'],ans['results'][1]['vicinity']
                # name3,place3 = ans['results'][2]['name'],ans['results'][2]['vicinity']
                resp.say(ta['message43'],voice='Polly.Aditi',language="hi-IN")
                # resp.say('1 '+name1+', '+place1,voice='Polly.Aditi',language="hi-IN")
                # resp.say('2'+name2+', '+place2,voice='Polly.Aditi',language="hi-IN")
                # resp.say('3'+name3+', '+place3,voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message41'],voice='Polly.Aditi',language="hi-IN")
                message = name1+ " "+ place1 + "\n"+ name2+ " "+ place2 + "\n"+ name3+ " "+ place3 + "\n"
                requests.post(url1,{"message":message,"caller":request.values['Caller']})
                # resp.redirect('/answer')
            elif menuItem == '5':
                resp.say(ta['message35'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message3'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherScheme/'+language
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            
            resp.redirect('/answer')
    return str(resp)




@app.route('/gatherScheme/<language>',methods=['GET','POST'])
def gatherScheme(language):

    resp = VoiceResponse()

    if 'Digits' in request.values:
        # print(request.values)
        schemeType = request.values['Digits']
        if language == '1':   
            if schemeType == '1':
                resp.say(en['message4'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            else:
                resp.say(en['message5'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(en['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)

        elif language == '2':
            if schemeType == '1':
                resp.say(hi['message4'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            else:
                resp.say(hi['message5'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(hi['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)


        elif language == '3':
            if schemeType == '1':
                resp.say(kn['message4'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            else:
                resp.say(kn['message5'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(kn['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)


        elif language == '4':
            if schemeType == '1':
                resp.say(ta['message4'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
            else:
                resp.say(ta['message5'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message6'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message7'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message8'],voice='Polly.Aditi',language="hi-IN")
                resp.say(ta['message9'],voice='Polly.Aditi',language="hi-IN")
                url = '/gatherStatus/'+language + '/'+schemeType;
                gather = Gather(num_digits=1, action=url)
                resp.append(gather)
        else:
            resp.say(en['message10'],voice='Polly.Aditi',language="hi-IN")
            resp.redirect('/answer')
    return str(resp)


@app.route('/gatherStatus/<language>/<schemeChoice>',methods=['GET', 'POST'])
def gatherStatus(language,schemeChoice):
    resp = VoiceResponse()
    if 'Digits' in request.values:
        if language == '1':
            resp.say(en['message11'],voice='Polly.Aditi',language="hi-IN")
            statusChoice = request.values['Digits']
            url = '/gatherSchemeFinal/'+language + '/' + schemeChoice+'/'+statusChoice
            gather = Gather(num_digits=2, action=url)
            gather.say(en['message12'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)
        if language == '2':
            resp.say(hi['message11'],voice='Polly.Aditi',language="hi-IN")
            statusChoice = request.values['Digits']
            url = '/gatherSchemeFinal/'+language + '/' + schemeChoice+'/'+statusChoice
            gather = Gather(num_digits=2, action=url)
            gather.say(hi['message12'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)
        if language == '3':
            resp.say(kn['message11'],voice='Polly.Aditi',language="hi-IN")
            statusChoice = request.values['Digits']
            url = '/gatherSchemeFinal/'+language + '/' + schemeChoice+'/'+statusChoice
            gather = Gather(num_digits=2, action=url)
            gather.say(kn['message12'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)
        if language == '4':
            resp.say(ta['message11'],voice='Polly.Aditi',language="hi-IN")
            statusChoice = request.values['Digits']
            url = '/gatherSchemeFinal/'+language + '/' + schemeChoice+'/'+statusChoice
            gather = Gather(num_digits=2, action=url)
            gather.say(ta['message12'],voice='Polly.Aditi',language="hi-IN")
            resp.append(gather)

    else:
        resp.redirect('/answer')
    
    return str(resp)

@app.route('/gatherSchemeFinal/<language>/<schemeChoice>/<statusChoice>',methods=['GET', 'POST'])
def gatherSchemeFinal(language,schemeChoice,statusChoice):
    resp = VoiceResponse()

    if 'Digits' in request.values:
        age = request.values['Digits']
        age = int(age)
        schemeChoice = int(schemeChoice)
        statusChoice = int(statusChoice)
        if language == '1':
            resp.say(en['message13'],voice='Polly.Aditi',language="hi-IN")
            resp.say(en['message40'], voice='Polly.Aditi',language="hi-IN")
            if(schemeChoice == 1):
                if(statusChoice == 1):
                    if(age < 60):
                        resp.say('1'+en['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message18'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+en['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message19'], voice='Polly.Aditi',language="hi-IN")

                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+en['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message16'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+en['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message18'], voice='Polly.Aditi',language="hi-IN")

                    
                elif(statusChoice == 3):
                    if(age < 60):
                        resp.say('1'+en['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message21'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message22'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+en['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message24'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 4):

                    if(age < 60):
                        resp.say('1.'+en['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2.'+en['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3.'+en['message21'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1.'+en['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2.'+en['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3.'+en['message24'], voice='Polly.Aditi',language="hi-IN")

        
            elif(schemeChoice == 2):
                if(statusChoice == 1):

                    if(age < 60):
                        resp.say('1.'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2.'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3.'+en['message27'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1.'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2.'+en['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3.'+en['message27'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message29'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+en['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message27'], voice='Polly.Aditi',language="hi-IN")


                        
                elif(statusChoice == 3):

                    if(age < 60):
                        resp.say('1'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message29'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1.'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2.'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3.'+en['message29'], voice='Polly.Aditi',language="hi-IN")
                    
                elif(statusChoice == 4):
                    if(age < 60):
                        resp.say('1'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message27'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+en['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+en['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+en['message29'], voice='Polly.Aditi',language="hi-IN")

            resp.say(en['message41'],voice='Polly.Aditi',language="hi-IN")
        
        if language == '2':
            resp.say(hi['message13'],voice='Polly.Aditi',language="hi-IN")
            resp.say(hi['message40'], voice='Polly.Aditi',language="hi-IN")
            if(schemeChoice == 1):
                if(statusChoice == 1):
                    if(age < 60):
                        resp.say('1'+hi['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message18'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+hi['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message19'], voice='Polly.Aditi',language="hi-IN")

                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+hi['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message16'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+hi['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message18'], voice='Polly.Aditi',language="hi-IN")

                    
                elif(statusChoice == 3):
                    if(age < 60):
                        resp.say('1'+hi['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message21'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message22'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+hi['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message24'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 4):

                    if(age < 60):
                        resp.say('1'+hi['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message21'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+hi['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message24'], voice='Polly.Aditi',language="hi-IN")

        
            elif(schemeChoice == 2):
                if(statusChoice == 1):

                    if(age < 60):
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message27'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message27'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message29'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+hi['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message27'], voice='Polly.Aditi',language="hi-IN")


                        
                elif(statusChoice == 3):

                    if(age < 60):
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message29'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message29'], voice='Polly.Aditi',language="hi-IN")
                    
                elif(statusChoice == 4):
                    if(age < 60):
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message27'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+hi['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+hi['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+hi['message29'], voice='Polly.Aditi',language="hi-IN")

            resp.say(hi['message41'],voice='Polly.Aditi',language="hi-IN")

        if language == '3':
            resp.say(kn['message13'],voice='Polly.Aditi',language="hi-IN")
            resp.say(kn['message40'], voice='Polly.Aditi',language="hi-IN")
            if(schemeChoice == 1):
                if(statusChoice == 1):
                    if(age < 60):
                        resp.say('1'+kn['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message18'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+kn['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message19'], voice='Polly.Aditi',language="hi-IN")

                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+kn['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message16'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+kn['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message18'], voice='Polly.Aditi',language="hi-IN")

                    
                elif(statusChoice == 3):
                    if(age < 60):
                        resp.say('1'+kn['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message21'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message22'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+kn['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message24'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 4):

                    if(age < 60):
                        resp.say('1'+kn['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message21'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+kn['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message24'], voice='Polly.Aditi',language="hi-IN")

        
            elif(schemeChoice == 2):
                if(statusChoice == 1):

                    if(age < 60):
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message27'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message27'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message29'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+kn['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message27'], voice='Polly.Aditi',language="hi-IN")


                        
                elif(statusChoice == 3):

                    if(age < 60):
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message29'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message29'], voice='Polly.Aditi',language="hi-IN")
                    
                elif(statusChoice == 4):
                    if(age < 60):
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message27'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+kn['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+kn['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+kn['message29'], voice='Polly.Aditi',language="hi-IN")

            resp.say(kn['message41'],voice='Polly.Aditi',language="hi-IN")
        if language == '4':
            resp.say(ta['message13'],voice='Polly.Aditi',language="hi-IN")
            resp.say(ta['message40'], voice='Polly.Aditi',language="hi-IN")
            if(schemeChoice == 1):
                if(statusChoice == 1):
                    if(age < 60):
                        resp.say('1'+ta['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message18'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+ta['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message19'], voice='Polly.Aditi',language="hi-IN")

                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+ta['message17'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message16'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+ta['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message18'], voice='Polly.Aditi',language="hi-IN")

                    
                elif(statusChoice == 3):
                    if(age < 60):
                        resp.say('1'+ta['message16'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message21'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message22'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+ta['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message24'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 4):

                    if(age < 60):
                        resp.say('1'+ta['message20'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message18'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message21'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+ta['message23'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message19'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message24'], voice='Polly.Aditi',language="hi-IN")

        
            elif(schemeChoice == 2):
                if(statusChoice == 1):

                    if(age < 60):
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message27'], voice='Polly.Aditi',language="hi-IN")
                    else:
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message27'], voice='Polly.Aditi',language="hi-IN")

                        
                elif(statusChoice == 2):

                    if(age < 60):
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message29'], voice='Polly.Aditi',language="hi-IN")


                    else:
                        resp.say('1'+ta['message28'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message27'], voice='Polly.Aditi',language="hi-IN")


                        
                elif(statusChoice == 3):

                    if(age < 60):
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message29'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message29'], voice='Polly.Aditi',language="hi-IN")
                    
                elif(statusChoice == 4):
                    if(age < 60):
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message27'], voice='Polly.Aditi',language="hi-IN")

                    else:
                        resp.say('1'+ta['message25'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('2'+ta['message26'], voice='Polly.Aditi',language="hi-IN")
                        resp.say('3'+ta['message29'], voice='Polly.Aditi',language="hi-IN")

        resp.say(ta['message41'],voice='Polly.Aditi',language="hi-IN")
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)