from appdirs import *

def readrate(ad,pos):
    import json
    with open(ad   + "/rates.json", "r") as json_file:
        data2 = json.load(json_file)



    #dictionary = json.loads(data2)
    print (data2[pos],'dictpos')
    return data2[pos]
def readuserdata(App, config_file, ios):

    import json

    ad = config_file
    if ios == True:
        ad = config_file
        app = App.get_running_app()
        ad = app.user_data_dir

    with open(ad + "/userdata.json.txt") as json_file:
        data = json.load(json_file)
        username = data["username"]
        password = data["password"]
        location = data["city"]
        usecache = data["usecache"]
        pcolor = data["pcolor"]
        scolor = data["scolor"]
        debug = data["debug"]
        # print("readuserdataOMG")
        # return username,password,location,usecache,pcolor,scolor,debug
        # print(ad, "lib_readuserdata ad", ios)
        return data
