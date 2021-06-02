# VM

#!/usr/bin/env python

import os
import sys

###############################################################################


class RSA(object) :

    def __init__ (self) :

        self.mylist = []

        self.e = 0

        self.d = 0

        self.N = 0


    ##

    ## inputFunc: reads in the number of entries from the user.

    ##            Then, read in those many values and add them to the list

    def inputFunc(self) :

        entries = int(input("Enter the number of messages: "))

        print("Enter the messages:")

        for k in range(0, entries) :

            x = int(input())

            self.mylist.append(x)

    ##

    ## printFunc: takes in a number and prints "message is " followed by the number

    ##

    def printFunc(self, number) :

        print("message is ", number)

    ##

    ##

    def is_prime(self, number) :

        if number < 2 :

            return False

        else :

            for k in range(2, number) :

                if (number % k) == 0 :

                    return False

            return True



    ##

    ## primeGen: take a minimum value as a parameter and then yield the next prime numbers

    def primeGen(self, min_value) :

        cnt = 0

        for num in range(min_value + 1, 4 * min_value) :

            if self.is_prime(num) :

                cnt += 1

                yield num

                if cnt == 2 :

                    break

 
    ##

    ## keyGen: read in a minimum value from the user. Then, use the primeGen generator to get

    ##         the next 2 prime numbers and generate the value N and the keys e and d.

    ##         Print e and N but not the other values

    def keyGen(self) :

        min_val = int(input("Enter the minimum value for the prime numbers: "))

        list = []

        for x in self.primeGen(min_val) :

            list.append(x)

 

        p = list[0]

        q = list[1]

        self.N = p * q

        phiN = self.Totient(p, q)
        for e in range(2, phiN) :
            if self.GCD(e, phiN) == 1 :

                break

 

        self.e = e
        self.d = self.mulinv(self.e, phiN)

 
        print("N is ", self.N)
        print("e is ", self.e)


    ##

    ## Greatest Common Divisor: gcd

    def GCD(self, x, y) :
        while y != 0 :
            x, y = y, x % y

        return x

 

 

    ##
    ## Lowest Common Multiple: lcm
    def LCM(self, x, y) :
        return (x * y ) / GCD(x, y)

 

 
    ##
    ## Euler's Totient function
    ## using Euler's product formula
    def Totient(self, p, q) :
        return (p - 1) * (q - 1)

 

 

    ##
    ## Extended Euclidean Algorithm
    ##
    def xgcd(self, a, b) :
        x, old_x = 0, 1
        y, old_y = 1, 0
        r, old_r = b, a
        while r != 0 :
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_x, x = x, old_x - quotient * x
            old_y, y = y, old_y - quotient * y
        return old_r, old_x, old_y

 

  
    ##
    ## return x such that (x * a) % b == 1
    ##
    def mulinv(self, a, b):
        g, x, y = self.xgcd(a, b)
        if g == 1:
            return x % b

 

 

    ##
    ## encrypt: takes in a number as a parameter and returns the RSA encrypted value of the number
    def encrypt(self, msg) :
        return pow(msg, self.e, self.N)

 

 

    ##
    ## decrypt: takes in an encrypted number as a parameter and returns the RSA decrypted value
    def decrypt (self, msg) :
        return pow(msg, self.d, self.N)

 

 

    ## encryptedMsg: decorator function for printFunc that will print "The encrypted " before the printed message
    def encryptedMsg(self, func) :
        def wrapper(number) :
            print("The encrypted", end = " ")
            func(number)
        return wrapper

 

 

    ##
    ## decryptedMsg: decorator function for printFunc that will print "The decrypted " before the printed message
    def decryptedMsg (self, func) :
        def wrapper(number) :
            print("The decrypted", end = " ")
            func(number)

 

        return wrapper

 

 

    ## messages: calls inputFunc and keyGen and then, uses an iterator to iterate through

    ##           the list and encrypts each of the numbers using the encrypt function.

    #            Store the results in another list. Then, go through the second list and

    #            print each encrypted number using the decorator for the encrypted message

    def messages(self) :
        self.inputFunc()
        self.keyGen()
        enc_list = []
        dec_list = []


        for x in self.mylist :
            enc_list.append(self.encrypt(x))
 

        for x in enc_list :
            dec_list.append(self.decrypt(x))


        for x in enc_list :
            self.encryptedMsg(self.printFunc)(x)



        for x in dec_list :
            self.decryptedMsg(self.printFunc)(x)

 

 

## end of class RSA

###############################################################################

##
##
##

def main() :
    ## Verify your results be decrypting each of the encrypted messages and checking if you get the old
    ## value back. Print the decrypted values using the decorator for the decrypted message

 
    ## In main, create an RSA object and call the messages function
    rsaObj = RSA()
    rsaObj.messages()


    return 1

 

 

#####################################################################


if __name__ == "__main__":
    main()
