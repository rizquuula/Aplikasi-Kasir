import sys
Stuff = []
Price = []
Number= []
loop = True
count = 0
def DataInput(S,P,N):
    if S.isalpha() and P.isdigit() and N.isdigit():
        Stuff.append(S)
        Price.append(P)
        Number.append(N)
    else:
        print('| Wrong input dude..(2)')

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

print ('|---------------------INPUT DATA---------------------|')
print ('|FORMAT : NAME OF STUFF (SPACE) PRICE (SPACE) NUMBERS|')

while loop:
    print('| > ',end='')
    isData = input()
    if isData=='' or isData==' ':
        break
    else:
        isData = isData.split(' ')
        DataInput(isData[0],isData[1],isData[2])
        count+=1
        #continue
        
for i in range(count):
    print('|',i,'. ',Stuff[i],end='     ')
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (7, i, Price[i]))
    #sys.stdout.flush()
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (11, i, Number[i]))
    sys.stdout.flush()
    print 
    #print(Price[i],end='     ')
    #print(Number[i])