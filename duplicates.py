import os
import sys

folderDict = dict()

try:

    for i in range( 1 , len(sys.argv) ):
        print(sys.argv[i])
        folderDict[ sys.argv[i] ] = os.listdir( sys.argv[i] )

except Exception:
    print("Error in fetching the files")

print(folderDict)
# for key in folderDict.keys():
#     packages = folderDict[key]
#     packagesConsidered = list()
#     for i in range(0,len(packages)):
#         if(packages[i] in packagesConsidered):
#             continue
#         try:
#             packageName = packages[i].split("-")[0]
#         except Exception:
#             print("Error in extracting package name")
#             break
#         duplicates = False
#         duplicateList = list()
#         duplicateList.append(packages[i])
#         packagesConsidered.append(packages[i])
#         for j in range(i+1,len(packages)):
#             if(packageName in packages[j]):
#                 duplicates = True
#                 duplicateList.append(packages[j])
#                 packagesConsidered.append(packages[i])
#         if(duplicates == True):
#             print(duplicateList)