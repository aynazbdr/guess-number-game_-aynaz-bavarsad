import random
# فراخوانی کتابخانه رندوم
while True:
    number =random.randint(1,100)
    count=0
    win= False
    while count<5:
         try:
             guess=int(input("guess a number between 1_100: "))
         except ValueError:
            print("Eror! enter only integer")
            continue       
         if guess<1 or guess>100:
            print("number must be between 1 and 100")
            continue
        # try برای این استفاده می شود که بتوانیم خطا را مدیریت کنیم و برنامه بخاطر خطا متوقف نشود.except زمانی که خطا رخ دهد دستورات این بخش اجرا می شه.
        # continue باعث میشودحلقه از اول اجرا شود و برنامه دوباره از کاربر ورودی بگیره.
         count+=1
        #  هر بار که کاربر یک ورودی وارد کند یکی به این رقم اضافه می شود
         difference=abs(number - guess)
# تابع abs:قدر مطلق یک عدد را برمیگرداند . قدر مطلق اختلاف عدد کاربر و عدد سیستم را وارد میکند.
         print("number of attemots:" , count)
         print("remaining attempts: " , 5-count)
         if guess==0 :
           print("game is over")
           break

         elif guess==number:
           print("you win")
           win=True
           break

         elif guess< number:
           print("choose a bigger number")

         else:
           print("choose a smaller number")  

         if difference <=5:
           print("you are so close")

         elif difference <=15:
           print("you are close but you still far")

         else:
           print("you are so far")       

    if win:
         if count==1:
          print("score: so good")
         elif count==2:
          print("score: good")
         elif count==3:
          print("score:fine")  
         elif count==4:
          print("score: not bad") 
         elif count==5:
          print("score:lucky")
    else:
        print("unfortunately,you lost")
        print("the correct number was this" , number)   
    again=input("do you want to play again? (yes/no)")
    if again !="yes":
      print("thank you, goodbye!")
      break
