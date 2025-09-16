all_path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\students\\all_students.txt'

failed_path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\students\\failed_students.txt'

pass_path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\students\\pass_students.txt'



all_students=open(all_path,'r')
failed_students=open(failed_path,'r')
pass_students=open(pass_path,'w')
all_set=set()
for name in all_students:
    all_set.add(name.rstrip("\n"))
fail_set=set()
for name in failed_students:
    fail_set.add(name.rstrip("\n"))

pass_list=set(all_set.difference(fail_set))


for n in pass_list:

    pass_students.write(n+'\n')




# all_students=open(all_path,'r')

# failed_students=open(failed_path,'r')

# pass_students=open(pass_path,'w')

# for s in all_students:

#         for ss in failed_students:

#                 # if ss.rstrip("\n")!=s.rstrip("\n"):
                        
#                 #         pass_students.write(s)

#             print(s)
