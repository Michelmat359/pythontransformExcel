import csv
# import numpy as np
from csv import DictWriter

class Transformdata:

    def __init__(self, id:int, ts:float, tn:float, ti:float, time):
        self.id = id
        self.ts = ts
        self.tn = tn
        self.ti = ti
        self.time = time
    
    def read ():
        with open("CalidadViejo.csv") as file_name:
            
            file_read = csv.reader(file_name)
            row_count = 0 
            for row in file_read:
                row_count = row_count + 1
                if(row_count == 2):          
                    first_data = row[0].split(";")
                    array_id = []
                    array_id.append(first_data[1]) # Reference
                    array_id.append(first_data[5]) # Id tool 1
                    array_id.append(first_data[11]) # Id tool 2
                    array_id.append(first_data[17]) # Id tool 3
                    array_id.append(first_data[23]) # Id tool 4
                    array_id.append(first_data[29]) # Id tool 5
                    array_id.append(first_data[35]) # Id tool 6
                    array_id.append(first_data[41]) # Id tool 7
                    array_id.append(first_data[47]) # Id tool 8    
                if(row_count == 3):
                    first_data = row[0].split(";")
                    array_valuets = []
                    array_valuets.append(first_data[0]) # Ts
                    array_valuets.append(first_data[5]) # Value Ts Id tool 1
                    array_valuets.append(first_data[11]) # Value Ts Id tool 2
                    array_valuets.append(first_data[17]) # Value Ts Id tool 3
                    array_valuets.append(first_data[23]) # Value Ts Id tool 4
                    array_valuets.append(first_data[29]) # Value Ts Id tool 5
                    array_valuets.append(first_data[35]) # Value Ts Id tool 6
                    array_valuets.append(first_data[41]) # Value Ts Id tool 7
                    array_valuets.append(first_data[47]) # Value Ts Id tool 8    
                if(row_count == 4):
                    first_data = row[0].split(";")
                    array_valuetn = []
                    array_valuetn.append(first_data[0]) # TN
                    array_valuetn.append(first_data[5]) # Value TN Id tool 1
                    array_valuetn.append(first_data[11]) # Value TN Id tool 2
                    array_valuetn.append(first_data[17]) # Value TN Id tool 3
                    array_valuetn.append(first_data[23]) # Value TN Id tool 4
                    array_valuetn.append(first_data[29]) # Value TN Id tool 5
                    array_valuetn.append(first_data[35]) # Value TN Id tool 6
                    array_valuetn.append(first_data[41]) # Value TN Id tool 7
                    array_valuetn.append(first_data[47]) # Value TN Id tool 8    
                if(row_count == 5):
                    first_data = row[0].split(";")
                    array_valueti = []
                    array_valueti.append(first_data[0]) # TN
                    array_valueti.append(first_data[5]) # Value TN Id tool 1
                    array_valueti.append(first_data[11]) # Value TN Id tool 2
                    array_valueti.append(first_data[17]) # Value TN Id tool 3
                    array_valueti.append(first_data[23]) # Value TN Id tool 4
                    array_valueti.append(first_data[29]) # Value TN Id tool 5
                    array_valueti.append(first_data[35]) # Value TN Id tool 6
                    array_valueti.append(first_data[41]) # Value TN Id tool 7
                    array_valueti.append(first_data[47]) # Value TN Id tool 8    
            final_array = []
            x = 0
            while x < len(array_valueti):
                if(x == 0):
                    final_array.append(array_id[x])
                else:
                    final_array.append(array_id[x])
                    final_array.append(array_valuets[x])
                    final_array.append(array_valuetn[x])
                    final_array.append(array_valueti[x])
                x+=1
            print(final_array)
            return final_array



    def append_list_as_row(file_name, list_of_elem):
        with open(file_name, 'a+', newline=',') as write_obj:
            csv_writer = csv.writer(write_obj)
            csv_writer.writerow(list_of_elem)


    first_line = read()
    append_list_as_row('sol.csv', first_line)






