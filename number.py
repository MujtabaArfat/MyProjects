from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input()) 
    li=[]
    li =[str(i) for i in range(1,n+1)]
    s=""
    s=s.join(li)
    print(s)