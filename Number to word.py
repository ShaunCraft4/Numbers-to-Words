number=input("Enter number: ")


#Adding 0s to make the length divisible by 3
if len(number)%3!=0:
    for i in range(1,4):
        if len("0"*i+number)%3==0:
            number="0"*i+number
            break
     
        
#Assigning variables        
worded_number=""
split_numbers=[]
counter=0
split_number=""
number_dictionary={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}                 
Term_dictionary={12:" Decillion ",11:" Nonillion ",10:" Octillion ",9:" Septillion ",8:" Sextillion ",7:" Quintillion ",6:" Quadrillion ",5:" Trillion ",4:" Billion ",3:" Million ",2:" Thousand ",1:""}


#Dividing the number into groups of 3 into a list
for i in number:
    counter+=1
    split_number+=i
    if counter==3:
        split_numbers.append(split_number)
        split_number=""
        counter=0
if len(split_number)!=0:
    split_numbers.append(split_number)



#The main working 
c=len(split_numbers)
for i in split_numbers:
    if split_numbers.count("000")==len(split_numbers):
        worded_number+="Zero"
    else:
        c1=0
        if int(i[-3])!=0:
            worded_number+=number_dictionary[int(i[-3])]+" Hundred"
            c1+=1
        if c1==1 and int(i[-2]+i[-1])!=0:
            worded_number+=" and "
            c1=0
        if int(i[-2]+i[-1])>10:
            if int(i[-2]+i[-1]) in number_dictionary:
                worded_number+=number_dictionary[int(i[-2]+i[-1])] #For ten numebrs like 10, 20, 30, etc
            elif int(i[-2])==2: #For Twenty numbers with a non zero ones digit
                worded_number+="Twenty "+number_dictionary[int(i[-1])]
            elif int(i[-2])==3: #For Thirty numbers with a non zero ones digit
                worded_number+="Thirty "+number_dictionary[int(i[-1])]
            elif int(i[-2])==5: #For Fifty numbers with a non zero ones digit
                worded_number+="Fifty "+number_dictionary[int(i[-1])]
            elif int(i[-2])==8: #For Eighty numbers with a non zero ones digit
                worded_number+="Eighty "+number_dictionary[int(i[-1])]
            else: #For other ten numbers with a non zero ones digit
                worded_number+=number_dictionary[int(i[-2])]+"ty "+number_dictionary[int(i[-1])]
        else:
            if int(i[-2]+i[-1])!=0: #For cases like 400
                worded_number+=number_dictionary[int(i[-2]+i[-1])]
        worded_number+=Term_dictionary[c]
        c-=1
            
print(worded_number)       