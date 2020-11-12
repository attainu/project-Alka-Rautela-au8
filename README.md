# Bitcoin Price Alert

using this command line application one can get update of bitcoin price on his/her telegram and if the bitcoin price becomes greater or smaller than some certain price then user will receive an ALERT email. 

# requirements: 
* creating ifttt applet https://ifttt.com/home (youTube link for learning ifttt https://www.youtube.com/watch?v=aLe65UkvZ5c&t=135s) 
* download pip 
* download requests module for python3 using command => $ python3 -m pip install requests

# used technologies 
* IFTTT for alert and message automation 
* external 'request' module for get and post request 
* internal module 'datetime' for converting epoch time stamp into human readable format 
* rest bitcoin API of https://www.bitfex.com/#/

# concept used:
* OOP (object oriented programming)
* get and post rest api 


# working steps: 
* Step 1: sign up to https://ifttt.com/home (ifttt)
  
* Step 2: create applet 1 => crypto_latest_price   //(any name)
    this applet is for sharing daily bitcoin price update in telegram 
    (if webhooks post request then telegram notification). 
    Message Text should look like following: 
        Latest {{Value3}} Price:<br>
        {{Value1}}<br>
        {{Value2}}

* Step 3: create applet 2 => alert //(any name)
    this applet is for Alerting user via email when upper or lower threshold is reached 
    (if webhooks post request then email Alert)
    subject should look like following: 
        ALERT!!! ({{Value3}} price)

    Body(optional) should look like following:
        <b>ALERT<b>
        Hurry Up!<br>
        current price of {{Value3}} is {{Value1}}
        {{Value2}}

* Step4: get your webhook key from webhook documentation https://ifttt.com/maker_webhooks

* Step5: open PriceAlert -> cryptoParent.py file and assign your own key to key variable which is inside cryptoCurrency class constructor.
   
* Step6: if you have given different name to your ifttt applets then change value of variable applet1 and applet2 accordingly. 
  
* Step7: open terminal and make sure that you are in PriceAlert folder

* Step8: before running code make sure that you have downloaded 'requests' module of python, if not then run command => $ python3 -m pip install requests 

* Step8: now run command =>  python3 bitcoin.py

if you have followed all these steps then after minimum 5 seconds you will receive telegram message and if at that moment bitcoin price is more or less than threshold price then you will also receive an Alert email. 
note: you can also assign different values to these lowerBoundPrice and upperBoundPrice variable in bitcoin.py file