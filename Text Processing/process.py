import json

inQuote = False
inQuoteLine = False

quotes = []
tempstring = ""
tempquote = ""

idx = 0


with open('bushismRedux.txt') as f:
    data = f.read()

for c in data:
    if((c == '"') and (not inQuote)):
        inQuote = True
        inQuoteLine = True

        idx += 1
        continue

    elif((c == '"') and (inQuote)):
        inQuote = False

        idx += 1
        continue

    elif(inQuote):
        if(c != '\n'):
            tempquote += c

        idx += 1
        continue

    elif(inQuoteLine and (c == '\n')):
        #print(tempquote + " : " + tempstring)
        if(tempquote not in quotes):
        	quotes.append(tempquote)# = tempstring
        inQuoteLine = False
        tempstring = ""
        tempquote = ""

        idx += 1
        continue

    elif(inQuoteLine):
        tempstring += c

        idx += 1
        continue
if(tempquote not in quotes):
    quotes.append(tempquote)# = tempstring


#print(quotes)
for q in quotes:
    print('"'+q+'"')


with open('bushtextprocessed.txt', 'w') as f:
    for q in quotes:
    	print('"'+q+'"')
    	f.write('"'+q+'"\n')
    
    

#print(quotes)