import logging
import os
import sympy
import json
import random
import discord
from discord.ext import commands
from discord import File


def header(n, name):
    return {
        "timed": 0,
        "count": n,
        "questions": list(range(1, n + 1)),
        "title": name
        + "​⁠⁠​​⁠​​​⁠⁠​​​​⁠​⁠⁠​⁠⁠​⁠​⁠⁠​⁠⁠⁠​​​⁠​⁠⁠⁠​​​⁠​⁠⁠⁠​​​⁠​⁠⁠⁠​​​⁠​​​​​​⁠⁠⁠⁠​​⁠​⁠⁠​⁠⁠⁠⁠​⁠⁠⁠​⁠​⁠​​⁠​​​​​​⁠⁠⁠​​⁠​​⁠⁠​​⁠​⁠​⁠⁠​​​​⁠​⁠⁠​⁠⁠​​​⁠⁠​⁠⁠​​​⁠⁠⁠⁠​​⁠​​⁠​​​​​​⁠⁠⁠​⁠​⁠​⁠⁠⁠​​⁠⁠​⁠⁠​​⁠​⁠​⁠⁠​​⁠​​​​⁠​​​​​​⁠⁠⁠​⁠​​​⁠⁠​⁠​​​​⁠⁠​⁠​​⁠​⁠⁠⁠​​⁠⁠​​⁠​​​​​​⁠⁠⁠​⁠⁠⁠​⁠⁠​⁠​​⁠​⁠⁠⁠​⁠​​​⁠⁠​⁠​​​​⁠⁠​⁠⁠⁠⁠​⁠⁠⁠​⁠​⁠​⁠⁠⁠​⁠​​​​⁠​​​​​​⁠⁠​⁠⁠​⁠​⁠⁠⁠⁠​​⁠​​⁠​​​​​​⁠⁠⁠​​​​​⁠⁠​​⁠​⁠​⁠⁠⁠​​⁠​​⁠⁠​⁠⁠​⁠​⁠⁠​⁠​​⁠​⁠⁠⁠​​⁠⁠​⁠⁠⁠​​⁠⁠​⁠⁠​⁠​​⁠​⁠⁠​⁠⁠⁠⁠​⁠⁠​⁠⁠⁠​​​⁠​​​​​​⁠⁠⁠​​⁠⁠​⁠⁠​⁠⁠​⁠​⁠⁠​⁠​​​​​​​⁠⁠​⁠​​​​⁠​⁠​​​​​⁠⁠​⁠​​​​⁠​⁠​​⁠⁠​​⁠​​​⁠⁠​⁠⁠⁠⁠​⁠⁠​⁠⁠⁠​​​⁠​​⁠⁠⁠​⁠⁠⁠​⁠​​​​⁠​​​​​​⁠⁠​⁠⁠​⁠​⁠⁠​​⁠​⁠​⁠⁠⁠​​⁠⁠​⁠⁠⁠​​⁠⁠​​⁠​​​​​​⁠⁠⁠​⁠⁠⁠​⁠⁠​⁠​​⁠​⁠⁠⁠​⁠​​​⁠⁠​⁠​​​​​⁠​​​​​​⁠⁠⁠​⁠​​​⁠⁠​⁠​​​​⁠⁠​​⁠​⁠​​⁠​​​​​​⁠⁠​​​⁠⁠​⁠⁠​⁠​​⁠​⁠⁠​​​​⁠​​⁠​​​​​​​⁠⁠⁠⁠⁠​​​⁠⁠⁠​⁠​​​⁠​⁠​​​",
        "useCustomHeader": False,
        "customHeader": "",
        "testtype": "cstate",
    }


