if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
   
    s1 = set(arr)
    sum = 0
    for i in s1:
        sum=sum+i
    den = len(s1)
    
    avg=sum/den
    print(avg)