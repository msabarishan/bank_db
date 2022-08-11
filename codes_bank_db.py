import pandas as pd

//to import the excel file with data in different sheets named with table name.
xls=pd.ExcelFile(r"F:\2.SQL\bank data.xlsx") 

//to create dataframe using the sheets in excel.
customer=pd.read_excel(xls,'customer',index_col=None)
cus_branch=pd.read_excel(xls,'cus_branch',index_col=None)
cus_branch=cus_branch.astype(int)
bank_branch=pd.read_excel(xls,'bank_branch',index_col=None)
bank_employee=pd.read_excel(xls,'bank_employee',index_col=None)
bank_workswith=pd.read_excel(xls,'bank_workswith',index_col=None)
loan=pd.read_excel(xls,'loan',index_col=None)
deposit=pd.read_excel(xls,'deposit',index_col=None)

// Opening and reading Sql BD. Password is removed for privacy.
import psycopg2
import psycopg2.extras
hostname = 'ec2-34-207-12-160.compute-1.amazonaws.com'
database = 'd5fmmj82e013ta'
username = 'gpwvcgfprcaaji'
pwd = 'ENTER PASSWORD HERE'
port_id = 5432
conn = None

with psycopg2.connect(
                     host = hostname,
                     dbname = database,
                     user = username,
                     password = pwd,
                     port = port_id) as conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                        // UPDATE POSTGRES SQL USING WITH THE DATA FROM EXCEL FILE
                            
                        bank_employee_values = bank_employee.values.tolist()
                        insert_script= 'insert into bank_employee (emp_id,emp_name,emp_address) values ( %s, %s, %s)'
                        for record in bank_employee_values:
                                  cur.execute(insert_script, record)
                       
                        bank_workswith_values = bank_workswith.values.tolist()
                        insert_script= 'insert into bank_workswith (emp_id,manager_id) values ( %s, %s)'
                        for record in bank_workswith_values:
                                  cur.execute(insert_script, record)
                                
                        loan_values = loan.values.tolist()
                        insert_script= 'insert into loan (loan_id,loan_amount,cus_id,branch_id) values ( %s, %s,%s,%s)'
                        for record in loan_values:
                                  cur.execute(insert_script, record)
                            
                        deposit_values = deposit.values.tolist()
                        insert_script= 'insert into deposit (deposit_id,deposit_amount,cus_id,branch_id) values ( %s, %s,%s,%s)'
                        for record in deposit_values:
                                  cur.execute(insert_script, record)

