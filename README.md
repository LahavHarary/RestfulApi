# RestfulApi
### To Run the project please make sure every requirement in the file req.txt

Python Rest Api project
<br>
This project consists of 4 json files that contain data about virtual machines and firewall rules.
<br>
Each file contains different machines and different firewall rules.
<br>
The Api goal is to check whether a vm can be accessed from a different machine inside its folder and give statistics regarding run time and amount of requests that the server receives.
<br>
<br>
Attack Path: will get a vm-id from the user and will present the vm's that can attack the specified vm according to the firerules inside the folder.
<br>
<br>
Stats Path: will present the amount of vm's inside a folder (the folder will change for every request), amount of requests that were send to the server and the average time it took to deal with a request.
<br>
<br>
To run the project localy on your computer run the "main.py" file and go to one of the following urls:
<br>
http://127.0.0.1:5000/api/v1/attack/PlaceMachineIdHere 
<br>
or 
<br>
http://127.0.0.1:5000/api/v1/stats/
<br>
Please make sure that if you picked the attack url you should enter a valid vm id instead of "PlaceMachineIdHere"
