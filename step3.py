def operation(operator,num1,num2):
  output=0
  if operator== "+":
    output = num1+num2
  if operator== "-":
    output = num1-num2
  if operator== "x":
    output = num1*num2
  if operator== "/":
    output = num1/num2
  return output

trackerarray=[]
def gotoline(linearray,linenum):
  if "calc" in linearray[linenum]:
    firstline=linearray[linenum].split(" ")
    nextline = operation(firstline[2],int(firstline[3]),int(firstline[4]))
    trackerarray.append(linearray[nextline])
    gotoline(linearray,nextline)
  else:
    trackerarray.append(linearray[nextline])
    gotoline(linearray,nextline)

file_object = open('step3.txt', 'r')
contents = file_object.read()
nextline=0
individuallines=contents.splitlines()
if "calc" in individuallines[0]:
    firstline=individuallines[0].split(" ")
    nextline = operation(firstline[2],int(firstline[3]),int(firstline[4]))
    trackerarray.append(individuallines[nextline])
    gotoline(individuallines,nextline)
else:
    gotoline(individuallines,nextline)
    



  
