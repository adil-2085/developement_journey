path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\job posting\\job_posting2.csv'

fr = open(path)

job_posting=[]

for line in fr:

    data=line.strip('\n').split(',')
# ['200', 'TCS', 'Data Analyst', 'Kochi', 'Contract', '1271521', '2025-08-19']
    if len(data)>1 :

        dictionary = {'JobID':data[0],
                      'company_name':data[1],
                      'job_title':data[2],
                      'location':data[3],
                      'job_title':data[4],
                      'salary':data[5],
                      'posted_date':data[6]
                      
                      }

        job_posting.append(dictionary)
    
job_posting.pop(0)
print(job_posting[0])