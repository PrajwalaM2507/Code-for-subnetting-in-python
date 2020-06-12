def rangevlsm(hids,n):
    k=n[0]
    if k<=256:
        print("enter a Network ID of Class C (i.e IP ranging from 192-223). For example, 192.168.10.0")
    elif k>256 and k<=65536:
        print("enter an Network ID of Class B (i.e IP ranging from 128-191). For example, 129.10.0.0")
    else:
        print("enter an Network ID of Class A (i.e IP ranging from 1-127). For example, 10.0.0.0")
    nid=input("enter the network id:")
    f=0
    a=0
    b=0
    co=0
    k=0
    for x in hids:
        f=f+(2**int(x))
        #print("f is",f)
        if int(x)<=8:
            #nid=input("enter the network id for C class:")
            l=nid.split('.')
            l=l[:-1]
            l=".".join(l)
            NID=l+'.ho'
            #f=f+(2**int(x))
            while k<=f and f<=255:
                    xid=NID.replace('ho',str(k))
                    hid=NID.replace('ho',str(f-1))
                    k=f-1
                    print(xid+'-'+hid)
                    if k==f-1:
                        break
            k=k+1
        elif int(x)>=8 and int(x)<=16:
            #nid=input("enter the network id for B class:")
            l=nid.split('.')
            #print(l)
            l=l[:-2]
            #print(l)
            l=".".join(l)
            nid1=l+".ho1.ho2"
            while b<=255:
               NID=nid1.replace('ho1',str(b))
               #if co==0:
                 # k=0
               while k<=255:
                  nid2=NID.replace('ho2',str(k))
                  if co==f-(2**int(x)):
                     xid=nid2
                     #print("co is",co)
                     #print(nid2)
                  if co==f-1:
                     bid=nid2
                     print(xid+'-'+bid)
                     break
                  co=co+1 
                  k=k+1
               if k==256:
                  k=0
                  b=b+1
                  
               if co==f-1:
                  co=co+1
                  k=k+1
                  #nid=bid
                  break
        elif int(x)>=16 and int(x)<=24:
            #nid=input("enter the network id for A class :")
            l=nid.split('.')
            l=l[:-3]
            l=".".join(l)
            nid1=l+".ho1.ho2.ho3"
            while a<=255:
                NID=nid1.replace('ho1',str(a))
                while b<=255:
                    NID1=NID.replace('ho2',str(b))
                    while k<=255:
                        nid2=NID1.replace('ho3',str(k))
                        if co==f-(2**int(x)):
                            xid=nid2
                        if co==f-1:
                            bid=nid2
                            print(xid+'-'+bid)
                            break
                        co=co+1
                        k=k+1
                    if k==256:
                        k=0
                        b=b+1
                    if co==f-1:
                        k=k+1
                        break
                if b==256:
                    b=0
                    a=a+1
                if co==f-1:
                    co=co+1
                    break
    print("In every network range the first IP is network ID , last IP is Broadcast ID and all the IPs in between are Usable IPs")
def ranges(h,n):
    if n<=256:
        print("enter a Network ID of Class C (i.e IP ranging from 192-223). For example, 192.168.10.0")
    elif n>256 and n<=65536:
        print("enter an Network ID of Class B (i.e IP ranging from 128-191). For example, 129.10.0.0")
    else:
        print("enter an Network ID of Class A (i.e IP ranging from 1-127). For example, 10.0.0.0")
    nid=input("enter the Network id:")
    a=0
    b=0
    co=0
    k=0
    if h<=8:
        l=nid.split('.')
        l=l[:-1]
        l=".".join(l)
        NID=l+'.ho'
        while k<255:
            if (k+(2**h)-1)<=255:
                xid=NID.replace('ho',str(k))
                hid=NID.replace('ho',str(k+(2**h)-1))
                print(xid+'-'+hid)
            k=k+(2**h)
    elif h>=8 and h<=16:
        l=nid.split('.')
        l=l[:-2]
        l=".".join(l)
        nid1=l+".ho1.ho2"
        n=1
        while b<=255:
            NID=nid1.replace('ho1',str(b))
            while k<=255:
                nid2=NID.replace('ho2',str(k))
                if co%(2**h)==0:
                    xid=nid2
                if co==n*(2**h)-1:
                    hid=nid2
                    print(xid+'-'+hid)
                    n=n+1
                co=co+1
                k=k+1
            if k==256:
                k=0
                b=b+1
    elif h>=16and h<=24:
        l=nid.split('.')
        l=l[:-3]
        l=".".join(l)
        nid1=l+".ho1.ho2.ho3"
        n=1
        while a<=255:
            NID=nid1.replace('ho1',str(a))
            while b<=255:
                NID1=NID.replace('ho2',str(b))
                while k<=255:
                    nid2=NID1.replace('ho3',str(k))
                    if co%(2**h)==0:
                        xid=nid2
                    if co==n*(2**h)-1:
                        bid=nid2
                        print(xid+'-'+bid)
                        n=n+1
                    co=co+1
                    k=k+1
                if k==256:
                    k=0
                    b=b+1
            if b==256:
                b=0
                a=a+1
    print("In every network range the first IP is network ID , last IP is Broadcast ID and all the IPs in between are Usable IPs")
   
