
userinput = input("whats your guess?")

SLAYER = userinput 

SLAYER0 = SLAYER[0]
SLAYER1 = SLAYER[1]
SLAYER2 = SLAYER[2]
SLAYER3 = SLAYER[3]
SLAYER4 = SLAYER[4]
SLAYER5 = SLAYER[5]

SLAYERLIST = [SLAYER0,SLAYER1,SLAYER2,SLAYER3,SLAYER4,SLAYER5]
LAYERLIST = [SLAYER5,SLAYER0,SLAYER1,SLAYER2,SLAYER3,SLAYER4]

SLAYERstring = SLAYER0+SLAYER1+SLAYER2+SLAYER3+SLAYER4+SLAYER5
SLAYERstringtoint = int(SLAYERstring)
SLAYERstringtointinto3 = SLAYERstringtoint*3



LAYERSstring = SLAYER1+SLAYER2+SLAYER3+SLAYER4+SLAYER5+SLAYER0
LAYERSstringtoint = int(LAYERSstring)



final = (LAYERSstringtoint == SLAYERstringtointinto3)



print( str(LAYERSstringtoint) +" == "+ str(SLAYERstringtointinto3) + " -> " + str(final))
