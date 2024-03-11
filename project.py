
# import RPi.GPIO as GPIO
# import time, sys, os

# import serial
# from sklearn import datasets
# from sklearn import svm

# import datetime
# from time import sleep

# ser = serial.Serial("/dev/ttyS0",9600, timeout = 1)

# # Define GPIO to LCD mapping
# LCD_RS = 11
# LCD_E  = 9
# LCD_D4 = 10
# #LCD_D5 = 24
# #LCD_D6 = 23
# #LCD_D7 = 18
# LCD_D5 = 22
# LCD_D6 = 27
# LCD_D7 = 17

# led = 18


# GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
# GPIO.setup(LCD_E, GPIO.OUT)  # E
# GPIO.setup(LCD_RS, GPIO.OUT) # RS
# GPIO.setup(LCD_D4, GPIO.OUT) # DB4
# GPIO.setup(LCD_D5, GPIO.OUT) # DB5
# GPIO.setup(LCD_D6, GPIO.OUT) # DB6
# GPIO.setup(LCD_D7, GPIO.OUT) # DB7

# GPIO.setup(led, GPIO.OUT) # DB7

# train = 10
# data = datasets_load()
# clf = svm.SVC()
# clf = svm.SVC(gamma = 0.001, c = 100)


# def main():
#   lcd_init()
 
#   lcd_string("  Welcome To",LCD_LINE_1)
#   lcd_string("The project ",LCD_LINE_2)
#   time.sleep(1) # 700 milli second delay

#   GPIO.output(led, True) # LED
#   time.sleep(0.7) # 700 milli second delay
#   GPIO.output(led, False) # LED
#   time.sleep(0.7) # 700 milli second delay  
#   GPIO.output(led, True) # LED
#   time.sleep(0.7) # 700 milli second delay
#   GPIO.output(led, False) # LED
#   k = 0
  
#   hb = 0
#   ser.flush()
#   ser.flush()
#   ser.flush()
#   while True:
          

#         received_data = (str)(ser.readline())                   #read NMEA string received        
#         print "Data received"
#         if len(received_data) > 3:
#             print(received_data)
#             data = received_data.split(',')

#             temp = float(data[0])
#             turb = float(data[1])
#             tds = float(data[2])
#             ph = float(data[3])
            
#             stemp = data[0]+"DegC "+data[1]+"NTU";
#             string = data[2]+"PPM "+str(ph)+"pH";

#             lcd_byte(0x01, LCD_CMD)
#             lcd_string(stemp,LCD_LINE_1) commands.getoutput('hostname -I')
#             lcd_string(string,LCD_LINE_2) commands.getoutput('hostname -I')
#             time.sleep(1)
#             ser.write(received_data)
#             ser.write("\r\n")
            
#             if tds > 1:
                    
#                 lcd_byte(0x01, LCD_CMD)
#                 lcd_string("Water Quality:",LCD_LINE_1) #commands.getoutput('hostname -I')                
#                 data = datasets_load()  
#                 lcd_string("Analysing...",LCD_LINE_2) #commands.getoutput('hostname -I')
#                 train = clf.thrsh(55,50,400,range(6.5,13))
#                 pred = str(train, clf.pred(temp,turb,tds,ph))
                
#                 lcd_string(pred,LCD_LINE_2) #commands.getoutput('hostname -I')
#                 time.sleep(2)
                
#                 ser.flush()
#                 ser.flush()
#                 ser.flush()
                


#         time.sleep(0.3) # 700 milli second delay


# def lcd_init():
#   # Initialise display
#   lcd_byte(0x33,LCD_CMD) # 110011 Initialise
#   lcd_byte(0x32,LCD_CMD) # 110010 Initialise
#   lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
#   lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
#   lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
#   lcd_byte(0x01,LCD_CMD) # 000001 Clear display
#   time.sleep(E_DELAY)
 
# def lcd_byte(bits, mode):
#   # Send byte to data pins
#   # bits = data
#   # mode = True  for character
#   #        False for command
 
#   GPIO.output(LCD_RS, mode) # RS
 
#   # High bits
#   GPIO.output(LCD_D4, False)
#   GPIO.output(LCD_D5, False)
#   GPIO.output(LCD_D6, False)
#   GPIO.output(LCD_D7, False)
#   if bits&0x10==0x10:
#     GPIO.output(LCD_D4, True)
#   if bits&0x20==0x20:
#     GPIO.output(LCD_D5, True)
#   if bits&0x40==0x40:
#     GPIO.output(LCD_D6, True)
#   if bits&0x80==0x80:
#     GPIO.output(LCD_D7, True)
 
#   # Toggle 'Enable' pin
#   lcd_toggle_enable()
 
#   # Low bits
#   GPIO.output(LCD_D4, False)
#   GPIO.output(LCD_D5, False)
#   GPIO.output(LCD_D6, False)
#   GPIO.output(LCD_D7, False)
#   if bits&0x01==0x01:
#     GPIO.output(LCD_D4, True)
#   if bits&0x02==0x02:
#     GPIO.output(LCD_D5, True)
#   if bits&0x04==0x04:
#     GPIO.output(LCD_D6, True)
#   if bits&0x08==0x08:
#     GPIO.output(LCD_D7, True)
 
#   # Toggle 'Enable' pin
#   lcd_toggle_enable()
 
# def lcd_toggle_enable():
#   # Toggle enable
#   time.sleep(E_DELAY)
#   GPIO.output(LCD_E, True)
#   time.sleep(E_PULSE)
#   GPIO.output(LCD_E, False)
#   time.sleep(E_DELAY)
 
# def lcd_string(message,line):
#   # Send string to display
 
#   message = message.ljust(LCD_WIDTH," ")
 
#   lcd_byte(line, LCD_CMD)
 
#   for i in range(LCD_WIDTH):
#     lcd_byte(ord(message[i]),LCD_CHR)
 
# if __name__ == '__main__':
 
#   try:
#     main()
#   except KeyboardInterrupt:
#     pass
#   finally:
#     lcd_byte(0x01, LCD_CMD)
#     lcd_string("Please Restart...",LCD_LINE_1)
#     GPIO.cleanup()
      
def fun():
    return [23.5625,235.395,470.7904]
        


