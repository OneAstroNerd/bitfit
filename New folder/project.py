

weight=float(input( "enter your weight(kg)"))
hight=float(input( "enter your hight(cm)"))
gender=str(input(  "enter your gender(male or female)"))
age=int(input( "enter your age"))

y = hight**2
x=float(weight/y)
bmim=(1.20*x)+(0.23*age)-16.02 
bmiw=((1.20*x)+(0.23*age)-16.02)-5.4



if gender == 'male':
    print("your fat percentage = ",bmim)
if gender == 'female':  
    print("your fat percentage = ",bmiw)
#variable1   
exercise=input( "do you exercsise?(yes or no)")

bmr_men=( 655.1+(9.6 * weight)+(1.8*hight)-(4.7*age))
bmr_women=(66.5+(13.75*weight)+(5*hight)-(6.755*age))

gymnastics=4.5
aerobics=11
aerobic_outdoors=11
hiking=10.5
rockclimbing=19.3
walking=7
running=15.8
skating=12.3
soccer=15
volleyball=5.2
basketball=14
pingpong=4.3
tennis=12.3
karate=14
tekwando=15.6
kungfo=14.1
boxing=15.8


if exercise == "yes":

    sports=input( 'enter your sport field')   
    t=input( 'enter your exercise time')
    if sports=="gymnastics":
        if gender=="male":
            kcal=(gymnastics*t)+(bmr_men)
        if gender=="female":
            kcal= (gymnastics*t)+(bmr_women)   
    if sports=="aerobics":
        if gender=="male":
            kcal=(aerobics*t)+(bmr_men)
        if gender=="female":
            kcal= (aerobics*t)+(bmr_women)  
    if sports=="aerobic_oudoors":
        if gender=="male":
            kcal=(aerobic_outdoors*t)+(bmr_men)
        if gender=="female":
            kcal= (aerobic_outdoors*t)+(bmr_women) 
    if sports=="hiking":
        if gender=="male":
            kcal=(hiking*t)+(bmr_men)
        if gender=="female":
            kcal= (hiking*t)+(bmr_women) 
    if sports=="rockclimbing":
        if gender=="male":
            kcal=(rockclimbing*t)+(bmr_men)
        if gender=="female":
            kcal= (rockclimbing*t)+(bmr_women) 
    if sports=="walking":
        if gender=="male":
            kcal=(walking*t)+(bmr_men)
        if gender=="female":
            kcal= (walking*t)+(bmr_women) 
    if sports=="running":
        if gender=="male":
            kcal=(running*t)+(bmr_men)
        if gender=="female":
            kcal= (running*t)+(bmr_women) 
    if sports=="skating":
        if gender=="male":
            kcal=(skating*t)+(bmr_men)
        if gender=="female":
            kcal= (skating*t)+(bmr_women) 
    if sports=="soccer":
        if gender=="male":
            kcal=(soccer*t)+(bmr_men)
        if gender=="female":
            kcal= (soccer*t)+(bmr_women) 
    if sports=="volleyball":
        if gender=="male":
            kcal=(volleyball*t)+(bmr_men)
        if gender=="female":
            kcal= (volleyball*t)+(bmr_women) 
    if sports=="basketball":
        if gender=="male":
            kcal=(basketball*t)+(bmr_men)
        if gender=="female":
            kcal= (basketball*t)+(bmr_women) 
    if sports=="pingpong":
        if gender=="male":
            kcal=(pingpong*t)+(bmr_men)
        if gender=="female":
            kcal= (pingpong*t)+(bmr_women) 
    if sports=="tennis":
        if gender=="male":
            kcal=(tennis*t)+(bmr_men)
        if gender=="female":
            kcal= (tennis*t)+(bmr_women) 
    if sports=="karate":
        if gender=="male":
            kcal=(karate*t)+(bmr_men)
        if gender=="female":
            kcal= (karate*t)+(bmr_women) 
    if sports=="tekwando":
        if gender=="male":
            kcal=(tekwando*t)+(bmr_men)
        if gender=="female":
            kcal= (tekwando*t)+(bmr_women) 
    if sports=="kungfo":
        if gender=="male":
            kcal=(kungfo*t)+(bmr_men)
        if gender=="female":
            kcal= (kungfo*t)+(bmr_women) 
    if sports=="boxing":
        if gender=="male":
            kcal=(boxing*t)+(bmr_men)
        if gender=="female":
            kcal= (boxing*t)+(bmr_women)
    print("calories burned(normal activity + exercise) = ",kcal)
    if t>=20 and t<=30 :
        print("Need for carbohydrates(gr) = ",weight*4)

    if t>=31 and t<=60 :
        print("Need for carbohydrates(gr) = ",weight*6)
    if t>=61 and t<=180 :
        print("Need for carbohydrates(gr) = ",weight*8)
    if t>180 :
        print("Need for carbohydrates(gr) = ",weight*10)
    if t >=44 and t<=20 :
        print("need for protein = ",weight*0.7)
    if t >= 45 and t <= 60: 
        print("need for protein = ",weight*1.1)
    if t >= 61  :
        print("need for protein = ",weight*1.7)



    
if exercise == "no":
    if gender=='male':
        print("calories burned = ",bmim)
    if gender=="female":
        print("calories burned = ",bmiw)

    print("need for protein = ",weight*0.8)



