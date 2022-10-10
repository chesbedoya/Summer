import os
from behave.__main__ import main as behave_main

file_name = f'C:\\Users\\JorgeRamsesBedoyaSua\\Desktop\\gingols.feature'
#f = open(file_name, "w", encoding='utf-8')
#f = open('nuevo.txt','w')
#f = f.write(file_name)
behave_main([f"{file_name}"])
