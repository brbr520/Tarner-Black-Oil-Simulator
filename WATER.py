from math import *

def Cw(p, t, SGwater):
    S = 24.9942 * ((SGwater * 62.366 - 32.3237) ** 0.5 - 5.48127)
    return 1 / (7.033 * p + 0.5415 * S - 537 * t + 403300)

def Bw(p, t): 
#From McCain
#UNITS bbl/STB    
    vwt = -1.0001 * (10 ** -2) + 1.33391 * (10 ** -4) \
        * t + 5.50654 * (10 ** -7) * t ** 2
    vwp = -1.95301 * (10 ** -9) * p * t - 1.72834 * (10 ** -13) \
        * p ** 2 * t - 3.58922 * (10 ** -7) * p - 2.25341 * (10 ** -10) * p ** 2
    return (1 + vwt) * (1 + vwp)

def Viswater(p, t, SGwater): 
    # Salinity in Mg/L
    #inverse of fig 16-8 McCain
    #S = 24.9942 * ((SGwater * 62.366 - 32.3237) ** 0.5 - 5.48127)
    S = (-0.438603 + ((0.438603 ** 2) - 4 * 1.60074 * 10 ^ (-3) * (62.368 - SGwater ** 62.368)) ^ 0.5) / (2 * 1.60074 * 10 ** (-3))
    
    A0 = 109.574
    A1 = -8.40564
    A2 = 0.313314
    A3 = 0.00872213
    A = A0 + A1 * S + A2 * S ** 2 + A3 * S ** 3
    
    B0 = -1.12166
    B1 = 0.0263951
    B2 = -0.000679461
    B3 = -0.0000547119
    B4 = 0.00000155586
    B = B0 + B1 * S + B2 * S ** 2 + B3 * S ** 3 + B4 * S ** 4
    
    mu1 = A * t ** B
    return (0.9994 + 0.000040295 * p + 0.0000000031062 * p ** 2) * mu1


