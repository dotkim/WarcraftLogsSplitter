import re

logFile = open("E:\\Blizzard\\World of Warcraft\\Logs\\WoWCombatLog.txt", "r", encoding='utf8')

Deaths = 0
for line in logFile:
    if "UNIT" in line:
        if "Magequest" in line:
            Deaths += 1

print(Deaths)