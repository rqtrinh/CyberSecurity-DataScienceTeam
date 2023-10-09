from DataExtraction.ConvertJSON.convertToCSV import convert_json_csv
from DataExtraction.GenerateGraphs.extract_data import extract_data
import os
import webbrowser

current_directory = os.getcwd()
html_path ='Webpage/index.html'

convert_json_csv()
extract_data()
html_file_path = "file:///" + os.getcwd() + '/Webpage/index.html'

webbrowser.open(html_file_path)