def keyStringRandom(xeno):
    spl = lambda word: [char for char in word]
    if xeno:
        A = spl("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
    else:
        A = spl("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while not test1(A):
        random.shuffle(A)
    return "".join(A)


def test1(l):
    for i in range(26):
        if ord(l[i]) - 65 == i:
            return False
    return True


def genRandMono(num, quote, pat, hint):
    key = keyStringRandom(False)
    r = {}
    for i in range(0, 26):
        r[chr(i + 65)] = key[i]
    x = {
        "cipherString": quote,
        "encodeType": "random",
        "offset": 1,
        "shift": 1,
        "offset2": 1,
        "keyword": "",
        "keyword2": "",
        "alphabetSource": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "alphabetDest": key,
        "curlang": "en",
        "replacement": r,
        "editEntry": str(num),
    }
    if pat == "1":
        x["cipherType"] = "patristocrat"
        x["question"] = "<p>Solve this patristocrat.</p>"
        x["points"] = 600
    else:
        x["cipherType"] = "aristocrat"
        x["question"] = "<p>Solve this aristocrat.</p>"
        x["points"] = 250
    if hint == "0":
        x["question"] = (
            x["question"][:-4] + " The first word is " + quote.split(" ")[0] + ".</p>"
        )
        if pat == "1":
            x["points"] = x["points"] - 30 * len(quote.split(" ")[0])
        else:
            x["points"] = x["points"] - 10 * len(quote.split(" ")[0])
    if hint == "1":
        letter = random.randint(97, 122)
        while r[chr(letter - 32)] not in quote.upper():
            letter = random.randint(97, 122)
        m = key[letter - 97]
        x["question"] = (
            x["question"][:-4]
            + " The letter "
            + chr(letter).upper()
            + " maps to "
            + m
            + ".</p>"
        )
        if pat == "1":
            x["points"] = x["points"] - 15 * quote.count(chr(letter))
        else:
            x["points"] = x["points"] - 5 * quote.count(chr(letter))
    return x


def genRandXeno(num, quote, hint):
    key = keyStringRandom(True)
    quote = genSpanishQuote(70, 160)
    r = {}
    for i in range(0, 14):
        r[chr(i + 65)] = key[i]
    r["Ñ"] = key[14]
    for i in range(14, 26):
        r[chr(i + 65)] = key[i + 1]
    x = {
        "cipherString": quote,
        "encodeType": "random",
        "offset": 1,
        "shift": 1,
        "offset2": 1,
        "keyword": "",
        "keyword2": "",
        "alphabetSource": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
        "alphabetDest": key,
        "curlang": "es",
        "replacement": r,
        "editEntry": str(num),
        "cipherType": "aristocrat",
        "question": "<p>Solve this xenocrypt.</p>",
        "points": 400,
    }
    return x


def genRandAffine(num, quote, enc):
    a = random.choice([3, 5, 7, 9, 11, 15, 17, 19, 21, 23])
    b = random.randint(3, 24)
    r = {}
    for i in range(0, 26):
        r[str(i + 65)] = chr((i * a + b) % 26 + 65)
    x = {
        "a": a,
        "b": b,
        "cipherString": quote,
        "cipherType": "affine",
        "solclick1": -1,
        "solclick2": -1,
        "replacement": r,
        "curlang": "en",
        "editEntry": num,
    }
    if enc == "E":
        x["operation"] = "encode"
        x["points"] = 175
        x["question"] = (
            "<p>Encode this sentence with the Affine cipher. (a,b)=("
            + str(a)
            + ","
            + str(b)
            + ").</p>"
        )
    elif enc == "D":
        x["operation"] = "decode"
        x["points"] = 150
        x["question"] = (
            "<p>Decode this sentence which has been encoded with an Affine cipher. (a,b)=("
            + str(a)
            + ","
            + str(b)
            + ").</p>"
        )
    elif enc == "C":
        one = random.randint(0, 12)
        two = random.randint(13, 25)
        onemap = (one * a + b) % 26
        twomap = (two * a + b) % 26
        x["operation"] = "crypt"
        x["points"] = 200
        x["question"] = (
            "<p>Decode this sentence which has been encoded with an Affine cipher. The letters "
            + chr(onemap + 65)
            + " and "
            + chr(twomap + 65)
            + " map to "
            + chr(one + 65)
            + " and "
            + chr(two + 65)
            + ".</p>"
        )
    return x


def genRandCaesar(num, quote, enc):
    a = random.randint(3, 24)
    r = {}
    for i in range(0, 26):
        r[str(i + 65)] = chr((i + a) % 26 + 65)
    x = {
        "offset": a,
        "offset2": None,
        "cipherString": quote,
        "cipherType": "caesar",
        "solclick1": -1,
        "solclick2": -1,
        "replacement": r,
        "curlang": "en",
        "editEntry": num,
        "shift": None,
    }
    if enc == "E":
        x["operation"] = "encode"
        x["points"] = 150
        x["question"] = (
            "<p>Encode this sentence with the Caesar cipher with offset "
            + str(a)
            + ".</p>"
        )
    elif enc == "D":
        x["operation"] = "decode"
        x["points"] = 125
        x[
            "question"
        ] = "<p>Decode this sentence which has been encoded with an Caesar cipher.</p>"
    return x


def genRandVig(num, quote, enc):
    quote = genQuoteLength(50, 70)
    key = getRandWord(5, 8)
    x = {
        "cipherType": "vigenere",
        "keyword": key,
        "cipherString": quote,
        "findString": "",
        "blocksize": len(key),
        "curlang": "en",
        "editEntry": str(num),
    }
    if enc == "E":
        x["operation"] = "encode"
        x["question"] = (
            "<p>Encode this sentence with the Vigenere cipher using the keyword "
            + key
            + ".</p>"
        )
        x["points"] = "200"
    if enc == "D":
        x["operation"] = "decode"
        x["question"] = (
            "<p>Decode this sentence with the Vigenere cipher using the keyword "
            + key
            + ".</p>"
        )
        x["points"] = "175"
    if enc == "C":
        x["operation"] = "crypt"
        x["question"] = (
            "<p>Decode this sentence with the Vigenere cipher. The first "
            + str(len(key))
            + " characters of the sentence is "
            + quote[: len(key)]
            + ".</p>"
        )
        x["points"] = "175"
    return x


def genRand2x2Hill(num, quote, enc):
    quote = quote.split(" ")
    q = ""
    a = 0
    while len(q) < 12:
        q += quote[a] + " "
        a += 1
    q = q[:-1]
    key = get2x2Key()
    x = {
        "cipherString": q,
        "cipherType": "hill",
        "curlang": "en",
        "editEntry": num,
        "keyword": key,
    }
    if enc == "C":
        x["operation"] = "decode"
        x["points"] = 100
        x["question"] = "<p>Compute the decryption matrix of the key " + key + ".</p>"
        x["cipherString"] = ""
    else:
        x["offset"] = None
        x["alphabetSource"] = ""
        x["alphabetDest"] = ""
        x["shift"] = None
        x["offset2"] = None
    if enc == "E":
        x["operation"] = "encode"
        x["points"] = 225
        x["question"] = (
            "<p>Encrypt this phrase with the key " + key + " using the Hill cipher.</p>"
        )
    if enc == "D":
        x["operation"] = "decode"
        x["points"] = 175
        x["question"] = (
            "<p>Decrypt this phrase with the key " + key + " using the Hill cipher.</p>"
        )
    return x


def genRand3x3Hill(num, quote, enc):
    quote = quote.split(" ")
    q = ""
    a = 0
    while len(q) < 12:
        q += quote[a] + " "
        a += 1
    q = q[:-1]
    key = get3x3Key()
    x = {
        "cipherString": q,
        "cipherType": "hill",
        "curlang": "en",
        "editEntry": num,
        "keyword": key,
    }
    if enc == "E":
        x["operation"] = "encode"
        x["points"] = 225
        x["question"] = (
            "<p>Encrypt this phrase with the key " + key + " using the Hill cipher.</p>"
        )
    if enc == "D":
        x["operation"] = "decode"
        x["points"] = 175
        x["question"] = (
            "<p>Decrypt this phrase with the key " + key + " using the Hill cipher.</p>"
        )
    return x


def genRandMorbit(num, quote, enc):
    quote = genQuoteLength(35, 55)
    l = ["OO", "O-", "OX", "-O", "--", "-X", "XO", "X-", "XX"]
    l2 = list(range(1, 10))
    random.shuffle(l2)
    replacement = {}
    for i in range(9):
        replacement[l[i]] = str(l2[i])
    x = {
        "cipherString": quote,
        "cipherType": "morbit",
        "curlang": "en",
        "editEntry": str(num),
        "offset": None,
        "alphabetSource": "",
        "alphabetDest": "",
        "shift": None,
        "offset2": None,
        "replacement": replacement,
    }
    if enc == "D":
        x["operation"] = "decode"
        x["points"] = 225
        x["question"] = (
            "<p>Decode this quote which has been encoded using the Morbit cipher. OO,OX,X-,XO,XX matches to "
            + replacement["OO"]
            + ","
            + replacement["OX"]
            + ","
            + replacement["X-"]
            + ","
            + replacement["XO"]
            + ","
            + replacement["XX"]
            + ".</p>"
        )
        x["hint"] = "123456"
    if enc == "C":
        x["operation"] = "crypt"
        x["points"] = 250
        x["question"] = (
            "<p>Decode this quote which has been encoded using the Morbit cipher. The first four letters decrypts to "
            + quote[:4]
            + ".</p>"
        )
        x["hint"] = "123456"
    return x


def genRandPollux(num, quote, enc):
    quote = genQuoteLength(35, 55)
    morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "xx",
    }
    l = list(range(0, 10))
    random.shuffle(l)
    enc1 = ""
    for i in quote:
        if i in morse:
            enc1 += morse[i] + "x"
    enc1 = enc1[:-1]
    enc2 = ""
    for i in enc1:
        if i == ".":
            enc2 += str(l[random.randint(0, 3)])
        if i == "-":
            enc2 += str(l[random.randint(0, 2) + 4])
        if i == "x":
            enc2 += str(l[random.randint(0, 2) + 7])
    x = {
        "cipherString": quote,
        "cipherType": "pollux",
        "replacement": {},
        "dotchars": str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]),
        "dashchars": str(l[4]) + str(l[5]) + str(l[6]),
        "xchars": str(l[7]) + str(l[8]) + str(l[9]),
        "curlang": "en",
        "editEntry": str(num),
        "offset": None,
        "alphabetSource": "",
        "alphabetDest": "",
        "shift": None,
        "offset2": None,
        "encoded": enc2,
    }
    if enc == "D":
        x["operation"] = "decode"
        x["points"] = 275
        x["question"] = (
            "<p>Decode this quote which has been encoded with a Pollux cipher. "
            + str(l[0])
            + ","
            + str(l[1])
            + ","
            + str(l[4])
            + ","
            + str(l[5])
            + ","
            + str(l[7])
            + ","
            + str(l[8])
            + "= . . - - x x.</p>"
        )
    if enc == "C":
        x["operation"] = "crypt"
        x["points"] = 350
        x["crib"] = quote[:4]
        x["question"] = (
            "<p>Decode this quote which has been encoded with a Pollux cipher. The first four letters are "
            + quote[:4]
            + ".</p>"
        )
    return x


