weather = {}
with open ('weather.txt') as f:
    lines = f.readlines ()
    for line in lines:
        splitted = line.strip ().split (';')
        date, temp = splitted
        if temp in weather:
            weather[temp].append (date)
        else:
            weather[temp] = [date] 
print (weather)
temps = []
for i in temp:
    temps.append(int(i)) 
min_temp = 0
min_date = ''
for temp, date in weather.items():
    if int(temp) < int(min_temp):
        min_temp = temp
        min_date = date
print ('Минимальные значения: ', min_temp, min_date)
max_temp = 0
max_date = ''
for temp, date in weather.items():
    if int(temp) > int(max_temp):
        max_temp = temp
        max_date = date
print ('Максимальные значения: ', max_temp, max_date)
