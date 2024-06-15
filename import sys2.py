import sys
def calc(g):
    W_Ko=0
    W_Ks=0
    D = 0
    for ge in g:
        kom,ksm=ge.split()
        if kom==ksm:
            D+=1
        elif (kom=='R' and ksm=="S") or (kom=="S" and ksm=="P") or (kom=="P" and ksm=="R"):
            W_Ko+=1
        else:
            W_Ks+=1
    totalg=len(g)
    if W_Ko>W_Ks:
        winner = "Костя"
    elif W_Ks>W_Ko:
        winner="Ксюша"
    else:
        winner="Ничья"
    if totalg>0:
        perc_W_Kost=(W_Ko/totalg)*100
        perc_W_Ksu=(W_Ks/totalg)*100
        perc_D=(D/totalg)*100
    else:
        perc_W_Kost=0
        perc_W_Ksu=0
        perc_D=0

    print(winner)
    print(f"W: {perc_W_Kost:.2f}%")
    print(f"D: {perc_D:.2f}%")
    print(f"L: {perc_W_Ksu:.2f}%")
inputd=sys.stdin.read().strip().splitlines()
calc(inputd)