def genRandBacon(num, quote, mode):
    quote = genQuoteLength(30, 45)
    x = {
        "cipherString": quote,
        "cipherType": "baconian",
        "curlang": "en",
        "editEntry": str(num),
        "offset": 1,
        "alphabetSource": "",
        "alphabetDest": "",
        "shift": None,
        "offset2": None,
        "linewidth": 53,
        "words": [],
        "question": "<p>Decode this quote which has been encoded using the Baconian cipher.</p>",
    }
    if mode == "W":
        x["operation"] = "words"
        x["points"] = 450
        x["abMapping"] = random.choice(
            [
                "ABABABABABABABABABABABABAB",
                "AAAAAAAAAAAAABBBBBBBBBBBBB",
                "BBBBBBBBBBBBBAAAAAAAAAAAAA",
            ]
        )
        x["texta"] = "A"
        x["textb"] = "B"
        return x
    mappings = random.choice(
        [
            ["ABC", "XYZ"],
            ["ACE", "BDF"],
            ["!@#$%", "^&*()"],
            ["!#%&(", "@$^*)"],
            ["QWERTY", "ASDFGH"],
            ["abcd", "ABCD"],
            ["{([", "}])"],
            ["aeiou", "bcdfghjklmnpqrstvwxyz"],
            ["acegikmoqsuwy", "bdfhjlnprtvxz"],
            ["abcdefghijklm", "nopqrstuvwxyz"],
            ["nopqrstuvwxyz", "abcdefghijklm"],
            ["XYZ", "ABC"],
            ["BDF", "ACE"],
            ["^&*()", "!@#$%"],
            ["@$^*)", "!#%&("],
            ["ASDFGH", "QWERTY"],
            ["ABCD", "abcd"],
            ["}])", "{(["],
            ["bcdfghjklmnpqrstvwxyz", "aeiou"],
            ["bdfhjlnprtvxz", "acegikmoqsuwy"],
            ["nopqrstuvwxyz", "abcdefghijklm"],
        ]
    )
    a = mappings[0]
    b = mappings[1]
    x["texta"] = a
    x["textb"] = b
    if random.randint(0, 2) == 2:
        temp = getBaconWords()
        x["texta"] = a[0]
        x["textb"] = a[1]
    if mode == "L":
        x["operation"] = "let4let"
        x["points"] = 200
        x["abMapping"] = "ABABABABABABABABABABABABAB"
    if mode == "S":
        x["operation"] = "sequence"
        x["points"] = 300
        x["abMapping"] = "ABABABABABABABABABABABABAB"
    return x


