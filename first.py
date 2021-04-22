def solve(num,vacation):
      if vacation=="True":
          if num=='2' and num=='3' and num=='4' and num=='5'and num==6:
              print("7:00")
          elif num=='1' and num=='7':
              print("9:00")
          else:
              pass

      else:
          if num=='2' and num=='3' and num=='4' and num=='5'and num==6:
              print("5:00")
          elif num=='1' and num=='7':
              print("6:00")
          else:
              pass

n=int(input("enter the number of inputs:"))       
for i in (1,n+1):
    print(i)
    num,vacation=input().split()
    solve(num,vacation)     
