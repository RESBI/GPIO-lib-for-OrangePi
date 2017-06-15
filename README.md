# GPIO-lib-for-OrangePi
Put the gpio.py to your code's local.
Then "import gpio".
Use:
[The PIN name must be spell in CAPITAL.As:"PA4","PD9"]
[And the PIN number must be units.]

gpio.pinMount("PIN name") #To export the PIN.

gpio.pinUmount("PIN name") #To Unexport the PIN.

gpio.pinMode("PIN name","INPUT/OUTPUT","on/off") #To set the PIN mode.

gpio.pinValue("PIN name","Value/high/low","on/off") #To set the PIN value.[high = 1,low = 0]
