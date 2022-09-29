
print("   _____                                  _____             __ _       ")
print("  / ____|                                / ____|           / _(_)      ")
print(" | (___  _   _ ___ _ __ ___   ___  _ __ | |     ___  _ __ | |_ _  __ _ ")
print("  \___ \| | | / __| '_ ` _ \ / _ \| '_ \| |    / _ \| '_ \|  _| |/ _` |")
print("  ____) | |_| \__ \ | | | | | (_) | | | | |___| (_) | | | | | | | (_| |")
print(" |_____/ \__, |___/_| |_| |_|\___/|_| |_|\_____\___/|_| |_|_| |_|\__, |")
print("          __/ |                                                   __/ |")
print("         |___/                                                   |___/ ")


currentFilters = ''

while(1):
    print("[+] What do you want to do :")
    print("[1] Add Filter")
    print("[2] Show current Filters")
    print("[3] Clear all Filters")
    print("[4] export xml file")
    commandEntered = input("? > ")
    if ( commandEntered == '1'):
        print("[+] Choose Event you want to Log : ")
        commandList = [ 'ProcessCreate' ,'FileCreateTime' ,'NetworkConnect' ,'ProcessTerminate' ,'ImageLoad' ,'CreateRemoteThread' ,'RawAccessRead' ,'ProcessAccess' ,'FileCreate' ,'RegistryEvent' ,'RegistryEvent' ,'RegistryEvent' ,'PipeEvent' ,'PipeEvent' ,'WmiEvent' ,'WmiEvent' ,'WmiEvent' ,'DNSQuery' ,'FileDelete' ,'ClipboardChange' ,'ProcessTampering' ,'FileDeleteDetected' ,'FileBlockExecutable' ]
        conditionList = [ 'is', 'is not', 'contains', 'include','exclude', 'begin with', 'end with', 'not begin with', 'not end with', 'less than', 'more than' ]
        EventFilterList = [['CommandLine','Image','ParentCommandLine'],['TargetFilename','Image'],['Image','DestinationPort'],['Image'],['Signature'],[],['StartModule','TargetImage'],[],['TargetFilename','Image'],['TargetObject','Image'],['TargetObject','Image'],['TargetObject','Image'],['PipeName'],['PipeName'],['QueryName'],[],[],[],[],[],[],[]]
        for i in range(1,23):
            print(" ["+ str(i) +"] " + commandList[i-1] )
        commandEntered = int(input("? > "))
        
        for i in range(1,10):
            print(" ["+ str(i) +"] " + conditionList[i-1] )
        conditionEntered = int(input("? > "))
        newFilter = '<' + commandList[int(commandEntered) - 1] + ' onmatch="'+ conditionList[conditionEntered -1] +'">\n' 
        endNewFilter = '</' + commandList[int(commandEntered) - 1] + '>\n'
        totalFilters = ''
        while(1):
            print("Do you want to add Filters?")
            print("[1] Yes")
            print("[2] No")
            answer = int(input("? > "))
            if(answer == 1):
                for i in range(0,len(EventFilterList[commandEntered - 1])):
                    print(" [" + str(i + 1)  + "] " + EventFilterList[commandEntered-1][i] )
                commandEntered2 = int(input("? > "))
                for i in range(1,10):
                    print(" ["+ str(i) +"] " + conditionList[i-1] )
                conditionEntered2 = int(input("? > "))
                print("[+] Enter the filter value")
                filterValue = input("? > ")
                totalFilters = totalFilters + '<' + EventFilterList[commandEntered-1][conditionEntered2-1] + ' condtion="' + conditionList[conditionEntered2-1] + '" >' + filterValue + '</' + conditionList[conditionEntered2-1] + '>\n'
                continue
            elif(answer == 2):
                currentFilters = currentFilters + newFilter + totalFilters + endNewFilter
                #print(currentFilters)
                break
            else:
                print("[!] Wrong Answer!")
                continue
            
        #print(currentFilters)
        
    elif ( commandEntered == '2'):
        print(currentFilters)
        continue
    elif ( commandEntered == '3'):    
        print("Are you sure ?! ")
        print("[1] YES")
        print("[2] No")
        answer = input("? > ")
        if(answer == '1'):
            currentFilters = ''
            print("[+] Event Filter is now Empty.")
            continue
        elif(answer == '2'):
            continue
        else:
            continue
    elif ( commandEntered == '4'):
        fileName = input("[+] Please Enter File name : ")
        text =  '<Sysmon schemaversion="4.50">\n<HashAlgorithms>md5,sha256</HashAlgorithms>\n\n<EventFiltering>\n\n' + currentFilters + '\n</EventFiltering>\n</Sysmon>'
        f=open(fileName, "w")
        f.write(text)
        f.close
        print("[+] Configuration saved to file : " + fileName)
        break
    else:
        print("[!] Please Choose right input! ")
        continue
    