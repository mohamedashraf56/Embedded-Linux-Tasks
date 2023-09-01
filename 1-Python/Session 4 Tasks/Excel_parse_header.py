import re
import openpyxl

function_list=[]
# read the header file 
with open("/home/mohamedashraf/LCD.h",'r') as f:
    lines_list=f.readlines()
    pattern = r'^\s*\w+\s+\w+\([^)]*\)\s*;'  
   
    for item in lines_list:
      
      if re.match(pattern,item):      
         function_list.append(item)  
      else:
         pass   

# clean each function line from the spaces and the \n using strip
cfunction_list = [string.strip() for string in function_list] 

# open the new workbook
workbook=openpyxl.Workbook()

sheet=workbook.active
# make the width of the column bigger
sheet.column_dimensions['A'].width = 40
sheet.column_dimensions['B'].width = 80

for i,item in enumerate(function_list,1):
   sheet['B'+str(i)]=item                        
   sheet['A'+str(i)]='IDX'+str(i).zfill(3)      
                                                 
     
workbook.save('/home/mohamedashraf/LCD.xlsx')
workbook.close() 
