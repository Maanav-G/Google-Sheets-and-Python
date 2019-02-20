import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint 

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('database_key.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Database').sheet1

pp = pprint.PrettyPrinter()

# Use for all records
database = sheet.get_all_records()

# Use to get a row, col or cell
# database = sheet.row_values(6)
# database = sheet.col_values(6)
# database = sheet.cell(6,2).value

# pp.pprint(database)

# Use to update a specific cell
# sheet.update_cell(6,2, 'Maanav')
# database = sheet.cell(6,2).value

# pp.pprint(database)

# Use to add row
# row = ["I'm", "updating", "this", "spreadsheet", "from", "python"]
# index = 2
# sheet.insert_row(row,index)

# Used to delete specfic row
# sheet.delete_row(2)

print(sheet.row_count)