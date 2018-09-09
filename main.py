# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
fileExcel = 'tutorial_python_1.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(fileExcel)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
sheetBuah = xl.parse('Buah')

# Print data in the sheet
print(sheetBuah)