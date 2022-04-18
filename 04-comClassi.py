import pdfplumber


pdf = pdfplumber.open('comClassi.pdf')

pages = pdf.pages

#将所有数据解析储存在tables中
tables = []
for page in pages:
    table = page.extract_tables()
    tables.append(table)


#将tables中的数据清洗，按条储存在new_tables中
new_tables =[]
for table in tables:
    for i in table:
        for data in i:
            if data[-1] == '上市公司简称':
                continue 
            new_tables.append(data)

classi1 = []
for com in new_tables:
    if not com[0] == None:
        classi1.append(com[0])
print('Total classi1',len(classi1)) 
print(classi1)

    
