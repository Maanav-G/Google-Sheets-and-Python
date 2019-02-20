import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('database_key.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Database').sheet1