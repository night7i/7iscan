# coding=utf-8
import urllib.request, tqdm
import threading, argparse, sys, ctypes

def get_status(url):
    try:
        status_code = urllib.request.urlopen(url, timeout=1).getcode()
        return status_code
    except:
        pass


def main():
    print(sys.argv[0])
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', dest='url', default='None', type=str, help='Specify the target site for the scan')
    parser.add_argument('-d', '--dict', dest='dict', default='None', type=str, help='Specify the dictionary as backdoor.txt/backup.txt')
    (options, args) = parser.parse_known_args()
    parser = argparse.ArgumentParser(prog='myprogram')
    _len = len(sys.argv)
    if _len < 2:
        print('\n  Please use the - h parameter to check the usage\n  Usage: [7iscan.py -h]')
    else:
        prefix = options.url
        print('Start scanning '+prefix+'\n')
        doc_path = 'doc/'+options.dict
        print(doc_path)
        try:
            f = open(doc_path)
            for suffix in f:
                scan_url = prefix + suffix
                status = get_status(scan_url)
                if status == 200:
                    print(suffix.strip()+' Exist Status is 200\n')
        except:
            print('The dictionary does not exist')


if __name__ == '__main__':
    main()
