import sqlite3
from locale import getlocale


class Table():
    ABILITIES = 'Abilities'
    CARDS = 'Cards'
    LOCALIZATIONS = 'Localizations'
    ENUMS = 'Enums'

class Column():
    CID = 0
    NAME = 1
    TYPE = 2
    NOTNULL = 3
    DEFAULT_VALUE = 4
    PRIMARY_KEY = 5

class Row():
    LOC_ID = 'LocId'
    FORMATTED = 'Formatted'
    TYPE = 'Type'

class Key():
    ID = 'id'
    TEXT = 'text'
    NAME = 'name'
    VALUES = 'values'

ISO_CODE = {
    'English': 'enUS',
    'Portuguese': 'ptBR',
    'French': 'frFR',
    'Italian': 'itIT',
    'German': 'deDE',
    'Spanish': 'esES',
    'Castilian': 'esES',
    'Russian': 'ruRU',
    'Japanese': 'jaJP',
    'Korean': 'koKR'
}    

ENUMS_TYPES = [
    'CardType',
    'Color',
    'CounterType',
    'FailureReason',
    'MatchState',
    'Phase',
    'ResultCode',
    'Step',
    'SubType',
    'SuperType'
]

def get_column_names(cur, table_name):
    rst = []
    records = cur.execute("PRAGMA table_info('"+table_name+"')")
    rst = [record[Column.NAME] for record in records]
    return rst

def sqlite2json(sqlite_filepath):
    abilities = []
    cards = []
    loc = []
    enums = []
    lang = getlocale()[0].split("_")[0]
    iso_code = ISO_CODE.get(lang) if ISO_CODE.get(lang) else ISO_CODE['English']

    con = sqlite3.connect(sqlite_filepath)
    cur = con.cursor()

    # Abilities
    column_names = get_column_names(cur, Table.ABILITIES)
    records = cur.execute("select * from "+Table.ABILITIES)
    for record in records:
        ability = {}
        for i in range(len(record)):
            ability[column_names[i]] = record[i]
        abilities.append(ability)

    # Cards
    column_names = get_column_names(cur, Table.CARDS)
    records = cur.execute("select * from "+Table.CARDS)
    for record in records:
        card = {}
        for i in range(len(record)):
            card[column_names[i]] = record[i]
        cards.append(card)

    # Localizations
    records = cur.execute("select "+Row.LOC_ID+", "+iso_code.replace('_', '')+" from "+Table.LOCALIZATIONS+" where "+Row.FORMATTED+" = 1")
    for record in records:
        loc.append(
            {
                Key.ID: record[0],
                Key.TEXT: record[1]
            }
        )
    
    # Enums
    for type in ENUMS_TYPES:
        enums.append(
            {
                Key.NAME: type,
                Key.VALUES: []
            }
        )
        records = cur.execute("select * from "+Table.ENUMS+" where "+Row.TYPE+ " = '"+type+"'")
        for record in records:
            enums[-1][Key.VALUES].append(
                {
                    Key.ID: record[1],
                    Key.TEXT: record[2]
                }
            )

    return abilities, cards, loc, enums

if __name__ == "__main__":
    from json import dump
    abilities, cards, loc, enums = sqlite2json(r'C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Raw\Raw_CardDatabase_252a56d6e7f5de84051785bf7dbb6d49.mtga')

    with open("abilities.json", "w", encoding='utf-8') as f:
       dump(abilities, f, indent=2, ensure_ascii=False)
    
    with open("cards.json", "w", encoding='utf-8') as f:
        dump(cards, f, indent=2, ensure_ascii=False)

    with open("loc.json", "w", encoding='utf-8') as f:
       dump(loc, f, indent=2, ensure_ascii=False)
    
    with open("enums.json", "w", encoding='utf-8') as f:
        dump(enums, f, indent=2, ensure_ascii=False)
