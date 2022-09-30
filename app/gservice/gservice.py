
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import json
import base64
import os


def read_config_sheet(account_code: str, campaign: str):
    google_spreadsheet_url = os.getenv('GOOGLE_SPREADHEET_URL')
    credentials_key_file_dict = json.loads(base64.b64decode(os.getenv('GOOGLE_CREDENTIALS')))
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_key_file_dict, scope)
    gc = gspread.authorize(credentials)
    master_account_sheet = gc.open_by_url(google_spreadsheet_url)
    master_account_worksheet = master_account_sheet.get_worksheet(0)  # sheet index in spreadsheets
    master_account_data = master_account_worksheet.get_all_values()
    master_account_headers = master_account_data.pop(0)
    master_account_df = pd.DataFrame(master_account_data, columns=master_account_headers)
    token = master_account_df[master_account_df['Account'] == account_code].iloc[0]['Token']
    setting_file_url = master_account_df[master_account_df['Account'] == account_code].iloc[0]['Setting File']

    setting_file_sheet = gc.open_by_url(setting_file_url)
    setting_file_worksheet = setting_file_sheet.get_worksheet(0)  # sheet index in spreadsheets
    setting_file_data = setting_file_worksheet.get_all_values()
    setting_file_headers = setting_file_data.pop(0)
    setting_file_df = pd.DataFrame(setting_file_data, columns=setting_file_headers)
    selected_setting = setting_file_df[setting_file_df['Campaign'] == campaign].iloc[0]

    return token, selected_setting