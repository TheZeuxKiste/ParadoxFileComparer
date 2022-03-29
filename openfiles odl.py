import argparse
import json
import os
import re
import subprocess


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
    # pull string, format it correctly
    delim = "<-split->"
    rexp = re.sub(r'\s(?=[A-Z]:\\)', delim, pullFiles(args.fileInQuestion)).split(delim)
    
    #################################################
    ####### mainpart: compare the two strings #######
    #################################################
 
    # iterate over the json and the pulled string, match steam ids
    finalstring = ""
    jsonOut = ""
    stringOut = ""
    for obj in rexp:
        # find the numbers in the string passed by findvalidfiles.bat
        # oldpattern:
        matchString = re.search(r'(\\1158310\\)(?P<out>\d*)(\\)', obj)
        if matchString:
            stringOut = matchString.group('out')

        # iterate through the "dlc_load.json" file, "enabled_mods" key, to find all active mods
        for row in dlc_load["enabled_mods"]:

            matchJson = re.search(r'(/ugc_)(?P<out>\w*)(\.mod)', row)
            if matchJson:
                jsonOut = matchJson.group('out')
            if stringOut == jsonOut:
                finalstring = finalstring + " " + obj
            else:
                finalstring = finalstring + ""
    
    FNULL = open(os.devnull, 'w')
    lArgs = "code"+" "+finalstring
    subprocess.call(lArgs, stdout=FNULL, stderr=FNULL, shell=False)
    return 0


if __name__ == "__main__":
    main()
