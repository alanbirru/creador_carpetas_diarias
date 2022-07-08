
import locale
locale.setlocale(locale.LC_TIME, "es_MX") 


from dataclasses import replace
import os
from datetime import datetime
now = datetime.now()


year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%B")
print("month:", month)

day = now.strftime("%d")
print("day:", day)




def create_folder_year():
    try:
        dir_path = "C:/Users/alanb/Desktop/Impresiones"
        os.chdir(dir_path)
        os.mkdir(year)
    except:
        return None
# create_folder_year()



def create_folder_month():
    try:
        dir_path = f"C:/Users/alanb/Desktop/Impresiones/{year}"
        os.chdir(dir_path)
        os.mkdir(month)
     
    except:
        return None
# create_folder_month()



def create_folder_day():
    try:
        dir_path = f"C:/Users/alanb/Desktop/Impresiones/{year}/{month}"
        os.chdir(dir_path)
        os.mkdir(day)
    except:
        return None
# create_folder_day()


def scripts():
    create_folder_year()
    create_folder_month()
    create_folder_day()
scripts()
