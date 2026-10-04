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

else :
    print("shoma vojood nadarid")

print("-------------------------------------------------------------------")
sen=year_of_birth

if 1280<=sen and 1307>=sen :
    print('shoma gozve (bozorg tarin nasl ha) hastid' )
    print("""nesel shma dar doran rakood bozorg, bozorg shodehand va dar jang jacpehani dovom niz jangidehand, sakhti hai egtesadi 
    va ejtemaei shadidi ra posht sar gozashtehand va dar natijeh an ha ra «bozorg» namidehand.""")

elif 1308<=sen and 1324>sen :
    print('shoma gozve (nasl khamoosh) hastid' )
    print("""in nasl dar zaman mak kartism va tars sorkh , zaher shod , keh aghlab monjar be fazaye siasi mishod keh dar an, sokoot 
    amntar az bian ashkar aghayed khod boud. benabarin, in nesel onvan «nesel khamush» ra beh khod ekhtesas dad.""")

    
elif 1325<=sen and 1343>=sen:
    print('shoma gozve nasl (enfejar jameiat) hastid' )
    print("""in nesel bah delil afzayesh ghabel tojoh nerkh zad o valad ya «bibi bomer» keh pas az jang jahani dovom 
    rokh dad, in nam ra beh khod ekhtesas dad. hamchenin in nasl be nam digar boomer niz shenakhteh mishavad!""")


elif 1344<=sen and 1359>=sen:
    print('shoma gozve nasl (X) hastid' )
    print("""(X) neshan dahandeh ye yek chiz nashenakhteh ast , shabih be karbord an dar riaziat , ke be potansiel in nasl 
    eshareh darad . tamayol be majhool boodan ra az vijhegi hay in nasl bayan kardehand .""")


elif 1360<=sen and 1375>=sen:
    print('shoma gozve nasl (Y) hastid' )
    print("""NAMGOZARIE NASL (Y) BE IN DALIL AST KEH BAAB AZ NASL (X) AMADEH VA RAVAND HOROOFE ALEFBA RA EDAMEH MIDAHAD , 
    BE AN HA NASL (HEZARE) HAM MIGOOYAND ZIRA DAR AVAKHER GHARN 21 OM BE BOLOOGH RESIDEHAND""")


elif sen>=1375 and sen<=1391:
    print('shoma gozve nasl (Z) hastid' )
    print("""in nasl bah in delil zad namideh shod keh daghighan bad az nesel vaye amodeh est ve rond horof elfba ra edameh
      midehad. AN HA DAR ASR FANNAVARIDIJITAL FARAGIR , BE VIJHE INTERNET VA SHABAKE HAY EJTEMAEI AST .""")


elif 1392<=sen and 1403>=sen:
    print('shoma gozve nasl (ALFA) hastid' )
    print("""in nasl beh lahaz teknologic, egtesadi va siasi, dar sath bartari gharar darand.""")


elif 1404<=sen and 1419>=sen:
    print('shoma gozve nasl (BETA) hastid' )
    print("""in nesel dar dorani roshd khahad kard keh fanavarihay pishraftehyi manand Hoosh masnoei, 
    internet a shia va vagheiat afzudeh va majazi betor kamel dar zendegi ruzmareh nahadineh shodehand.
    nesel beta hamchenin dar dOniayi motevaled mishavad keh takid bishtari bar payedari mohitzist, 
    taghirat abohavayi va hoosh jamei vojood darad.""")


else : 
    print('shoma hanooz be donya nayoomadid' )
print("-------------------------------------------------------------------")

