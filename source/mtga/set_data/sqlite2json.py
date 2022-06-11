import sqlite3
from locale import getlocale

class Table():
    LOCALIZATIONS = 'Localizations'
    ENUMS = 'Enums'

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

def sqlite2json(sqlite_filepath):
    loc = []
    enums = []
    lang = getlocale()[0].split("_")[0]
    iso_code = ISO_CODE.get(lang) if ISO_CODE.get(lang) else ISO_CODE['English']

    con = sqlite3.connect(sqlite_filepath)
    cur = con.cursor()

    records = cur.execute("select "+Row.LOC_ID+", "+iso_code.replace('_', '')+" from "+Table.LOCALIZATIONS+" where "+Row.FORMATTED+" = 1")
    for record in records:
        loc.append(
            {
                Key.ID: record[0],
                Key.TEXT: record[1]
            }
        )
    
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

    return loc, enums

if __name__ == "__main__":
    from json import dump
    loc, enums = sqlite2json(r'C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Raw\Raw_CardDatabase_3fc09d06a61a10dcabcc28369ea62b2b.mtga')

    with open("loc.json", "w", encoding='utf-8') as f:
        dump(loc, f, indent=2, ensure_ascii=False)
    
    with open("enums.json", "w", encoding='utf-8') as f:
        dump(enums, f, indent=2, ensure_ascii=False)
