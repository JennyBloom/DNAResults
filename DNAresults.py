"""
Jenny Bloom
9/17/2015
Homework #4
Collaborators: Collin Duncan, a friend who knows Python; StackOverflow
for various error corrections: 
http://stackoverflow.com/questions/19016194/nameerror-name-split-is-not-defined)
This assignment generates a dictionary from DNA sequence data to show
user certain genotypes within DNA are related to specific diseases and 
skin types.  
"""

import sys

file_name = sys.argv[1] #Creates universe - stores datafile as variable.

def main(): #Defines main function
		print("Parsing ", file_name) #Shows user what file is being parsed.
		return None #Similar to hitting 'enter' on the defined function

def parseFile(): #Leaving () empty allows parameters to be globally applicable.
	dnaDict = {} #Creates new dictionary to store parsed Data into.
	f = open(file_name, 'r') #Opens file
	for line in f: #for loop of line splitting to create dnaDict
		splitLine = line.split() #Splits lines according to spaces
		if '#' in str(splitLine[0]): #If line is commented, move on.
			next(f) #next = the move on function. Wish I had this in my life.
		else: #if not a comment, throw into dnaDictionary
			dnaDict [splitLine[0]] = splitLine[3] #column values for RSID and Genotype
	f.close() #close the loop for good measure.
	if 'rs1426654' not in dnaDict: #Failsafe: if key isn't there, stop fxn.
		print('The key is not present.') #Tells user key isn't present.
		return None #code stops executing if no key found.
	elif 'rs7754840' not in dnaDict: #same as 'if' statement above
		print('The key is not present.')
		return None
	else: #if the key is present, begin looking for specifics.
		skin = checkSkinType(dnaDict.get('rs1426654')) #get RSID values for skin type
		disease = checkType2Diabetes(dnaDict.get('rs7754840')) #get RSID values for diabetes
		print(skin)
		print(disease)
		return None #Closes function.

def checkSkinType(arg): #define arguments for checking skin type
	if arg == str('AA'): #if arg parameter is the 'AA' genotype
		return 'Probably light-skinned, European ancestry' 
	elif arg == str('AG'): #else if arg parameter is 'AG' genotype
		return 'Probably mixed African/European ancestry'
	elif arg == str('GG'): #else if arg parameter is 'GG' genotype
		return 'Probably darker-skinned, Asian or African ancestry'
	else: #else arg parameter is none of the above genotypes...
		return 'No DNA info on Skin Type.'

def checkType2Diabetes(arg): #defome arg for diabetes
	if arg == str('CG') or str ('CC'): #if arg is either 'CG' OR 'CC' it has the same return
		return '1.3 Increased risk for Type-2 Diabetes' 
	elif arg == str('GG'): #arg parameter is 'GG' it returns normal risk
		return 'Normal risk for Type-2 Diabetes'
	else: #if arg parameter doesn't match any of the above...
		return 'No DNA info on Type-2 Diabetes'

main() #Begins executing script here.
parseFile() #Begins executing here, not at def. f.close is ABOVE!
