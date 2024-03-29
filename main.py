import scrapping_functions as scr
import dictionaries_fucntions as dic
import database_functions as dat

data_list = scr.scrap_data()
filtered_data_list = dic.filter_data(data_list)

for data in filtered_data_list:
    for key, value in data.items():
        print(f"{key}: {value}")
    print()

dat.save_to_mongodb(filtered_data_list)