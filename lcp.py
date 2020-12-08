import sys
import sys
# make sure module is in the path
sys.path.append('/home/pi/lcd')
import lcd
import RPi.GPIO as GPIO
import time
# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11
ticket = 0
cmd_beg = 'espeak '
btnPin = 17 


while 1:
    #if button not pressed do something
    if btnPin.NotClicked:
        #if button is pressed 
        ticket=ticket+1
    else :
        #if button is pressed 
        ticket=ticket+1
        text  = "ticket numero"+ticket+" va au gichet "+gichet
        call([cmd_beg+text]) 
        #ticket  = input('Entrer le numero de ticket : ') 
        #gichet  = input('Entrer le numero de gichet : ') 
        lcd.lcd_init()
        # set cursor to line 1
        lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
        # display text centered on line 1
        lcd.lcd_string("Raspberry Pi", 2)
        #  set cursor to line 2
        # lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        #  display additional text on line 2
        # lcd.lcd_string("Model B+", 2)
        # lcd.GPIO.cleanup()

