import base64

def PrintStats(floatdata):
    keywords = ['Assists:', 'Kills:','Double Kills:', 'Total gold Earned:', 'Total gold Spent:', 'Current Killing Spree:', 'Largest Crit:', 'Largest Killing Spree:', 'Largest Multikill:', 'Longest Time Spent Living:', 'Total Magic Damage Dealt:', 'Magic Damage Dealt to Champions:', 'Magic Damage Taken:', 'Total Minion Kills:', 'Total Neutral Minions Killed:' , 'Total Neutral Minions Killed in Enemy Jungle:', 'Neutral Minions Killed in Team Jungle:', 'Deaths:', 'Penta Kills:', 'Total Physical Damage Dealt:', 'Physical Damage Dealt to Champions:', 'Physical Damage Taken', 'Quadra Kills:', 'Team ID:', 'Total Damage Dealt:', 'Damage Dealt to Champions', 'Damage Taken:', 'Total Healing:', 'Total cc Dealt:', 'Time Spent Dead:', 'Total unit Healed:', 'Triple Kills:', 'Total True Damage Dealt:', 'True Damage Dealt to Champions:', 'True Damage Taken:', 'Turrets Destroyed:', 'Inhibitors Destroyed:', 'Wards Destroyed:', 'Wards Placed:']
    for x in range(len(floatdata)):
        print keywords[x], floatdata[x]
    #print '!'*50

import struct

def HextoFloatStat(HexNumber):
    Number = ''
    for i in range(-1,-len(HexNumber),-2):
        Number = '%s%s%s' %(Number,HexNumber[i-1],HexNumber[i])
    FloatNumber = struct.unpack('!f', Number.decode('hex'))[0]
    return FloatNumber

def FixNumberStat(Number):
    realnumber = ''
    #print Number
    for x in range(0,len(Number),2):
        couple = '%s%s' %(Number[x],Number[x+1])
        #print couple
        realnumber = '%s%s' %(couple,realnumber)
    #print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! %s' %realnumber
    return realnumber

def StatCreater(data):
    realdata = []
    Number = ''
    unknown = [0,2,4,6,7,8,9,12,13,14,15,16,17,18,19,20,21,26,35,41,43,44,45,46,47,48,49,50,51,53,54,55,56,70,73,74]
    Floats = [10,11,23,27,28,29,30,38,39,40,57,58,59,61,62,65,66,67]
    for x in range(len(data)):
        if x not in unknown:
            if x in Floats:
                Number = HextoFloatStat(data[x])
            else:
                Number = int(FixNumberStat(data[x]),16)
                #print Number
            realdata.append(Number)
    return realdata

def PlayerStatsCreater(Players):
    for x in Players:
        data=StatCreater(Players[x][6])
        Players[x][6]=data
        #print Players[x][2]
        #print 'Summoner: %s' %Players[x][0]
        #print 'Champsion: %s' %Players[x][1]
        #PrintStats(Players[x][6])

def HextoFloatitem(HexNumber):
    Number = ''
    for i in range(len(HexNumber)):
        Number = '%s%s' %(HexNumber[i], Number)
    FloatNumber = struct.unpack('!f', Number.decode('hex'))[0]
    return FloatNumber

def FixNumberItem(Number):
    realnumber = ''
    for x in range(0,len(Number),2):
        couple = '%s%s' %(Number[x],Number[x+1])
        realnumber = '%s%s' %(couple,realnumber)
    return realnumber

def PrintItems(data):
    for x in data:
        #print data
        if x[2] == '00':
            #print 'Item Slot %d: Empty' %int(x[1])
            print 'Item Slot %d: %s' %(int(x[1])+1,int(x[0],16))
        else:
            if x[2] != '01':
                if x[3] != '00':
                    print 'Item Slot %d: %s(%d)' %(int(x[1])+1,int(x[0],16),int(x[3]))
                else:
                    print 'Item Slot %d: %s(%d)' %(int(x[1])+1,int(x[0],16),int(x[2]))
            else:
                if x[4]==-1.0:
                    print 'Item Slot %d: %s' %(int(x[1])+1, int(x[0],16))
                else:
                    print 'Item Slot %d: %s | %d(%d)' %(int(x[1])+1, int(x[0],16), int(x[4]), int(x[5]))

