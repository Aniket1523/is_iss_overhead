# is_iss_overhead
This project is going check every one minute and email you whenever ISS is near to you in the sky. 
It's going to use two very basic APIs :
  1. iss-now - to check current location of ISS
  2. sunrise-sunset - to check sunrise and sunset time of your location for decision whether it's night. 
We have used smtp library to send mail to user. 
We have also used datetime module to find current hour. 
