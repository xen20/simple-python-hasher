import zlib
import hashlib


def crc_checksum(userfile, buffersize):

    # Possibly filter out 0x from crc32 - it is possibly unnecessary
    filehandle = open(userfile, "rb")
    buffer = filehandle.read(buffersize)
    crc = 0

    while len(buffer) > 0:
        crc = zlib.crc32(buffer, crc) & 0xFFFFFFFF
        buffer = filehandle.read(buffersize)
    filehandle.close()

    return hex(crc)


def md5_hash(userfile, buffersize):

    filehandle = open(userfile, "rb")
    contents = filehandle.read(buffersize)
    md5handler = hashlib.md5()
    md5handler.update(contents)

    while len(contents) > 0:
        contents = filehandle.read(buffersize)
        md5handler.update(contents)
    filehandle.close()

    return md5handler.hexdigest()


def sha1_hash(userfile, buffersize):

    filehandle = open(userfile, "rb")
    contents = filehandle.read(buffersize)
    sha1handler = hashlib.sha1()
    sha1handler.update(contents)

    while len(contents) > 0:
        contents = filehandle.read(buffersize)
        sha1handler.update(contents)
    filehandle.close()

    return sha1handler.hexdigest()
