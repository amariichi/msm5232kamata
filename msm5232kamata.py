# -*- coding: utf-8 -*-
import sys
import numpy as np
from scipy.stats import norm

def argumentsparser():
    usage = "Usage: python {}".format(__file__)
    arguments = sys.argv
    if len(arguments) > 1:
        return usage

if __name__ == '__main__' :
    if argumentsparser() is None :

        # normal distribution curve is used to simulate msm5232 output volume.        
        def dist(x):
            func = norm.pdf(x,1,5.8)*4000-23
            return func

        # an alternative curve
        #def tanh(x):
        #    a = 3
        #    b = 6.4/15
        #    tanh = ((np.exp(a - b*(x)) - 1)/(np.exp(a - b*(x)) + 1)/((np.exp(a)-1)/(np.exp(a)+1)) + 1)*100
        #    return tanh
        
        def wav1(x):
            xx = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            flip = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
            ans = flip[x]*dist(xx[x])
            return ans
        
        def wav2(x):
            xx = np.array([0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7])
            flip = np.array([-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1])
            ans = flip[x]*dist(xx[x])
            ans = ans*0.6
            return ans
        
        def wav4(x):
            xx = np.array([0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3])
            flip = np.array([-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,-1,-1,-1,1,1,1,1])
            ans = flip[x]*dist(xx[x])
            ans = ans*0.5
            return ans
        
        def wav8(x):
            xx = np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
            flip = np.array([-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,1])
            ans = flip[x]*dist(xx[x])
            ans = ans*0.45
            return ans
        
        def switch(num: int, n: int):
            if num & (1 << n):
                return 1
            return 0

        fout = open("MSM5232likeWaveTable.kamata_programs", mode="wb")

        fileheader1 = "000100004B616D617461000000000000" \
                      "00000000000000000000000000000000" \
                      "00000000000000000000000000000000" \
                      "00000000000000000000000000000000"

        fileheader15 = "0004000041000000DC3A000004000000" \
                       "00000000000400000F000000"
        
        tableheader1 = "02000000"
        tableheader2 = "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000"
        tableheader3 = "0102030405060708090A0B0C0D0E0F10" # some 16 bytes data (unknown)

        tableheader4 = "00000000000000000000000000000000" \
                       "00000000000000006F12033C00000000" \
                       "000000006F12833C0000000000000000" \
                       "6666E63E00000000000000000AD7A33D" \
                       "00000000000000000000003F00000000" \
                       "00000000000000000000000000000000" \
                       "0000003F000000000000000000000000" \
                       "00000000000000000000003F00000000" \
                       "00000000000000000000000000000000" \
                       "0000003F000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "000000000000003F0000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000000000000000" \
                       "00000000000000000000803F00000000" \
                       "00000000000000000000000000000000" \
                       "0000003F0000000000000000" # envelope data

        fout.write(bytes.fromhex(fileheader1))
        fout.write(bytes.fromhex(fileheader15))

        y = np.empty(32)        

        for i in range(1,16):
            
            for j in range(32):
                y[j] = switch(i,0)*wav1(j) + switch(i,1)*wav2(j) + switch(i,2)*wav4(j) + switch(i,3)*wav8(j)
            y = y * 127/max(max(y),-min(y))
            y = (y + 127)/254
            
            fout.write(bytes.fromhex(tableheader1)) 
            
            if i > 9 :
                number = i + 1
            else:
                number = i
            tablename = "MSM5232Tbl-".encode('utf-8', 'replace').hex() + str(number + 30)
            
            fout.write(bytes.fromhex(tablename))
            fout.write(bytes.fromhex(tableheader2))
            fout.write(bytes.fromhex(tableheader3))
            fout.write(bytes.fromhex(tableheader4))

            for j in range(32):
                tablevalue = y[j].astype("<f").tobytes()
                fout.write(tablevalue)
                fout.write(bytes.fromhex("0000000000000000"))

        fout.close()
        print("MSM5232likeWaveTable.kamata_programs has been created successfully.")

    else: 
        print(argumentsparser())