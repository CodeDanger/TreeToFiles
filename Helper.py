

from Tree import TreeElement

def convertTreeToListOfFilesAndFolders(lines:list[str]):
    # get tree max depth
    max_depth = getTreeMaxDepth(lines)
    # convert lines to Tree Element
    tree=createTreeElementFromLines(lines,max_depth)
    tree.create()
    tree.display()
    
    
    
def getTreeMaxDepth(lines:list[str]):
    max_depth = 0
    for line in lines:
        depth = len(line.split())
        if depth > max_depth:
            max_depth = depth
    return max_depth

def createTreeElementFromLines(lines:list[str],max_depth):
    # current_depth = 1
    
    max_lines = len(lines)-1
    bigParent = TreeElement()  
    counter = 0   
    depthDict = {
        0:bigParent
    }   
    while True:
        if counter > max_lines :
            break
        line = lines[counter]
        splitted = line.split()
        folderOrFile = splitted[-1]
        depth = len(splitted) +(line.count('       ') if '       ' in line else 0)
        # let's create parent
        for theDepthToCheck in range(1,max_depth+1):
            if depth == theDepthToCheck:
                parent = depthDict[ theDepthToCheck-1]
                depthDict[theDepthToCheck] = TreeElement(folderOrFile,parent=parent)
                break
                
        
        counter+=1
        
    return bigParent


# def splitByDepth(lines:list[str], max_depth):
#     depth_dict = {}
#     for line in lines:
#         depth = len(line.split())
#         if depth not in depth_dict.keys():
#             depth_dict[depth] = []
#             depth_dict[depth].append(line.split()[-1])
#         else:
#             depth_dict[depth].append(line.split()[-1])
#     return depth_dict