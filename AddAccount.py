import csv  

def AddAccount(file_name, user_name, password):
    fields=[user_name,password]
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields) 