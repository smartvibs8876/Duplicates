import os
import sys

folderDict = dict()


try:
    for i in range( 1 , len(sys.argv) ):
        print(sys.argv[i])
        folderDict[ sys.argv[i] ] = os.listdir( sys.argv[i] )

except Exception:
    print("Failed to load the files")


def extractBasePackageName(packageName: str) -> str:
    tmp = packageName.split("-")
    extractedPackageName = ""
    for item in tmp:
        foundChar = False
        for char in item:
            if( char.isalpha() ):
                if(extractedPackageName == ""):
                    extractedPackageName = item
                else:
                    extractedPackageName +=  "-" + item
                foundChar = True
                break
        if foundChar == False:
            break
    return extractedPackageName


for key in folderDict.keys():
    print("Reading from folder ",key)
    packages = folderDict[key]
    packagesConsidered = list()
    for i in range(0,len(packages)):
        if( (packages[i] in packagesConsidered) or ( ".conda" not in packages[i] )):
            continue
        try:
            packageName = extractBasePackageName(packages[i])
        except Exception:
            print("Error in extracting package name")
            break
        if (packageName in packagesConsidered):
            continue
        duplicates = False
        duplicateList = list()
        duplicateList.append(packages[i])
        packagesConsidered.append(packageName)
        for j in range(i+1,len(packages)):
            if( packageName == extractBasePackageName(packages[j]) ):
                duplicates = True
                duplicateList.append(packages[j])
        if(duplicates == True):
            for item in duplicateList:
                print( item , end="  ")
            print("")
            print("**********************************************************************************************")