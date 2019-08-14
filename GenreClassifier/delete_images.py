''' Deleting images '''
def empty_folder(deletion_path):
    import os
    count = 0
    while True:
        try:
            os.remove(os.path.join(deletion_path ,"frame%d.jpg"%(count)))
            count+=1
        except:
            break
    