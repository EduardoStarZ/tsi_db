# module to define the file structure

files: {
        'names': [],
        'sizes': [],
        'sender': [],
        'content': [],
        'curator': ''
    }    

def queryFiles(request):
    
    for x in request:
        files.names.append(request.Names[x])
        files.sizes.append(request.Names[x])
        files.sender.append(request.Names[x])
        files.content.append(request.Names[x])
        files.curator = request.curator
                
        return files
    
def insertFiles(request):
    dbInsert(files)