# useful little script for retrieving a crc32 checksum and two different hashes
# iterates over the file imported as binary data in 64mb chunks so as to be fast and memory effective
# imports file from CLI argument, and is windows/linux portable
# timer function used to compare effectiveness/speed of script vs existing linux tools, such as md5sum and sha1sum
# Author: Konstantin Mishin


import time as timer
import os

import hash
import parse
import log


def main():

    buffer_size = 65536
    args = parse.parse_arguments()
    userfiles = args.func(args)
    hash_data = {}

    start_time = timer.time()

    for userfile in userfiles:
        filename = os.path.basename(userfile)

        crc32 = hash.crc_checksum(userfile, buffer_size)
        md5 = hash.md5_hash(userfile, buffer_size)
        sha1 = hash.sha1_hash(userfile, buffer_size)

        hash_data.update({'filename': filename, 'crc32': crc32, 'md5': md5, 'sha1': sha1})

        print("File: {}\ncrc32: {}\nmd5: {}\nsha1: {}\n".format(filename, crc32, md5, sha1))
        log.log_results(hash_data, "log.csv", "log.txt")

    end_time = timer.time()

    print("execution took {} seconds".format((end_time - start_time)))


if __name__ == "__main__":
    main()