def RSA(num, enc):
    p = sympy.randprime(200, 1000)
    q = sympy.randprime(200, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = sympy.randprime(0, n)
    while sympy.gcd(e, phi) != 1:
        e = sympy.randprime(0, n)
    d = sympy.mod_inverse(e, phi)
    x = {
        "cipherString": "",
        "cipherType": "rsa",
        "curlang": "en",
        "editEntry": "1308",
        "offset": None,
        "alphabetSource": "",
        "alphabetDest": "",
        "shift": None,
        "offset2": None,
        "name1": "Allen",
        "rsa": {"p": p, "q": q, "n": n, "phi": phi, "e": e, "d": d},
    }
    if enc == "E":
        x["operation"] = "rsa2"
        x["digitsPrime"] = 4
        x["digitsCombo"] = 4
        x["points"] = 350
        x["combo"] = 1000
        x["question"] = (
            "<p>Given primes (p,q,e)=("
            + str(p)
            + ","
            + str(q)
            + ","
            + str(e)
            + "), compute the private key d.</p>"
        )
    if enc == "D":
        year = random.randint(1950, 2000)
        enc = pow(year, e, n)
        x["operation"] = "rsa4"
        x["digitsPrime"] = 4
        x["digitsCombo"] = 4
        x["points"] = 500
        x["year"] = year
        x["encrypted"] = enc
        x["name2"] = "Jason"
        x["question"] = (
            "<p>Given (n,c,d)=("
            + str(n)
            + ","
            + str(enc)
            + ","
            + str(d)
            + "), compute the original message m.</p>"
        )
    return x


def getBaconWords():
    while 1:
        a = getRandWord(4, 7)
        b = getRandWord(4, 7)
        if len(a) + len(b) == len(set(a + b)):
            return [a, b]


def getRandWord(min, max):
    f = open("words.txt", "r")
    for i in range(random.randint(0, 9000)):
        f.readline()
    r = ""
    while len(r) < min or len(r) > max:
        r = f.readline().strip()
    return r


def genQuotes(n):
    quotes = open("quotes.txt", "r")
    l = []
    for i in range(40569):
        l.append(quotes.readline().strip())
    random.shuffle(l)
    count = 0
    loc = 0
    r = []
    while count < n:
        if len(l[loc]) > 65 and len(l[loc]) < 160:
            r.append(l[loc])
            count += 1
        loc += 1
    return r


def genQuoteLength(min, max):
    quotes = open("quotes.txt", "r")
    l = []
    for i in range(40569):
        l.append(quotes.readline().strip())
    random.shuffle(l)
    loc = 0
    while 1:
        if len(l[loc]) > min and len(l[loc]) < max:
            return l[loc]
        loc += 1


def genSpanishQuote(min, max):
    json_file = open("spanish.json", "r")
    l = []
    data = json.load(json_file)
    for p in data["quotes"]:
        l.append(p["Cita"])
    random.shuffle(l)
    loc = 0
    while 1:
        if len(l[loc]) > min and len(l[loc]) < max:
            q = l[loc][1:-1]
            return q
        loc += 1


def getDeterminant(l):
    if len(l) == 4:
        return (l[1] * l[2] - l[0] * l[3]) % 26
    return 0


def get2x2Key():
    f = open("2x2hillwords", "r")
    for i in range(0, random.randint(0, 490)):
        f.readline()
    return f.readline().strip().lower()


def get3x3Key():
    f = open("3x3hillwords", "r")
    for i in range(0, random.randint(0, 4900)):
        f.readline()
    return f.readline().strip().lower()


def genTest():
    na = input("Test Name: ")
    preset = input(
        "Would you like to use a preset? 1 = All types, 2 = National level test, 3 = Regional level test, 4 = Aristo Spam, 5 = Patristo Spam, 6 = No: "
    )
    l = []
    if preset == "1":
        l = [
            "1 2",
            "1 1",
            "1 0",
            "2 2",
            "2 1",
            "2 0",
            "3 D",
            "3 E",
            "3 C",
            "4 D",
            "4 E",
            "5 D",
            "5 E",
            "5 C",
            "6 D",
            "6 E",
            "6 C",
            "7 D",
            "7 E",
            "8 1",
            "9 L",
            "9 S",
            "9 W",
            "10 D",
            "10 E",
            "11 D",
            "11 C",
            "12 D",
            "12 C",
        ]
        n = 29
    elif preset == "2":
        aff = ["3 D", "3 E", "3 C"]
        vig = ["5 D", "5 E", "5 C"]
        hill2 = ["6 D", "6 E", "6 C"]
        hill3 = ["7 D", "7 E"]
        bac = ["9 L", "9 S", "9 W"]
        mor = ["11 D", "11 C", "12 D", "12 C"]
        random.shuffle(aff)
        random.shuffle(vig)
        random.shuffle(hill2)
        random.shuffle(hill3)
        random.shuffle(bac)
        random.shuffle(mor)
        l = [
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "2 2",
            "2 1",
            "2 0",
            aff[0],
            aff[1],
            "4 D",
            "4 E",
            vig[0],
            vig[1],
            hill2[0],
            hill2[1],
            hill3[0],
            "8 1",
            bac[0],
            bac[1],
            "10 D",
            "10 E",
            mor[0],
            mor[1],
            mor[2],
        ]
        n = 30
    elif preset == "3":
        enc = ["3 E", "4 E", "5 E", "6 E"]
        bac = ["9 L", "9 S", "9 W"]
        random.shuffle(enc)
        random.shuffle(bac)
        l = [
            "1 0",
            "1 1",
            "1 2",
            "1 2",
            "1 2",
            "1 2",
            "2 2",
            "2 0",
            "3 D",
            "4 D",
            "5 D",
            "6 D",
            enc[0],
            enc[1],
            "8 1",
            bac[0],
            bac[1],
            "11 D",
            "12 D",
        ]
        n = 19
    elif preset == "4":
        l = ["1 2"] * 20
        n = 20
    elif preset == "5":
        l = ["2 2"] * 10
        n = 10
    else:
        l = preset
        n = len(l)
    q = genQuotes(n + 1)
    test = {"TEST.0": header(n, na)}
    test["CIPHER.0"] = genRandMono(0, q[len(q) - 1], False, 0)
    for i in range(n):
        question = l[i].split(" ")
        if int(question[0]) <= 2:
            test["CIPHER." + str(i + 1)] = genRandMono(
                i, q[i], "1" if question[0] == "2" else 0, question[1]
            )
        if int(question[0]) == 3:
            test["CIPHER." + str(i + 1)] = genRandAffine(i, q[i], question[1])
        if int(question[0]) == 4:
            test["CIPHER." + str(i + 1)] = genRandCaesar(i, q[i], question[1])
        if int(question[0]) == 5:
            test["CIPHER." + str(i + 1)] = genRandVig(i, q[i], question[1])
        if int(question[0]) == 6:
            test["CIPHER." + str(i + 1)] = genRand2x2Hill(i, q[i], question[1])
        if int(question[0]) == 7:
            test["CIPHER." + str(i + 1)] = genRand3x3Hill(i, q[i], question[1])
        if int(question[0]) == 8:
            test["CIPHER." + str(i + 1)] = genRandXeno(i, q[i], question[1])
        if int(question[0]) == 9:
            test["CIPHER." + str(i + 1)] = genRandBacon(i, q[i], question[1])
        if int(question[0]) == 10:
            test["CIPHER." + str(i + 1)] = RSA(i, question[1])
        if int(question[0]) == 11:
            test["CIPHER." + str(i + 1)] = genRandMorbit(i, q[i], question[1])
        if int(question[0]) == 12:
            test["CIPHER." + str(i + 1)] = genRandPollux(i, q[i], question[1])
    file = open("CodeTests/" + na + ".json", "w")
    file.write(json.dumps(test))
    file.close()
    return json.dumps(test)


genTest()

