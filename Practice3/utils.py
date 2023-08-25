#First 4 letters
def first4(name):
    name = name.upper()
    listName = name.split()
    letters = listName[-2][0] + listName[-2][1] + listName[-1][0] + listName[0][0]
    return letters

#Adding birth date letters
def second6(birthdate):
    listBirth = list(birthdate)
    letters = ''.join(listBirth[2:])
    return letters

#Adding gender
def third1(gender):
    gender = gender.upper()
    if gender == 'MALE':
        return 'H'
    else:
        return 'M'

#Adding federal entity
def fourth2(entity):
    entity = entity.lower()
    for value in entity_dict:
        if value == entity:
            print('Logrado')
            return entity_dict[value].upper()
    return 'c'

#Adding consonants
def fifth3(name):
    return 'e'

#Adding random code
def sixth2():
    return 'f'

##############################################
def firstInternalVocal(word):
    pass

def firstInternalConsonant():
    pass

entity_dict = {
    "aguascalientes": "as",
    "baja california": "bc",
    "baja california sur": "bs",
    "campeche": "cc",
    "chiapas": "cs",
    "chihuahua": "ch",
    "ciudad de mexico": "df",
    "coahuila": "cl",
    "colima": "cm",
    "durango": "dg",
    "guanajuato": "gt",
    "guerrero": "gr",
    "hidalgo": "hg",
    "jalisco": "jc",
    "mexico": "mc",
    "michoacan": "mn",
    "morelos": "ms",
    "nayarit": "nt",
    "nuevo leon": "nl",
    "oaxaca": "oc",
    "puebla": "pl",
    "queretaro": "qo",
    "quintana roo": "qr",
    "san luis potosi": "sp",
    "sinaloa": "sl",
    "sonora": "sr",
    "tabasco": "tc",
    "tamaulipas": "ts",
    "tlaxcala": "tl",
    "veracruz": "vz",
    "yucatan": "yn",
    "zacatecas": "zs"
}