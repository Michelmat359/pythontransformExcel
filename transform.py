import csv
import pandas as pd



class Transformdata():

    # constructor
    def __init__(self):
        # Initialization
        self.num_tool = 8
        self.start_data = 21
        self.finish_data = 78
        self.namefile = "CalidadViejo.csv"
        self.exitnamefile = "sol1.csv"

    def read(self):
        with open(self.namefile) as file_name:

            file_read = csv.reader(file_name)
            row_count = 0
            final_list = []
            for row in file_read:
                row_count = row_count + 1
                if (row_count == 2):
                    first_data = row[0].split(";")
                    array_id = []
                    array_id.append(float(first_data[1]))  # Reference
                    for i in range(5, ((self.num_tool) * 6) + 5):
                        if (first_data[i] != ""):
                            array_id.append(float(first_data[i]))

                if (row_count == 3):
                    first_data = row[0].split(";")
                    array_valuets = []
                    array_valuets.append(first_data[0])  # Ts
                    for i in range(5, ((self.num_tool) * 6) + 5):
                        if (first_data[i] != ""):
                            array_valuets.append(float(first_data[i]))

                if (row_count == 4):
                    first_data = row[0].split(";")
                    array_valuetn = []
                    array_valuetn.append(first_data[0])  # TN
                    for i in range(5, ((self.num_tool) * 6) + 5):
                        if (first_data[i] != ""):
                            array_valuetn.append(float(first_data[i]))

                if (row_count == 5):
                    first_data = row[0].split(";")
                    array_valueti = []
                    array_valueti.append(first_data[0])  # TN
                    for i in range(5, ((self.num_tool) * 6) + 5):
                        if (first_data[i] != ""):
                            array_valueti.append(float(first_data[i]))
                    print(array_valueti)
                if (row_count >= self.start_data and row_count <= self.finish_data):
                    line = []
                    data_rowdata = row[0].split(";")
                    line.append(data_rowdata[0])
                    line.append(data_rowdata[1])
                    line.append(data_rowdata[2])
                    aux = 0
                    for i in range(5, ((self.num_tool - 1) * 6) + 5):
                        if (data_rowdata[i] != ""):
                            aux = aux +1
                            line.append(float(data_rowdata[i]))
                            if(float(data_rowdata[i]) - float(array_valuetn[aux])== 0):
                                line.append(3)
                            elif (float(data_rowdata[i]) - float(array_valuetn[aux])< 0 and float(data_rowdata[i]) >= float(array_valueti[aux])):
                                line.append(2)
                            elif (float(data_rowdata[i]) - float(array_valuetn[aux]) > 0 and float(data_rowdata[i]) <= float(array_valuets[aux])):
                                line.append(1)
                            else:
                                line.append(0)
                            line.append(round(float(data_rowdata[i]) - float(array_valuetn[aux]),3))
                    final_list.append(line)


            final_array_head = []
            arraY_vacio = []
            x = 0
            while x < len(array_valueti):
                if (x == 0):
                    final_array_head.append(array_id[x])
                else:
                    final_array_head.append(array_id[x])
                    final_array_head.append(array_valuets[x])
                    final_array_head.append(array_valuetn[x])
                    final_array_head.append(array_valueti[x])
                x += 1

            final_list.insert(0, final_array_head)
            final_list.insert(1, arraY_vacio)
            data = pd.DataFrame(final_list)
            data.to_csv(self.exitnamefile, sep='\t', index=False)
            print(data)
            # self.write(data)


    # def write(self, list_of_elem):
    #     print(self.exitnamefile)
    #     print(list_of_elem)
    #     with open(self.exitnamefile, 'a+', newline='') as write_obj:
    #         csv_writer = csv.writer(write_obj)
    #         aux = 0
    #         for row in list_of_elem:
    #             csv_writer.writerows(row)
    #
    #             # csv_writer.writerows(([list_of_elem[index]] for index in range(0, len(list_of_elem))))


Object = Transformdata()
Object.read()

