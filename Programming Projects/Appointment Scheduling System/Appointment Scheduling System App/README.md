# ![Logo](https://github.com/JoshuaRW1995/CIS4375-TechSoftSystems/blob/main/READMEscreenshots/Logo.PNG)

Ensure you have nodejs installed prior to following the instructions below

Database Connection Guide:
1. Download MySQL Workbench (https://dev.mysql.com/downloads/workbench/)
2. Set up connection in MySQL Workbench with the following credentials

# ![MySQL connection screenshot](https://github.com/JoshuaRW1995/CIS4375-TechSoftSystems/blob/main/READMEscreenshots/MySQLconnection.PNG)

Connection Name: Enter whatever name you wish\
Hostname: cis4375-techsoftsystemsdb.cfj7rtjvoqjp.us-east-2.rds.amazonaws.com\
Username: TSSDB_admin\
Password: t3%ch#!S0*f$t051222

Visual Studio Code clone Github repository:
1. Open a fresh VS code window
2. Select "Clone Git repository..." and enter the URL (https://github.com/JoshuaRW1995/CIS4375-TechSoftSystems.git) in the popup area and press enter
3. Select a location on your system for the repository

# ![MySQL connection screenshot](https://github.com/JoshuaRW1995/CIS4375-TechSoftSystems/blob/main/READMEscreenshots/vsCodeRepoSetup.PNG)

How to commit changes to the Github repository from within VS Code:
1. Use the command git add . to stage all changes you've made within your project directory
2. Use the command git commit -m "enter a short message for your commit" to commit the changes you've previously staged
3. Use the command git push to send the committed changes to the Github repository
4.  *** Use the command git pull to retrieve changes made by other people *** be sure to do this each time you begin working

For utilizing nodemon to automatically restart the API during development:
1. Run the API with npm start
