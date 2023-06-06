# from apps import db
import pandas as pd

def upload():
    df = pd.read_excel('data.xlsx', sheet_name=None)
    # print(df)
    for key, value in df.items():
        print(key)
        if key == "projection":
            # print(value)
            columns = list(value.columns)
            print(columns)
            


if __name__ == "__main__":
    # from apps.config import config_dict
    # from apps import create_app, db
    # app_config = config_dict[get_config_mode.capitalize()]
    # app = create_app(app_config)
    upload()