def nearest(n): 
    count = 0;
    t=n
    while t != 0: 
        count=count+1
        t >>= 1
    return count
def subnetmask(n,h):
    s=0
    s1=0
    s2=0
    if n<255 or n==255:
        k=h
        while k<=7:
            s=s+2**k
            k=k+1
        return("255.255.255."+str(s))
    elif n<65536 and n>255:
        if h>8:
            k=h-8
            while k<=7:
                s1=s1+2**k
                k=k+1
            return("255.255."+str(s1)+".0")
        elif h<8:
            k=h
            while k<7 or k==7:
                s1=s1+2**k
                k=k+1
            return("255.255.255."+str(s1))
        elif h==8:
            return("255.255.255.0")
    elif n>65536:
        if h>16:
            k=h-16
            while k<7 or k==7:
                s2=s2+2**k
                k=k+1
            return("255."+str(s2)+".0.0")
        elif h<16 and h>8:
            while k<7 or k==7:
                s2=s2+2**k
                k=k+1
            return("255.255."+str(s1)+".0")
        elif h<8:
            k=h
            while k<7 or k==7:
                s2=s2+2**k
                k=k+1
            return("255.255.255."+str(s2))
        elif h==16 or h==8:
            return("255.255.0.0")
def networks(h):
    if h<=8:
        h=8-h
        return 2**h
    elif h>8 and h<=16:
        h=16-h
        return 2**h
    elif h>16 and h<=24:
        h=24-h
        return 2**h
    elif h>24 and h<=32:
        h=32-h
        return 2**h
def subnetbinary(s):
    l=s.split('.')
    b=[]
    for i in l:
        b.append(str(decToBinary(int(i))))
    k=".".join(b)
    return k
def decToBinary(n): 
      
    # array to store 
    # binary number 
    binaryNum = [0] * n 
  
    # counter for binary array 
    i = 0
    if n==0:
        return "00000000"
    else:
        while (n != 0):
            binaryNum[i] = n % 2
            n = int(n / 2)
            i += 1
        b=[]
        j=i-1
        while j>=0:
            b.append(str(binaryNum[j]))
            j=j-1
        x="".join(b)
        return x
print("This program is used for Subnetting IP adresses as per your requirement.")
print("There are 2 types of Subnetting : (1)Fixed Length Subnet Mask(FLSM)  and (2)Variable Length Subnet Mask(VLSM)")
print("If you require fixed number of IPs in all networks, then enter 'FLSM'")
print("If you require variable number of IPs in each network,then enter 'VLSM'")
print(end="\n")
print(end="\n")
print(end="\n")
s=input("What Subnetting would you prefer? (FLSM or VLSM)")
if s=='FLSM' or s=='flsm':
    n=int(input("What is the ip requirement?(enter number of ip's you need)"))
    h=nearest(n)
    net=networks(h)
    print("Prefix length",32-h)
    print ("Number of networks:",net)
    print("Number of hosts:",2**h)
    s=subnetmask(n,h)
    print("SUBNETMASK:",s)
    print(subnetbinary(s))
    r=input("Do you want range ? (Y/N) :")
    if r=='Y' or r=='y':
        #print("In every network range the first IP is network ID , last IP is Broadcast ID and all the IPs in between are Usable IPs")
        ranges(h,n)
else:
    print("What are the ip requirements?(required number of ips in descending order): ",end=" ")
    n=list(map(int,input().split()))
    l=[]
    for k in n:
        h=nearest(k)
        l.append(h)
        net=networks(h)
        print("Prefix length",32-h,end=" ")
        print ("Number of networks:",net,end=" ")
        print("Number of hosts:",2**h,end=" ")
        s=subnetmask(k,h)
        print("SUBNETMASK:",s)
        print(subnetbinary(s))
    r=input("Do you want range ? (Y/N) :")
    if r=='Y' or r=='y':
        #print("In every network range the first IP is network ID , last IP is Broadcast ID and all the IPs in between are Usable IPs")
        rangevlsm(l,n)

        
