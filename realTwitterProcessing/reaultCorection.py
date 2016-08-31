

tweets=[]
with open("/media/kitware/My Passport/twitter_USA/2013-05_man_label/2013-05-01.txt","r") as rF:
    for line in rF.readlines():
        terms=line.strip().split(",")
        if len(terms[2])!=1:
            print terms[0],terms[1],terms[2]
