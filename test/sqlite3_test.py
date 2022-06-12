import json
import sqlite3

class Key():
    LANGKEY = 'langkey'
    ISO_CODE = 'isoCode'
    KEYS = 'keys'
    ID = 'id'
    RAW = 'raw'
    TEXT = 'text'

ISO_CODE = {
    'enUS': "en-US",
    "ptBR": "pt-BR",
    "frFR": "fr-FR",
    "itIT": "it-IT",
    "deDE": "de-DE",
    "esES": "es-ES",
    "ruRU": "ru-RU",
    "jaJP": "ja-JP",
    "koKR": "ko-KR"
}    

DB_FILE = r'C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Raw\Raw_CardDatabase_3fc09d06a61a10dcabcc28369ea62b2b.mtga'

    
# locsの準備
locs = []
for v in ISO_CODE.values():
    locs.append(
        {
            Key.LANGKEY: None,
            Key.ISO_CODE: v,
            Key.KEYS: []
        }
    )

def exist_id(loc, id):
    for key in loc[Key.KEYS]:
        if key.get(Key.ID) == id:
            return True
    return False

def get_index_by_id(keys, id):
    for i in range(len(keys)):
        if keys[i].get(Key.ID) == id:
            return i
    return None

# SQL参照
con = sqlite3.connect(DB_FILE)
cur = con.cursor()
records = cur.execute('''select * from Localizations''')
for record in records:
    print("{}, {}".format(record[0], record[1]))
    i = 3
    is_raw = True if record[1] == 1 else False
    for loc in locs:
        if exist_id(loc, record[0]):
            j = get_index_by_id(loc[Key.KEYS], record[0])
            if is_raw:
                loc[Key.KEYS][j][Key.RAW] = record[i]
            else:
                loc[Key.KEYS][j][Key.TEXT] = record[i]
        else:
            loc[Key.KEYS].append(
                {
                    Key.ID: record[0]
                }
            )
            if is_raw:
                loc[Key.KEYS][-1][Key.RAW] = record[i]
            else:
                loc[Key.KEYS][-1][Key.TEXT] = record[i]
        i += 1

with open("Localizations.json", "w", encoding='utf-8') as f:
    json.dump(locs, f)


#i = 0
#with open("Localizations.txt", "w", encoding='utf-8') as f:
 #   for record in records:
 #       #print(record)
 #       line = ''
  #      for item in record:
   #         line += str(item) + ", "
   #     f.write(line + '\n')
   #     i += 1
    #    if i >= 10:
    #       break
