print("1.Major/Natural Minor Scale")
print("2.Harmonic Minor Scale")
print("3.Melodic Minor Scale")
print("4.Blues/Jazz Scale")
print("5.Custom 5 Note Scale")
print("6.Custom 6 Note Scale")
print("7.Custom 7 Note Scale")
print("8.Custom 8 Note Scale")
print("9.Custom 9 Note Scale")
print("10.Custom 10 Note Scale")
print("#####################################")
a=int(input("Enter Any Number From Above Given Choices::"))
notes=['C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb','E',
       'F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb',
       'B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F',
       'F#/Gb','G','G#/Ab','A','A#/Bb','B']
notes1=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
keys=['Escape','F1','F2','F3','F4','F5','F6','F7','F8','`','1','2','3','4','5','6','7','8','9','0','-','=','BackSpace','Insert','Home','Prior',
      'q','w','e','r','t','y','u','i','o','p','[',']','\\','Delete','End','Next','a','s','d','f','g','h','j','k','l',';',"'",'Return','z','x','c','v','b','n']
keysforchords=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','','','','','','','','','','',''
               ,'','','','','','','','','','','','','','','','','','','','','','',
               '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
stafflines=['G','B','D','F','A','E','G','B','D','F']
staffspaces=['A','C','E','G','F','A','C','E']


dotpos=[625,625,610,610,595,580,580,560,560,547,
        547,533,519,519,501,501,488,473,473,459,
        459,443,443,427,405,405,388,388,371,356,
        356,341,341,326,326,311,298,298,281,281,
        269,255,255,245,245,235,235,225,215,215,
        206,206,195,187,187,177,177,168,168,158]
