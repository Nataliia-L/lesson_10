f = open ('app.log.txt')
logs = []
for line in f:
    ip, date, time, *others = line.split(' ')
    dates = ''.join (date + ' '+ time)
    d = {'ip':ip, 'time':dates}
    logs.append(d)
print (logs) 
