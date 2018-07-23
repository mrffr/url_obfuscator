#!/usr/bin/python3

def ipv4_lookup(url):
    import subprocess
    cmd = ['ping', '-c', '1', url, '-4']
    status,res = subprocess.getstatusoutput(' '.join([x for x in cmd]))
    if status == 0: #0 success, 1 no reply, 2 other error
        res = res.split()[2][1:-1] #ip addr
    return status, res


if __name__ == "__main__":
    print(ipv4_lookup("www.facebook.oneno"))
