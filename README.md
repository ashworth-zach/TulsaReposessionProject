# TulsaReposessionProject
Project to make Tulsa Reposession data easily accessible with automatic license plate recognition
This project was made to run on ubuntu v16.0.4.
dependencies are included in the requirements.txt.
Project was made using python 3.7 and django v1.10.

# Follow instructions to use:
First you need to:  $pip install -r requirements.txt
Then you need to follow the Alpr installation guide for ubuntu v16.0.4 found here: https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux).
Once you are able to use the alpr command line utility you can then python manage.py runserver, to start.


# Summary:
this uses the openAlpr(automatic liscence plate recognition) to find the text on your liscence plate, then it does a simple search through the tulsa repossession list to check if the your plate is listed.
if your plate is found it will display.
you can also search plates.

TulsaRepoList: https://www.cityoftulsa.org/apps/opendata/OpenData_VehicleTowList.jsn

OpenAlpr: https://github.com/openalpr/openalpr
