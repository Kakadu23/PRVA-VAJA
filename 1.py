import random
smer = random.randint(0,360)

if smer > 337.25 and smer < 22.5:
    print(smer, "sever")
elif smer > 292.5 and smer < 337.25:
    print(smer, "severo-zahod")
elif smer > 247.5 and smer < 292.5:
    print(smer, "zahod")
elif smer > 202.5 and smer < 247.5:
    print(smer, "jugo-zahod")
elif smer > 157.5 and smer < 202.5:
    print(smer, "jug")
elif smer > 112.5 and smer < 157.5:
    print(smer, "jugo-vzhod")
elif smer > 67.5 and smer < 112.5:
    print(smer, "vzhod")
else:
    print(smer, "severo.zvhod")
