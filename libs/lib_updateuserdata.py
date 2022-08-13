def updateuser(data, ad):
    import json

    # with open(ad+'/userdata.json.txt') as json_file:
    #    data = json.load(json_file)

    # print (data)
    # print (type(data))
    (data["username"]) = data["username"]
    (data["password"]) = data["password"]
    (data["city"]) = data["city"]
    (data["usecache"]) = data["usecache"]
    (data["pcolor"]) = data["pcolor"]
    (data["scolor"]) = data["scolor"]
    # (data["name"]) = data["name"]
    try:
        (data["theme"]) = data["theme"]
    except:
        """"""
    # print (data['username'])
    # data=str(data)
    data = json.dumps(data, indent=4)

    # print(data, ad, "gaga")
    x = open(ad + "/userdata.json.txt", "w")
    x.write(data)
    x.close()
