import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('database_key.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Database').sheet1

database = sheet.get_all_records()
print(database)