def ItemCreater(data):
    newdata = []
    item = []
    for x in range(7):
        #print data
        #print data
        item.append(FixNumberItem(Makehexstring(data[x][0])))
        item.append(data[x][1])
        item.append(data[x][2])
        item.append(data[x][3])
        item.append(HextoFloatitem((data[x][4])))
        #print FixNumber(Makehexstring(data[x][4]))
        item.append(HextoFloatitem(data[x][5]))
        newdata.append(item[:])
        del item[:]
    return newdata

def PlayerItemCreater(Players):
    for x in Players:
        #print Players[x]
        Items = ItemCreater(Players[x][5])
        Players[x][5] = Items
        #print 'Summoner: %s' %Players[x][0]
        #print 'Champion: %s' %Players[x][1]
        #PrintItems(Players[x][5])

def PrintRunes(runes):
    last = -1
    count = 1
    for rune in runes:
        if rune == last:
            count+=1
        else:
            if last != -1:
                print '%d (x%d)' %(last,count)
                count = 1
        last = rune
    print '%d (x%d)' %(last,count)

def FixNumberRune(rune):
    realnumber = ''
    for x in range(len(rune)):
        couple = '%s' %(rune[x])
        realnumber = '%s%s' %(couple, realnumber)
    return realnumber

def RuneCreater(runes):
    newrunes = []
    for x in runes:
        newrunes.append(int(FixNumberRune(x),16))
    return newrunes

def PrintSummoners(summonerspells):
    for x in summonerspells:
        if x == '244F3606':
            print 'Ignite'
        elif x == 'A86E4906':
            print 'Flash'
        elif x == '1CAF6403':
            print 'Heal'
        elif x == 'F5740005' or x == 'DCE68D0F' or x == '82B19902':
            print 'Smite'
        elif x == '64134F00':
            print 'Teleport'
        elif x == 'E4BAA808':
            print 'Exhaust'
        elif x == '82B9CF0C':
            print 'Barrier'
        elif x == '21746503':
            print 'Clarity'
        elif x == '95CC4A06':
            print 'Ghost'
        elif x == 'EEAF870D':
            print 'Garrison'
        elif x == '65678909':
            print 'Clairvoyance'
        elif x == '94204D06':
            print 'Cleanse'
        elif x == 'A5B3C805':
            print 'Revive'
        else:
            print 'Unknown Summoner Spell %s' %x

def SummonerSpellCreater(summonerspells):
    newsummonerspells = []
    for x in summonerspells:
        newsummonerspells.append(Makehexstring(x))
    return newsummonerspells

def CreateMasteryid(mastery):
    masteryid = 4100
    #print int(mastery[4],16)
    points = int(mastery[4],16)
    firstnum = (int(mastery[1],16)-116)*100
    secondnum = ((int(mastery[0],16)/16)-3)*10
    thirdnum = (int(mastery[0],16))%8
    masteryid = masteryid + firstnum + secondnum + thirdnum
    return [masteryid, points]
    
def MasteryCreater(masteries):
    newmasteries = []
    for x in masteries:
        newmasteries.append(CreateMasteryid(x))
    return newmasteries

def PrintStuff(Player):
    print '\nRUNES'
    PrintRunes(Player[2])
    print '\nSummoner Spells'
    PrintSummoners(Player[3])
    print '\nMasteries'
    for x in Player[4]:
        print x[0], x[1]

def PlayerRuneMasterySpellCreater(Players):
    #print Players
    for x in Players:
        runes = RuneCreater(Players[x][2])
        spells = SummonerSpellCreater(Players[x][3])
        masteries = MasteryCreater(Players[x][4])
        Players[x][2] = runes
        Players[x][3] = spells
        Players[x][4] = masteries
        #PrintStuff(Players[x])

def decodehex(hexlist):
    decoded = []
    for hexnum in hexlist:
        decoded.append(hexnum.decode('hex'))
    word = ''.join(decoded)
    return word

def Makehexstring(hexstring):
    word = ''.join(hexstring)
    return word

def PrintAbilities(abilities):
    letters = ['Q','W','E','R']
    for x in range(len(abilities)):
        print '%s: %d' %(letters[x],int(abilities[x]))
    print '!'*50

