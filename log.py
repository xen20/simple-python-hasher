import csv
import os


def log_results(results, destination_csv, destination_txt):

    log_to_txt(destination_txt, results['filename'], results['crc32'], results['md5'], results['sha1'])

    csv_file_exists = os.path.isfile(destination_csv)

    with open(destination_csv, 'a') as csvfile:
        fieldnames = ['Filename', 'crc32', 'md5', 'sha1']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not csv_file_exists:
            writer.writeheader()

        writer.writerow({'Filename': results['filename'], 'crc32': results['crc32'], 'md5': results['md5'],
                         'sha1': results['sha1']})


def log_to_txt(destination_txt, filename, crc32, md5, sha1):

    with open(destination_txt, 'a') as txt_log:
        txt_log.write("\nFilename: {}\nCRC32: {}\nmd5: {}\nsha1: {}\n".format(filename, crc32, md5, sha1))
