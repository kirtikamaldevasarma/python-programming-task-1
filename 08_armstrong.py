num=int(input('Enter a number: '))
order=len(str(num));temp=num;total=0
while temp>0:
 d=temp%10
 total+=d**order
 temp//=10
print('Armstrong Number' if total==num else 'Not Armstrong Number')
