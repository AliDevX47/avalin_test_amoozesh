a=int (1405)

f_name=input("Eter yuor name : ")

print("-------------------------------------------------------------------")

lname=str(input("Enter yuor family : "))

print("-------------------------------------------------------------------")

print("mikhay bedooni tooye che nasli hasti ?")

year_of_birth=int(input('pas lotfan sal tavallodet ro benevis : '))

print("-------------------------------------------------------------------")

if  year_of_birth<=1419 and year_of_birth>=1280:

    print(f"This is yuor Age: ",(a-year_of_birth))

print("-------------------------------------------------------------------")
sen=year_of_birth

if 1280<=sen and 1307>=sen :
    print('shoma gozve (bozorg tarin nasl ha) hastid' )

elif 1308<=sen and 1324>sen :
    print('shoma gozve (nasl khamoosh) hastid' )

elif 1325<=sen and 1343>=sen:
    print('shoma gozve nasl (B) hastid' )

elif 1344<=sen and 1359>=sen:
    print('shoma gozve nasl (X) hastid' )

elif 1360<=sen and 1375>=sen:
    print('shoma gozve nasl (Y) hastid' )

elif sen>=1375 and sen<=1391:
    print('shoma gozve nasl (Z) hastid' )

elif 1392<=sen and 1403>=sen:
    print('shoma gozve nasl (ALFA) hastid' )

elif 1404<=sen and 1419>=sen:
    print('shoma gozve nasl (BETA) hastid' )

else : 
    print('shoma hanooz be donya nayoomadid' )
print("-------------------------------------------------------------------")

