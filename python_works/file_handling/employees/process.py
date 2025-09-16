

path = 'C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\employees\\employees.csv'

fr = open(path)
# pep dtandard
all_employees = []

for line in fr:

    data = line.rstrip('\n').split(',')

    dictionary = {'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}

    all_employees.append(dictionary)



all_employees={'id':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[0],'name':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[1],'department':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[2],'salary':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[3],'email':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[4],'location':{'id':data[0],'name':data[1],'department':data[2],'salary':data[3],'email':data[4],'location':data[5]}[5]}


ekm_employees= [e.get('name') for e in all_employees if e.get('location')=='ekm']

print(ekm_employees)

max_salary_employe= max(all_employees,key=lambda e:e.get('salary')).get('name')

print(max_salary_employe)

min_salary = min(all_employees,key=lambda e:e.get('salary')).get('salary')

min_salary_employees = [e.get('name') for e in all_employees if e.get('salary') == min_salary]

print(min_salary_employees)

