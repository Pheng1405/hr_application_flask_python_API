import pyodbc as po

# server = '103.80.26.179'
server = 'localhost'

database = 'hrmdb'

username = 'sa'

password = 'Password123'

# Connection string

# conn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' +
#                   username + ';PWD=' + password + ';MARS_Connection=yes')

conn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=.;Database=hrmdb;Trusted_Connection=yes;')

myCursor = conn.cursor()
print(conn)

git_token = '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'