import re

logFile = open("E:\\Blizzard\\World of Warcraft\\Logs\\WoWCombatLog.txt", "r", encoding='utf8')
logsPath = "H:\\Github\\WarcraftLogs\\TestLogs\\"

encounterName = ""
ID = 0
combat = 0

for line in logFile:
    if "ENCOUNTER_START" in line:
        # Create var for file
        encounterName = re.search('.*ENCOUNTER_START,.*"(.*)",.*', line).group(1)
        combat = 1
        ID += 1
        encounterFile = open(logsPath+str(ID)+'_'+str(encounterName)+'.txt', 'w+')
        print(encounterName)
    if "ENCOUNTER_END" in line:
        # Empty var for file
        combat = 0
        encounterFile.write(line)
        encounterFile.close()
    if combat == 1:
        # Write to file
        encounterFile.write(line)
