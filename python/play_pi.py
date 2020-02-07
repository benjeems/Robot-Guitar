#!/usr/bin/python
# Playing 1000 decimal points of pi on a guitar  
#             |                      |
#             |   Strings plucked    |
#              \  E  A  D  G  B  e  /
# Digit of pi:  \__________________/
#           1     |  |  |  |  |  *
#           2     |  |  |  |  *  |
#           3     |  |  |  *  |  |
#           4     |  |  *  |  |  |
#           5     |  *  |  |  |  |
#           6     *  |  |  |  |  *
#           7     *  |  |  |  *  |
#           8     *  |  |  *  |  |
#           9     *  |  *  |  |  |
#           0     *  *  |  |  |  |
#                 |  |  |  |  |  |
import sys
import glob
import serial
from time import sleep

arduino_serial_id = glob.glob("/dev/ttyACM*")[0]
ser = serial.Serial(arduino_serial_id , 9600)
pi_1000 = 141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198
print(pi_1000)
pi = ((str(pi_1000)[:(int(sys.argv[1]))]))
#pi = '0987654321'
wait = 2
print('')
print "Now playing pi!"


# Play the 3 before the trailing decimals
print"3"
ser.write(str(3).encode())
sleep(wait)


count = 0
for digit in pi:
    digit = int(digit)
    print(digit)
    if (digit != 0 and digit < 6):
        # Digits 5,4,3,2,1 are played as a single note on strings:
        #        A,D,G,B,e
        ser.write(str(6 - digit).encode())

    elif(digit ==0 or digit > 5):
        # Digits 0,9,8,7,6 are played as two notes on strings:
        #        A,D,G,B,e
        #    and E,E,E,E,E
        # i/e the playing of the deep E signifies this is a digit > 5
        # This is the deep E note
        ser.write('0')
        # This is the corresponding digit note
        if (digit == 0):
            ser.write('1')
        else:
            ser.write(str(11 - digit).encode())
    if count < 5:
        sleep(wait)
    elif count < 20 :
        sleep(wait/2)
    elif count < 30:
        sleep(wait/4)
    else:
        # Include a minumum sleep, to allow servos to complete the note
        sleep(0.05)
    count += 1
