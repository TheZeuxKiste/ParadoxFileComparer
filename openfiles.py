import argparse
import json
import os
import re
import subprocess

#from Scripts.Exceptions import StringTooLargeError


def homeDriveNPath():  # get user directory, for use later
    var1 = os.environ['HOMEDRIVE']
    var2 = os.environ['HOMEPATH']
    var3 = re.sub(r'(Users\\)(\w+)', r'\1\\\2', var2)
    var = var1+"\\"+var3
    return(var)


# pulls a string with all files that you are searching from findvalidfiles.bat
# catches the errors it would produce when supplied with invalid input
def pullFiles(var):
    rtrn = subprocess.check_output(
        ["findvalidfiles.bat ", var], universal_newlines=True)
    return rtrn


def main():
    #declare important variables
    delim = "<-split->"
    fileString = ""
    stringOut = ""
    
    # Parse arguments into the program
    parser = argparse.ArgumentParser()
    parser.add_argument("fileInQuestion",
                        help="openfiles.py: what file do you want? exact matches only")
    args = parser.parse_args()
    
    
    # pull neccessary data from respective sources: JSON file at local game data directory
    
    # pull json
    jsonTarget = homeDriveNPath()+'\Documents\\Paradox Interactive\\Crusader Kings III\\dlc_load.json' 
    with open(jsonTarget) as f:
        dlc_load = json.load(f)
        

    
    # find the location of the local VS code installation
    for i in re.sub(r'(?<==|;)(?=[A-Z])', delim, os.environ['PATH']).split(delim):
        if re.search(r'(?:(?=[A-Z]:)(.*)(\\Microsoft VS Code\\bin))', i):
            exeLoc = i
            break
    # construct the complete path
    exeLoc = os.path.join(exeLoc, "code.cmd")
    
    # pull target files string, format it correctly to process later
    findValidFilesResults = re.sub(r'\s(?=[A-Z]:\\)', delim, pullFiles(args.fileInQuestion)).split(delim)
       
    #################################################
    ####### mainpart: compare the two strings #######
    #################################################
    
    #iterater over the string
    for obj in findValidFilesResults:
        # find the numbers in the Directory String passed by findvalidfiles.bat
        matchString = re.search(r'(\\1158310\\)(?P<out>\d*)(\\)', obj)
        if matchString:
            stringOut = matchString.group('out')#save all results here, to compare them later

        # iterate through the "dlc_load.json" file, "enabled_mods" key, to find all active mods
        for row in dlc_load["enabled_mods"]:

            # match every object belonging to the key enabled_mods in the dlc_load.json and save results in matchJson
            matchJson = re.search(r'(/ugc_)(?P<out>\w*)(\.mod)', row)
            if matchJson:
           
                #Combine matches into fileString
                if stringOut == matchJson.group('out'): #if the mod is in the playset, add its path to the final output file
                    fileString = fileString + " " + obj
                    
        # for i in fileString:
        #     j = j + 1
        #     if j >= 8000:
        #         raise StringTooLargeError
    # except StringTooLargeError:
    #     print("i found too many files, sorry")
    #     print("because of limitation of the commandline, i can only pass 8000 characters to it")
    #     print("and because i found too many matches to your query, the command line would throw an error")
    #     print("im trying to fix this problem, but itll take time!")
        
    # else:
    #     exeLoc="\'"+exeLoc+"\\code.exe\'"
    #     subprocess.run(['cmd.exe','/c', exeLoc, fileString], shell=True)#syntax error, probably the quote marks
    
    s = r" "
    countr = 0
    
    tesSTR = re.sub(r'\s(?=[A-Z]:\\)', delim, fileString).split(delim)
    
    for i in tesSTR:
        s = s + r" " + re.sub(r"(?<=\\)", r"\\", i, re.MULTILINE)
        
    fileString = re.sub(r'\s(?=[A-Z]:\\)', delim, s).split(delim)
    
    for i in fileString:
        print("Match: "+i)
    
    for i in fileString:
        subprocess.run([exeLoc, "--reuse-window", i])
            
    return 0


if __name__ == "__main__":
    main()