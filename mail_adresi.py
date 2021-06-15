mail=input("Please Write Your Mail:")
#dp= ". place"     ap= "@ place"
ap=mail.index("@")
dp=mail.index(".")

nick=mail[0:ap] #bu 3 satırda yerlerini alıyoruz
server=mail[ap+1:dp]
ext=mail[dp+1:]

if(len(nick) >=5):
    if(len(server) >=3):
        if(len(ext) >=2):
            print("Your Mail Adress is True")
        else:
            print("Your Mail Extension is Wrong")
    else:
        print("Your Mail Server is Wrong")
else:
    print("Your Mail Nick is Wrong")