leftlines=[480,450,260]
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0
count10=0
count11=0
count12=0
count13=0
mainchordcounter=0
mainchordcounterscale2=0
mainchordcounterscale3=0
mainchordcounterscale4=0
mainchordcounterscale5=0
mainchordcounterscale6=0
mainchordcounterscale7=0
mainchordcounterscale8=0
mainchordcounterscale9=0
mainchordcounterscale10=0
mainchordcounterscale11=0
mainchordcounterscale12=0
u=[]
unewscale2=[]
unewscale3=[]
unewscale4=[]
unewscale5=[]
unewscale6=[]
unewscale7=[]
unewscale8=[]
unewscale9=[]
unewscale10=[]
unewscale11=[]
unewscale12=[]
if(a==1):
    u1=1
    u2=3
    u3=5
    u4=6
    u5=8
    u6=10
    u7=12
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
elif(a==2):
    u1=1
    u2=3
    u3=4
    u4=6
    u5=8
    u6=9
    u7=12
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
elif(a==3):
    u1=1
    u2=3
    u3=4
    u4=6
    u5=8
    u6=9
    u7=11
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
elif(a==4):
    u1=1
    u2=4
    u3=6
    u4=7
    u5=8
    u6=11
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
elif(a==5):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
elif(a==6):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u6=int(input("note 5"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
elif(a==7):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u6=int(input("note 6"))
    u7=int(input("note 7"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
elif(a==8):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u6=int(input("note 6"))
    u7=int(input("note 7"))
    u8=int(input("note 8"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
    u.append(u8)
    u.append(u8+12)
    u.append(u8+24)
    u.append(u8+36)
    u.append(u8+48)
elif(a==9):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u6=int(input("note 6"))
    u7=int(input("note 7"))
    u8=int(input("note 8"))
    u9=int(input("note 9"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
    u.append(u8)
    u.append(u8+12)
    u.append(u8+24)
    u.append(u8+36)
    u.append(u8+48)
    u.append(u9)
    u.append(u9+12)
    u.append(u9+24)
    u.append(u9+36)
    u.append(u9+48)
elif(a==10):
    u1=int(input("note 1"))
    u2=int(input("note 2"))
    u3=int(input("note 3"))
    u4=int(input("note 4"))
    u5=int(input("note 5"))
    u6=int(input("note 6"))
    u7=int(input("note 7"))
    u8=int(input("note 8"))
    u9=int(input("note 9"))
    u10=int(input("note 10"))
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
    u.append(u8)
    u.append(u8+12)
    u.append(u8+24)
    u.append(u8+36)
    u.append(u8+48)
    u.append(u9)
    u.append(u9+12)
    u.append(u9+24)
    u.append(u9+36)
    u.append(u9+48) 
    u.append(u10)
    u.append(u10+12)
    u.append(u10+24)
    u.append(u10+36)
    u.append(u10+48)
elif(a==11):
    u1=1
    u2=2
    u3=3
    u4=4
    u5=5
    u6=6
    u7=7
    u8=8
    u9=9
    u10=10
    u11=11
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
    u.append(u8)
    u.append(u8+12)
    u.append(u8+24)
    u.append(u8+36)
    u.append(u8+48)
    u.append(u9)
    u.append(u9+12)
    u.append(u9+24)
    u.append(u9+36)
    u.append(u9+48) 
    u.append(u10)
    u.append(u10+12)
    u.append(u10+24)
    u.append(u10+36)
    u.append(u10+48)
    u.append(u11)
    u.append(u11+12)
    u.append(u11+24)
    u.append(u11+36)
    u.append(u11+48)
elif(a==12):
    u.append(1)
    u.append(2)
    u.append(3)
    u.append(4)
    u.append(5)
    u.append(6)
    u.append(7)
    u.append(8)
    u.append(9)
    u.append(10)
    u.append(11)
    u.append(12)
    u.append(13)
    u.append(14)
    u.append(15)
    u.append(16)
    u.append(17)
    u.append(18)
    u.append(19)
    u.append(20)
    u.append(21)
    u.append(22)
    u.append(23)
    u.append(24)
    u.append(25)
    u.append(26)
    u.append(27)
    u.append(28)
    u.append(29)
    u.append(30)
    u.append(31)
    u.append(32)
    u.append(33)
    u.append(34)
    u.append(35)
    u.append(36)
    u.append(37)
    u.append(38)
    u.append(39)
    u.append(40)
    u.append(41)
    u.append(42)
    u.append(43)
    u.append(44)
    u.append(45)
    u.append(46)
    u.append(47)
    u.append(48)
    u.append(49)
    u.append(50)
    u.append(51)
    u.append(52)
    u.append(53)
    u.append(54)
    u.append(55)
    u.append(56)
    u.append(57)
    u.append(58)
    u.append(59)
    u.append(60)
elif(a==14):
    u1=1
    u2=2
    u3=6
    u4=8
    u5=11    
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
elif(a==15):
    u1=1
    u2=3
    u3=4
    u4=6
    u5=7
    u6=9
    u7=10
    u8=12 
    u.append(u1)
    u.append(u1+12)
    u.append(u1+24)
    u.append(u1+36)
    u.append(u1+48)
    u.append(u2)
    u.append(u2+12)
    u.append(u2+24)
    u.append(u2+36)
    u.append(u2+48)
    u.append(u3)
    u.append(u3+12)
    u.append(u3+24)
    u.append(u3+36)
    u.append(u3+48)
    u.append(u4)
    u.append(u4+12)
    u.append(u4+24)
    u.append(u4+36)
    u.append(u4+48)
    u.append(u5)
    u.append(u5+12)
    u.append(u5+24)
    u.append(u5+36)
    u.append(u5+48)
    u.append(u6)
    u.append(u6+12)
    u.append(u6+24)
    u.append(u6+36)
    u.append(u6+48)
    u.append(u7)
    u.append(u7+12)
    u.append(u7+24)
    u.append(u7+36)
    u.append(u7+48)
    u.append(u8)
    u.append(u8+12)
    u.append(u8+24)
    u.append(u8+36)
    u.append(u8+48)
for i in range(1,len(u)+1):
    if((u[i-1]+1)==61):
        unewscale2.append(1)
    else:
        unewscale2.append(u[i-1]+1)
for i in range(1,len(u)+1):
    if((u[i-1]+2)==61):
        unewscale3.append(1)
    elif((u[i-1]+2)==62):
        unewscale3.append(2)
    else:
        unewscale3.append(u[i-1]+2)
for i in range(1,len(u)+1):
    if((u[i-1]+3)==61):
        unewscale4.append(1)
    elif((u[i-1]+3)==62):
        unewscale4.append(2)
    elif((u[i-1]+3)==63):
        unewscale4.append(3)
    else:
        unewscale4.append(u[i-1]+3)
for i in range(1,len(u)+1):
    if((u[i-1]+4)==61):
        unewscale5.append(1)
    elif((u[i-1]+4)==62):
        unewscale5.append(2)
    elif((u[i-1]+4)==63):
        unewscale5.append(3)
    elif((u[i-1]+4)==64):
        unewscale5.append(4)
    else:
        unewscale5.append(u[i-1]+4)
for i in range(1,len(u)+1):
    if((u[i-1]+5)==61):
        unewscale6.append(1)
    elif((u[i-1]+5)==62):
        unewscale6.append(2)
    elif((u[i-1]+5)==63):
        unewscale6.append(3)
    elif((u[i-1]+5)==64):
        unewscale6.append(4)
    elif((u[i-1]+5)==65):
        unewscale6.append(5)
    else:
        unewscale6.append(u[i-1]+5)
for i in range(1,len(u)+1):
    if((u[i-1]+6)==61):
        unewscale7.append(1)
    elif((u[i-1]+6)==62):
        unewscale7.append(2)
    elif((u[i-1]+6)==63):
        unewscale7.append(3)
    elif((u[i-1]+6)==64):
        unewscale7.append(4)
    elif((u[i-1]+6)==65):
        unewscale7.append(5)
    elif((u[i-1]+6)==66):
        unewscale7.append(6)
    else:
        unewscale7.append(u[i-1]+6)
for i in range(1,len(u)+1):
    if((u[i-1]+7)==61):
        unewscale8.append(1)
    elif((u[i-1]+7)==62):
        unewscale8.append(2)
    elif((u[i-1]+7)==63):
        unewscale8.append(3)
    elif((u[i-1]+7)==64):
        unewscale8.append(4)
    elif((u[i-1]+7)==65):
        unewscale8.append(5)
    elif((u[i-1]+7)==66):
        unewscale8.append(6)
    elif((u[i-1]+7)==67):
        unewscale8.append(7)
    else:
        unewscale8.append(u[i-1]+7)
for i in range(1,len(u)+1):
    if((u[i-1]+8)==61):
        unewscale9.append(1)
    elif((u[i-1]+8)==62):
        unewscale9.append(2)
    elif((u[i-1]+8)==63):
        unewscale9.append(3)
    elif((u[i-1]+8)==64):
        unewscale9.append(4)
    elif((u[i-1]+8)==65):
        unewscale9.append(5)
    elif((u[i-1]+8)==66):
        unewscale9.append(6)
    elif((u[i-1]+8)==67):
        unewscale9.append(7)
    elif((u[i-1]+8)==68):
        unewscale9.append(8)
    else:
        unewscale9.append(u[i-1]+8)
for i in range(1,len(u)+1):
    if((u[i-1]+9)==61):
        unewscale10.append(1)
    elif((u[i-1]+9)==62):
        unewscale10.append(2)
    elif((u[i-1]+9)==63):
        unewscale10.append(3)
    elif((u[i-1]+9)==64):
        unewscale10.append(4)
    elif((u[i-1]+9)==65):
        unewscale10.append(5)
    elif((u[i-1]+9)==66):
        unewscale10.append(6)
    elif((u[i-1]+9)==67):
        unewscale10.append(7)
    elif((u[i-1]+9)==68):
        unewscale10.append(8)
    elif((u[i-1]+9)==69):
        unewscale10.append(9)
    else:
        unewscale10.append(u[i-1]+9)
for i in range(1,len(u)+1):
    if((u[i-1]+10)==61):
        unewscale11.append(1)
    elif((u[i-1]+10)==62):
        unewscale11.append(2)
    elif((u[i-1]+10)==63):
        unewscale11.append(3)
    elif((u[i-1]+10)==64):
        unewscale11.append(4)
    elif((u[i-1]+10)==65):
        unewscale11.append(5)
    elif((u[i-1]+10)==66):
        unewscale11.append(6)
    elif((u[i-1]+10)==67):
        unewscale11.append(7)
    elif((u[i-1]+10)==68):
        unewscale11.append(8)
    elif((u[i-1]+10)==69):
        unewscale11.append(9)
    elif((u[i-1]+10)==70):
        unewscale11.append(10)
    else:
        unewscale11.append(u[i-1]+10)
for i in range(1,len(u)+1):
    if((u[i-1]+11)==61):
        unewscale12.append(1)
    elif((u[i-1]+11)==62):
        unewscale12.append(2)
    elif((u[i-1]+11)==63):
        unewscale12.append(3)
    elif((u[i-1]+11)==64):
        unewscale12.append(4)
    elif((u[i-1]+11)==65):
        unewscale12.append(5)
    elif((u[i-1]+11)==66):
        unewscale12.append(6)
    elif((u[i-1]+11)==67):
        unewscale12.append(7)
    elif((u[i-1]+11)==68):
        unewscale12.append(8)
    elif((u[i-1]+11)==69):
        unewscale12.append(9)
    elif((u[i-1]+11)==70):
        unewscale12.append(10)
    elif((u[i-1]+11)==71):
        unewscale12.append(11)
    else:
        unewscale12.append(u[i-1]+11)
lu=len(u)//5

u.sort()
unewscale2.sort()
unewscale3.sort()
unewscale4.sort()
unewscale5.sort()
unewscale6.sort()
unewscale7.sort()
unewscale8.sort()
unewscale9.sort()
unewscale10.sort()
unewscale11.sort()
unewscale12.sort()

fname='op.py'
with open(fname,'w+') as f:
    f.write('from pygame import mixer\n')
    f.write('mixer.init()\n')
    f.write('mixer.set_num_channels(1000)\n')
    f.write('from tkinter import *\n')
    f.write('from PIL import Image, ImageTk\n')
    f.write('root=Tk()\n')
    f.write('root.title("Ultimate piano")\n')
    f.write('root.geometry("1360x700+0+0")\n')
    f.write('flagfornotemode=0\n')
    f.write('c=Canvas(root,bg="#b53b35")\n')
    f.write('c.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabel=Label(c,text="chord")\n')
    f.write('chordlabel.place(x=200,y=200)\n')
    f.write('chordlabel.config(font=("Courier", 44))\n')
    f.write('def thap(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('root.bind("<KeyPress-space>", thap) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('F=Canvas(c,bg="white")\n')
    f.write('F.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(F,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(F,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(F,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(F,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(F,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(F,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%d():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   root.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemode==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   root.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemode==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemode\n')
    f.write('   flagfornotemode=1\n')
    f.write('   flagfornotemodebtn.config(bg="green")\n')
    f.write('   flagfornotemodebtn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemode\n')
    f.write('   flagfornotemode=0\n')
    f.write('   flagfornotemodebtn2.config(bg="green")\n')
    f.write('   flagfornotemodebtn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodebtn=Button(c,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodebtn.place(x=10,y=220)\n')
    f.write('flagfornotemodebtn2=Button(c,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodebtn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(u[i-1]==2 or u[i-1]==4 or u[i-1]==7 or u[i-1]==9 or u[i-1]==11 or u[i-1]==14 or u[i-1]==16
           or u[i-1]==19 or u[i-1]==21 or u[i-1]==23 or u[i-1]==26 or u[i-1]==28 or u[i-1]==31 or u[i-1]==33
           or u[i-1]==35 or u[i-1]==38 or u[i-1]==40 or u[i-1]==43 or u[i-1]==45 or u[i-1]==47 or u[i-1]==50 or u[i-1]==52 or u[i-1]==55
           or u[i-1]==57 or u[i-1]==59):        
            f.write('def flashb%d(event):\n'%u[i-1])
            f.write('    b%d.config(bg = "green")\n'%u[i-1])     
            f.write('    root.after(175, lambda: b%d.config(bg = "black"))\n'%u[i-1])
            f.write('    d%d()\n'%u[i-1])
            if(keys[i-1]=='-'):
                f.write('root.bind("%s", flashb%d)\n'%(keys[i-1],u[i-1]))    
            else:
                f.write('root.bind("<KeyPress-%s>", flashb%d)\n'%(keys[i-1],u[i-1]))
        else:
            f.write('def flashb%d(event):\n'%u[i-1])
            f.write('    b%d.config(bg = "green")\n'%u[i-1])     
            f.write('    root.after(175, lambda: b%d.config(bg = "white"))\n'%u[i-1])
            f.write('    d%d()\n'%u[i-1])
            if(keys[i-1]=='-'):
                f.write('root.bind("%s", flashb%d)\n'%(keys[i-1],u[i-1]))    
            else:
                f.write('root.bind("<KeyPress-%s>", flashb%d)\n'%(keys[i-1],u[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%d=Button(c,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%d)\n'%(i,notes[i-1],i))
            f.write('b%d.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%d=Button(c,text="%s",bg="white",command=d%d)\n'%(i,notes[i-1],i))
            f.write('b%d.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(u[i-1]==2 or u[i-1]==4 or u[i-1]==7 or u[i-1]==9 or u[i-1]==11 or
 u[i-1]==14 or u[i-1]==16 or u[i-1]==19 or u[i-1]==21 or u[i-1]==23 or
 u[i-1]==26 or u[i-1]==28 or u[i-1]==31 or u[i-1]==33 or u[i-1]==35 or
 u[i-1]==38 or u[i-1]==40 or u[i-1]==43 or u[i-1]==45 or u[i-1]==47 or
 u[i-1]==50 or u[i-1]==52 or u[i-1]==55 or u[i-1]==57 or u[i-1]==59):
            f.write('l%d=Label(c,text="",bg="green")\n'%u[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(u[i-1],u[i-1]*22+5))
        else:
            f.write('l%d=Label(c,text="",bg="green")\n'%u[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(u[i-1],u[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%d%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%u[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%u[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%u[k])
                    f.write('   b%d.config(bg="green")\n'%(u[i]))
                    f.write('   b%d.config(bg="green")\n'%(u[j]))
                    f.write('   b%d.config(bg="green")\n'%(u[k]))                   
                    if(u[j]-u[i]==4 and u[k]-u[j]==3):
                        f.write('   chordlabel.config(text="%s")\n'%(notes1[u[i]-1]))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==4):
                        f.write('   chordlabel.config(text="%sm")\n'%(notes1[u[i]-1]))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==5):
                        f.write('   chordlabel.config(text="%s inv-1")\n'%(notes1[u[k]-1]))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==4):
                        f.write('   chordlabel.config(text="%s inv-2")\n'%(notes1[u[j]-1]))
                    elif(u[j]-u[i]==4 and u[k]-u[j]==5):
                        f.write('   chordlabel.config(text="%sm inv-1")\n'%(notes1[u[k]-1]))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==3):
                        f.write('   chordlabel.config(text="%sm inv-2")\n'%(notes1[u[j]-1]))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==3):
                        f.write('   chordlabel.config(text="%sdim")\n'%(notes1[u[i]-1]))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==6):
                        f.write('   chordlabel.config(text="%sdim inv1")\n'%(notes1[u[k]-1]))
                    elif(u[j]-u[i]==6 and u[k]-u[j]==3):
                        f.write('   chordlabel.config(text="%sdim inv2")\n'%(notes1[u[j]-1]))
                    elif(u[j]-u[i]==4 and u[k]-u[j]==4):
                        f.write('   chordlabel.config(text="%saug")\n'%(notes1[u[i]-1]))
                    elif(u[j]-u[i]==2 and u[k]-u[j]==5):
                        f.write('   chordlabel.config(text="%ssus2")\n'%(notes1[u[i]-1]))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==5):
                        f.write('   chordlabel.config(text="%ssus2 inv1")\n'%(notes1[u[k]-1]))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==2):
                        f.write('   chordlabel.config(text="%ssus4")\n'%(notes1[u[i]-1]))
                    if(u[i]==2 or u[i]==4 or u[i]==7 or u[i]==9 or u[i]==11
                       or u[i]==14 or u[i]==16 or u[i]==19 or u[i]==21 or u[i]==23 or u[i]==26 or u[i]==28 or u[i]==31 or u[i]==33
                       or u[i]==35 or u[i]==38 or u[i]==40 or u[i]==43 or u[i]==45 or u[i]==47 or u[i]==50 or u[i]==52 or u[i]==55
                       or u[i]==57 or u[i]==59):
                       f.write('   root.after(175, lambda: b%d.config(bg = "black"))\n'%u[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[u[i]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   root.after(175, lambda: b%d.config(bg = "white"))\n'%u[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[u[i]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%i)
                    if(u[j]==2 or u[j]==4 or u[j]==7 or u[j]==9 or u[j]==11 or u[j]==14 or u[j]==16 or u[j]==19 or u[j]==21 or
                       u[j]==23 or
                       u[j]==26 or u[j]==28 or u[j]==31 or u[j]==33 or u[j]==35 or
                       u[j]==38 or u[j]==40 or u[j]==43 or u[j]==45 or u[j]==47 or u[j]==50 or u[j]==52 or u[j]==55 or u[j]==57 or u[j]==59):
                       f.write('   root.after(175, lambda: b%d.config(bg = "black"))\n'%u[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[u[j]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   root.after(175, lambda: b%d.config(bg = "white"))\n'%u[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[u[j]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(u[k]==2 or u[k]==4
                       or u[k]==7 or u[k]==9 or u[k]==11 or u[k]==14 or u[k]==16 or u[k]==19 or u[k]==21 or u[k]==23 or u[k]==26 or u[k]==28
                       or u[k]==31 or u[k]==33 or u[k]==35 or u[k]==38 or u[k]==40 or u[k]==43 or u[k]==45 or
                       u[k]==47 or u[k]==50 or u[k]==52 or u[k]==55 or u[k]==57 or u[k]==59):
                       f.write('   root.after(175, lambda: b%d.config(bg = "black"))\n'%u[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[u[k]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   root.after(175, lambda: b%d.config(bg = "white"))\n'%u[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[u[k]-1]))
                       f.write('   root.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count2=count2+1
                    f.write('b%d%d%d=Button(c,text="%d%d%d",command=c%d%d%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count2<21):
                        f.write('b%d%d%d.place(x=%d,y=300)\n'%(i,j,k,count2*50-45))
                    elif(count2>20 and count2<41):
                        f.write('b%d%d%d.place(x=%d,y=340)\n'%(i,j,k,count2*50-1045))
                    elif(count2>40 and count2<61):
                        f.write('b%d%d%d.place(x=%d,y=380)\n'%(i,j,k,count2*50-2045))
                    elif(count2>60 and count2<81):
                        f.write('b%d%d%d.place(x=%d,y=420)\n'%(i,j,k,count2*50-3045))
                    elif(count2>80 and count2<101):
                        f.write('b%d%d%d.place(x=%d,y=460)\n'%(i,j,k,count2*50-4045))
                        
                    elif(count2>100 and count2<121):
                        f.write('b%d%d%d.place(x=%d,y=500)\n'%(i,j,k,count2*50-5045))
                        
                    elif(count2>120 and count2<141):
                        f.write('b%d%d%d.place(x=%d,y=540)\n'%(i,j,k,count2*50-6045))
                    elif(count2>140 and count2<161):
                        f.write('b%d%d%d.place(x=%d,y=580)\n'%(i,j,k,count2*50-7045))
                    elif(count2>160 and count2<181):
                        f.write('b%d%d%d.place(x=%d,y=620)\n'%(i,j,k,count2*50-8045))
                    elif(count2>180 and count2<201):
                        f.write('b%d%d%d.place(x=%d,y=660)\n'%(i,j,k,count2*50-9045))   
                    elif(count2>200 and count2<221):
                        f.write('b%d%d%d.place(x=%d,y=700)\n'%(i,j,k,count2*50-10045))
                        
                    if(u[j]-u[i]==4 and u[k]-u[j]==3):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%s")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==4):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%sm")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==5):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%sI1")\n'%(i,j,k,notes1[u[k]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==4):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%sI2")\n'%(i,j,k,notes1[u[j]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==4 and u[k]-u[j]==5):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%smI1")\n'%(i,j,k,notes1[u[k]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==3):
                        mainchordcounter=mainchordcounter+1
                        f.write('b%d%d%d.config(text="%smI2")\n'%(i,j,k,notes1[u[j]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==3 and u[k]-u[j]==3):
                        f.write('b%d%d%d.config(text="%sdim")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))

                    elif(u[j]-u[i]==3 and u[k]-u[j]==6):
                        f.write('b%d%d%d.config(text="%sdI1")\n'%(i,j,k,notes1[u[k]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==6 and u[k]-u[j]==3):
                        f.write('b%d%d%d.config(text="%sdI2")\n'%(i,j,k,notes1[u[j]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==4 and u[k]-u[j]==4):
                        f.write('b%d%d%d.config(text="%saug")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==2 and u[k]-u[j]==5):
                        f.write('b%d%d%d.config(text="%ssus2")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==5):
                        f.write('b%d%d%d.config(text="%ss2I1")\n'%(i,j,k,notes1[u[k]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
                    elif(u[j]-u[i]==5 and u[k]-u[j]==2):
                        f.write('b%d%d%d.config(text="%ssus4")\n'%(i,j,k,notes1[u[i]-1]))
                        f.write('b%d%d%d.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounter=mainchordcounter+1
                        f.write('def f%d%d%d(event):\n'%(i,j,k))
                        f.write('   c%d%d%d()\n'%(i,j,k))
                        f.write('   b%d%d%d.config(bg="green")\n'%(i,j,k))
                        f.write('   root.after(175, lambda: b%d%d%d.config(bg = "black"))\n'%(i,j,k))
                        f.write('root.bind("<KeyPress-%s>", f%d%d%d)\n'%(keysforchords[mainchordcounter-1],i,j,k))
        
########################################################################################################################
    f.write('rootscale2=Toplevel()\n')
    f.write('rootscale2.title("Ultimate piano-Scale 2")\n')
    f.write('rootscale2.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale2=0\n')
    f.write('cscale2=Canvas(rootscale2,bg="#b53b35")\n')
    f.write('cscale2.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale2=Label(cscale2,text="chord")\n')
    f.write('chordlabelscale2.place(x=200,y=200)\n')
    f.write('chordlabelscale2.config(font=("Courier", 44))\n')
    f.write('def thapscale2(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale2.bind("<KeyPress-space>", thapscale2) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale2,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale2,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale2=Canvas(cscale2,bg="white")\n')
    f.write('Fscale2.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale2,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale2,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale2,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale2,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale2,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale2,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale2scale2():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale2,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale2==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale2,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale2==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale2\n')
    f.write('   flagfornotemodescale2=1\n')
    f.write('   flagfornotemodescale2btn.config(bg="green")\n')
    f.write('   flagfornotemodescale2btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale2\n')
    f.write('   flagfornotemodescale2=0\n')
    f.write('   flagfornotemodescale2btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale2btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale2btn=Button(cscale2,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale2btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale2btn2=Button(cscale2,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale2btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale2[i-1]==2 or unewscale2[i-1]==4 or unewscale2[i-1]==7 or unewscale2[i-1]==9 or unewscale2[i-1]==11 or unewscale2[i-1]==14 or unewscale2[i-1]==16
           or unewscale2[i-1]==19 or unewscale2[i-1]==21 or unewscale2[i-1]==23 or unewscale2[i-1]==26 or unewscale2[i-1]==28 or unewscale2[i-1]==31 or unewscale2[i-1]==33
           or unewscale2[i-1]==35 or unewscale2[i-1]==38 or unewscale2[i-1]==40 or unewscale2[i-1]==43 or unewscale2[i-1]==45 or unewscale2[i-1]==47 or unewscale2[i-1]==50 or unewscale2[i-1]==52 or unewscale2[i-1]==55
           or unewscale2[i-1]==57 or unewscale2[i-1]==59):        
            f.write('def flashb%dscale2scale2(event):\n'%unewscale2[i-1])
            f.write('    b%dscale2.config(bg = "green")\n'%unewscale2[i-1])     
            f.write('    rootscale2.after(175, lambda: b%dscale2.config(bg = "black"))\n'%unewscale2[i-1])
            f.write('    d%dscale2scale2()\n'%unewscale2[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale2.bind("%s", flashb%dscale2scale2)\n'%(keys[i-1],unewscale2[i-1]))    
            else:
                f.write('rootscale2.bind("<KeyPress-%s>", flashb%dscale2scale2)\n'%(keys[i-1],unewscale2[i-1]))
        else:
            f.write('def flashb%dscale2scale2(event):\n'%unewscale2[i-1])
            f.write('    b%dscale2.config(bg = "green")\n'%unewscale2[i-1])     
            f.write('    rootscale2.after(175, lambda: b%dscale2.config(bg = "white"))\n'%unewscale2[i-1])
            f.write('    d%dscale2scale2()\n'%unewscale2[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale2.bind("%s", flashb%dscale2scale2)\n'%(keys[i-1],unewscale2[i-1]))    
            else:
                f.write('rootscale2.bind("<KeyPress-%s>", flashb%dscale2scale2)\n'%(keys[i-1],unewscale2[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale2=Button(cscale2,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale2scale2)\n'%(i,notes[i-1],i))
            f.write('b%dscale2.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale2=Button(cscale2,text="%s",bg="white",command=d%dscale2scale2)\n'%(i,notes[i-1],i))
            f.write('b%dscale2.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale2[i-1]==2 or unewscale2[i-1]==4 or unewscale2[i-1]==7 or unewscale2[i-1]==9 or unewscale2[i-1]==11 or
 unewscale2[i-1]==14 or unewscale2[i-1]==16 or unewscale2[i-1]==19 or unewscale2[i-1]==21 or unewscale2[i-1]==23 or
 unewscale2[i-1]==26 or unewscale2[i-1]==28 or unewscale2[i-1]==31 or unewscale2[i-1]==33 or unewscale2[i-1]==35 or
 unewscale2[i-1]==38 or unewscale2[i-1]==40 or unewscale2[i-1]==43 or unewscale2[i-1]==45 or unewscale2[i-1]==47 or
 unewscale2[i-1]==50 or unewscale2[i-1]==52 or unewscale2[i-1]==55 or unewscale2[i-1]==57 or unewscale2[i-1]==59):
            f.write('l%d=Label(cscale2,text="",bg="green")\n'%unewscale2[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale2[i-1],unewscale2[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale2,text="",bg="green")\n'%unewscale2[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale2[i-1],unewscale2[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale2scale2%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale2[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale2[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale2[k])
                    f.write('   b%dscale2.config(bg="green")\n'%(unewscale2[i]))
                    f.write('   b%dscale2.config(bg="green")\n'%(unewscale2[j]))
                    f.write('   b%dscale2.config(bg="green")\n'%(unewscale2[k]))                   
                    if(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==3):
                        f.write('   chordlabelscale2.config(text="%s")\n'%(notes1[unewscale2[i]-1]))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==4):
                        f.write('   chordlabelscale2.config(text="%sm")\n'%(notes1[unewscale2[i]-1]))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==5):
                        f.write('   chordlabelscale2.config(text="%s inv-1")\n'%(notes1[unewscale2[k]-1]))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==4):
                        f.write('   chordlabelscale2.config(text="%s inv-2")\n'%(notes1[unewscale2[j]-1]))
                    elif(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==5):
                        f.write('   chordlabelscale2.config(text="%sm inv-1")\n'%(notes1[unewscale2[k]-1]))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==3):
                        f.write('   chordlabelscale2.config(text="%sm inv-2")\n'%(notes1[unewscale2[j]-1]))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==3):
                        f.write('   chordlabelscale2.config(text="%sdim")\n'%(notes1[unewscale2[i]-1]))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==6):
                        f.write('   chordlabelscale2.config(text="%sdim inv1")\n'%(notes1[unewscale2[k]-1]))
                    elif(unewscale2[j]-unewscale2[i]==6 and unewscale2[k]-unewscale2[j]==3):
                        f.write('   chordlabelscale2.config(text="%sdim inv2")\n'%(notes1[unewscale2[j]-1]))
                    elif(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==4):
                        f.write('   chordlabelscale2.config(text="%saug")\n'%(notes1[unewscale2[i]-1]))
                    elif(unewscale2[j]-unewscale2[i]==2 and unewscale2[k]-unewscale2[j]==5):
                        f.write('   chordlabelscale2.config(text="%ssus2")\n'%(notes1[unewscale2[i]-1]))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==5):
                        f.write('   chordlabelscale2.config(text="%ssus2 inv1")\n'%(notes1[unewscale2[k]-1]))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==2):
                        f.write('   chordlabelscale2.config(text="%ssus4")\n'%(notes1[unewscale2[i]-1]))
                    if(unewscale2[i]==2 or unewscale2[i]==4 or unewscale2[i]==7 or unewscale2[i]==9 or unewscale2[i]==11
                       or unewscale2[i]==14 or unewscale2[i]==16 or unewscale2[i]==19 or unewscale2[i]==21 or unewscale2[i]==23 or unewscale2[i]==26 or unewscale2[i]==28 or unewscale2[i]==31 or unewscale2[i]==33
                       or unewscale2[i]==35 or unewscale2[i]==38 or unewscale2[i]==40 or unewscale2[i]==43 or unewscale2[i]==45 or unewscale2[i]==47 or unewscale2[i]==50 or unewscale2[i]==52 or unewscale2[i]==55
                       or unewscale2[i]==57 or unewscale2[i]==59):
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "black"))\n'%unewscale2[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale2[i]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "white"))\n'%unewscale2[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale2[i]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale2[j]==2 or unewscale2[j]==4 or unewscale2[j]==7 or unewscale2[j]==9 or unewscale2[j]==11 or unewscale2[j]==14 or unewscale2[j]==16 or unewscale2[j]==19 or unewscale2[j]==21 or
                       unewscale2[j]==23 or
                       unewscale2[j]==26 or unewscale2[j]==28 or unewscale2[j]==31 or unewscale2[j]==33 or unewscale2[j]==35 or
                       unewscale2[j]==38 or unewscale2[j]==40 or unewscale2[j]==43 or unewscale2[j]==45 or unewscale2[j]==47 or unewscale2[j]==50 or unewscale2[j]==52 or unewscale2[j]==55 or unewscale2[j]==57 or unewscale2[j]==59):
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "black"))\n'%unewscale2[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale2[j]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "white"))\n'%unewscale2[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale2[j]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale2[k]==2 or unewscale2[k]==4
                       or unewscale2[k]==7 or unewscale2[k]==9 or unewscale2[k]==11 or unewscale2[k]==14 or unewscale2[k]==16 or unewscale2[k]==19 or unewscale2[k]==21 or unewscale2[k]==23 or unewscale2[k]==26 or unewscale2[k]==28
                       or unewscale2[k]==31 or unewscale2[k]==33 or unewscale2[k]==35 or unewscale2[k]==38 or unewscale2[k]==40 or unewscale2[k]==43 or unewscale2[k]==45 or
                       unewscale2[k]==47 or unewscale2[k]==50 or unewscale2[k]==52 or unewscale2[k]==55 or unewscale2[k]==57 or unewscale2[k]==59):
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "black"))\n'%unewscale2[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale2[k]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale2.after(175, lambda: b%dscale2.config(bg = "white"))\n'%unewscale2[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale2,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale2[k]-1]))
                       f.write('   rootscale2.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count3=count3+1
                    f.write('b%dscale2%d%dscale2scale2=Button(cscale2,text="%d%d%d",command=c%d%dscale2scale2%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count3<21):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=300)\n'%(i,j,k,count3*50-45))
                    elif(count3>20 and count3<41):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=340)\n'%(i,j,k,count3*50-1045))
                    elif(count3>40 and count3<61):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=380)\n'%(i,j,k,count3*50-2045))
                    elif(count3>60 and count3<81):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=420)\n'%(i,j,k,count3*50-3045))
                    elif(count3>80 and count3<101):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=460)\n'%(i,j,k,count3*50-4045))
                        
                    elif(count3>100 and count3<121):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=500)\n'%(i,j,k,count3*50-5045))
                        
                    elif(count3>120 and count3<141):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=540)\n'%(i,j,k,count3*50-6045))
                    elif(count3>140 and count3<161):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=580)\n'%(i,j,k,count3*50-7045))
                    elif(count3>160 and count3<181):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=620)\n'%(i,j,k,count3*50-8045))
                    elif(count3>180 and count3<201):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=660)\n'%(i,j,k,count3*50-9045))   
                    elif(count3>200 and count3<221):
                        f.write('b%dscale2%d%dscale2scale2.place(x=%d,y=700)\n'%(i,j,k,count3*50-10045))
                        
                    if(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==3):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%s")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==4):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sm")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==5):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sI1")\n'%(i,j,k,notes1[unewscale2[k]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==4):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sI2")\n'%(i,j,k,notes1[unewscale2[j]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==5):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%smI1")\n'%(i,j,k,notes1[unewscale2[k]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==3):
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('b%dscale2%d%dscale2scale2.config(text="%smI2")\n'%(i,j,k,notes1[unewscale2[j]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==3):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sdim")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))

                    elif(unewscale2[j]-unewscale2[i]==3 and unewscale2[k]-unewscale2[j]==6):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale2[k]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==6 and unewscale2[k]-unewscale2[j]==3):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale2[j]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==4 and unewscale2[k]-unewscale2[j]==4):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%saug")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==2 and unewscale2[k]-unewscale2[j]==5):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==5):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale2[k]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
                    elif(unewscale2[j]-unewscale2[i]==5 and unewscale2[k]-unewscale2[j]==2):
                        f.write('b%dscale2%d%dscale2scale2.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale2[i]-1]))
                        f.write('b%dscale2%d%dscale2scale2.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale2=mainchordcounterscale2+1
                        f.write('def f%d%dscale2scale2%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale2scale2%d()\n'%(i,j,k))
                        f.write('   b%dscale2%d%dscale2scale2.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale2.after(175, lambda: b%dscale2%d%dscale2scale2.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale2.bind("<KeyPress-%s>", f%d%dscale2scale2%d)\n'%(keysforchords[mainchordcounterscale2-1],i,j,k))
##############################################################SCALE 3 BEGINS########################################################################
    f.write('rootscale3=Toplevel()\n')
    f.write('rootscale3.title("Ultimate piano-Scale 3")\n')
    f.write('rootscale3.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale3=0\n')
    f.write('cscale3=Canvas(rootscale3,bg="#b53b35")\n')
    f.write('cscale3.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale3=Label(cscale3,text="chord")\n')
    f.write('chordlabelscale3.place(x=200,y=200)\n')
    f.write('chordlabelscale3.config(font=("Courier", 44))\n')
    f.write('def thapscale3(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale3.bind("<KeyPress-space>", thapscale3) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale3,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale3,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale3=Canvas(cscale3,bg="white")\n')
    f.write('Fscale3.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale3,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale3,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale3,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale3,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale3,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale3,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale3scale3():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale3,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale3==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale3,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale3==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale3\n')
    f.write('   flagfornotemodescale3=1\n')
    f.write('   flagfornotemodescale3btn.config(bg="green")\n')
    f.write('   flagfornotemodescale3btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale3\n')
    f.write('   flagfornotemodescale3=0\n')
    f.write('   flagfornotemodescale3btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale3btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale3btn=Button(cscale3,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale3btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale3btn2=Button(cscale3,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale3btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale3[i-1]==2 or unewscale3[i-1]==4 or unewscale3[i-1]==7 or unewscale3[i-1]==9 or unewscale3[i-1]==11 or unewscale3[i-1]==14 or unewscale3[i-1]==16
           or unewscale3[i-1]==19 or unewscale3[i-1]==21 or unewscale3[i-1]==23 or unewscale3[i-1]==26 or unewscale3[i-1]==28 or unewscale3[i-1]==31 or unewscale3[i-1]==33
           or unewscale3[i-1]==35 or unewscale3[i-1]==38 or unewscale3[i-1]==40 or unewscale3[i-1]==43 or unewscale3[i-1]==45 or unewscale3[i-1]==47 or unewscale3[i-1]==50 or unewscale3[i-1]==52 or unewscale3[i-1]==55
           or unewscale3[i-1]==57 or unewscale3[i-1]==59):        
            f.write('def flashb%dscale3scale3(event):\n'%unewscale3[i-1])
            f.write('    b%dscale3.config(bg = "green")\n'%unewscale3[i-1])     
            f.write('    rootscale3.after(175, lambda: b%dscale3.config(bg = "black"))\n'%unewscale3[i-1])
            f.write('    d%dscale3scale3()\n'%unewscale3[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale3.bind("%s", flashb%dscale3scale3)\n'%(keys[i-1],unewscale3[i-1]))    
            else:
                f.write('rootscale3.bind("<KeyPress-%s>", flashb%dscale3scale3)\n'%(keys[i-1],unewscale3[i-1]))
        else:
            f.write('def flashb%dscale3scale3(event):\n'%unewscale3[i-1])
            f.write('    b%dscale3.config(bg = "green")\n'%unewscale3[i-1])     
            f.write('    rootscale3.after(175, lambda: b%dscale3.config(bg = "white"))\n'%unewscale3[i-1])
            f.write('    d%dscale3scale3()\n'%unewscale3[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale3.bind("%s", flashb%dscale3scale3)\n'%(keys[i-1],unewscale3[i-1]))    
            else:
                f.write('rootscale3.bind("<KeyPress-%s>", flashb%dscale3scale3)\n'%(keys[i-1],unewscale3[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale3=Button(cscale3,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale3scale3)\n'%(i,notes[i-1],i))
            f.write('b%dscale3.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale3=Button(cscale3,text="%s",bg="white",command=d%dscale3scale3)\n'%(i,notes[i-1],i))
            f.write('b%dscale3.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale3[i-1]==2 or unewscale3[i-1]==4 or unewscale3[i-1]==7 or unewscale3[i-1]==9 or unewscale3[i-1]==11 or
 unewscale3[i-1]==14 or unewscale3[i-1]==16 or unewscale3[i-1]==19 or unewscale3[i-1]==21 or unewscale3[i-1]==23 or
 unewscale3[i-1]==26 or unewscale3[i-1]==28 or unewscale3[i-1]==31 or unewscale3[i-1]==33 or unewscale3[i-1]==35 or
 unewscale3[i-1]==38 or unewscale3[i-1]==40 or unewscale3[i-1]==43 or unewscale3[i-1]==45 or unewscale3[i-1]==47 or
 unewscale3[i-1]==50 or unewscale3[i-1]==52 or unewscale3[i-1]==55 or unewscale3[i-1]==57 or unewscale3[i-1]==59):
            f.write('l%d=Label(cscale3,text="",bg="green")\n'%unewscale3[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale3[i-1],unewscale3[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale3,text="",bg="green")\n'%unewscale3[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale3[i-1],unewscale3[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale3scale3%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale3[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale3[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale3[k])
                    f.write('   b%dscale3.config(bg="green")\n'%(unewscale3[i]))
                    f.write('   b%dscale3.config(bg="green")\n'%(unewscale3[j]))
                    f.write('   b%dscale3.config(bg="green")\n'%(unewscale3[k]))                   
                    if(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==3):
                        f.write('   chordlabelscale3.config(text="%s")\n'%(notes1[unewscale3[i]-1]))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==4):
                        f.write('   chordlabelscale3.config(text="%sm")\n'%(notes1[unewscale3[i]-1]))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==5):
                        f.write('   chordlabelscale3.config(text="%s inv-1")\n'%(notes1[unewscale3[k]-1]))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==4):
                        f.write('   chordlabelscale3.config(text="%s inv-2")\n'%(notes1[unewscale3[j]-1]))
                    elif(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==5):
                        f.write('   chordlabelscale3.config(text="%sm inv-1")\n'%(notes1[unewscale3[k]-1]))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==3):
                        f.write('   chordlabelscale3.config(text="%sm inv-2")\n'%(notes1[unewscale3[j]-1]))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==3):
                        f.write('   chordlabelscale3.config(text="%sdim")\n'%(notes1[unewscale3[i]-1]))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==6):
                        f.write('   chordlabelscale3.config(text="%sdim inv1")\n'%(notes1[unewscale3[k]-1]))
                    elif(unewscale3[j]-unewscale3[i]==6 and unewscale3[k]-unewscale3[j]==3):
                        f.write('   chordlabelscale3.config(text="%sdim inv2")\n'%(notes1[unewscale3[j]-1]))
                    elif(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==4):
                        f.write('   chordlabelscale3.config(text="%saug")\n'%(notes1[unewscale3[i]-1]))
                    elif(unewscale3[j]-unewscale3[i]==2 and unewscale3[k]-unewscale3[j]==5):
                        f.write('   chordlabelscale3.config(text="%ssus2")\n'%(notes1[unewscale3[i]-1]))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==5):
                        f.write('   chordlabelscale3.config(text="%ssus2 inv1")\n'%(notes1[unewscale3[k]-1]))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==2):
                        f.write('   chordlabelscale3.config(text="%ssus4")\n'%(notes1[unewscale3[i]-1]))
                    if(unewscale3[i]==2 or unewscale3[i]==4 or unewscale3[i]==7 or unewscale3[i]==9 or unewscale3[i]==11
                       or unewscale3[i]==14 or unewscale3[i]==16 or unewscale3[i]==19 or unewscale3[i]==21 or unewscale3[i]==23 or unewscale3[i]==26 or unewscale3[i]==28 or unewscale3[i]==31 or unewscale3[i]==33
                       or unewscale3[i]==35 or unewscale3[i]==38 or unewscale3[i]==40 or unewscale3[i]==43 or unewscale3[i]==45 or unewscale3[i]==47 or unewscale3[i]==50 or unewscale3[i]==52 or unewscale3[i]==55
                       or unewscale3[i]==57 or unewscale3[i]==59):
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "black"))\n'%unewscale3[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale3[i]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "white"))\n'%unewscale3[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale3[i]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale3[j]==2 or unewscale3[j]==4 or unewscale3[j]==7 or unewscale3[j]==9 or unewscale3[j]==11 or unewscale3[j]==14 or unewscale3[j]==16 or unewscale3[j]==19 or unewscale3[j]==21 or
                       unewscale3[j]==23 or
                       unewscale3[j]==26 or unewscale3[j]==28 or unewscale3[j]==31 or unewscale3[j]==33 or unewscale3[j]==35 or
                       unewscale3[j]==38 or unewscale3[j]==40 or unewscale3[j]==43 or unewscale3[j]==45 or unewscale3[j]==47 or unewscale3[j]==50 or unewscale3[j]==52 or unewscale3[j]==55 or unewscale3[j]==57 or unewscale3[j]==59):
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "black"))\n'%unewscale3[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale3[j]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "white"))\n'%unewscale3[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale3[j]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale3[k]==2 or unewscale3[k]==4
                       or unewscale3[k]==7 or unewscale3[k]==9 or unewscale3[k]==11 or unewscale3[k]==14 or unewscale3[k]==16 or unewscale3[k]==19 or unewscale3[k]==21 or unewscale3[k]==23 or unewscale3[k]==26 or unewscale3[k]==28
                       or unewscale3[k]==31 or unewscale3[k]==33 or unewscale3[k]==35 or unewscale3[k]==38 or unewscale3[k]==40 or unewscale3[k]==43 or unewscale3[k]==45 or
                       unewscale3[k]==47 or unewscale3[k]==50 or unewscale3[k]==52 or unewscale3[k]==55 or unewscale3[k]==57 or unewscale3[k]==59):
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "black"))\n'%unewscale3[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale3[k]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale3.after(175, lambda: b%dscale3.config(bg = "white"))\n'%unewscale3[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale3,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale3[k]-1]))
                       f.write('   rootscale3.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count4=count4+1
                    f.write('b%dscale3%d%dscale3scale3=Button(cscale3,text="%d%d%d",command=c%d%dscale3scale3%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count4<21):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=300)\n'%(i,j,k,count4*50-45))
                    elif(count4>20 and count4<41):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=340)\n'%(i,j,k,count4*50-1045))
                    elif(count4>40 and count4<61):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=380)\n'%(i,j,k,count4*50-2045))
                    elif(count4>60 and count4<81):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=420)\n'%(i,j,k,count4*50-3045))
                    elif(count4>80 and count4<101):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=460)\n'%(i,j,k,count4*50-4045))
                        
                    elif(count4>100 and count4<121):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=500)\n'%(i,j,k,count4*50-5045))
                        
                    elif(count4>120 and count4<141):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=540)\n'%(i,j,k,count4*50-6045))
                    elif(count4>140 and count4<161):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=580)\n'%(i,j,k,count4*50-7045))
                    elif(count4>160 and count4<181):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=620)\n'%(i,j,k,count4*50-8045))
                    elif(count4>180 and count4<201):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=660)\n'%(i,j,k,count4*50-9045))   
                    elif(count4>200 and count4<221):
                        f.write('b%dscale3%d%dscale3scale3.place(x=%d,y=700)\n'%(i,j,k,count4*50-10045))
                        
                    if(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==3):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%s")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==4):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sm")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==5):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sI1")\n'%(i,j,k,notes1[unewscale3[k]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==4):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sI2")\n'%(i,j,k,notes1[unewscale3[j]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==5):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%smI1")\n'%(i,j,k,notes1[unewscale3[k]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==3):
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('b%dscale3%d%dscale3scale3.config(text="%smI2")\n'%(i,j,k,notes1[unewscale3[j]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==3):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sdim")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))

                    elif(unewscale3[j]-unewscale3[i]==3 and unewscale3[k]-unewscale3[j]==6):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale3[k]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==6 and unewscale3[k]-unewscale3[j]==3):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale3[j]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==4 and unewscale3[k]-unewscale3[j]==4):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%saug")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==2 and unewscale3[k]-unewscale3[j]==5):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==5):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale3[k]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
                    elif(unewscale3[j]-unewscale3[i]==5 and unewscale3[k]-unewscale3[j]==2):
                        f.write('b%dscale3%d%dscale3scale3.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale3[i]-1]))
                        f.write('b%dscale3%d%dscale3scale3.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale3=mainchordcounterscale3+1
                        f.write('def f%d%dscale3scale3%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale3scale3%d()\n'%(i,j,k))
                        f.write('   b%dscale3%d%dscale3scale3.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale3.after(175, lambda: b%dscale3%d%dscale3scale3.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale3.bind("<KeyPress-%s>", f%d%dscale3scale3%d)\n'%(keysforchords[mainchordcounterscale3-1],i,j,k))
############################################################SCALE 4 BEGINS#############################
    f.write('rootscale4=Toplevel()\n')
    f.write('rootscale4.title("Ultimate piano-Scale 4")\n')
    f.write('rootscale4.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale4=0\n')
    f.write('cscale4=Canvas(rootscale4,bg="#b53b35")\n')
    f.write('cscale4.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale4=Label(cscale4,text="chord")\n')
    f.write('chordlabelscale4.place(x=200,y=200)\n')
    f.write('chordlabelscale4.config(font=("Courier", 44))\n')
    f.write('def thapscale4(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale4.bind("<KeyPress-space>", thapscale4) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale4,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale4,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale4=Canvas(cscale4,bg="white")\n')
    f.write('Fscale4.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale4,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale4,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale4,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale4,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale4,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale4,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale4scale4():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale4,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale4==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale4,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale4==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale4\n')
    f.write('   flagfornotemodescale4=1\n')
    f.write('   flagfornotemodescale4btn.config(bg="green")\n')
    f.write('   flagfornotemodescale4btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale4\n')
    f.write('   flagfornotemodescale4=0\n')
    f.write('   flagfornotemodescale4btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale4btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale4btn=Button(cscale4,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale4btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale4btn2=Button(cscale4,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale4btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale4[i-1]==2 or unewscale4[i-1]==4 or unewscale4[i-1]==7 or unewscale4[i-1]==9 or unewscale4[i-1]==11 or unewscale4[i-1]==14 or unewscale4[i-1]==16
           or unewscale4[i-1]==19 or unewscale4[i-1]==21 or unewscale4[i-1]==23 or unewscale4[i-1]==26 or unewscale4[i-1]==28 or unewscale4[i-1]==31 or unewscale4[i-1]==33
           or unewscale4[i-1]==35 or unewscale4[i-1]==38 or unewscale4[i-1]==40 or unewscale4[i-1]==43 or unewscale4[i-1]==45 or unewscale4[i-1]==47 or unewscale4[i-1]==50 or unewscale4[i-1]==52 or unewscale4[i-1]==55
           or unewscale4[i-1]==57 or unewscale4[i-1]==59):        
            f.write('def flashb%dscale4scale4(event):\n'%unewscale4[i-1])
            f.write('    b%dscale4.config(bg = "green")\n'%unewscale4[i-1])     
            f.write('    rootscale4.after(175, lambda: b%dscale4.config(bg = "black"))\n'%unewscale4[i-1])
            f.write('    d%dscale4scale4()\n'%unewscale4[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale4.bind("%s", flashb%dscale4scale4)\n'%(keys[i-1],unewscale4[i-1]))    
            else:
                f.write('rootscale4.bind("<KeyPress-%s>", flashb%dscale4scale4)\n'%(keys[i-1],unewscale4[i-1]))
        else:
            f.write('def flashb%dscale4scale4(event):\n'%unewscale4[i-1])
            f.write('    b%dscale4.config(bg = "green")\n'%unewscale4[i-1])     
            f.write('    rootscale4.after(175, lambda: b%dscale4.config(bg = "white"))\n'%unewscale4[i-1])
            f.write('    d%dscale4scale4()\n'%unewscale4[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale4.bind("%s", flashb%dscale4scale4)\n'%(keys[i-1],unewscale4[i-1]))    
            else:
                f.write('rootscale4.bind("<KeyPress-%s>", flashb%dscale4scale4)\n'%(keys[i-1],unewscale4[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale4=Button(cscale4,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale4scale4)\n'%(i,notes[i-1],i))
            f.write('b%dscale4.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale4=Button(cscale4,text="%s",bg="white",command=d%dscale4scale4)\n'%(i,notes[i-1],i))
            f.write('b%dscale4.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale4[i-1]==2 or unewscale4[i-1]==4 or unewscale4[i-1]==7 or unewscale4[i-1]==9 or unewscale4[i-1]==11 or
 unewscale4[i-1]==14 or unewscale4[i-1]==16 or unewscale4[i-1]==19 or unewscale4[i-1]==21 or unewscale4[i-1]==23 or
 unewscale4[i-1]==26 or unewscale4[i-1]==28 or unewscale4[i-1]==31 or unewscale4[i-1]==33 or unewscale4[i-1]==35 or
 unewscale4[i-1]==38 or unewscale4[i-1]==40 or unewscale4[i-1]==43 or unewscale4[i-1]==45 or unewscale4[i-1]==47 or
 unewscale4[i-1]==50 or unewscale4[i-1]==52 or unewscale4[i-1]==55 or unewscale4[i-1]==57 or unewscale4[i-1]==59):
            f.write('l%d=Label(cscale4,text="",bg="green")\n'%unewscale4[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale4[i-1],unewscale4[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale4,text="",bg="green")\n'%unewscale4[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale4[i-1],unewscale4[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale4scale4%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale4[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale4[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale4[k])
                    f.write('   b%dscale4.config(bg="green")\n'%(unewscale4[i]))
                    f.write('   b%dscale4.config(bg="green")\n'%(unewscale4[j]))
                    f.write('   b%dscale4.config(bg="green")\n'%(unewscale4[k]))                   
                    if(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==3):
                        f.write('   chordlabelscale4.config(text="%s")\n'%(notes1[unewscale4[i]-1]))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==4):
                        f.write('   chordlabelscale4.config(text="%sm")\n'%(notes1[unewscale4[i]-1]))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==5):
                        f.write('   chordlabelscale4.config(text="%s inv-1")\n'%(notes1[unewscale4[k]-1]))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==4):
                        f.write('   chordlabelscale4.config(text="%s inv-2")\n'%(notes1[unewscale4[j]-1]))
                    elif(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==5):
                        f.write('   chordlabelscale4.config(text="%sm inv-1")\n'%(notes1[unewscale4[k]-1]))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==3):
                        f.write('   chordlabelscale4.config(text="%sm inv-2")\n'%(notes1[unewscale4[j]-1]))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==3):
                        f.write('   chordlabelscale4.config(text="%sdim")\n'%(notes1[unewscale4[i]-1]))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==6):
                        f.write('   chordlabelscale4.config(text="%sdim inv1")\n'%(notes1[unewscale4[k]-1]))
                    elif(unewscale4[j]-unewscale4[i]==6 and unewscale4[k]-unewscale4[j]==3):
                        f.write('   chordlabelscale4.config(text="%sdim inv2")\n'%(notes1[unewscale4[j]-1]))
                    elif(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==4):
                        f.write('   chordlabelscale4.config(text="%saug")\n'%(notes1[unewscale4[i]-1]))
                    elif(unewscale4[j]-unewscale4[i]==2 and unewscale4[k]-unewscale4[j]==5):
                        f.write('   chordlabelscale4.config(text="%ssus2")\n'%(notes1[unewscale4[i]-1]))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==5):
                        f.write('   chordlabelscale4.config(text="%ssus2 inv1")\n'%(notes1[unewscale4[k]-1]))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==2):
                        f.write('   chordlabelscale4.config(text="%ssus4")\n'%(notes1[unewscale4[i]-1]))
                    if(unewscale4[i]==2 or unewscale4[i]==4 or unewscale4[i]==7 or unewscale4[i]==9 or unewscale4[i]==11
                       or unewscale4[i]==14 or unewscale4[i]==16 or unewscale4[i]==19 or unewscale4[i]==21 or unewscale4[i]==23 or unewscale4[i]==26 or unewscale4[i]==28 or unewscale4[i]==31 or unewscale4[i]==33
                       or unewscale4[i]==35 or unewscale4[i]==38 or unewscale4[i]==40 or unewscale4[i]==43 or unewscale4[i]==45 or unewscale4[i]==47 or unewscale4[i]==50 or unewscale4[i]==52 or unewscale4[i]==55
                       or unewscale4[i]==57 or unewscale4[i]==59):
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "black"))\n'%unewscale4[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale4[i]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "white"))\n'%unewscale4[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale4[i]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale4[j]==2 or unewscale4[j]==4 or unewscale4[j]==7 or unewscale4[j]==9 or unewscale4[j]==11 or unewscale4[j]==14 or unewscale4[j]==16 or unewscale4[j]==19 or unewscale4[j]==21 or
                       unewscale4[j]==23 or
                       unewscale4[j]==26 or unewscale4[j]==28 or unewscale4[j]==31 or unewscale4[j]==33 or unewscale4[j]==35 or
                       unewscale4[j]==38 or unewscale4[j]==40 or unewscale4[j]==43 or unewscale4[j]==45 or unewscale4[j]==47 or unewscale4[j]==50 or unewscale4[j]==52 or unewscale4[j]==55 or unewscale4[j]==57 or unewscale4[j]==59):
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "black"))\n'%unewscale4[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale4[j]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "white"))\n'%unewscale4[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale4[j]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale4[k]==2 or unewscale4[k]==4
                       or unewscale4[k]==7 or unewscale4[k]==9 or unewscale4[k]==11 or unewscale4[k]==14 or unewscale4[k]==16 or unewscale4[k]==19 or unewscale4[k]==21 or unewscale4[k]==23 or unewscale4[k]==26 or unewscale4[k]==28
                       or unewscale4[k]==31 or unewscale4[k]==33 or unewscale4[k]==35 or unewscale4[k]==38 or unewscale4[k]==40 or unewscale4[k]==43 or unewscale4[k]==45 or
                       unewscale4[k]==47 or unewscale4[k]==50 or unewscale4[k]==52 or unewscale4[k]==55 or unewscale4[k]==57 or unewscale4[k]==59):
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "black"))\n'%unewscale4[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale4[k]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale4.after(175, lambda: b%dscale4.config(bg = "white"))\n'%unewscale4[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale4,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale4[k]-1]))
                       f.write('   rootscale4.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count5=count5+1
                    f.write('b%dscale4%d%dscale4scale4=Button(cscale4,text="%d%d%d",command=c%d%dscale4scale4%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count5<21):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=300)\n'%(i,j,k,count5*50-45))
                    elif(count5>20 and count5<41):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=340)\n'%(i,j,k,count5*50-1045))
                    elif(count5>40 and count5<61):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=380)\n'%(i,j,k,count5*50-2045))
                    elif(count5>60 and count5<81):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=420)\n'%(i,j,k,count5*50-3045))
                    elif(count5>80 and count5<101):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=460)\n'%(i,j,k,count5*50-4045))
                        
                    elif(count5>100 and count5<121):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=500)\n'%(i,j,k,count5*50-5045))
                        
                    elif(count5>120 and count5<141):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=540)\n'%(i,j,k,count5*50-6045))
                    elif(count5>140 and count5<161):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=580)\n'%(i,j,k,count5*50-7045))
                    elif(count5>160 and count5<181):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=620)\n'%(i,j,k,count5*50-8045))
                    elif(count5>180 and count5<201):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=660)\n'%(i,j,k,count5*50-9045))   
                    elif(count5>200 and count5<221):
                        f.write('b%dscale4%d%dscale4scale4.place(x=%d,y=700)\n'%(i,j,k,count5*50-10045))
                        
                    if(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==3):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%s")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==4):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sm")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==5):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sI1")\n'%(i,j,k,notes1[unewscale4[k]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==4):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sI2")\n'%(i,j,k,notes1[unewscale4[j]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==5):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%smI1")\n'%(i,j,k,notes1[unewscale4[k]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==3):
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('b%dscale4%d%dscale4scale4.config(text="%smI2")\n'%(i,j,k,notes1[unewscale4[j]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==3):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sdim")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))

                    elif(unewscale4[j]-unewscale4[i]==3 and unewscale4[k]-unewscale4[j]==6):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale4[k]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==6 and unewscale4[k]-unewscale4[j]==3):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale4[j]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==4 and unewscale4[k]-unewscale4[j]==4):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%saug")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==2 and unewscale4[k]-unewscale4[j]==5):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==5):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale4[k]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
                    elif(unewscale4[j]-unewscale4[i]==5 and unewscale4[k]-unewscale4[j]==2):
                        f.write('b%dscale4%d%dscale4scale4.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale4[i]-1]))
                        f.write('b%dscale4%d%dscale4scale4.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale4=mainchordcounterscale4+1
                        f.write('def f%d%dscale4scale4%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale4scale4%d()\n'%(i,j,k))
                        f.write('   b%dscale4%d%dscale4scale4.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale4.after(175, lambda: b%dscale4%d%dscale4scale4.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale4.bind("<KeyPress-%s>", f%d%dscale4scale4%d)\n'%(keysforchords[mainchordcounterscale4-1],i,j,k))
#################################################SCALE 5 BEGINS################################################
    f.write('rootscale5=Toplevel()\n')
    f.write('rootscale5.title("Ultimate piano-Scale 5")\n')
    f.write('rootscale5.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale5=0\n')
    f.write('cscale5=Canvas(rootscale5,bg="#b53b35")\n')
    f.write('cscale5.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale5=Label(cscale5,text="chord")\n')
    f.write('chordlabelscale5.place(x=200,y=200)\n')
    f.write('chordlabelscale5.config(font=("Courier", 44))\n')
    f.write('def thapscale5(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale5.bind("<KeyPress-space>", thapscale5) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale5,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale5,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale5=Canvas(cscale5,bg="white")\n')
    f.write('Fscale5.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale5,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale5,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale5,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale5,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale5,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale5,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale5scale5():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale5,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale5==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale5,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale5==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale5\n')
    f.write('   flagfornotemodescale5=1\n')
    f.write('   flagfornotemodescale5btn.config(bg="green")\n')
    f.write('   flagfornotemodescale5btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale5\n')
    f.write('   flagfornotemodescale5=0\n')
    f.write('   flagfornotemodescale5btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale5btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale5btn=Button(cscale5,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale5btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale5btn2=Button(cscale5,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale5btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale5[i-1]==2 or unewscale5[i-1]==4 or unewscale5[i-1]==7 or unewscale5[i-1]==9 or unewscale5[i-1]==11 or unewscale5[i-1]==14 or unewscale5[i-1]==16
           or unewscale5[i-1]==19 or unewscale5[i-1]==21 or unewscale5[i-1]==23 or unewscale5[i-1]==26 or unewscale5[i-1]==28 or unewscale5[i-1]==31 or unewscale5[i-1]==33
           or unewscale5[i-1]==35 or unewscale5[i-1]==38 or unewscale5[i-1]==40 or unewscale5[i-1]==43 or unewscale5[i-1]==45 or unewscale5[i-1]==47 or unewscale5[i-1]==50 or unewscale5[i-1]==52 or unewscale5[i-1]==55
           or unewscale5[i-1]==57 or unewscale5[i-1]==59):        
            f.write('def flashb%dscale5scale5(event):\n'%unewscale5[i-1])
            f.write('    b%dscale5.config(bg = "green")\n'%unewscale5[i-1])     
            f.write('    rootscale5.after(175, lambda: b%dscale5.config(bg = "black"))\n'%unewscale5[i-1])
            f.write('    d%dscale5scale5()\n'%unewscale5[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale5.bind("%s", flashb%dscale5scale5)\n'%(keys[i-1],unewscale5[i-1]))    
            else:
                f.write('rootscale5.bind("<KeyPress-%s>", flashb%dscale5scale5)\n'%(keys[i-1],unewscale5[i-1]))
        else:
            f.write('def flashb%dscale5scale5(event):\n'%unewscale5[i-1])
            f.write('    b%dscale5.config(bg = "green")\n'%unewscale5[i-1])     
            f.write('    rootscale5.after(175, lambda: b%dscale5.config(bg = "white"))\n'%unewscale5[i-1])
            f.write('    d%dscale5scale5()\n'%unewscale5[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale5.bind("%s", flashb%dscale5scale5)\n'%(keys[i-1],unewscale5[i-1]))    
            else:
                f.write('rootscale5.bind("<KeyPress-%s>", flashb%dscale5scale5)\n'%(keys[i-1],unewscale5[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale5=Button(cscale5,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale5scale5)\n'%(i,notes[i-1],i))
            f.write('b%dscale5.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale5=Button(cscale5,text="%s",bg="white",command=d%dscale5scale5)\n'%(i,notes[i-1],i))
            f.write('b%dscale5.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale5[i-1]==2 or unewscale5[i-1]==4 or unewscale5[i-1]==7 or unewscale5[i-1]==9 or unewscale5[i-1]==11 or
 unewscale5[i-1]==14 or unewscale5[i-1]==16 or unewscale5[i-1]==19 or unewscale5[i-1]==21 or unewscale5[i-1]==23 or
 unewscale5[i-1]==26 or unewscale5[i-1]==28 or unewscale5[i-1]==31 or unewscale5[i-1]==33 or unewscale5[i-1]==35 or
 unewscale5[i-1]==38 or unewscale5[i-1]==40 or unewscale5[i-1]==43 or unewscale5[i-1]==45 or unewscale5[i-1]==47 or
 unewscale5[i-1]==50 or unewscale5[i-1]==52 or unewscale5[i-1]==55 or unewscale5[i-1]==57 or unewscale5[i-1]==59):
            f.write('l%d=Label(cscale5,text="",bg="green")\n'%unewscale5[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale5[i-1],unewscale5[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale5,text="",bg="green")\n'%unewscale5[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale5[i-1],unewscale5[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale5scale5%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale5[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale5[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale5[k])
                    f.write('   b%dscale5.config(bg="green")\n'%(unewscale5[i]))
                    f.write('   b%dscale5.config(bg="green")\n'%(unewscale5[j]))
                    f.write('   b%dscale5.config(bg="green")\n'%(unewscale5[k]))                   
                    if(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==3):
                        f.write('   chordlabelscale5.config(text="%s")\n'%(notes1[unewscale5[i]-1]))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==4):
                        f.write('   chordlabelscale5.config(text="%sm")\n'%(notes1[unewscale5[i]-1]))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==5):
                        f.write('   chordlabelscale5.config(text="%s inv-1")\n'%(notes1[unewscale5[k]-1]))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==4):
                        f.write('   chordlabelscale5.config(text="%s inv-2")\n'%(notes1[unewscale5[j]-1]))
                    elif(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==5):
                        f.write('   chordlabelscale5.config(text="%sm inv-1")\n'%(notes1[unewscale5[k]-1]))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==3):
                        f.write('   chordlabelscale5.config(text="%sm inv-2")\n'%(notes1[unewscale5[j]-1]))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==3):
                        f.write('   chordlabelscale5.config(text="%sdim")\n'%(notes1[unewscale5[i]-1]))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==6):
                        f.write('   chordlabelscale5.config(text="%sdim inv1")\n'%(notes1[unewscale5[k]-1]))
                    elif(unewscale5[j]-unewscale5[i]==6 and unewscale5[k]-unewscale5[j]==3):
                        f.write('   chordlabelscale5.config(text="%sdim inv2")\n'%(notes1[unewscale5[j]-1]))
                    elif(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==4):
                        f.write('   chordlabelscale5.config(text="%saug")\n'%(notes1[unewscale5[i]-1]))
                    elif(unewscale5[j]-unewscale5[i]==2 and unewscale5[k]-unewscale5[j]==5):
                        f.write('   chordlabelscale5.config(text="%ssus2")\n'%(notes1[unewscale5[i]-1]))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==5):
                        f.write('   chordlabelscale5.config(text="%ssus2 inv1")\n'%(notes1[unewscale5[k]-1]))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==2):
                        f.write('   chordlabelscale5.config(text="%ssus4")\n'%(notes1[unewscale5[i]-1]))
                    if(unewscale5[i]==2 or unewscale5[i]==4 or unewscale5[i]==7 or unewscale5[i]==9 or unewscale5[i]==11
                       or unewscale5[i]==14 or unewscale5[i]==16 or unewscale5[i]==19 or unewscale5[i]==21 or unewscale5[i]==23 or unewscale5[i]==26 or unewscale5[i]==28 or unewscale5[i]==31 or unewscale5[i]==33
                       or unewscale5[i]==35 or unewscale5[i]==38 or unewscale5[i]==40 or unewscale5[i]==43 or unewscale5[i]==45 or unewscale5[i]==47 or unewscale5[i]==50 or unewscale5[i]==52 or unewscale5[i]==55
                       or unewscale5[i]==57 or unewscale5[i]==59):
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "black"))\n'%unewscale5[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale5[i]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "white"))\n'%unewscale5[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale5[i]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale5[j]==2 or unewscale5[j]==4 or unewscale5[j]==7 or unewscale5[j]==9 or unewscale5[j]==11 or unewscale5[j]==14 or unewscale5[j]==16 or unewscale5[j]==19 or unewscale5[j]==21 or
                       unewscale5[j]==23 or
                       unewscale5[j]==26 or unewscale5[j]==28 or unewscale5[j]==31 or unewscale5[j]==33 or unewscale5[j]==35 or
                       unewscale5[j]==38 or unewscale5[j]==40 or unewscale5[j]==43 or unewscale5[j]==45 or unewscale5[j]==47 or unewscale5[j]==50 or unewscale5[j]==52 or unewscale5[j]==55 or unewscale5[j]==57 or unewscale5[j]==59):
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "black"))\n'%unewscale5[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale5[j]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "white"))\n'%unewscale5[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale5[j]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale5[k]==2 or unewscale5[k]==4
                       or unewscale5[k]==7 or unewscale5[k]==9 or unewscale5[k]==11 or unewscale5[k]==14 or unewscale5[k]==16 or unewscale5[k]==19 or unewscale5[k]==21 or unewscale5[k]==23 or unewscale5[k]==26 or unewscale5[k]==28
                       or unewscale5[k]==31 or unewscale5[k]==33 or unewscale5[k]==35 or unewscale5[k]==38 or unewscale5[k]==40 or unewscale5[k]==43 or unewscale5[k]==45 or
                       unewscale5[k]==47 or unewscale5[k]==50 or unewscale5[k]==52 or unewscale5[k]==55 or unewscale5[k]==57 or unewscale5[k]==59):
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "black"))\n'%unewscale5[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale5[k]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale5.after(175, lambda: b%dscale5.config(bg = "white"))\n'%unewscale5[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale5,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale5[k]-1]))
                       f.write('   rootscale5.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count6=count6+1
                    f.write('b%dscale5%d%dscale5scale5=Button(cscale5,text="%d%d%d",command=c%d%dscale5scale5%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count6<21):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=300)\n'%(i,j,k,count6*50-45))
                    elif(count6>20 and count6<41):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=340)\n'%(i,j,k,count6*50-1045))
                    elif(count6>40 and count6<61):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=380)\n'%(i,j,k,count6*50-2045))
                    elif(count6>60 and count6<81):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=420)\n'%(i,j,k,count6*50-3045))
                    elif(count6>80 and count6<101):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=460)\n'%(i,j,k,count6*50-4045))
                        
                    elif(count6>100 and count6<121):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=500)\n'%(i,j,k,count6*50-5045))
                        
                    elif(count6>120 and count6<141):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=540)\n'%(i,j,k,count6*50-6045))
                    elif(count6>140 and count6<161):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=580)\n'%(i,j,k,count6*50-7045))
                    elif(count6>160 and count6<181):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=620)\n'%(i,j,k,count6*50-8045))
                    elif(count6>180 and count6<201):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=660)\n'%(i,j,k,count6*50-9045))   
                    elif(count6>200 and count6<221):
                        f.write('b%dscale5%d%dscale5scale5.place(x=%d,y=700)\n'%(i,j,k,count6*50-10045))
                        
                    if(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==3):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%s")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==4):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sm")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==5):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sI1")\n'%(i,j,k,notes1[unewscale5[k]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==4):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sI2")\n'%(i,j,k,notes1[unewscale5[j]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==5):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%smI1")\n'%(i,j,k,notes1[unewscale5[k]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==3):
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('b%dscale5%d%dscale5scale5.config(text="%smI2")\n'%(i,j,k,notes1[unewscale5[j]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==3):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sdim")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))

                    elif(unewscale5[j]-unewscale5[i]==3 and unewscale5[k]-unewscale5[j]==6):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale5[k]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==6 and unewscale5[k]-unewscale5[j]==3):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale5[j]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==4 and unewscale5[k]-unewscale5[j]==4):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%saug")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==2 and unewscale5[k]-unewscale5[j]==5):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==5):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale5[k]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
                    elif(unewscale5[j]-unewscale5[i]==5 and unewscale5[k]-unewscale5[j]==2):
                        f.write('b%dscale5%d%dscale5scale5.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale5[i]-1]))
                        f.write('b%dscale5%d%dscale5scale5.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale5=mainchordcounterscale5+1
                        f.write('def f%d%dscale5scale5%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale5scale5%d()\n'%(i,j,k))
                        f.write('   b%dscale5%d%dscale5scale5.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale5.after(175, lambda: b%dscale5%d%dscale5scale5.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale5.bind("<KeyPress-%s>", f%d%dscale5scale5%d)\n'%(keysforchords[mainchordcounterscale5-1],i,j,k))
#########################################SCALE 6 ################################################################
    f.write('rootscale6=Toplevel()\n')
    f.write('rootscale6.title("Ultimate piano-Scale 6")\n')
    f.write('rootscale6.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale6=0\n')
    f.write('cscale6=Canvas(rootscale6,bg="#b53b35")\n')
    f.write('cscale6.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale6=Label(cscale6,text="chord")\n')
    f.write('chordlabelscale6.place(x=200,y=200)\n')
    f.write('chordlabelscale6.config(font=("Courier", 44))\n')
    f.write('def thapscale6(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale6.bind("<KeyPress-space>", thapscale6) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale6,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale6,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale6=Canvas(cscale6,bg="white")\n')
    f.write('Fscale6.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale6,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale6,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale6,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale6,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale6,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale6,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale6scale6():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale6,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale6==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale6,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale6==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale6\n')
    f.write('   flagfornotemodescale6=1\n')
    f.write('   flagfornotemodescale6btn.config(bg="green")\n')
    f.write('   flagfornotemodescale6btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale6\n')
    f.write('   flagfornotemodescale6=0\n')
    f.write('   flagfornotemodescale6btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale6btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale6btn=Button(cscale6,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale6btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale6btn2=Button(cscale6,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale6btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale6[i-1]==2 or unewscale6[i-1]==4 or unewscale6[i-1]==7 or unewscale6[i-1]==9 or unewscale6[i-1]==11 or unewscale6[i-1]==14 or unewscale6[i-1]==16
           or unewscale6[i-1]==19 or unewscale6[i-1]==21 or unewscale6[i-1]==23 or unewscale6[i-1]==26 or unewscale6[i-1]==28 or unewscale6[i-1]==31 or unewscale6[i-1]==33
           or unewscale6[i-1]==35 or unewscale6[i-1]==38 or unewscale6[i-1]==40 or unewscale6[i-1]==43 or unewscale6[i-1]==45 or unewscale6[i-1]==47 or unewscale6[i-1]==50 or unewscale6[i-1]==52 or unewscale6[i-1]==55
           or unewscale6[i-1]==57 or unewscale6[i-1]==59):        
            f.write('def flashb%dscale6scale6(event):\n'%unewscale6[i-1])
            f.write('    b%dscale6.config(bg = "green")\n'%unewscale6[i-1])     
            f.write('    rootscale6.after(175, lambda: b%dscale6.config(bg = "black"))\n'%unewscale6[i-1])
            f.write('    d%dscale6scale6()\n'%unewscale6[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale6.bind("%s", flashb%dscale6scale6)\n'%(keys[i-1],unewscale6[i-1]))    
            else:
                f.write('rootscale6.bind("<KeyPress-%s>", flashb%dscale6scale6)\n'%(keys[i-1],unewscale6[i-1]))
        else:
            f.write('def flashb%dscale6scale6(event):\n'%unewscale6[i-1])
            f.write('    b%dscale6.config(bg = "green")\n'%unewscale6[i-1])     
            f.write('    rootscale6.after(175, lambda: b%dscale6.config(bg = "white"))\n'%unewscale6[i-1])
            f.write('    d%dscale6scale6()\n'%unewscale6[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale6.bind("%s", flashb%dscale6scale6)\n'%(keys[i-1],unewscale6[i-1]))    
            else:
                f.write('rootscale6.bind("<KeyPress-%s>", flashb%dscale6scale6)\n'%(keys[i-1],unewscale6[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale6=Button(cscale6,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale6scale6)\n'%(i,notes[i-1],i))
            f.write('b%dscale6.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale6=Button(cscale6,text="%s",bg="white",command=d%dscale6scale6)\n'%(i,notes[i-1],i))
            f.write('b%dscale6.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale6[i-1]==2 or unewscale6[i-1]==4 or unewscale6[i-1]==7 or unewscale6[i-1]==9 or unewscale6[i-1]==11 or
 unewscale6[i-1]==14 or unewscale6[i-1]==16 or unewscale6[i-1]==19 or unewscale6[i-1]==21 or unewscale6[i-1]==23 or
 unewscale6[i-1]==26 or unewscale6[i-1]==28 or unewscale6[i-1]==31 or unewscale6[i-1]==33 or unewscale6[i-1]==35 or
 unewscale6[i-1]==38 or unewscale6[i-1]==40 or unewscale6[i-1]==43 or unewscale6[i-1]==45 or unewscale6[i-1]==47 or
 unewscale6[i-1]==50 or unewscale6[i-1]==52 or unewscale6[i-1]==55 or unewscale6[i-1]==57 or unewscale6[i-1]==59):
            f.write('l%d=Label(cscale6,text="",bg="green")\n'%unewscale6[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale6[i-1],unewscale6[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale6,text="",bg="green")\n'%unewscale6[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale6[i-1],unewscale6[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale6scale6%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale6[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale6[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale6[k])
                    f.write('   b%dscale6.config(bg="green")\n'%(unewscale6[i]))
                    f.write('   b%dscale6.config(bg="green")\n'%(unewscale6[j]))
                    f.write('   b%dscale6.config(bg="green")\n'%(unewscale6[k]))                   
                    if(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==3):
                        f.write('   chordlabelscale6.config(text="%s")\n'%(notes1[unewscale6[i]-1]))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==4):
                        f.write('   chordlabelscale6.config(text="%sm")\n'%(notes1[unewscale6[i]-1]))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==5):
                        f.write('   chordlabelscale6.config(text="%s inv-1")\n'%(notes1[unewscale6[k]-1]))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==4):
                        f.write('   chordlabelscale6.config(text="%s inv-2")\n'%(notes1[unewscale6[j]-1]))
                    elif(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==5):
                        f.write('   chordlabelscale6.config(text="%sm inv-1")\n'%(notes1[unewscale6[k]-1]))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==3):
                        f.write('   chordlabelscale6.config(text="%sm inv-2")\n'%(notes1[unewscale6[j]-1]))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==3):
                        f.write('   chordlabelscale6.config(text="%sdim")\n'%(notes1[unewscale6[i]-1]))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==6):
                        f.write('   chordlabelscale6.config(text="%sdim inv1")\n'%(notes1[unewscale6[k]-1]))
                    elif(unewscale6[j]-unewscale6[i]==6 and unewscale6[k]-unewscale6[j]==3):
                        f.write('   chordlabelscale6.config(text="%sdim inv2")\n'%(notes1[unewscale6[j]-1]))
                    elif(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==4):
                        f.write('   chordlabelscale6.config(text="%saug")\n'%(notes1[unewscale6[i]-1]))
                    elif(unewscale6[j]-unewscale6[i]==2 and unewscale6[k]-unewscale6[j]==5):
                        f.write('   chordlabelscale6.config(text="%ssus2")\n'%(notes1[unewscale6[i]-1]))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==5):
                        f.write('   chordlabelscale6.config(text="%ssus2 inv1")\n'%(notes1[unewscale6[k]-1]))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==2):
                        f.write('   chordlabelscale6.config(text="%ssus4")\n'%(notes1[unewscale6[i]-1]))
                    if(unewscale6[i]==2 or unewscale6[i]==4 or unewscale6[i]==7 or unewscale6[i]==9 or unewscale6[i]==11
                       or unewscale6[i]==14 or unewscale6[i]==16 or unewscale6[i]==19 or unewscale6[i]==21 or unewscale6[i]==23 or unewscale6[i]==26 or unewscale6[i]==28 or unewscale6[i]==31 or unewscale6[i]==33
                       or unewscale6[i]==35 or unewscale6[i]==38 or unewscale6[i]==40 or unewscale6[i]==43 or unewscale6[i]==45 or unewscale6[i]==47 or unewscale6[i]==50 or unewscale6[i]==52 or unewscale6[i]==55
                       or unewscale6[i]==57 or unewscale6[i]==59):
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "black"))\n'%unewscale6[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale6[i]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "white"))\n'%unewscale6[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale6[i]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale6[j]==2 or unewscale6[j]==4 or unewscale6[j]==7 or unewscale6[j]==9 or unewscale6[j]==11 or unewscale6[j]==14 or unewscale6[j]==16 or unewscale6[j]==19 or unewscale6[j]==21 or
                       unewscale6[j]==23 or
                       unewscale6[j]==26 or unewscale6[j]==28 or unewscale6[j]==31 or unewscale6[j]==33 or unewscale6[j]==35 or
                       unewscale6[j]==38 or unewscale6[j]==40 or unewscale6[j]==43 or unewscale6[j]==45 or unewscale6[j]==47 or unewscale6[j]==50 or unewscale6[j]==52 or unewscale6[j]==55 or unewscale6[j]==57 or unewscale6[j]==59):
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "black"))\n'%unewscale6[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale6[j]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "white"))\n'%unewscale6[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale6[j]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale6[k]==2 or unewscale6[k]==4
                       or unewscale6[k]==7 or unewscale6[k]==9 or unewscale6[k]==11 or unewscale6[k]==14 or unewscale6[k]==16 or unewscale6[k]==19 or unewscale6[k]==21 or unewscale6[k]==23 or unewscale6[k]==26 or unewscale6[k]==28
                       or unewscale6[k]==31 or unewscale6[k]==33 or unewscale6[k]==35 or unewscale6[k]==38 or unewscale6[k]==40 or unewscale6[k]==43 or unewscale6[k]==45 or
                       unewscale6[k]==47 or unewscale6[k]==50 or unewscale6[k]==52 or unewscale6[k]==55 or unewscale6[k]==57 or unewscale6[k]==59):
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "black"))\n'%unewscale6[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale6[k]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale6.after(175, lambda: b%dscale6.config(bg = "white"))\n'%unewscale6[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale6,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale6[k]-1]))
                       f.write('   rootscale6.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count7=count7+1
                    f.write('b%dscale6%d%dscale6scale6=Button(cscale6,text="%d%d%d",command=c%d%dscale6scale6%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count7<21):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=300)\n'%(i,j,k,count7*50-45))
                    elif(count7>20 and count7<41):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=340)\n'%(i,j,k,count7*50-1045))
                    elif(count7>40 and count7<61):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=380)\n'%(i,j,k,count7*50-2045))
                    elif(count7>60 and count7<81):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=420)\n'%(i,j,k,count7*50-3045))
                    elif(count7>80 and count7<101):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=460)\n'%(i,j,k,count7*50-4045))
                        
                    elif(count7>100 and count7<121):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=500)\n'%(i,j,k,count7*50-5045))
                        
                    elif(count7>120 and count7<141):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=540)\n'%(i,j,k,count7*50-6045))
                    elif(count7>140 and count7<161):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=580)\n'%(i,j,k,count7*50-7045))
                    elif(count7>160 and count7<181):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=620)\n'%(i,j,k,count7*50-8045))
                    elif(count7>180 and count7<201):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=660)\n'%(i,j,k,count7*50-9045))   
                    elif(count7>200 and count7<221):
                        f.write('b%dscale6%d%dscale6scale6.place(x=%d,y=700)\n'%(i,j,k,count7*50-10045))
                        
                    if(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==3):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%s")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==4):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sm")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==5):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sI1")\n'%(i,j,k,notes1[unewscale6[k]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==4):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sI2")\n'%(i,j,k,notes1[unewscale6[j]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==5):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%smI1")\n'%(i,j,k,notes1[unewscale6[k]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==3):
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('b%dscale6%d%dscale6scale6.config(text="%smI2")\n'%(i,j,k,notes1[unewscale6[j]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==3):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sdim")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))

                    elif(unewscale6[j]-unewscale6[i]==3 and unewscale6[k]-unewscale6[j]==6):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale6[k]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==6 and unewscale6[k]-unewscale6[j]==3):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale6[j]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==4 and unewscale6[k]-unewscale6[j]==4):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%saug")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==2 and unewscale6[k]-unewscale6[j]==5):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==5):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale6[k]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
                    elif(unewscale6[j]-unewscale6[i]==5 and unewscale6[k]-unewscale6[j]==2):
                        f.write('b%dscale6%d%dscale6scale6.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale6[i]-1]))
                        f.write('b%dscale6%d%dscale6scale6.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale6=mainchordcounterscale6+1
                        f.write('def f%d%dscale6scale6%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale6scale6%d()\n'%(i,j,k))
                        f.write('   b%dscale6%d%dscale6scale6.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale6.after(175, lambda: b%dscale6%d%dscale6scale6.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale6.bind("<KeyPress-%s>", f%d%dscale6scale6%d)\n'%(keysforchords[mainchordcounterscale6-1],i,j,k))
#######################################################SCALE 7 BEGINS
    f.write('rootscale7=Toplevel()\n')
    f.write('rootscale7.title("Ultimate piano-Scale 7")\n')
    f.write('rootscale7.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale7=0\n')
    f.write('cscale7=Canvas(rootscale7,bg="#b53b35")\n')
    f.write('cscale7.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale7=Label(cscale7,text="chord")\n')
    f.write('chordlabelscale7.place(x=200,y=200)\n')
    f.write('chordlabelscale7.config(font=("Courier", 44))\n')
    f.write('def thapscale7(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale7.bind("<KeyPress-space>", thapscale7) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale7,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale7,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale7=Canvas(cscale7,bg="white")\n')
    f.write('Fscale7.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale7,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale7,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale7,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale7,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale7,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale7,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale7scale7():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale7,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale7==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale7,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale7==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale7\n')
    f.write('   flagfornotemodescale7=1\n')
    f.write('   flagfornotemodescale7btn.config(bg="green")\n')
    f.write('   flagfornotemodescale7btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale7\n')
    f.write('   flagfornotemodescale7=0\n')
    f.write('   flagfornotemodescale7btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale7btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale7btn=Button(cscale7,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale7btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale7btn2=Button(cscale7,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale7btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale7[i-1]==2 or unewscale7[i-1]==4 or unewscale7[i-1]==7 or unewscale7[i-1]==9 or unewscale7[i-1]==11 or unewscale7[i-1]==14 or unewscale7[i-1]==16
           or unewscale7[i-1]==19 or unewscale7[i-1]==21 or unewscale7[i-1]==23 or unewscale7[i-1]==26 or unewscale7[i-1]==28 or unewscale7[i-1]==31 or unewscale7[i-1]==33
           or unewscale7[i-1]==35 or unewscale7[i-1]==38 or unewscale7[i-1]==40 or unewscale7[i-1]==43 or unewscale7[i-1]==45 or unewscale7[i-1]==47 or unewscale7[i-1]==50 or unewscale7[i-1]==52 or unewscale7[i-1]==55
           or unewscale7[i-1]==57 or unewscale7[i-1]==59):        
            f.write('def flashb%dscale7scale7(event):\n'%unewscale7[i-1])
            f.write('    b%dscale7.config(bg = "green")\n'%unewscale7[i-1])     
            f.write('    rootscale7.after(175, lambda: b%dscale7.config(bg = "black"))\n'%unewscale7[i-1])
            f.write('    d%dscale7scale7()\n'%unewscale7[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale7.bind("%s", flashb%dscale7scale7)\n'%(keys[i-1],unewscale7[i-1]))    
            else:
                f.write('rootscale7.bind("<KeyPress-%s>", flashb%dscale7scale7)\n'%(keys[i-1],unewscale7[i-1]))
        else:
            f.write('def flashb%dscale7scale7(event):\n'%unewscale7[i-1])
            f.write('    b%dscale7.config(bg = "green")\n'%unewscale7[i-1])     
            f.write('    rootscale7.after(175, lambda: b%dscale7.config(bg = "white"))\n'%unewscale7[i-1])
            f.write('    d%dscale7scale7()\n'%unewscale7[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale7.bind("%s", flashb%dscale7scale7)\n'%(keys[i-1],unewscale7[i-1]))    
            else:
                f.write('rootscale7.bind("<KeyPress-%s>", flashb%dscale7scale7)\n'%(keys[i-1],unewscale7[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale7=Button(cscale7,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale7scale7)\n'%(i,notes[i-1],i))
            f.write('b%dscale7.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale7=Button(cscale7,text="%s",bg="white",command=d%dscale7scale7)\n'%(i,notes[i-1],i))
            f.write('b%dscale7.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale7[i-1]==2 or unewscale7[i-1]==4 or unewscale7[i-1]==7 or unewscale7[i-1]==9 or unewscale7[i-1]==11 or
 unewscale7[i-1]==14 or unewscale7[i-1]==16 or unewscale7[i-1]==19 or unewscale7[i-1]==21 or unewscale7[i-1]==23 or
 unewscale7[i-1]==26 or unewscale7[i-1]==28 or unewscale7[i-1]==31 or unewscale7[i-1]==33 or unewscale7[i-1]==35 or
 unewscale7[i-1]==38 or unewscale7[i-1]==40 or unewscale7[i-1]==43 or unewscale7[i-1]==45 or unewscale7[i-1]==47 or
 unewscale7[i-1]==50 or unewscale7[i-1]==52 or unewscale7[i-1]==55 or unewscale7[i-1]==57 or unewscale7[i-1]==59):
            f.write('l%d=Label(cscale7,text="",bg="green")\n'%unewscale7[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale7[i-1],unewscale7[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale7,text="",bg="green")\n'%unewscale7[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale7[i-1],unewscale7[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale7scale7%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale7[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale7[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale7[k])
                    f.write('   b%dscale7.config(bg="green")\n'%(unewscale7[i]))
                    f.write('   b%dscale7.config(bg="green")\n'%(unewscale7[j]))
                    f.write('   b%dscale7.config(bg="green")\n'%(unewscale7[k]))                   
                    if(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==3):
                        f.write('   chordlabelscale7.config(text="%s")\n'%(notes1[unewscale7[i]-1]))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==4):
                        f.write('   chordlabelscale7.config(text="%sm")\n'%(notes1[unewscale7[i]-1]))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==5):
                        f.write('   chordlabelscale7.config(text="%s inv-1")\n'%(notes1[unewscale7[k]-1]))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==4):
                        f.write('   chordlabelscale7.config(text="%s inv-2")\n'%(notes1[unewscale7[j]-1]))
                    elif(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==5):
                        f.write('   chordlabelscale7.config(text="%sm inv-1")\n'%(notes1[unewscale7[k]-1]))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==3):
                        f.write('   chordlabelscale7.config(text="%sm inv-2")\n'%(notes1[unewscale7[j]-1]))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==3):
                        f.write('   chordlabelscale7.config(text="%sdim")\n'%(notes1[unewscale7[i]-1]))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==6):
                        f.write('   chordlabelscale7.config(text="%sdim inv1")\n'%(notes1[unewscale7[k]-1]))
                    elif(unewscale7[j]-unewscale7[i]==6 and unewscale7[k]-unewscale7[j]==3):
                        f.write('   chordlabelscale7.config(text="%sdim inv2")\n'%(notes1[unewscale7[j]-1]))
                    elif(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==4):
                        f.write('   chordlabelscale7.config(text="%saug")\n'%(notes1[unewscale7[i]-1]))
                    elif(unewscale7[j]-unewscale7[i]==2 and unewscale7[k]-unewscale7[j]==5):
                        f.write('   chordlabelscale7.config(text="%ssus2")\n'%(notes1[unewscale7[i]-1]))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==5):
                        f.write('   chordlabelscale7.config(text="%ssus2 inv1")\n'%(notes1[unewscale7[k]-1]))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==2):
                        f.write('   chordlabelscale7.config(text="%ssus4")\n'%(notes1[unewscale7[i]-1]))
                    if(unewscale7[i]==2 or unewscale7[i]==4 or unewscale7[i]==7 or unewscale7[i]==9 or unewscale7[i]==11
                       or unewscale7[i]==14 or unewscale7[i]==16 or unewscale7[i]==19 or unewscale7[i]==21 or unewscale7[i]==23 or unewscale7[i]==26 or unewscale7[i]==28 or unewscale7[i]==31 or unewscale7[i]==33
                       or unewscale7[i]==35 or unewscale7[i]==38 or unewscale7[i]==40 or unewscale7[i]==43 or unewscale7[i]==45 or unewscale7[i]==47 or unewscale7[i]==50 or unewscale7[i]==52 or unewscale7[i]==55
                       or unewscale7[i]==57 or unewscale7[i]==59):
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "black"))\n'%unewscale7[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale7[i]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "white"))\n'%unewscale7[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale7[i]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale7[j]==2 or unewscale7[j]==4 or unewscale7[j]==7 or unewscale7[j]==9 or unewscale7[j]==11 or unewscale7[j]==14 or unewscale7[j]==16 or unewscale7[j]==19 or unewscale7[j]==21 or
                       unewscale7[j]==23 or
                       unewscale7[j]==26 or unewscale7[j]==28 or unewscale7[j]==31 or unewscale7[j]==33 or unewscale7[j]==35 or
                       unewscale7[j]==38 or unewscale7[j]==40 or unewscale7[j]==43 or unewscale7[j]==45 or unewscale7[j]==47 or unewscale7[j]==50 or unewscale7[j]==52 or unewscale7[j]==55 or unewscale7[j]==57 or unewscale7[j]==59):
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "black"))\n'%unewscale7[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale7[j]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "white"))\n'%unewscale7[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale7[j]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale7[k]==2 or unewscale7[k]==4
                       or unewscale7[k]==7 or unewscale7[k]==9 or unewscale7[k]==11 or unewscale7[k]==14 or unewscale7[k]==16 or unewscale7[k]==19 or unewscale7[k]==21 or unewscale7[k]==23 or unewscale7[k]==26 or unewscale7[k]==28
                       or unewscale7[k]==31 or unewscale7[k]==33 or unewscale7[k]==35 or unewscale7[k]==38 or unewscale7[k]==40 or unewscale7[k]==43 or unewscale7[k]==45 or
                       unewscale7[k]==47 or unewscale7[k]==50 or unewscale7[k]==52 or unewscale7[k]==55 or unewscale7[k]==57 or unewscale7[k]==59):
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "black"))\n'%unewscale7[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale7[k]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale7.after(175, lambda: b%dscale7.config(bg = "white"))\n'%unewscale7[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale7,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale7[k]-1]))
                       f.write('   rootscale7.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count8=count8+1
                    f.write('b%dscale7%d%dscale7scale7=Button(cscale7,text="%d%d%d",command=c%d%dscale7scale7%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count8<21):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=300)\n'%(i,j,k,count8*50-45))
                    elif(count8>20 and count8<41):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=340)\n'%(i,j,k,count8*50-1045))
                    elif(count8>40 and count8<61):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=380)\n'%(i,j,k,count8*50-2045))
                    elif(count8>60 and count8<81):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=420)\n'%(i,j,k,count8*50-3045))
                    elif(count8>80 and count8<101):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=460)\n'%(i,j,k,count8*50-4045))
                        
                    elif(count8>100 and count8<121):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=500)\n'%(i,j,k,count8*50-5045))
                        
                    elif(count8>120 and count8<141):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=540)\n'%(i,j,k,count8*50-6045))
                    elif(count8>140 and count8<161):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=580)\n'%(i,j,k,count8*50-7045))
                    elif(count8>160 and count8<181):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=620)\n'%(i,j,k,count8*50-8045))
                    elif(count8>180 and count8<201):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=660)\n'%(i,j,k,count8*50-9045))   
                    elif(count8>200 and count8<221):
                        f.write('b%dscale7%d%dscale7scale7.place(x=%d,y=700)\n'%(i,j,k,count8*50-10045))
                        
                    if(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==3):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%s")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==4):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sm")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==5):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sI1")\n'%(i,j,k,notes1[unewscale7[k]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==4):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sI2")\n'%(i,j,k,notes1[unewscale7[j]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==5):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%smI1")\n'%(i,j,k,notes1[unewscale7[k]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==3):
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('b%dscale7%d%dscale7scale7.config(text="%smI2")\n'%(i,j,k,notes1[unewscale7[j]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==3):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sdim")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))

                    elif(unewscale7[j]-unewscale7[i]==3 and unewscale7[k]-unewscale7[j]==6):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale7[k]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==6 and unewscale7[k]-unewscale7[j]==3):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale7[j]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==4 and unewscale7[k]-unewscale7[j]==4):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%saug")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==2 and unewscale7[k]-unewscale7[j]==5):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==5):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale7[k]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
                    elif(unewscale7[j]-unewscale7[i]==5 and unewscale7[k]-unewscale7[j]==2):
                        f.write('b%dscale7%d%dscale7scale7.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale7[i]-1]))
                        f.write('b%dscale7%d%dscale7scale7.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale7=mainchordcounterscale7+1
                        f.write('def f%d%dscale7scale7%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale7scale7%d()\n'%(i,j,k))
                        f.write('   b%dscale7%d%dscale7scale7.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale7.after(175, lambda: b%dscale7%d%dscale7scale7.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale7.bind("<KeyPress-%s>", f%d%dscale7scale7%d)\n'%(keysforchords[mainchordcounterscale7-1],i,j,k))
###############################################Scale 8 begins
    f.write('rootscale8=Toplevel()\n')
    f.write('rootscale8.title("Ultimate piano-Scale 8")\n')
    f.write('rootscale8.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale8=0\n')
    f.write('cscale8=Canvas(rootscale8,bg="#b53b35")\n')
    f.write('cscale8.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale8=Label(cscale8,text="chord")\n')
    f.write('chordlabelscale8.place(x=200,y=200)\n')
    f.write('chordlabelscale8.config(font=("Courier", 44))\n')
    f.write('def thapscale8(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale8.bind("<KeyPress-space>", thapscale8) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale8,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale8,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale8=Canvas(cscale8,bg="white")\n')
    f.write('Fscale8.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale8,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale8,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale8,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale8,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale8,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale8,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale8scale8():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale8,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale8==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale8,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale8==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale8\n')
    f.write('   flagfornotemodescale8=1\n')
    f.write('   flagfornotemodescale8btn.config(bg="green")\n')
    f.write('   flagfornotemodescale8btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale8\n')
    f.write('   flagfornotemodescale8=0\n')
    f.write('   flagfornotemodescale8btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale8btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale8btn=Button(cscale8,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale8btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale8btn2=Button(cscale8,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale8btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale8[i-1]==2 or unewscale8[i-1]==4 or unewscale8[i-1]==7 or unewscale8[i-1]==9 or unewscale8[i-1]==11 or unewscale8[i-1]==14 or unewscale8[i-1]==16
           or unewscale8[i-1]==19 or unewscale8[i-1]==21 or unewscale8[i-1]==23 or unewscale8[i-1]==26 or unewscale8[i-1]==28 or unewscale8[i-1]==31 or unewscale8[i-1]==33
           or unewscale8[i-1]==35 or unewscale8[i-1]==38 or unewscale8[i-1]==40 or unewscale8[i-1]==43 or unewscale8[i-1]==45 or unewscale8[i-1]==47 or unewscale8[i-1]==50 or unewscale8[i-1]==52 or unewscale8[i-1]==55
           or unewscale8[i-1]==57 or unewscale8[i-1]==59):        
            f.write('def flashb%dscale8scale8(event):\n'%unewscale8[i-1])
            f.write('    b%dscale8.config(bg = "green")\n'%unewscale8[i-1])     
            f.write('    rootscale8.after(175, lambda: b%dscale8.config(bg = "black"))\n'%unewscale8[i-1])
            f.write('    d%dscale8scale8()\n'%unewscale8[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale8.bind("%s", flashb%dscale8scale8)\n'%(keys[i-1],unewscale8[i-1]))    
            else:
                f.write('rootscale8.bind("<KeyPress-%s>", flashb%dscale8scale8)\n'%(keys[i-1],unewscale8[i-1]))
        else:
            f.write('def flashb%dscale8scale8(event):\n'%unewscale8[i-1])
            f.write('    b%dscale8.config(bg = "green")\n'%unewscale8[i-1])     
            f.write('    rootscale8.after(175, lambda: b%dscale8.config(bg = "white"))\n'%unewscale8[i-1])
            f.write('    d%dscale8scale8()\n'%unewscale8[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale8.bind("%s", flashb%dscale8scale8)\n'%(keys[i-1],unewscale8[i-1]))    
            else:
                f.write('rootscale8.bind("<KeyPress-%s>", flashb%dscale8scale8)\n'%(keys[i-1],unewscale8[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale8=Button(cscale8,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale8scale8)\n'%(i,notes[i-1],i))
            f.write('b%dscale8.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale8=Button(cscale8,text="%s",bg="white",command=d%dscale8scale8)\n'%(i,notes[i-1],i))
            f.write('b%dscale8.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale8[i-1]==2 or unewscale8[i-1]==4 or unewscale8[i-1]==7 or unewscale8[i-1]==9 or unewscale8[i-1]==11 or
 unewscale8[i-1]==14 or unewscale8[i-1]==16 or unewscale8[i-1]==19 or unewscale8[i-1]==21 or unewscale8[i-1]==23 or
 unewscale8[i-1]==26 or unewscale8[i-1]==28 or unewscale8[i-1]==31 or unewscale8[i-1]==33 or unewscale8[i-1]==35 or
 unewscale8[i-1]==38 or unewscale8[i-1]==40 or unewscale8[i-1]==43 or unewscale8[i-1]==45 or unewscale8[i-1]==47 or
 unewscale8[i-1]==50 or unewscale8[i-1]==52 or unewscale8[i-1]==55 or unewscale8[i-1]==57 or unewscale8[i-1]==59):
            f.write('l%d=Label(cscale8,text="",bg="green")\n'%unewscale8[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale8[i-1],unewscale8[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale8,text="",bg="green")\n'%unewscale8[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale8[i-1],unewscale8[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale8scale8%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale8[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale8[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale8[k])
                    f.write('   b%dscale8.config(bg="green")\n'%(unewscale8[i]))
                    f.write('   b%dscale8.config(bg="green")\n'%(unewscale8[j]))
                    f.write('   b%dscale8.config(bg="green")\n'%(unewscale8[k]))                   
                    if(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==3):
                        f.write('   chordlabelscale8.config(text="%s")\n'%(notes1[unewscale8[i]-1]))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==4):
                        f.write('   chordlabelscale8.config(text="%sm")\n'%(notes1[unewscale8[i]-1]))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==5):
                        f.write('   chordlabelscale8.config(text="%s inv-1")\n'%(notes1[unewscale8[k]-1]))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==4):
                        f.write('   chordlabelscale8.config(text="%s inv-2")\n'%(notes1[unewscale8[j]-1]))
                    elif(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==5):
                        f.write('   chordlabelscale8.config(text="%sm inv-1")\n'%(notes1[unewscale8[k]-1]))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==3):
                        f.write('   chordlabelscale8.config(text="%sm inv-2")\n'%(notes1[unewscale8[j]-1]))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==3):
                        f.write('   chordlabelscale8.config(text="%sdim")\n'%(notes1[unewscale8[i]-1]))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==6):
                        f.write('   chordlabelscale8.config(text="%sdim inv1")\n'%(notes1[unewscale8[k]-1]))
                    elif(unewscale8[j]-unewscale8[i]==6 and unewscale8[k]-unewscale8[j]==3):
                        f.write('   chordlabelscale8.config(text="%sdim inv2")\n'%(notes1[unewscale8[j]-1]))
                    elif(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==4):
                        f.write('   chordlabelscale8.config(text="%saug")\n'%(notes1[unewscale8[i]-1]))
                    elif(unewscale8[j]-unewscale8[i]==2 and unewscale8[k]-unewscale8[j]==5):
                        f.write('   chordlabelscale8.config(text="%ssus2")\n'%(notes1[unewscale8[i]-1]))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==5):
                        f.write('   chordlabelscale8.config(text="%ssus2 inv1")\n'%(notes1[unewscale8[k]-1]))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==2):
                        f.write('   chordlabelscale8.config(text="%ssus4")\n'%(notes1[unewscale8[i]-1]))
                    if(unewscale8[i]==2 or unewscale8[i]==4 or unewscale8[i]==7 or unewscale8[i]==9 or unewscale8[i]==11
                       or unewscale8[i]==14 or unewscale8[i]==16 or unewscale8[i]==19 or unewscale8[i]==21 or unewscale8[i]==23 or unewscale8[i]==26 or unewscale8[i]==28 or unewscale8[i]==31 or unewscale8[i]==33
                       or unewscale8[i]==35 or unewscale8[i]==38 or unewscale8[i]==40 or unewscale8[i]==43 or unewscale8[i]==45 or unewscale8[i]==47 or unewscale8[i]==50 or unewscale8[i]==52 or unewscale8[i]==55
                       or unewscale8[i]==57 or unewscale8[i]==59):
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "black"))\n'%unewscale8[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale8[i]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "white"))\n'%unewscale8[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale8[i]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale8[j]==2 or unewscale8[j]==4 or unewscale8[j]==7 or unewscale8[j]==9 or unewscale8[j]==11 or unewscale8[j]==14 or unewscale8[j]==16 or unewscale8[j]==19 or unewscale8[j]==21 or
                       unewscale8[j]==23 or
                       unewscale8[j]==26 or unewscale8[j]==28 or unewscale8[j]==31 or unewscale8[j]==33 or unewscale8[j]==35 or
                       unewscale8[j]==38 or unewscale8[j]==40 or unewscale8[j]==43 or unewscale8[j]==45 or unewscale8[j]==47 or unewscale8[j]==50 or unewscale8[j]==52 or unewscale8[j]==55 or unewscale8[j]==57 or unewscale8[j]==59):
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "black"))\n'%unewscale8[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale8[j]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "white"))\n'%unewscale8[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale8[j]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale8[k]==2 or unewscale8[k]==4
                       or unewscale8[k]==7 or unewscale8[k]==9 or unewscale8[k]==11 or unewscale8[k]==14 or unewscale8[k]==16 or unewscale8[k]==19 or unewscale8[k]==21 or unewscale8[k]==23 or unewscale8[k]==26 or unewscale8[k]==28
                       or unewscale8[k]==31 or unewscale8[k]==33 or unewscale8[k]==35 or unewscale8[k]==38 or unewscale8[k]==40 or unewscale8[k]==43 or unewscale8[k]==45 or
                       unewscale8[k]==47 or unewscale8[k]==50 or unewscale8[k]==52 or unewscale8[k]==55 or unewscale8[k]==57 or unewscale8[k]==59):
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "black"))\n'%unewscale8[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale8[k]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale8.after(175, lambda: b%dscale8.config(bg = "white"))\n'%unewscale8[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale8,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale8[k]-1]))
                       f.write('   rootscale8.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count9=count9+1
                    f.write('b%dscale8%d%dscale8scale8=Button(cscale8,text="%d%d%d",command=c%d%dscale8scale8%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count9<21):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=300)\n'%(i,j,k,count9*50-45))
                    elif(count9>20 and count9<41):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=340)\n'%(i,j,k,count9*50-1045))
                    elif(count9>40 and count9<61):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=380)\n'%(i,j,k,count9*50-2045))
                    elif(count9>60 and count9<81):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=420)\n'%(i,j,k,count9*50-3045))
                    elif(count9>80 and count9<101):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=460)\n'%(i,j,k,count9*50-4045))
                        
                    elif(count9>100 and count9<121):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=500)\n'%(i,j,k,count9*50-5045))
                        
                    elif(count9>120 and count9<141):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=540)\n'%(i,j,k,count9*50-6045))
                    elif(count9>140 and count9<161):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=580)\n'%(i,j,k,count9*50-7045))
                    elif(count9>160 and count9<181):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=620)\n'%(i,j,k,count9*50-8045))
                    elif(count9>180 and count9<201):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=660)\n'%(i,j,k,count9*50-9045))   
                    elif(count9>200 and count9<221):
                        f.write('b%dscale8%d%dscale8scale8.place(x=%d,y=700)\n'%(i,j,k,count9*50-10045))
                        
                    if(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==3):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%s")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==4):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sm")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==5):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sI1")\n'%(i,j,k,notes1[unewscale8[k]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==4):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sI2")\n'%(i,j,k,notes1[unewscale8[j]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==5):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%smI1")\n'%(i,j,k,notes1[unewscale8[k]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==3):
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('b%dscale8%d%dscale8scale8.config(text="%smI2")\n'%(i,j,k,notes1[unewscale8[j]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==3):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sdim")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))

                    elif(unewscale8[j]-unewscale8[i]==3 and unewscale8[k]-unewscale8[j]==6):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale8[k]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==6 and unewscale8[k]-unewscale8[j]==3):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale8[j]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==4 and unewscale8[k]-unewscale8[j]==4):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%saug")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==2 and unewscale8[k]-unewscale8[j]==5):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==5):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale8[k]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
                    elif(unewscale8[j]-unewscale8[i]==5 and unewscale8[k]-unewscale8[j]==2):
                        f.write('b%dscale8%d%dscale8scale8.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale8[i]-1]))
                        f.write('b%dscale8%d%dscale8scale8.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale8=mainchordcounterscale8+1
                        f.write('def f%d%dscale8scale8%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale8scale8%d()\n'%(i,j,k))
                        f.write('   b%dscale8%d%dscale8scale8.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale8.after(175, lambda: b%dscale8%d%dscale8scale8.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale8.bind("<KeyPress-%s>", f%d%dscale8scale8%d)\n'%(keysforchords[mainchordcounterscale8-1],i,j,k))
##########################################scale 9################################################
    f.write('rootscale9=Toplevel()\n')
    f.write('rootscale9.title("Ultimate piano-Scale 9")\n')
    f.write('rootscale9.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale9=0\n')
    f.write('cscale9=Canvas(rootscale9,bg="#b53b35")\n')
    f.write('cscale9.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale9=Label(cscale9,text="chord")\n')
    f.write('chordlabelscale9.place(x=200,y=200)\n')
    f.write('chordlabelscale9.config(font=("Courier", 44))\n')
    f.write('def thapscale9(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale9.bind("<KeyPress-space>", thapscale9) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale9,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale9,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale9=Canvas(cscale9,bg="white")\n')
    f.write('Fscale9.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale9,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale9,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale9,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale9,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale9,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale9,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale9scale9():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale9,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale9==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale9,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale9==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale9\n')
    f.write('   flagfornotemodescale9=1\n')
    f.write('   flagfornotemodescale9btn.config(bg="green")\n')
    f.write('   flagfornotemodescale9btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale9\n')
    f.write('   flagfornotemodescale9=0\n')
    f.write('   flagfornotemodescale9btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale9btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale9btn=Button(cscale9,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale9btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale9btn2=Button(cscale9,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale9btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale9[i-1]==2 or unewscale9[i-1]==4 or unewscale9[i-1]==7 or unewscale9[i-1]==9 or unewscale9[i-1]==11 or unewscale9[i-1]==14 or unewscale9[i-1]==16
           or unewscale9[i-1]==19 or unewscale9[i-1]==21 or unewscale9[i-1]==23 or unewscale9[i-1]==26 or unewscale9[i-1]==28 or unewscale9[i-1]==31 or unewscale9[i-1]==33
           or unewscale9[i-1]==35 or unewscale9[i-1]==38 or unewscale9[i-1]==40 or unewscale9[i-1]==43 or unewscale9[i-1]==45 or unewscale9[i-1]==47 or unewscale9[i-1]==50 or unewscale9[i-1]==52 or unewscale9[i-1]==55
           or unewscale9[i-1]==57 or unewscale9[i-1]==59):        
            f.write('def flashb%dscale9scale9(event):\n'%unewscale9[i-1])
            f.write('    b%dscale9.config(bg = "green")\n'%unewscale9[i-1])     
            f.write('    rootscale9.after(175, lambda: b%dscale9.config(bg = "black"))\n'%unewscale9[i-1])
            f.write('    d%dscale9scale9()\n'%unewscale9[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale9.bind("%s", flashb%dscale9scale9)\n'%(keys[i-1],unewscale9[i-1]))    
            else:
                f.write('rootscale9.bind("<KeyPress-%s>", flashb%dscale9scale9)\n'%(keys[i-1],unewscale9[i-1]))
        else:
            f.write('def flashb%dscale9scale9(event):\n'%unewscale9[i-1])
            f.write('    b%dscale9.config(bg = "green")\n'%unewscale9[i-1])     
            f.write('    rootscale9.after(175, lambda: b%dscale9.config(bg = "white"))\n'%unewscale9[i-1])
            f.write('    d%dscale9scale9()\n'%unewscale9[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale9.bind("%s", flashb%dscale9scale9)\n'%(keys[i-1],unewscale9[i-1]))    
            else:
                f.write('rootscale9.bind("<KeyPress-%s>", flashb%dscale9scale9)\n'%(keys[i-1],unewscale9[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale9=Button(cscale9,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale9scale9)\n'%(i,notes[i-1],i))
            f.write('b%dscale9.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale9=Button(cscale9,text="%s",bg="white",command=d%dscale9scale9)\n'%(i,notes[i-1],i))
            f.write('b%dscale9.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale9[i-1]==2 or unewscale9[i-1]==4 or unewscale9[i-1]==7 or unewscale9[i-1]==9 or unewscale9[i-1]==11 or
 unewscale9[i-1]==14 or unewscale9[i-1]==16 or unewscale9[i-1]==19 or unewscale9[i-1]==21 or unewscale9[i-1]==23 or
 unewscale9[i-1]==26 or unewscale9[i-1]==28 or unewscale9[i-1]==31 or unewscale9[i-1]==33 or unewscale9[i-1]==35 or
 unewscale9[i-1]==38 or unewscale9[i-1]==40 or unewscale9[i-1]==43 or unewscale9[i-1]==45 or unewscale9[i-1]==47 or
 unewscale9[i-1]==50 or unewscale9[i-1]==52 or unewscale9[i-1]==55 or unewscale9[i-1]==57 or unewscale9[i-1]==59):
            f.write('l%d=Label(cscale9,text="",bg="green")\n'%unewscale9[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale9[i-1],unewscale9[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale9,text="",bg="green")\n'%unewscale9[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale9[i-1],unewscale9[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale9scale9%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale9[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale9[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale9[k])
                    f.write('   b%dscale9.config(bg="green")\n'%(unewscale9[i]))
                    f.write('   b%dscale9.config(bg="green")\n'%(unewscale9[j]))
                    f.write('   b%dscale9.config(bg="green")\n'%(unewscale9[k]))                   
                    if(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==3):
                        f.write('   chordlabelscale9.config(text="%s")\n'%(notes1[unewscale9[i]-1]))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==4):
                        f.write('   chordlabelscale9.config(text="%sm")\n'%(notes1[unewscale9[i]-1]))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==5):
                        f.write('   chordlabelscale9.config(text="%s inv-1")\n'%(notes1[unewscale9[k]-1]))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==4):
                        f.write('   chordlabelscale9.config(text="%s inv-2")\n'%(notes1[unewscale9[j]-1]))
                    elif(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==5):
                        f.write('   chordlabelscale9.config(text="%sm inv-1")\n'%(notes1[unewscale9[k]-1]))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==3):
                        f.write('   chordlabelscale9.config(text="%sm inv-2")\n'%(notes1[unewscale9[j]-1]))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==3):
                        f.write('   chordlabelscale9.config(text="%sdim")\n'%(notes1[unewscale9[i]-1]))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==6):
                        f.write('   chordlabelscale9.config(text="%sdim inv1")\n'%(notes1[unewscale9[k]-1]))
                    elif(unewscale9[j]-unewscale9[i]==6 and unewscale9[k]-unewscale9[j]==3):
                        f.write('   chordlabelscale9.config(text="%sdim inv2")\n'%(notes1[unewscale9[j]-1]))
                    elif(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==4):
                        f.write('   chordlabelscale9.config(text="%saug")\n'%(notes1[unewscale9[i]-1]))
                    elif(unewscale9[j]-unewscale9[i]==2 and unewscale9[k]-unewscale9[j]==5):
                        f.write('   chordlabelscale9.config(text="%ssus2")\n'%(notes1[unewscale9[i]-1]))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==5):
                        f.write('   chordlabelscale9.config(text="%ssus2 inv1")\n'%(notes1[unewscale9[k]-1]))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==2):
                        f.write('   chordlabelscale9.config(text="%ssus4")\n'%(notes1[unewscale9[i]-1]))
                    if(unewscale9[i]==2 or unewscale9[i]==4 or unewscale9[i]==7 or unewscale9[i]==9 or unewscale9[i]==11
                       or unewscale9[i]==14 or unewscale9[i]==16 or unewscale9[i]==19 or unewscale9[i]==21 or unewscale9[i]==23 or unewscale9[i]==26 or unewscale9[i]==28 or unewscale9[i]==31 or unewscale9[i]==33
                       or unewscale9[i]==35 or unewscale9[i]==38 or unewscale9[i]==40 or unewscale9[i]==43 or unewscale9[i]==45 or unewscale9[i]==47 or unewscale9[i]==50 or unewscale9[i]==52 or unewscale9[i]==55
                       or unewscale9[i]==57 or unewscale9[i]==59):
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "black"))\n'%unewscale9[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale9[i]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "white"))\n'%unewscale9[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale9[i]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale9[j]==2 or unewscale9[j]==4 or unewscale9[j]==7 or unewscale9[j]==9 or unewscale9[j]==11 or unewscale9[j]==14 or unewscale9[j]==16 or unewscale9[j]==19 or unewscale9[j]==21 or
                       unewscale9[j]==23 or
                       unewscale9[j]==26 or unewscale9[j]==28 or unewscale9[j]==31 or unewscale9[j]==33 or unewscale9[j]==35 or
                       unewscale9[j]==38 or unewscale9[j]==40 or unewscale9[j]==43 or unewscale9[j]==45 or unewscale9[j]==47 or unewscale9[j]==50 or unewscale9[j]==52 or unewscale9[j]==55 or unewscale9[j]==57 or unewscale9[j]==59):
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "black"))\n'%unewscale9[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale9[j]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "white"))\n'%unewscale9[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale9[j]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale9[k]==2 or unewscale9[k]==4
                       or unewscale9[k]==7 or unewscale9[k]==9 or unewscale9[k]==11 or unewscale9[k]==14 or unewscale9[k]==16 or unewscale9[k]==19 or unewscale9[k]==21 or unewscale9[k]==23 or unewscale9[k]==26 or unewscale9[k]==28
                       or unewscale9[k]==31 or unewscale9[k]==33 or unewscale9[k]==35 or unewscale9[k]==38 or unewscale9[k]==40 or unewscale9[k]==43 or unewscale9[k]==45 or
                       unewscale9[k]==47 or unewscale9[k]==50 or unewscale9[k]==52 or unewscale9[k]==55 or unewscale9[k]==57 or unewscale9[k]==59):
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "black"))\n'%unewscale9[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale9[k]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale9.after(175, lambda: b%dscale9.config(bg = "white"))\n'%unewscale9[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale9,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale9[k]-1]))
                       f.write('   rootscale9.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count10=count10+1
                    f.write('b%dscale9%d%dscale9scale9=Button(cscale9,text="%d%d%d",command=c%d%dscale9scale9%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count10<21):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=300)\n'%(i,j,k,count10*50-45))
                    elif(count10>20 and count10<41):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=340)\n'%(i,j,k,count10*50-1045))
                    elif(count10>40 and count10<61):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=380)\n'%(i,j,k,count10*50-2045))
                    elif(count10>60 and count10<81):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=420)\n'%(i,j,k,count10*50-3045))
                    elif(count10>80 and count10<101):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=460)\n'%(i,j,k,count10*50-4045))
                        
                    elif(count10>100 and count10<121):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=500)\n'%(i,j,k,count10*50-5045))
                        
                    elif(count10>120 and count10<141):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=540)\n'%(i,j,k,count10*50-6045))
                    elif(count10>140 and count10<161):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=580)\n'%(i,j,k,count10*50-7045))
                    elif(count10>160 and count10<181):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=620)\n'%(i,j,k,count10*50-8045))
                    elif(count10>180 and count10<201):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=660)\n'%(i,j,k,count10*50-9045))   
                    elif(count10>200 and count10<221):
                        f.write('b%dscale9%d%dscale9scale9.place(x=%d,y=700)\n'%(i,j,k,count10*50-10045))
                        
                    if(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==3):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%s")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==4):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sm")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==5):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sI1")\n'%(i,j,k,notes1[unewscale9[k]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==4):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sI2")\n'%(i,j,k,notes1[unewscale9[j]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==5):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%smI1")\n'%(i,j,k,notes1[unewscale9[k]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==3):
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('b%dscale9%d%dscale9scale9.config(text="%smI2")\n'%(i,j,k,notes1[unewscale9[j]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==3):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sdim")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))

                    elif(unewscale9[j]-unewscale9[i]==3 and unewscale9[k]-unewscale9[j]==6):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale9[k]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==6 and unewscale9[k]-unewscale9[j]==3):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale9[j]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==4 and unewscale9[k]-unewscale9[j]==4):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%saug")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==2 and unewscale9[k]-unewscale9[j]==5):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==5):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale9[k]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
                    elif(unewscale9[j]-unewscale9[i]==5 and unewscale9[k]-unewscale9[j]==2):
                        f.write('b%dscale9%d%dscale9scale9.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale9[i]-1]))
                        f.write('b%dscale9%d%dscale9scale9.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale9=mainchordcounterscale9+1
                        f.write('def f%d%dscale9scale9%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale9scale9%d()\n'%(i,j,k))
                        f.write('   b%dscale9%d%dscale9scale9.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale9.after(175, lambda: b%dscale9%d%dscale9scale9.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale9.bind("<KeyPress-%s>", f%d%dscale9scale9%d)\n'%(keysforchords[mainchordcounterscale9-1],i,j,k))
######################################################################scale 10 BEGINS                    
    f.write('rootscale10=Toplevel()\n')
    f.write('rootscale10.title("Ultimate piano-Scale 10")\n')
    f.write('rootscale10.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale10=0\n')
    f.write('cscale10=Canvas(rootscale10,bg="#b53b35")\n')
    f.write('cscale10.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale10=Label(cscale10,text="chord")\n')
    f.write('chordlabelscale10.place(x=200,y=200)\n')
    f.write('chordlabelscale10.config(font=("Courier", 44))\n')
    f.write('def thapscale10(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale10.bind("<KeyPress-space>", thapscale10) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale10,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale10,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale10=Canvas(cscale10,bg="white")\n')
    f.write('Fscale10.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale10,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale10,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale10,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale10,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale10,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale10,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale10scale10():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale10,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale10==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale10,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale10==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale10\n')
    f.write('   flagfornotemodescale10=1\n')
    f.write('   flagfornotemodescale10btn.config(bg="green")\n')
    f.write('   flagfornotemodescale10btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale10\n')
    f.write('   flagfornotemodescale10=0\n')
    f.write('   flagfornotemodescale10btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale10btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale10btn=Button(cscale10,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale10btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale10btn2=Button(cscale10,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale10btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale10[i-1]==2 or unewscale10[i-1]==4 or unewscale10[i-1]==7 or unewscale10[i-1]==9 or unewscale10[i-1]==11 or unewscale10[i-1]==14 or unewscale10[i-1]==16
           or unewscale10[i-1]==19 or unewscale10[i-1]==21 or unewscale10[i-1]==23 or unewscale10[i-1]==26 or unewscale10[i-1]==28 or unewscale10[i-1]==31 or unewscale10[i-1]==33
           or unewscale10[i-1]==35 or unewscale10[i-1]==38 or unewscale10[i-1]==40 or unewscale10[i-1]==43 or unewscale10[i-1]==45 or unewscale10[i-1]==47 or unewscale10[i-1]==50 or unewscale10[i-1]==52 or unewscale10[i-1]==55
           or unewscale10[i-1]==57 or unewscale10[i-1]==59):        
            f.write('def flashb%dscale10scale10(event):\n'%unewscale10[i-1])
            f.write('    b%dscale10.config(bg = "green")\n'%unewscale10[i-1])     
            f.write('    rootscale10.after(175, lambda: b%dscale10.config(bg = "black"))\n'%unewscale10[i-1])
            f.write('    d%dscale10scale10()\n'%unewscale10[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale10.bind("%s", flashb%dscale10scale10)\n'%(keys[i-1],unewscale10[i-1]))    
            else:
                f.write('rootscale10.bind("<KeyPress-%s>", flashb%dscale10scale10)\n'%(keys[i-1],unewscale10[i-1]))
        else:
            f.write('def flashb%dscale10scale10(event):\n'%unewscale10[i-1])
            f.write('    b%dscale10.config(bg = "green")\n'%unewscale10[i-1])     
            f.write('    rootscale10.after(175, lambda: b%dscale10.config(bg = "white"))\n'%unewscale10[i-1])
            f.write('    d%dscale10scale10()\n'%unewscale10[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale10.bind("%s", flashb%dscale10scale10)\n'%(keys[i-1],unewscale10[i-1]))    
            else:
                f.write('rootscale10.bind("<KeyPress-%s>", flashb%dscale10scale10)\n'%(keys[i-1],unewscale10[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale10=Button(cscale10,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale10scale10)\n'%(i,notes[i-1],i))
            f.write('b%dscale10.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale10=Button(cscale10,text="%s",bg="white",command=d%dscale10scale10)\n'%(i,notes[i-1],i))
            f.write('b%dscale10.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale10[i-1]==2 or unewscale10[i-1]==4 or unewscale10[i-1]==7 or unewscale10[i-1]==9 or unewscale10[i-1]==11 or
 unewscale10[i-1]==14 or unewscale10[i-1]==16 or unewscale10[i-1]==19 or unewscale10[i-1]==21 or unewscale10[i-1]==23 or
 unewscale10[i-1]==26 or unewscale10[i-1]==28 or unewscale10[i-1]==31 or unewscale10[i-1]==33 or unewscale10[i-1]==35 or
 unewscale10[i-1]==38 or unewscale10[i-1]==40 or unewscale10[i-1]==43 or unewscale10[i-1]==45 or unewscale10[i-1]==47 or
 unewscale10[i-1]==50 or unewscale10[i-1]==52 or unewscale10[i-1]==55 or unewscale10[i-1]==57 or unewscale10[i-1]==59):
            f.write('l%d=Label(cscale10,text="",bg="green")\n'%unewscale10[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale10[i-1],unewscale10[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale10,text="",bg="green")\n'%unewscale10[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale10[i-1],unewscale10[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale10scale10%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale10[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale10[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale10[k])
                    f.write('   b%dscale10.config(bg="green")\n'%(unewscale10[i]))
                    f.write('   b%dscale10.config(bg="green")\n'%(unewscale10[j]))
                    f.write('   b%dscale10.config(bg="green")\n'%(unewscale10[k]))                   
                    if(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==3):
                        f.write('   chordlabelscale10.config(text="%s")\n'%(notes1[unewscale10[i]-1]))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==4):
                        f.write('   chordlabelscale10.config(text="%sm")\n'%(notes1[unewscale10[i]-1]))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==5):
                        f.write('   chordlabelscale10.config(text="%s inv-1")\n'%(notes1[unewscale10[k]-1]))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==4):
                        f.write('   chordlabelscale10.config(text="%s inv-2")\n'%(notes1[unewscale10[j]-1]))
                    elif(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==5):
                        f.write('   chordlabelscale10.config(text="%sm inv-1")\n'%(notes1[unewscale10[k]-1]))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==3):
                        f.write('   chordlabelscale10.config(text="%sm inv-2")\n'%(notes1[unewscale10[j]-1]))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==3):
                        f.write('   chordlabelscale10.config(text="%sdim")\n'%(notes1[unewscale10[i]-1]))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==6):
                        f.write('   chordlabelscale10.config(text="%sdim inv1")\n'%(notes1[unewscale10[k]-1]))
                    elif(unewscale10[j]-unewscale10[i]==6 and unewscale10[k]-unewscale10[j]==3):
                        f.write('   chordlabelscale10.config(text="%sdim inv2")\n'%(notes1[unewscale10[j]-1]))
                    elif(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==4):
                        f.write('   chordlabelscale10.config(text="%saug")\n'%(notes1[unewscale10[i]-1]))
                    elif(unewscale10[j]-unewscale10[i]==2 and unewscale10[k]-unewscale10[j]==5):
                        f.write('   chordlabelscale10.config(text="%ssus2")\n'%(notes1[unewscale10[i]-1]))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==5):
                        f.write('   chordlabelscale10.config(text="%ssus2 inv1")\n'%(notes1[unewscale10[k]-1]))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==2):
                        f.write('   chordlabelscale10.config(text="%ssus4")\n'%(notes1[unewscale10[i]-1]))
                    if(unewscale10[i]==2 or unewscale10[i]==4 or unewscale10[i]==7 or unewscale10[i]==9 or unewscale10[i]==11
                       or unewscale10[i]==14 or unewscale10[i]==16 or unewscale10[i]==19 or unewscale10[i]==21 or unewscale10[i]==23 or unewscale10[i]==26 or unewscale10[i]==28 or unewscale10[i]==31 or unewscale10[i]==33
                       or unewscale10[i]==35 or unewscale10[i]==38 or unewscale10[i]==40 or unewscale10[i]==43 or unewscale10[i]==45 or unewscale10[i]==47 or unewscale10[i]==50 or unewscale10[i]==52 or unewscale10[i]==55
                       or unewscale10[i]==57 or unewscale10[i]==59):
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "black"))\n'%unewscale10[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale10[i]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "white"))\n'%unewscale10[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale10[i]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale10[j]==2 or unewscale10[j]==4 or unewscale10[j]==7 or unewscale10[j]==9 or unewscale10[j]==11 or unewscale10[j]==14 or unewscale10[j]==16 or unewscale10[j]==19 or unewscale10[j]==21 or
                       unewscale10[j]==23 or
                       unewscale10[j]==26 or unewscale10[j]==28 or unewscale10[j]==31 or unewscale10[j]==33 or unewscale10[j]==35 or
                       unewscale10[j]==38 or unewscale10[j]==40 or unewscale10[j]==43 or unewscale10[j]==45 or unewscale10[j]==47 or unewscale10[j]==50 or unewscale10[j]==52 or unewscale10[j]==55 or unewscale10[j]==57 or unewscale10[j]==59):
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "black"))\n'%unewscale10[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale10[j]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "white"))\n'%unewscale10[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale10[j]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale10[k]==2 or unewscale10[k]==4
                       or unewscale10[k]==7 or unewscale10[k]==9 or unewscale10[k]==11 or unewscale10[k]==14 or unewscale10[k]==16 or unewscale10[k]==19 or unewscale10[k]==21 or unewscale10[k]==23 or unewscale10[k]==26 or unewscale10[k]==28
                       or unewscale10[k]==31 or unewscale10[k]==33 or unewscale10[k]==35 or unewscale10[k]==38 or unewscale10[k]==40 or unewscale10[k]==43 or unewscale10[k]==45 or
                       unewscale10[k]==47 or unewscale10[k]==50 or unewscale10[k]==52 or unewscale10[k]==55 or unewscale10[k]==57 or unewscale10[k]==59):
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "black"))\n'%unewscale10[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale10[k]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale10.after(175, lambda: b%dscale10.config(bg = "white"))\n'%unewscale10[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale10,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale10[k]-1]))
                       f.write('   rootscale10.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count11=count11+1
                    f.write('b%dscale10%d%dscale10scale10=Button(cscale10,text="%d%d%d",command=c%d%dscale10scale10%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count11<21):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=300)\n'%(i,j,k,count11*50-45))
                    elif(count11>20 and count11<41):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=340)\n'%(i,j,k,count11*50-1045))
                    elif(count11>40 and count11<61):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=380)\n'%(i,j,k,count11*50-2045))
                    elif(count11>60 and count11<81):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=420)\n'%(i,j,k,count11*50-3045))
                    elif(count11>80 and count11<101):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=460)\n'%(i,j,k,count11*50-4045))
                        
                    elif(count11>100 and count11<121):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=500)\n'%(i,j,k,count11*50-5045))
                        
                    elif(count11>120 and count11<141):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=540)\n'%(i,j,k,count11*50-6045))
                    elif(count11>140 and count11<161):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=580)\n'%(i,j,k,count11*50-7045))
                    elif(count11>160 and count11<181):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=620)\n'%(i,j,k,count11*50-8045))
                    elif(count11>180 and count11<201):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=660)\n'%(i,j,k,count11*50-9045))   
                    elif(count11>200 and count11<221):
                        f.write('b%dscale10%d%dscale10scale10.place(x=%d,y=700)\n'%(i,j,k,count11*50-10045))
                        
                    if(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==3):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%s")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==4):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sm")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==5):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sI1")\n'%(i,j,k,notes1[unewscale10[k]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==4):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sI2")\n'%(i,j,k,notes1[unewscale10[j]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==5):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%smI1")\n'%(i,j,k,notes1[unewscale10[k]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==3):
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('b%dscale10%d%dscale10scale10.config(text="%smI2")\n'%(i,j,k,notes1[unewscale10[j]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==3):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sdim")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))

                    elif(unewscale10[j]-unewscale10[i]==3 and unewscale10[k]-unewscale10[j]==6):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale10[k]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==6 and unewscale10[k]-unewscale10[j]==3):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale10[j]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==4 and unewscale10[k]-unewscale10[j]==4):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%saug")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==2 and unewscale10[k]-unewscale10[j]==5):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==5):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale10[k]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
                    elif(unewscale10[j]-unewscale10[i]==5 and unewscale10[k]-unewscale10[j]==2):
                        f.write('b%dscale10%d%dscale10scale10.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale10[i]-1]))
                        f.write('b%dscale10%d%dscale10scale10.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale10=mainchordcounterscale10+1
                        f.write('def f%d%dscale10scale10%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale10scale10%d()\n'%(i,j,k))
                        f.write('   b%dscale10%d%dscale10scale10.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale10.after(175, lambda: b%dscale10%d%dscale10scale10.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale10.bind("<KeyPress-%s>", f%d%dscale10scale10%d)\n'%(keysforchords[mainchordcounterscale10-1],i,j,k))
################################################################scale 11#####################################
    f.write('rootscale11=Toplevel()\n')
    f.write('rootscale11.title("Ultimate piano-Scale 11")\n')
    f.write('rootscale11.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale11=0\n')
    f.write('cscale11=Canvas(rootscale11,bg="#b53b35")\n')
    f.write('cscale11.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale11=Label(cscale11,text="chord")\n')
    f.write('chordlabelscale11.place(x=200,y=200)\n')
    f.write('chordlabelscale11.config(font=("Courier", 44))\n')
    f.write('def thapscale11(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale11.bind("<KeyPress-space>", thapscale11) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale11,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale11,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale11=Canvas(cscale11,bg="white")\n')
    f.write('Fscale11.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale11,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale11,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale11,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale11,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale11,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale11,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale11scale11():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale11,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale11==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale11,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale11==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale11\n')
    f.write('   flagfornotemodescale11=1\n')
    f.write('   flagfornotemodescale11btn.config(bg="green")\n')
    f.write('   flagfornotemodescale11btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale11\n')
    f.write('   flagfornotemodescale11=0\n')
    f.write('   flagfornotemodescale11btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale11btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale11btn=Button(cscale11,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale11btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale11btn2=Button(cscale11,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale11btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale11[i-1]==2 or unewscale11[i-1]==4 or unewscale11[i-1]==7 or unewscale11[i-1]==9 or unewscale11[i-1]==11 or unewscale11[i-1]==14 or unewscale11[i-1]==16
           or unewscale11[i-1]==19 or unewscale11[i-1]==21 or unewscale11[i-1]==23 or unewscale11[i-1]==26 or unewscale11[i-1]==28 or unewscale11[i-1]==31 or unewscale11[i-1]==33
           or unewscale11[i-1]==35 or unewscale11[i-1]==38 or unewscale11[i-1]==40 or unewscale11[i-1]==43 or unewscale11[i-1]==45 or unewscale11[i-1]==47 or unewscale11[i-1]==50 or unewscale11[i-1]==52 or unewscale11[i-1]==55
           or unewscale11[i-1]==57 or unewscale11[i-1]==59):        
            f.write('def flashb%dscale11scale11(event):\n'%unewscale11[i-1])
            f.write('    b%dscale11.config(bg = "green")\n'%unewscale11[i-1])     
            f.write('    rootscale11.after(175, lambda: b%dscale11.config(bg = "black"))\n'%unewscale11[i-1])
            f.write('    d%dscale11scale11()\n'%unewscale11[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale11.bind("%s", flashb%dscale11scale11)\n'%(keys[i-1],unewscale11[i-1]))    
            else:
                f.write('rootscale11.bind("<KeyPress-%s>", flashb%dscale11scale11)\n'%(keys[i-1],unewscale11[i-1]))
        else:
            f.write('def flashb%dscale11scale11(event):\n'%unewscale11[i-1])
            f.write('    b%dscale11.config(bg = "green")\n'%unewscale11[i-1])     
            f.write('    rootscale11.after(175, lambda: b%dscale11.config(bg = "white"))\n'%unewscale11[i-1])
            f.write('    d%dscale11scale11()\n'%unewscale11[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale11.bind("%s", flashb%dscale11scale11)\n'%(keys[i-1],unewscale11[i-1]))    
            else:
                f.write('rootscale11.bind("<KeyPress-%s>", flashb%dscale11scale11)\n'%(keys[i-1],unewscale11[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale11=Button(cscale11,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale11scale11)\n'%(i,notes[i-1],i))
            f.write('b%dscale11.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale11=Button(cscale11,text="%s",bg="white",command=d%dscale11scale11)\n'%(i,notes[i-1],i))
            f.write('b%dscale11.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale11[i-1]==2 or unewscale11[i-1]==4 or unewscale11[i-1]==7 or unewscale11[i-1]==9 or unewscale11[i-1]==11 or
 unewscale11[i-1]==14 or unewscale11[i-1]==16 or unewscale11[i-1]==19 or unewscale11[i-1]==21 or unewscale11[i-1]==23 or
 unewscale11[i-1]==26 or unewscale11[i-1]==28 or unewscale11[i-1]==31 or unewscale11[i-1]==33 or unewscale11[i-1]==35 or
 unewscale11[i-1]==38 or unewscale11[i-1]==40 or unewscale11[i-1]==43 or unewscale11[i-1]==45 or unewscale11[i-1]==47 or
 unewscale11[i-1]==50 or unewscale11[i-1]==52 or unewscale11[i-1]==55 or unewscale11[i-1]==57 or unewscale11[i-1]==59):
            f.write('l%d=Label(cscale11,text="",bg="green")\n'%unewscale11[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale11[i-1],unewscale11[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale11,text="",bg="green")\n'%unewscale11[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale11[i-1],unewscale11[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale11scale11%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale11[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale11[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale11[k])
                    f.write('   b%dscale11.config(bg="green")\n'%(unewscale11[i]))
                    f.write('   b%dscale11.config(bg="green")\n'%(unewscale11[j]))
                    f.write('   b%dscale11.config(bg="green")\n'%(unewscale11[k]))                   
                    if(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==3):
                        f.write('   chordlabelscale11.config(text="%s")\n'%(notes1[unewscale11[i]-1]))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==4):
                        f.write('   chordlabelscale11.config(text="%sm")\n'%(notes1[unewscale11[i]-1]))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==5):
                        f.write('   chordlabelscale11.config(text="%s inv-1")\n'%(notes1[unewscale11[k]-1]))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==4):
                        f.write('   chordlabelscale11.config(text="%s inv-2")\n'%(notes1[unewscale11[j]-1]))
                    elif(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==5):
                        f.write('   chordlabelscale11.config(text="%sm inv-1")\n'%(notes1[unewscale11[k]-1]))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==3):
                        f.write('   chordlabelscale11.config(text="%sm inv-2")\n'%(notes1[unewscale11[j]-1]))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==3):
                        f.write('   chordlabelscale11.config(text="%sdim")\n'%(notes1[unewscale11[i]-1]))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==6):
                        f.write('   chordlabelscale11.config(text="%sdim inv1")\n'%(notes1[unewscale11[k]-1]))
                    elif(unewscale11[j]-unewscale11[i]==6 and unewscale11[k]-unewscale11[j]==3):
                        f.write('   chordlabelscale11.config(text="%sdim inv2")\n'%(notes1[unewscale11[j]-1]))
                    elif(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==4):
                        f.write('   chordlabelscale11.config(text="%saug")\n'%(notes1[unewscale11[i]-1]))
                    elif(unewscale11[j]-unewscale11[i]==2 and unewscale11[k]-unewscale11[j]==5):
                        f.write('   chordlabelscale11.config(text="%ssus2")\n'%(notes1[unewscale11[i]-1]))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==5):
                        f.write('   chordlabelscale11.config(text="%ssus2 inv1")\n'%(notes1[unewscale11[k]-1]))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==2):
                        f.write('   chordlabelscale11.config(text="%ssus4")\n'%(notes1[unewscale11[i]-1]))
                    if(unewscale11[i]==2 or unewscale11[i]==4 or unewscale11[i]==7 or unewscale11[i]==9 or unewscale11[i]==11
                       or unewscale11[i]==14 or unewscale11[i]==16 or unewscale11[i]==19 or unewscale11[i]==21 or unewscale11[i]==23 or unewscale11[i]==26 or unewscale11[i]==28 or unewscale11[i]==31 or unewscale11[i]==33
                       or unewscale11[i]==35 or unewscale11[i]==38 or unewscale11[i]==40 or unewscale11[i]==43 or unewscale11[i]==45 or unewscale11[i]==47 or unewscale11[i]==50 or unewscale11[i]==52 or unewscale11[i]==55
                       or unewscale11[i]==57 or unewscale11[i]==59):
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "black"))\n'%unewscale11[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale11[i]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "white"))\n'%unewscale11[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale11[i]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale11[j]==2 or unewscale11[j]==4 or unewscale11[j]==7 or unewscale11[j]==9 or unewscale11[j]==11 or unewscale11[j]==14 or unewscale11[j]==16 or unewscale11[j]==19 or unewscale11[j]==21 or
                       unewscale11[j]==23 or
                       unewscale11[j]==26 or unewscale11[j]==28 or unewscale11[j]==31 or unewscale11[j]==33 or unewscale11[j]==35 or
                       unewscale11[j]==38 or unewscale11[j]==40 or unewscale11[j]==43 or unewscale11[j]==45 or unewscale11[j]==47 or unewscale11[j]==50 or unewscale11[j]==52 or unewscale11[j]==55 or unewscale11[j]==57 or unewscale11[j]==59):
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "black"))\n'%unewscale11[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale11[j]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "white"))\n'%unewscale11[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale11[j]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale11[k]==2 or unewscale11[k]==4
                       or unewscale11[k]==7 or unewscale11[k]==9 or unewscale11[k]==11 or unewscale11[k]==14 or unewscale11[k]==16 or unewscale11[k]==19 or unewscale11[k]==21 or unewscale11[k]==23 or unewscale11[k]==26 or unewscale11[k]==28
                       or unewscale11[k]==31 or unewscale11[k]==33 or unewscale11[k]==35 or unewscale11[k]==38 or unewscale11[k]==40 or unewscale11[k]==43 or unewscale11[k]==45 or
                       unewscale11[k]==47 or unewscale11[k]==50 or unewscale11[k]==52 or unewscale11[k]==55 or unewscale11[k]==57 or unewscale11[k]==59):
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "black"))\n'%unewscale11[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale11[k]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale11.after(175, lambda: b%dscale11.config(bg = "white"))\n'%unewscale11[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale11,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale11[k]-1]))
                       f.write('   rootscale11.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count12=count12+1
                    f.write('b%dscale11%d%dscale11scale11=Button(cscale11,text="%d%d%d",command=c%d%dscale11scale11%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count12<21):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=300)\n'%(i,j,k,count12*50-45))
                    elif(count12>20 and count12<41):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=340)\n'%(i,j,k,count12*50-1045))
                    elif(count12>40 and count12<61):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=380)\n'%(i,j,k,count12*50-2045))
                    elif(count12>60 and count12<81):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=420)\n'%(i,j,k,count12*50-3045))
                    elif(count12>80 and count12<101):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=460)\n'%(i,j,k,count12*50-4045))
                        
                    elif(count12>100 and count12<121):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=500)\n'%(i,j,k,count12*50-5045))
                        
                    elif(count12>120 and count12<141):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=540)\n'%(i,j,k,count12*50-6045))
                    elif(count12>140 and count12<161):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=580)\n'%(i,j,k,count12*50-7045))
                    elif(count12>160 and count12<181):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=620)\n'%(i,j,k,count12*50-8045))
                    elif(count12>180 and count12<201):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=660)\n'%(i,j,k,count12*50-9045))   
                    elif(count12>200 and count12<221):
                        f.write('b%dscale11%d%dscale11scale11.place(x=%d,y=700)\n'%(i,j,k,count12*50-10045))
                        
                    if(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==3):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%s")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==4):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sm")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==5):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sI1")\n'%(i,j,k,notes1[unewscale11[k]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==4):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sI2")\n'%(i,j,k,notes1[unewscale11[j]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==5):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%smI1")\n'%(i,j,k,notes1[unewscale11[k]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==3):
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('b%dscale11%d%dscale11scale11.config(text="%smI2")\n'%(i,j,k,notes1[unewscale11[j]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==3):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sdim")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))

                    elif(unewscale11[j]-unewscale11[i]==3 and unewscale11[k]-unewscale11[j]==6):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale11[k]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==6 and unewscale11[k]-unewscale11[j]==3):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale11[j]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==4 and unewscale11[k]-unewscale11[j]==4):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%saug")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==2 and unewscale11[k]-unewscale11[j]==5):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==5):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale11[k]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
                    elif(unewscale11[j]-unewscale11[i]==5 and unewscale11[k]-unewscale11[j]==2):
                        f.write('b%dscale11%d%dscale11scale11.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale11[i]-1]))
                        f.write('b%dscale11%d%dscale11scale11.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale11=mainchordcounterscale11+1
                        f.write('def f%d%dscale11scale11%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale11scale11%d()\n'%(i,j,k))
                        f.write('   b%dscale11%d%dscale11scale11.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale11.after(175, lambda: b%dscale11%d%dscale11scale11.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale11.bind("<KeyPress-%s>", f%d%dscale11scale11%d)\n'%(keysforchords[mainchordcounterscale11-1],i,j,k))
################################################################SCALE 12################
    f.write('rootscale12=Toplevel()\n')
    f.write('rootscale12.title("Ultimate piano-Scale 12")\n')
    f.write('rootscale12.geometry("1360x700+0+0")\n')
    f.write('flagfornotemodescale12=0\n')
    f.write('cscale12=Canvas(rootscale12,bg="#b53b35")\n')
    f.write('cscale12.place(x=0,y=0,width=1360,height=700)\n')
    f.write('chordlabelscale12=Label(cscale12,text="chord")\n')
    f.write('chordlabelscale12.place(x=200,y=200)\n')
    f.write('chordlabelscale12.config(font=("Courier", 44))\n')
    f.write('def thapscale12(event):\n')
    f.write('   stopchannels()\n')
    f.write('   mixer.Channel(100).stop()\n')
    f.write('   mixer.Channel(101).stop()\n')
    f.write('   mixer.Channel(102).stop()\n')
    f.write('rootscale12.bind("<KeyPress-space>", thapscale12) \n')
    
    f.write('def stopchannels():\n')
    for i in range(1,61):
        f.write('    mixer.Channel(%d).stop()\n'%i)
    f.write('load = Image.open("Images/trebel.jpg")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale12,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=222)\n')
    f.write('load = Image.open("Images/bass.png")\n')
    f.write('render = ImageTk.PhotoImage(load)\n')
    f.write('img = Label(rootscale12,image=render)\n')
    f.write('img.image = render\n')
    f.write('img.place(x=1000, y=400)\n')
    
    f.write('Fscale12=Canvas(cscale12,bg="white")\n')
    f.write('Fscale12.place(x=1000,y=155,width=350,height=500)\n')
    for i in range(1,6):
        f.write('l%d=Label(Fscale12,text="",bg="black")\n'%i)
        f.write('l%d.place(x=100,y=%d,width=200,height=3)\n'%(i,255-i*29))
    for i in range(1,6):
        f.write('ln%d=Label(Fscale12,text="",bg="black")\n'%i)
        f.write('ln%d.place(x=90,y=%d,width=200,height=3)\n'%(i,446-i*29))
    for i in range(1,6):
        f.write('lp%d=Label(Fscale12,text="",bg="black")\n'%i)
        f.write('lp%d.place(x=130,y=%d,width=100,height=3)\n'%(i,110-i*19))
    for i in range(1,4):
        f.write('lk%d=Label(Fscale12,text="",bg="black")\n'%i)
        f.write('lk%d.place(x=130,y=%d,width=100,height=3)\n'%(i,leftlines[i-1]))
    for i in range(1,11):
        f.write('labbrstaffline%d=Label(Fscale12,text="%s",bg="white",font=40)\n'%(i,stafflines[i-1]))
        if(i<6):
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,433-i*29))
        else:
           f.write('labbrstaffline%d.place(x=300,y=%d)\n'%(i,388-i*29))
    for i in range(1,9):
        f.write('labbrstaffspace%d=Label(Fscale12,text="%s",bg="white",font=40)\n'%(i,staffspaces[i-1]))
        if(i<5):
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,420-i*29))
        else:
           f.write('labbrstaffspace%d.place(x=100,y=%d)\n'%(i,345-i*29))        
    for i in range(1,61):
        f.write('def d%dscale12scale12():\n'%i)
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26
           or i==28 or i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('   load = Image.open("Images/sharp.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale12,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale12==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
        else:
            f.write('   load = Image.open("Images/dot.png")\n')
            f.write('   render = ImageTk.PhotoImage(load)\n')
            f.write('   img%d = Label(rootscale12,image=render)\n'%i)
            f.write('   img%d.image = render\n'%i)
            f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[i-1]))
            f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%i)
            f.write('   if(flagfornotemodescale12==0):\n')
            f.write('      stopchannels()\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
            f.write('   else:\n')
            f.write('      mixer.Channel(%d).play(mixer.Sound("Audio/P%d.wav"))\n'%(i,i))
    f.write('def doublenotemode():\n')
    f.write('   global flagfornotemodescale12\n')
    f.write('   flagfornotemodescale12=1\n')
    f.write('   flagfornotemodescale12btn.config(bg="green")\n')
    f.write('   flagfornotemodescale12btn2.config(bg="SystemButtonFace")\n')
    f.write('def singlenotemode():\n')
    f.write('   global flagfornotemodescale12\n')
    f.write('   flagfornotemodescale12=0\n')
    f.write('   flagfornotemodescale12btn2.config(bg="green")\n')
    f.write('   flagfornotemodescale12btn.config(bg="SystemButtonFace")\n')
    f.write('flagfornotemodescale12btn=Button(cscale12,text="notemodedouble",command=doublenotemode)\n')
    f.write('flagfornotemodescale12btn.place(x=10,y=220)\n')
    f.write('flagfornotemodescale12btn2=Button(cscale12,text="notemodesingle",command=singlenotemode,bg="green")\n')
    f.write('flagfornotemodescale12btn2.place(x=10,y=250)\n')        
  
    for i in range(1,len(u)+1):
        if(unewscale12[i-1]==2 or unewscale12[i-1]==4 or unewscale12[i-1]==7 or unewscale12[i-1]==9 or unewscale12[i-1]==11 or unewscale12[i-1]==14 or unewscale12[i-1]==16
           or unewscale12[i-1]==19 or unewscale12[i-1]==21 or unewscale12[i-1]==23 or unewscale12[i-1]==26 or unewscale12[i-1]==28 or unewscale12[i-1]==31 or unewscale12[i-1]==33
           or unewscale12[i-1]==35 or unewscale12[i-1]==38 or unewscale12[i-1]==40 or unewscale12[i-1]==43 or unewscale12[i-1]==45 or unewscale12[i-1]==47 or unewscale12[i-1]==50 or unewscale12[i-1]==52 or unewscale12[i-1]==55
           or unewscale12[i-1]==57 or unewscale12[i-1]==59):        
            f.write('def flashb%dscale12scale12(event):\n'%unewscale12[i-1])
            f.write('    b%dscale12.config(bg = "green")\n'%unewscale12[i-1])     
            f.write('    rootscale12.after(175, lambda: b%dscale12.config(bg = "black"))\n'%unewscale12[i-1])
            f.write('    d%dscale12scale12()\n'%unewscale12[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale12.bind("%s", flashb%dscale12scale12)\n'%(keys[i-1],unewscale12[i-1]))    
            else:
                f.write('rootscale12.bind("<KeyPress-%s>", flashb%dscale12scale12)\n'%(keys[i-1],unewscale12[i-1]))
        else:
            f.write('def flashb%dscale12scale12(event):\n'%unewscale12[i-1])
            f.write('    b%dscale12.config(bg = "green")\n'%unewscale12[i-1])     
            f.write('    rootscale12.after(175, lambda: b%dscale12.config(bg = "white"))\n'%unewscale12[i-1])
            f.write('    d%dscale12scale12()\n'%unewscale12[i-1])
            if(keys[i-1]=='-'):
                f.write('rootscale12.bind("%s", flashb%dscale12scale12)\n'%(keys[i-1],unewscale12[i-1]))    
            else:
                f.write('rootscale12.bind("<KeyPress-%s>", flashb%dscale12scale12)\n'%(keys[i-1],unewscale12[i-1]))
    for i in range(1,61):
        if(i==2 or i==4 or i==7 or i==9 or i==11 or i==14 or i==16 or i==19 or i==21 or i==23 or i==26 or i==28 or
           i==31 or i==33 or i==35 or i==38 or i==40 or i==43 or i==45 or i==47 or i==50 or i==52 or i==55 or i==57 or i==59):
            f.write('b%dscale12=Button(cscale12,text="%s",wraplength=20,justify=LEFT,bg="black",fg="white",command=d%dscale12scale12)\n'%(i,notes[i-1],i))
            f.write('b%dscale12.place(x=%d,y=10,width=22,height=100)\n'%(i,i*22))
        else:
            f.write('b%dscale12=Button(cscale12,text="%s",bg="white",command=d%dscale12scale12)\n'%(i,notes[i-1],i))
            f.write('b%dscale12.place(x=%d,y=10,width=22,height=140)\n'%(i,i*22))

    for i in range(1,len(u)+1):
        if(unewscale12[i-1]==2 or unewscale12[i-1]==4 or unewscale12[i-1]==7 or unewscale12[i-1]==9 or unewscale12[i-1]==11 or
 unewscale12[i-1]==14 or unewscale12[i-1]==16 or unewscale12[i-1]==19 or unewscale12[i-1]==21 or unewscale12[i-1]==23 or
 unewscale12[i-1]==26 or unewscale12[i-1]==28 or unewscale12[i-1]==31 or unewscale12[i-1]==33 or unewscale12[i-1]==35 or
 unewscale12[i-1]==38 or unewscale12[i-1]==40 or unewscale12[i-1]==43 or unewscale12[i-1]==45 or unewscale12[i-1]==47 or
 unewscale12[i-1]==50 or unewscale12[i-1]==52 or unewscale12[i-1]==55 or unewscale12[i-1]==57 or unewscale12[i-1]==59):
            f.write('l%d=Label(cscale12,text="",bg="green")\n'%unewscale12[i-1])
            f.write('l%d.place(x=%d,y=80,width=10,height=10)\n'%(unewscale12[i-1],unewscale12[i-1]*22+5))
        else:
            f.write('l%d=Label(cscale12,text="",bg="green")\n'%unewscale12[i-1])
            f.write('l%d.place(x=%d,y=120,width=10,height=10)\n'%(unewscale12[i-1],unewscale12[i-1]*22+5))
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    f.write('def c%d%dscale12scale12%d():\n'%(i,j,k))
                    f.write('   mixer.Channel(100).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale12[i])
                    f.write('   mixer.Channel(101).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale12[j])
                    f.write('   mixer.Channel(102).play(mixer.Sound("Audio/P%d.wav"))\n'%unewscale12[k])
                    f.write('   b%dscale12.config(bg="green")\n'%(unewscale12[i]))
                    f.write('   b%dscale12.config(bg="green")\n'%(unewscale12[j]))
                    f.write('   b%dscale12.config(bg="green")\n'%(unewscale12[k]))                   
                    if(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==3):
                        f.write('   chordlabelscale12.config(text="%s")\n'%(notes1[unewscale12[i]-1]))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==4):
                        f.write('   chordlabelscale12.config(text="%sm")\n'%(notes1[unewscale12[i]-1]))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==5):
                        f.write('   chordlabelscale12.config(text="%s inv-1")\n'%(notes1[unewscale12[k]-1]))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==4):
                        f.write('   chordlabelscale12.config(text="%s inv-2")\n'%(notes1[unewscale12[j]-1]))
                    elif(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==5):
                        f.write('   chordlabelscale12.config(text="%sm inv-1")\n'%(notes1[unewscale12[k]-1]))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==3):
                        f.write('   chordlabelscale12.config(text="%sm inv-2")\n'%(notes1[unewscale12[j]-1]))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==3):
                        f.write('   chordlabelscale12.config(text="%sdim")\n'%(notes1[unewscale12[i]-1]))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==6):
                        f.write('   chordlabelscale12.config(text="%sdim inv1")\n'%(notes1[unewscale12[k]-1]))
                    elif(unewscale12[j]-unewscale12[i]==6 and unewscale12[k]-unewscale12[j]==3):
                        f.write('   chordlabelscale12.config(text="%sdim inv2")\n'%(notes1[unewscale12[j]-1]))
                    elif(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==4):
                        f.write('   chordlabelscale12.config(text="%saug")\n'%(notes1[unewscale12[i]-1]))
                    elif(unewscale12[j]-unewscale12[i]==2 and unewscale12[k]-unewscale12[j]==5):
                        f.write('   chordlabelscale12.config(text="%ssus2")\n'%(notes1[unewscale12[i]-1]))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==5):
                        f.write('   chordlabelscale12.config(text="%ssus2 inv1")\n'%(notes1[unewscale12[k]-1]))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==2):
                        f.write('   chordlabelscale12.config(text="%ssus4")\n'%(notes1[unewscale12[i]-1]))
                    if(unewscale12[i]==2 or unewscale12[i]==4 or unewscale12[i]==7 or unewscale12[i]==9 or unewscale12[i]==11
                       or unewscale12[i]==14 or unewscale12[i]==16 or unewscale12[i]==19 or unewscale12[i]==21 or unewscale12[i]==23 or unewscale12[i]==26 or unewscale12[i]==28 or unewscale12[i]==31 or unewscale12[i]==33
                       or unewscale12[i]==35 or unewscale12[i]==38 or unewscale12[i]==40 or unewscale12[i]==43 or unewscale12[i]==45 or unewscale12[i]==47 or unewscale12[i]==50 or unewscale12[i]==52 or unewscale12[i]==55
                       or unewscale12[i]==57 or unewscale12[i]==59):
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "black"))\n'%unewscale12[i])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale12[i]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%i)
                    else:
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "white"))\n'%unewscale12[i])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%i)
                       f.write('   img%d.image = render\n'%i)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(i,dotpos[unewscale12[i]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%i)
                    if(unewscale12[j]==2 or unewscale12[j]==4 or unewscale12[j]==7 or unewscale12[j]==9 or unewscale12[j]==11 or unewscale12[j]==14 or unewscale12[j]==16 or unewscale12[j]==19 or unewscale12[j]==21 or
                       unewscale12[j]==23 or
                       unewscale12[j]==26 or unewscale12[j]==28 or unewscale12[j]==31 or unewscale12[j]==33 or unewscale12[j]==35 or
                       unewscale12[j]==38 or unewscale12[j]==40 or unewscale12[j]==43 or unewscale12[j]==45 or unewscale12[j]==47 or unewscale12[j]==50 or unewscale12[j]==52 or unewscale12[j]==55 or unewscale12[j]==57 or unewscale12[j]==59):
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "black"))\n'%unewscale12[j])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale12[j]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%j)
                    else:
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "white"))\n'%unewscale12[j])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%j)
                       f.write('   img%d.image = render\n'%j)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(j,dotpos[unewscale12[j]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%j)                    
                    if(unewscale12[k]==2 or unewscale12[k]==4
                       or unewscale12[k]==7 or unewscale12[k]==9 or unewscale12[k]==11 or unewscale12[k]==14 or unewscale12[k]==16 or unewscale12[k]==19 or unewscale12[k]==21 or unewscale12[k]==23 or unewscale12[k]==26 or unewscale12[k]==28
                       or unewscale12[k]==31 or unewscale12[k]==33 or unewscale12[k]==35 or unewscale12[k]==38 or unewscale12[k]==40 or unewscale12[k]==43 or unewscale12[k]==45 or
                       unewscale12[k]==47 or unewscale12[k]==50 or unewscale12[k]==52 or unewscale12[k]==55 or unewscale12[k]==57 or unewscale12[k]==59):
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "black"))\n'%unewscale12[k])
                       f.write('   load = Image.open("Images/sharp.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale12[k]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%k)
                    else:
                       f.write('   rootscale12.after(175, lambda: b%dscale12.config(bg = "white"))\n'%unewscale12[k])
                       f.write('   load = Image.open("Images/dot.png")\n')
                       f.write('   render = ImageTk.PhotoImage(load)\n')
                       f.write('   img%d = Label(rootscale12,image=render)\n'%k)
                       f.write('   img%d.image = render\n'%k)
                       f.write('   img%d.place(x=1150, y=%d)\n'%(k,dotpos[unewscale12[k]-1]))
                       f.write('   rootscale12.after(175, lambda: img%d.place_forget())\n'%k)
    f.write('mixer.Channel(100).set_volume(0.5)\n')
    f.write('mixer.Channel(101).set_volume(0.5)\n')
    f.write('mixer.Channel(102).set_volume(0.5)\n')  
    for i in range(0,lu-1):
        for j in range(1,lu):
            for k in range(2,lu):
                if(i==j or j==k or k==i or j==lu-1 or i==lu-2 or i>j or i>k or j>k):
                    pass
                else:
                    count13=count13+1
                    f.write('b%dscale12%d%dscale12scale12=Button(cscale12,text="%d%d%d",command=c%d%dscale12scale12%d)\n'%(i,j,k,i,j,k,i,j,k))
                    if(count13<21):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=300)\n'%(i,j,k,count13*50-45))
                    elif(count13>20 and count13<41):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=340)\n'%(i,j,k,count13*50-1045))
                    elif(count13>40 and count13<61):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=380)\n'%(i,j,k,count13*50-2045))
                    elif(count13>60 and count13<81):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=420)\n'%(i,j,k,count13*50-3045))
                    elif(count13>80 and count13<101):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=460)\n'%(i,j,k,count13*50-4045))
                        
                    elif(count13>100 and count13<121):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=500)\n'%(i,j,k,count13*50-5045))
                        
                    elif(count13>120 and count13<141):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=540)\n'%(i,j,k,count13*50-6045))
                    elif(count13>140 and count13<161):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=580)\n'%(i,j,k,count13*50-7045))
                    elif(count13>160 and count13<181):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=620)\n'%(i,j,k,count13*50-8045))
                    elif(count13>180 and count13<201):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=660)\n'%(i,j,k,count13*50-9045))   
                    elif(count13>200 and count13<221):
                        f.write('b%dscale12%d%dscale12scale12.place(x=%d,y=700)\n'%(i,j,k,count13*50-10045))
                        
                    if(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==3):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%s")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==4):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sm")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==5):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sI1")\n'%(i,j,k,notes1[unewscale12[k]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==4):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sI2")\n'%(i,j,k,notes1[unewscale12[j]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==5):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%smI1")\n'%(i,j,k,notes1[unewscale12[k]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==3):
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('b%dscale12%d%dscale12scale12.config(text="%smI2")\n'%(i,j,k,notes1[unewscale12[j]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==3):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sdim")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))

                    elif(unewscale12[j]-unewscale12[i]==3 and unewscale12[k]-unewscale12[j]==6):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sdI1")\n'%(i,j,k,notes1[unewscale12[k]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==6 and unewscale12[k]-unewscale12[j]==3):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%sdI2")\n'%(i,j,k,notes1[unewscale12[j]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==4 and unewscale12[k]-unewscale12[j]==4):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%saug")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==2 and unewscale12[k]-unewscale12[j]==5):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%ssus2")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==5):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%ss2I1")\n'%(i,j,k,notes1[unewscale12[k]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
                    elif(unewscale12[j]-unewscale12[i]==5 and unewscale12[k]-unewscale12[j]==2):
                        f.write('b%dscale12%d%dscale12scale12.config(text="%ssus4")\n'%(i,j,k,notes1[unewscale12[i]-1]))
                        f.write('b%dscale12%d%dscale12scale12.config(bg="black",fg="white")\n'%(i,j,k))
                        mainchordcounterscale12=mainchordcounterscale12+1
                        f.write('def f%d%dscale12scale12%d(event):\n'%(i,j,k))
                        f.write('   c%d%dscale12scale12%d()\n'%(i,j,k))
                        f.write('   b%dscale12%d%dscale12scale12.config(bg="green")\n'%(i,j,k))
                        f.write('   rootscale12.after(175, lambda: b%dscale12%d%dscale12scale12.config(bg = "black"))\n'%(i,j,k))
                        f.write('rootscale12.bind("<KeyPress-%s>", f%d%dscale12scale12%d)\n'%(keysforchords[mainchordcounterscale12-1],i,j,k))
########################################################FUNCTION FOR TOPLEVEL#############
    f.write('def rootscale1toplevel():\n')
    f.write('   root.focus_set()\n')
    f.write('def rootscale2toplevel():\n')
    f.write('   rootscale2.focus_set()\n')
    f.write('def rootscale3toplevel():\n')
    f.write('   rootscale3.focus_set()\n')
    f.write('def rootscale4toplevel():\n')
    f.write('   rootscale4.focus_set()\n')
    f.write('def rootscale5toplevel():\n')
    f.write('   rootscale5.focus_set()\n')
    f.write('def rootscale6toplevel():\n')
    f.write('   rootscale6.focus_set()\n')
    f.write('def rootscale7toplevel():\n')
    f.write('   rootscale7.focus_set()\n')
    f.write('def rootscale8toplevel():\n')
    f.write('   rootscale8.focus_set()\n')
    f.write('def rootscale9toplevel():\n')
    f.write('   rootscale9.focus_set()\n')
    f.write('def rootscale10toplevel():\n')
    f.write('   rootscale10.focus_set()\n')
    f.write('def rootscale11toplevel():\n')
    f.write('   rootscale11.focus_set()\n')
    f.write('def rootscale12toplevel():\n')
    f.write('   rootscale12.focus_set()\n')
##############################################SCALE 1 screen navigation scale buttons
    f.write('rootscale1navigator1=Button(root,text="1",bg="green")\n')
    f.write('rootscale1navigator1.place(x=780,y=200)\n')
    f.write('rootscale1navigator2=Button(root,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale1navigator2.place(x=810,y=200)\n')
    f.write('rootscale1navigator3=Button(root,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale1navigator3.place(x=840,y=200)\n')
    f.write('rootscale1navigator4=Button(root,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale1navigator4.place(x=870,y=200)\n')
    f.write('rootscale1navigator5=Button(root,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale1navigator5.place(x=900,y=200)\n')
    f.write('rootscale1navigator6=Button(root,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale1navigator6.place(x=930,y=200)\n')

    f.write('rootscale1navigator7=Button(root,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale1navigator7.place(x=780,y=240)\n')
    f.write('rootscale1navigator8=Button(root,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale1navigator8.place(x=810,y=240)\n')
    f.write('rootscale1navigator9=Button(root,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale1navigator9.place(x=840,y=240)\n')
    f.write('rootscale1navigator10=Button(root,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale1navigator10.place(x=870,y=240)\n')
    f.write('rootscale1navigator11=Button(root,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale1navigator11.place(x=900,y=240)\n')
    f.write('rootscale1navigator12=Button(root,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale1navigator12.place(x=930,y=240)\n')
##############################################################SCALE 2 screen navigation scale buttons
    f.write('rootscale2navigator1=Button(rootscale2,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale2navigator1.place(x=780,y=200)\n')
    f.write('rootscale2navigator2=Button(rootscale2,text="2",bg="green")\n')
    f.write('rootscale2navigator2.place(x=810,y=200)\n')
    f.write('rootscale2navigator3=Button(rootscale2,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale2navigator3.place(x=840,y=200)\n')
    f.write('rootscale2navigator4=Button(rootscale2,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale2navigator4.place(x=870,y=200)\n')
    f.write('rootscale2navigator5=Button(rootscale2,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale2navigator5.place(x=900,y=200)\n')
    f.write('rootscale2navigator6=Button(rootscale2,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale2navigator6.place(x=930,y=200)\n')

    f.write('rootscale2navigator7=Button(rootscale2,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale2navigator7.place(x=780,y=240)\n')
    f.write('rootscale2navigator8=Button(rootscale2,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale2navigator8.place(x=810,y=240)\n')
    f.write('rootscale2navigator9=Button(rootscale2,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale2navigator9.place(x=840,y=240)\n')
    f.write('rootscale2navigator10=Button(rootscale2,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale2navigator10.place(x=870,y=240)\n')
    f.write('rootscale2navigator11=Button(rootscale2,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale2navigator11.place(x=900,y=240)\n')
    f.write('rootscale2navigator12=Button(rootscale2,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale2navigator12.place(x=930,y=240)\n')
###############################################################SCALE 3 screen navigation scale buttons
    f.write('rootscale3navigator1=Button(rootscale3,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale3navigator1.place(x=780,y=200)\n')
    f.write('rootscale3navigator2=Button(rootscale3,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale3navigator2.place(x=810,y=200)\n')
    f.write('rootscale3navigator3=Button(rootscale3,text="3",bg="green")\n')
    f.write('rootscale3navigator3.place(x=840,y=200)\n')
    f.write('rootscale3navigator4=Button(rootscale3,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale3navigator4.place(x=870,y=200)\n')
    f.write('rootscale3navigator5=Button(rootscale3,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale3navigator5.place(x=900,y=200)\n')
    f.write('rootscale3navigator6=Button(rootscale3,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale3navigator6.place(x=930,y=200)\n')

    f.write('rootscale3navigator7=Button(rootscale3,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale3navigator7.place(x=780,y=240)\n')
    f.write('rootscale3navigator8=Button(rootscale3,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale3navigator8.place(x=810,y=240)\n')
    f.write('rootscale3navigator9=Button(rootscale3,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale3navigator9.place(x=840,y=240)\n')
    f.write('rootscale3navigator10=Button(rootscale3,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale3navigator10.place(x=870,y=240)\n')
    f.write('rootscale3navigator11=Button(rootscale3,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale3navigator11.place(x=900,y=240)\n')
    f.write('rootscale3navigator12=Button(rootscale3,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale3navigator12.place(x=930,y=240)\n')
#########################################################scale4 nsb
    f.write('rootscale4navigator1=Button(rootscale4,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale4navigator1.place(x=780,y=200)\n')
    f.write('rootscale4navigator2=Button(rootscale4,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale4navigator2.place(x=810,y=200)\n')
    f.write('rootscale4navigator3=Button(rootscale4,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale4navigator3.place(x=840,y=200)\n')
    f.write('rootscale4navigator4=Button(rootscale4,text="4",bg="green")\n')
    f.write('rootscale4navigator4.place(x=870,y=200)\n')
    f.write('rootscale4navigator5=Button(rootscale4,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale4navigator5.place(x=900,y=200)\n')
    f.write('rootscale4navigator6=Button(rootscale4,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale4navigator6.place(x=930,y=200)\n')

    f.write('rootscale4navigator7=Button(rootscale4,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale4navigator7.place(x=780,y=240)\n')
    f.write('rootscale4navigator8=Button(rootscale4,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale4navigator8.place(x=810,y=240)\n')
    f.write('rootscale4navigator9=Button(rootscale4,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale4navigator9.place(x=840,y=240)\n')
    f.write('rootscale4navigator10=Button(rootscale4,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale4navigator10.place(x=870,y=240)\n')
    f.write('rootscale4navigator11=Button(rootscale4,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale4navigator11.place(x=900,y=240)\n')
    f.write('rootscale4navigator12=Button(rootscale4,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale4navigator12.place(x=930,y=240)\n')
########################################################SCALE 5 nsb
    f.write('rootscale5navigator1=Button(rootscale5,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale5navigator1.place(x=780,y=200)\n')
    f.write('rootscale5navigator2=Button(rootscale5,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale5navigator2.place(x=810,y=200)\n')
    f.write('rootscale5navigator3=Button(rootscale5,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale5navigator3.place(x=840,y=200)\n')
    f.write('rootscale5navigator4=Button(rootscale5,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale5navigator4.place(x=870,y=200)\n')
    f.write('rootscale5navigator5=Button(rootscale5,text="5",bg="green")\n')
    f.write('rootscale5navigator5.place(x=900,y=200)\n')
    f.write('rootscale5navigator6=Button(rootscale5,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale5navigator6.place(x=930,y=200)\n')

    f.write('rootscale5navigator7=Button(rootscale5,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale5navigator7.place(x=780,y=240)\n')
    f.write('rootscale5navigator8=Button(rootscale5,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale5navigator8.place(x=810,y=240)\n')
    f.write('rootscale5navigator9=Button(rootscale5,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale5navigator9.place(x=840,y=240)\n')
    f.write('rootscale5navigator10=Button(rootscale5,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale5navigator10.place(x=870,y=240)\n')
    f.write('rootscale5navigator11=Button(rootscale5,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale5navigator11.place(x=900,y=240)\n')
    f.write('rootscale5navigator12=Button(rootscale5,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale5navigator12.place(x=930,y=240)\n')
#########################################scale 6 nsb
    f.write('rootscale6navigator1=Button(rootscale6,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale6navigator1.place(x=780,y=200)\n')
    f.write('rootscale6navigator2=Button(rootscale6,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale6navigator2.place(x=810,y=200)\n')
    f.write('rootscale6navigator3=Button(rootscale6,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale6navigator3.place(x=840,y=200)\n')
    f.write('rootscale6navigator4=Button(rootscale6,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale6navigator4.place(x=870,y=200)\n')
    f.write('rootscale6navigator5=Button(rootscale6,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale6navigator5.place(x=900,y=200)\n')
    f.write('rootscale6navigator6=Button(rootscale6,text="6",bg="green")\n')
    f.write('rootscale6navigator6.place(x=930,y=200)\n')

    f.write('rootscale6navigator7=Button(rootscale6,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale6navigator7.place(x=780,y=240)\n')
    f.write('rootscale6navigator8=Button(rootscale6,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale6navigator8.place(x=810,y=240)\n')
    f.write('rootscale6navigator9=Button(rootscale6,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale6navigator9.place(x=840,y=240)\n')
    f.write('rootscale6navigator10=Button(rootscale6,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale6navigator10.place(x=870,y=240)\n')
    f.write('rootscale6navigator11=Button(rootscale6,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale6navigator11.place(x=900,y=240)\n')
    f.write('rootscale6navigator12=Button(rootscale6,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale6navigator12.place(x=930,y=240)\n')
###################################scale 7nsb
    f.write('rootscale7navigator1=Button(rootscale7,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale7navigator1.place(x=780,y=200)\n')
    f.write('rootscale7navigator2=Button(rootscale7,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale7navigator2.place(x=810,y=200)\n')
    f.write('rootscale7navigator3=Button(rootscale7,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale7navigator3.place(x=840,y=200)\n')
    f.write('rootscale7navigator4=Button(rootscale7,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale7navigator4.place(x=870,y=200)\n')
    f.write('rootscale7navigator5=Button(rootscale7,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale7navigator5.place(x=900,y=200)\n')
    f.write('rootscale7navigator6=Button(rootscale7,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale7navigator6.place(x=930,y=200)\n')

    f.write('rootscale7navigator7=Button(rootscale7,text="7",bg="green")\n')
    f.write('rootscale7navigator7.place(x=780,y=240)\n')
    f.write('rootscale7navigator8=Button(rootscale7,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale7navigator8.place(x=810,y=240)\n')
    f.write('rootscale7navigator9=Button(rootscale7,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale7navigator9.place(x=840,y=240)\n')
    f.write('rootscale7navigator10=Button(rootscale7,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale7navigator10.place(x=870,y=240)\n')
    f.write('rootscale7navigator11=Button(rootscale7,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale7navigator11.place(x=900,y=240)\n')
    f.write('rootscale7navigator12=Button(rootscale7,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale7navigator12.place(x=930,y=240)\n')
#########################scale8 nsb
    f.write('rootscale8navigator1=Button(rootscale8,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale8navigator1.place(x=780,y=200)\n')
    f.write('rootscale8navigator2=Button(rootscale8,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale8navigator2.place(x=810,y=200)\n')
    f.write('rootscale8navigator3=Button(rootscale8,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale8navigator3.place(x=840,y=200)\n')
    f.write('rootscale8navigator4=Button(rootscale8,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale8navigator4.place(x=870,y=200)\n')
    f.write('rootscale8navigator5=Button(rootscale8,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale8navigator5.place(x=900,y=200)\n')
    f.write('rootscale8navigator6=Button(rootscale8,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale8navigator6.place(x=930,y=200)\n')

    f.write('rootscale8navigator7=Button(rootscale8,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale8navigator7.place(x=780,y=240)\n')
    f.write('rootscale8navigator8=Button(rootscale8,text="8",bg="green")\n')
    f.write('rootscale8navigator8.place(x=810,y=240)\n')
    f.write('rootscale8navigator9=Button(rootscale8,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale8navigator9.place(x=840,y=240)\n')
    f.write('rootscale8navigator10=Button(rootscale8,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale8navigator10.place(x=870,y=240)\n')
    f.write('rootscale8navigator11=Button(rootscale8,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale8navigator11.place(x=900,y=240)\n')
    f.write('rootscale8navigator12=Button(rootscale8,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale8navigator12.place(x=930,y=240)\n')
###########################SCALE9 nsb
    f.write('rootscale9navigator1=Button(rootscale9,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale9navigator1.place(x=780,y=200)\n')
    f.write('rootscale9navigator2=Button(rootscale9,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale9navigator2.place(x=810,y=200)\n')
    f.write('rootscale9navigator3=Button(rootscale9,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale9navigator3.place(x=840,y=200)\n')
    f.write('rootscale9navigator4=Button(rootscale9,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale9navigator4.place(x=870,y=200)\n')
    f.write('rootscale9navigator5=Button(rootscale9,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale9navigator5.place(x=900,y=200)\n')
    f.write('rootscale9navigator6=Button(rootscale9,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale9navigator6.place(x=930,y=200)\n')

    f.write('rootscale9navigator7=Button(rootscale9,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale9navigator7.place(x=780,y=240)\n')
    f.write('rootscale9navigator8=Button(rootscale9,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale9navigator8.place(x=810,y=240)\n')
    f.write('rootscale9navigator9=Button(rootscale9,text="9",bg="green")\n')
    f.write('rootscale9navigator9.place(x=840,y=240)\n')
    f.write('rootscale9navigator10=Button(rootscale9,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale9navigator10.place(x=870,y=240)\n')
    f.write('rootscale9navigator11=Button(rootscale9,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale9navigator11.place(x=900,y=240)\n')
    f.write('rootscale9navigator12=Button(rootscale9,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale9navigator12.place(x=930,y=240)\n')
##########################scale 10 nsb
    f.write('rootscale10navigator1=Button(rootscale10,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale10navigator1.place(x=780,y=200)\n')
    f.write('rootscale10navigator2=Button(rootscale10,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale10navigator2.place(x=810,y=200)\n')
    f.write('rootscale10navigator3=Button(rootscale10,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale10navigator3.place(x=840,y=200)\n')
    f.write('rootscale10navigator4=Button(rootscale10,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale10navigator4.place(x=870,y=200)\n')
    f.write('rootscale10navigator5=Button(rootscale10,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale10navigator5.place(x=900,y=200)\n')
    f.write('rootscale10navigator6=Button(rootscale10,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale10navigator6.place(x=930,y=200)\n')

    f.write('rootscale10navigator7=Button(rootscale10,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale10navigator7.place(x=780,y=240)\n')
    f.write('rootscale10navigator8=Button(rootscale10,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale10navigator8.place(x=810,y=240)\n')
    f.write('rootscale10navigator9=Button(rootscale10,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale10navigator9.place(x=840,y=240)\n')
    f.write('rootscale10navigator10=Button(rootscale10,text="10",bg="green")\n')
    f.write('rootscale10navigator10.place(x=870,y=240)\n')
    f.write('rootscale10navigator11=Button(rootscale10,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale10navigator11.place(x=900,y=240)\n')
    f.write('rootscale10navigator12=Button(rootscale10,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale10navigator12.place(x=930,y=240)\n')
#############################scale 11 nsb
    f.write('rootscale11navigator1=Button(rootscale11,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale11navigator1.place(x=780,y=200)\n')
    f.write('rootscale11navigator2=Button(rootscale11,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale11navigator2.place(x=810,y=200)\n')
    f.write('rootscale11navigator3=Button(rootscale11,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale11navigator3.place(x=840,y=200)\n')
    f.write('rootscale11navigator4=Button(rootscale11,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale11navigator4.place(x=870,y=200)\n')
    f.write('rootscale11navigator5=Button(rootscale11,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale11navigator5.place(x=900,y=200)\n')
    f.write('rootscale11navigator6=Button(rootscale11,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale11navigator6.place(x=930,y=200)\n')

    f.write('rootscale11navigator7=Button(rootscale11,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale11navigator7.place(x=780,y=240)\n')
    f.write('rootscale11navigator8=Button(rootscale11,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale11navigator8.place(x=810,y=240)\n')
    f.write('rootscale11navigator9=Button(rootscale11,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale11navigator9.place(x=840,y=240)\n')
    f.write('rootscale11navigator10=Button(rootscale11,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale11navigator10.place(x=870,y=240)\n')
    f.write('rootscale11navigator11=Button(rootscale11,text="11",bg="green")\n')
    f.write('rootscale11navigator11.place(x=900,y=240)\n')
    f.write('rootscale11navigator12=Button(rootscale11,text="12",command=rootscale12toplevel)\n')
    f.write('rootscale11navigator12.place(x=930,y=240)\n')
#############################scale 12 nsb
    f.write('rootscale12navigator1=Button(rootscale12,text="1",command=rootscale1toplevel)\n')
    f.write('rootscale12navigator1.place(x=780,y=200)\n')
    f.write('rootscale12navigator2=Button(rootscale12,text="2",command=rootscale2toplevel)\n')
    f.write('rootscale12navigator2.place(x=810,y=200)\n')
    f.write('rootscale12navigator3=Button(rootscale12,text="3",command=rootscale3toplevel)\n')
    f.write('rootscale12navigator3.place(x=840,y=200)\n')
    f.write('rootscale12navigator4=Button(rootscale12,text="4",command=rootscale4toplevel)\n')
    f.write('rootscale12navigator4.place(x=870,y=200)\n')
    f.write('rootscale12navigator5=Button(rootscale12,text="5",command=rootscale5toplevel)\n')
    f.write('rootscale12navigator5.place(x=900,y=200)\n')
    f.write('rootscale12navigator6=Button(rootscale12,text="6",command=rootscale6toplevel)\n')
    f.write('rootscale12navigator6.place(x=930,y=200)\n')

    f.write('rootscale12navigator7=Button(rootscale12,text="7",command=rootscale7toplevel)\n')
    f.write('rootscale12navigator7.place(x=780,y=240)\n')
    f.write('rootscale12navigator8=Button(rootscale12,text="8",command=rootscale8toplevel)\n')
    f.write('rootscale12navigator8.place(x=810,y=240)\n')
    f.write('rootscale12navigator9=Button(rootscale12,text="9",command=rootscale9toplevel)\n')
    f.write('rootscale12navigator9.place(x=840,y=240)\n')
    f.write('rootscale12navigator10=Button(rootscale12,text="10",command=rootscale10toplevel)\n')
    f.write('rootscale12navigator10.place(x=870,y=240)\n')
    f.write('rootscale12navigator11=Button(rootscale12,text="11",command=rootscale11toplevel)\n')
    f.write('rootscale12navigator11.place(x=900,y=240)\n')
    f.write('rootscale12navigator12=Button(rootscale12,text="12",bg="green")\n')
    f.write('rootscale12navigator12.place(x=930,y=240)\n')
#################################
    f.write('rootscale1toplevel()\n')
################################
    f.write('def closewindows():\n')
    f.write('   root.destroy()\n')
    f.write('closewindows=Button(root,text="close all windows",command=closewindows)\n')
    f.write('closewindows.place(x=800,y=160)\n')

    
#################################
__import__('op')
a=0

