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


file_object = open('step2.txt', 'r')
contents = file_object.read()
finalresult=0
for line in contents.splitlines():
  linesplits=line.split(" ")
  finalresult+=operation(linesplits[1],int(linesplits[2]),int(linesplits[3]))
print(finalresult)#final output 756216.3057730488


