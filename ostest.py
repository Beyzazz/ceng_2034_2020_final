#!/usr/bin/python3

#Beyzanur Öztürk 150709024
import os
import requests
import uuid
import hashlib
from multiprocessing import Pool
from multiprocessing import Process
'''question1'''

new_child = os.fork() 
if new_child == 0:
    print("child proc ID", os.getpid())

    '''question2'''
    def download_file(url, file_name=None):
        print("downloading", url) 
    
        r = requests.get(url, allow_redirects=True)
        file = file_name if file_name else str(uuid.uuid4())
        open(file,'wb').write(r.content)

        with open(file,"rb") as f:
            bytes = f.read() 
            readable_hash = hashlib.sha256(bytes).hexdigest()
            print(readable_hash)


    for url in ['http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg' , 'https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png' , 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg' , 'http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg' , 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg']:
        download_file(url)


    '''question3'''
    os._exit(0)


child_proc_exit_info=os.wait() 
print("Child process" , child_proc_exit_info[0], "exited")
print("Parent process", os.getpid(), "exiting after child has exited")
print("The wait() method of os module in Python enables a parent process to synchronize with the child process. i.e, To wait till the child process exits and then proceed. So, we can use wait() method to avoid orphan process situation")

'''question4'''

def items():
    array1 = {}
    unique = dict()
    for file_name in os.listdir('.'):
        if os.path.isfile(file_name):
            filehash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()
            if filehash not in unique:
                unique[filehash] = file_name
            else:
                array1[filehash] = file_name
    return unique, array1


def compare_array(array,unique):
    for h,f in unique.items():
        if array.get(h) is not None:
            print (f , " and ", array.get(h), " are same.")
        else:
            continue

if __name__ == '__main__':
    with Pool(4) as p:
        unique, array1 = items()
        p = Process(target=compare_array, args=(unique, array1))
        p.start()
        p.join()



