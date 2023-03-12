#python code for sending WhatsApp message to a specific number in a specific time
import pywhatkit
number = input("Enter the phone number with country code: ")
message = input("Enter the message: ")
hour = int(input("Enter the Hour in 24 hour format: "))
minute = int(input("Enter the Minute: "))
pywhatkit.sendwhatmsg(number, message, hour, minute)
#owner:@Harajit
