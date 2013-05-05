from random import randrange as i;r,S,p,l,s,C,P,c,w = ("rock","Spock",
"paper","lizard","scissors","\nComputer","\nPlayer","chooses"," Wins!")
n2n,w = [r,S,p,l,s],["\nTie!",P+w,P+w,C+w,C+w]
def z(x):v = i(0, 5);print P,c,x,C,c,n2n[v]+"\n"+w[(n2n.index(x)- v)] 
z(r),z(S),z(p),z(l),z(s)