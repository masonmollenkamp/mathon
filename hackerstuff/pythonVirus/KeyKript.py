from math import gcd

def genaratePair(p, q):
    #get mod
    n = (p * q)
    #Phi(n)
    m = int(((p-1)*(q-1))/gcd(p - 1, q - 1))

    #debugging
    print('p = ' + str(p))
    print('q = ' + str(q))
    print('n = ' + str(n))
    print('m = ' + str(m))
    #Finds encription key
    for e in range(2, m - 1):
        if gcd(e, m) == 1:
            #for every valid encription key find a decription key
            for d in range(1, n):
                if( (d * e) % m == 1):
                    return(str(d) +  "-" + str(e) + " mod " + str(n))

        
def ecdc(key1, key2, ed, text):
    if ed == "e":
        j = ""
        key = [key1, key2]
        for letter in text:
            j += (str((ord(letter) ** key[0]) % key[1]) + " ")
        return j               
    else:
        j = ""
        key = [key1, key2]
        for letter in text:
            x = (int(letter) ** key[0]) % key[1]
            j += chr(x) 
        return j  

def main():
    command = input("e = encription, d = decription, g = genKeyPair")
    if command == "g":
        print(genaratePair(int(input("prime number?")), int(input("prime number?"))))
    elif command == "e":
        print(ecdc(int(input("First part: ")), int(input("Second part: ")), input(), input("what text to encript").strip(" ").split(" ")))

if __name__ == "__main__":
    main()