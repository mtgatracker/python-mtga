import json
import sqlite3
from locale import getlocale

class Key():
    TEXT = 'text' 

class Row():
    LOC_ID = 'LocId'
    FORMATTED = 'Formatted'

class Table():
    LOCALIZATIONS = 'Localizations'

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

DB_FILE = r'C:\Program Files\Wizards of the Coast\MTGA\MTGA_Data\Downloads\Raw\Raw_CardDatabase_3fc09d06a61a10dcabcc28369ea62b2b.mtga'

    
# locsの準備
locs = {}

# SQL参照
con = sqlite3.connect(DB_FILE)
cur = con.cursor()
lang = getlocale()[0].split("_")[0]
iso_code = ISO_CODE.get(lang) if ISO_CODE.get(lang) else ISO_CODE['English']
records = cur.execute("select "+Row.LOC_ID+", "+iso_code.replace('_', '')+" from "+Table.LOCALIZATIONS+" where "+Row.FORMATTED+" = 0 ")
for record in records:
    locs[record[0]] = record[1]

with open("Raw_Localizations.json", "w", encoding='utf-8-sig') as f:
    json.dump(locs, f, indent=4, ensure_ascii=False)


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
