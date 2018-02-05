#useful little script for retrieving a crc32 checksum and two different hashes
#iterates over the file imported as binary data in 64mb chunks so as to be fast and
#memory effective
#imports file as CLI argument, and is windows/linux portable
#timer function used to compare effectiveness/speed of script vs existing linux
# CLI tools, such as md5sum and sha1sum
#Author: Konstantin Mishin

import zlib
import hashlib
import time as timer
import sys

def crc_checksm(userfile,buffersize):
    filehandle = open(userfile, "rb")
    buffer = filehandle.read(buffersize)
    crc = 0
    while len(buffer) > 0:
        crc = zlib.crc32(buffer,crc) & 0xFFFFFFFF #makes script 2.7/3.6+ portable, 
        buffer = filehandle.read(buffersize)      #as crc32 was changed between releases
    filehandle.close()
    return hex(crc)

def md5_hash(userfile,buffersize):
    filehandle = open(userfile,"rb")
    contents = filehandle.read(buffersize)
    md5handler = hashlib.md5()
    md5handler.update(contents)
    while len(contents) > 0:
        contents = filehandle.read(buffersize)
        md5handler.update(contents)
    filehandle.close()
    return md5handler.hexdigest()

def sha1_hash(userfile,buffersize):
    filehandle = open(userfile,"rb")
    contents = filehandle.read(buffersize)
    sha1handler = hashlib.sha1()
    sha1handler.update(contents)
    while len(contents) > 0:
        contents = filehandle.read(buffersize)
        sha1handler.update(contents)
    filehandle.close()
    return sha1handler.hexdigest()
        

buffersize = 65536
userfile = sys.argv[1]

start_time = timer.time()
print(crc_checksm(userfile,buffersize))
print(md5_hash(userfile,buffersize))
print(sha1_hash(userfile,buffersize))
end_time = timer.time()

print("execution took %s seconds" % (end_time - start_time))
