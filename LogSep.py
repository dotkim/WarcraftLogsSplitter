import re

logFile = open("D:\\Blizzard\\World of Warcraft\\Logs\\WoWCombatLog.txt", "r", encoding='utf8')

encounterName = ""
ID = 0
combat = 0

def getEncounterName():
    return re.search('(.*:..):.*ENCOUNTER_START.*"(.*)",.*', line)

def createEncounterFile():
    logsPath = "H:\\Github\\WarcraftLogs\\TestLogs\\"
    date = str(encounterName.group(1)).replace('/', '_').replace(' ', '_').replace(':', '')
    name = str(encounterName.group(2)).replace(' ', '_')
    return open(logsPath+date+'_'+name+'.txt', 'w+')

for line in logFile:
    if "ENCOUNTER_START" in line:
        # Create var for file
        encounterName = getEncounterName()
        combat = 1
        ID += 1
        encounterFile = createEncounterFile()
        print(encounterName.group(2))
    if "ENCOUNTER_END" in line:
        # Empty var for file
        combat = 0
        encounterFile.write(line)
        encounterFile.close()
    if combat == 1:
        # Write to file
        encounterFile.write(line)