import datetime
import time
end_time=datetime.datetime(2023,12,18)
site_block=["www.facebook.com","www.instagram.com","www.sreyas.ac.in"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"
while True:
    if datetime.datetime.now()<end_time:
        print("Websites are Blocked!!!")
        with open(host_path,"r+") as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
                    print(f"{website} Blocked")
                else:
                     print(f"{website} Already Blocked")
                     pass
        time.sleep(30)
    else:
        print("Webites are unblocked! Have Fun!!!")
        with open(host_path,"r+") as host_file:
            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
            print(f"{site_block} Unblocked...!")
        time.sleep(30)