def Final_Print(Players):
    for Entityid in Players:
        print 'Summoner Name: %s' %Players[Entityid][0]
        print '\nChampion: %s' %Players[Entityid][1]
        PrintStuff(Players[Entityid])
        print '\nItems'
        PrintItems(Players[Entityid][5])
        print '\nStatistics'
        PrintStats(Players[Entityid][6])
        print '\nAbilities'
        PrintAbilities(Players[Entityid][7])

def Parser(data):
    previous = ''
    lengthbool = [0,0,0]
    length = []
    blocktypes = ['4C','4B','2A','FE','46','45','15']
    blocktype = ''
    hexnum = ''
    count = 0;
    Players = {}
    player_name = False
    champion_name = False
    Entityid = []
    #Playernum = []
    SummonerName = []      #lists for names
    ChampionName = []
    Stats = []             #lists for stats
    stat = []
    Items = []             #lists for items
    item = []
    itemid = []
    cooldown = []
    rune = []               #lists for runes/masteries
    runes = []
    summoner_spell = []
    summoner_spells = []
    masteries = []
    mastery = []
    Abilities = []
    marker = ''
    #4C/4B=player header, 2A=Summoner Data, FE=Inventory, 46/45=Player Stats
    for x in range(0,len(data),2):
        if x+1 == len(data):
            break
        hexnum = '%s%s' %(data[x],data[x+1])
        if lengthbool[0] == 1:
            if hexnum in blocktypes or (marker == 'F3' and lengthbool[1]==lengthbool[2]):
                if marker != 'F3':
                    blocktype = hexnum
                count=0
                #print blocktype, Entityid, count
                lengthbool[0]=0
                lengthbool[2] = lengthbool[1]
                lengthbool[1]=0
                #print length
            else:
                length.append(hexnum) #insert to account for little endian?
                lengthbool[1] += 1
                #print lengthbool[1], lengthbool[2], length
                #if marker == 'F3':
                    #print lengthbool[1], lengthbool[2], Abilities
                '''
                if lengthbool[1] == 4:
                    lengthbool[0] = 0
                    lengthbool[1] = 0
                    #print length
                    '''                
        #if (previous == 'B3' or previous == '83' or previous == 'A3' or previous == '93') and hexnum == '00':
        if (previous == 'B3' or previous == 'F3' or previous == 'A3' or previous == '83') and hexnum == '00':
            marker = previous
            lengthbool[0] = 1
            del length[:]

        #getting summoner names and champions
        if blocktype == '4C' and length: #could be '4B'?
            comparehex = '%X' %(count-2)
            #print hexnum, count
            if count == 0:
                player_name = True
                champion_name = True
                del Entityid[:]
                #del Playernum[:]
                del SummonerName[:]
                del ChampionName[:]

                    
            count+=1
            if count in range(3,7):
                Entityid.append(hexnum)
            elif count > 19 and count < 148 and player_name == True:
                if hexnum != '00':
                    SummonerName.append(hexnum)
                else:
                    player_name = False
            elif count > 147 and champion_name == True:
                if hexnum != '00':
                    ChampionName.append(hexnum)
                else:
                    champion_name = False
            elif comparehex == length[0]:
                #print comparehex, length[0]
                #print Entityid
                if Entityid and Entityid[-1] == '40':
                    Players[Makehexstring(Entityid)] = [decodehex(SummonerName),decodehex(ChampionName)]
                #player_data.append(Entityid)
                #player_data.append(Playernum)
                #player_data.append(decodehex(SummonerName))
                #player_data.append(decodehex(ChampionName))
                #Players.append(player_data)
                #count = 0
                blocktype = ''
        
        if blocktype == 'FE' and length:
            comparehex = '%X' %(count-2)
            if len(length)>1:
                blocktype = ''
                #continue
            if len(comparehex)%2==1:
                coparehex = '0%s' %comparehex
            if count == 0:
                del cooldown[:]
                del Items[:]
                del item[:]
                del itemid[:]
            count += 1
            '''
            if comparehex == length:
                count = 0
                blocktype = ''
                Players[Makehexstring(Entityid)].append(Items[:])
            '''
            if (len(Items) == 10 and len(Items[9])==6) or comparehex == length[0]:
                #print Entityid
                if Makehexstring(Entityid) not in Players.keys():
                    continue
                Players[Makehexstring(Entityid)].append(Items[:])
                #print Players
                #count = 0
                blocktype = ''
            if count < 75 and count > 4:
                if len(itemid)<4:
                    itemid.append(hexnum)
                    if len(itemid)==4:
                        item.append(itemid[:])
                else:
                    item.append(hexnum)
                if len(item) == 4:
                    Items.append(item[:])
                    del item[:]
                    del itemid[:]
            elif count > 74: 
                itemnum = (count-75)/4
                if itemnum > 9:
                    itemnum %= 10
                cooldown.append(hexnum)
                if len(cooldown) == 4:
                    #print count, length, Items
                    if Entityid and Entityid[3] == '40':
                        Items[itemnum].append(cooldown[:])
                        del cooldown[:]
                        #continue
                    #print cooldown
                    #Items[itemnum].append(cooldown[:])
                    #print len(Items)
                    '''
                    if len(Items) == 10 and len(Items[9])==6:
                        #print Entityid
                        Players[Makehexstring(Entityid)].append(Items[:])
                        #print Players
                        count = 0
                        blocktype = ''
                    '''
                    
        
        if blocktype == '46' and len(length) == 4:
            comparehex = '0%X' %(count-2)
            if length[1]+length[0] != '0130':
                del length[:]
                blocktype = ''
                continue
                #make sure that there isnt a false positive
                
            if count == 0:
                #reset things
                del Stats[:]
                del stat[:]
            count+=1
            if comparehex == length[1]+length[0]:
                #count = 0
                blocktype = ''                   
                if Entityid[3] != '40':
                    continue
                Players[Makehexstring(Entityid)].append(Stats[:])
                #print Players[Makehexstring(['19','00','00','40'])]
                #print Players
            elif count>2:
                if count == 130 or count == 131:
                    continue
                stat.append(hexnum)
                '''
                if len(stat)%4 == 0:
                    print stat , str(count)
                    '''
                if len(stat)==4:
                    Stats.append(Makehexstring(stat))
                    del stat[:]
        
        if blocktype == '2A' and length:
            comparehex = '%X' %(count-1)
            if len(comparehex)%2==1:
                coparehex = '0%s' %comparehex
            
            if count == 0:
                del rune[:]
                del runes[:]
                del summoner_spells[:]
                del masteries[:]
                del mastery[:]
            count+=1
            
            if count>5 and count<126:
                rune.append(hexnum)
                if len(rune) == 4:
                    runes.append(rune[:])
                    del rune[:]
            elif count>125 and count < 134:
                summoner_spell.append(hexnum)
                if len(summoner_spell) == 4:
                    if summoner_spell not in summoner_spells:
                        summoner_spells.append(summoner_spell[:])
                    del summoner_spell[:]
            elif count>141:
                mastery.append(hexnum)
                if mastery == ['00','00','00','00','00']:
                    if not Entityid or Entityid[-1] != '40':
                        blocktype = ''
                        continue
                    
                    Players[Makehexstring(Entityid)].append(runes[:])
                    Players[Makehexstring(Entityid)].append(summoner_spells[:])
                    Players[Makehexstring(Entityid)].append(masteries[:])
                    blocktype = ''                    
                if len(mastery) == 5:
                    masteries.append(mastery[:])
                    del mastery[:]
        
        if blocktype == '15' and length:
            comparehex = '%X' %(count-2)
            if count == 0:
                if marker == 'F3':
                    count+=1
                else:
                    del Abilities[:]
            
            count+=1
            
            if count==4:
                Abilities.append(hexnum)
                
                if len(Abilities)==4:
                    if Entityid and Entityid[3] != '40':
                        blocktype = ''
                        #continue
                        del Entityid[:]
                    elif Entityid:
                        Players[Makehexstring(Entityid)].append(Abilities[:])
                        del length[:]
                        blocktype = ''
                        del Entityid[:]
        

            
        previous = hexnum

    #print Players
    PlayerRuneMasterySpellCreater(Players)
    PlayerItemCreater(Players)
    PlayerStatsCreater(Players)
    #print Players
    Final_Print(Players)