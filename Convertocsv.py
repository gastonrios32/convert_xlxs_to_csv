import pandas as pd
import os
import pathlib
import openpyxl

filePath = str(pathlib.Path(__file__).parent.absolute()) + '\\'

#test ubicacion 
#print(" path is ", filePath)

delimiter = input('Seleccione un delimitador : ')

content = os.listdir(filePath)
for file in content:
    if os.path.isfile(os.path.join(filePath, file)) and file.endswith('.xlsx'):
        rutfile= os.path.join(filePath, file)
        #identificamos el nombre que lleva la hoja 1
        wb = openpyxl.load_workbook(str(rutfile))
        sheet = wb.get_sheet_names()        
        file_xlsx = file
        file_csv = file.replace('.xlsx','.csv')
        Rut=pathlib.Path(__file__).parent.absolute()
        #Se generan las rutas de entrada y de salida 
        rutfile= os.path.join(Rut, file_xlsx)
        rutfile2= os.path.join(Rut, file_csv)
        #los archivos .csv solo permiten una hoja 
        data_xls = pd.read_excel(rutfile, sheet[0] , index_col=None)
        data_xls.to_csv(rutfile2, encoding='utf-8', index=False, sep=delimiter)

