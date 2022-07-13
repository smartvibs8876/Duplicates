def readFileContentsInADict(*files) -> dict:
    fileDict = dict()
    for file in files:
        txtFile = open(file, "r")
        fileContent = txtFile.read()
        fileContentList = fileContent.split("\n")
        for line in fileContentList:
            key, value = line.split("/")
            if key not in fileDict.keys():
                fileDict[key] = list()
            fileDict[key].append(value)
    return fileDict

try:
    fileDict = readFileContentsInADict(r"C:\Users\AVVVER744\DocumentsVibs\OpenCETraining\PackageList\packages.txt")
except Exception:
    print("File error")

for key in fileDict.keys():
    packages = fileDict[key]
    packagesConsidered = list()
    for i in range(0,len(packages)):
        if(packages[i] in packagesConsidered):
            continue
        try:
            packageName = packages[i].split("-")[0]
        except Exception:
            print("Error in extracting package name")
            break
        duplicates = False
        duplicateList = list()
        duplicateList.append(packages[i])
        packagesConsidered.append(packages[i])
        for j in range(i+1,len(packages)):
            if(packageName in packages[j]):
                duplicates = True
                duplicateList.append(packages[j])
                packagesConsidered.append(packages[i])
        if(duplicates == True):
            print(duplicateList)