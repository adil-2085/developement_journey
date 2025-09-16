

path='C:\\Users\\adilp\\OneDrive\\Desktop\\developement journey\\python_works\\file_handling\\food logs\\food.csv'

fr = open(path)

food_logs=[]

for line in fr:

    data=line.strip('\n').split(',')
    # 2025-08-23,Breakfast,Upma,1 plate,300

    if len(data)>1:

        dictionary = {'date':data[0],
                      'meal_type':data[1],
                      'name':data[2],
                      'serve_size':data[3],
                      'calories':data[4]}

        food_logs.append(dictionary)
    

print(food_logs)


# daily_summary={line.get('date'): if line.get('date') in a  else line.get('date'):line.get('calories') for line in food_logs }


daily_summary=[]

for line in food_logs:

    if line.get('date') in daily_summary:

        daily_summary[line.get('date')] += int(line.get('calories'))


    else:

        daily_summary[line.get('date')] = int(line.get('calories'))


print(daily_summary)