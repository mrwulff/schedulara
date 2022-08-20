def make_json_schedule(x, ad):
    from bs4 import BeautifulSoup

    # import lib_think

    print("asdfasdf", x["usecache"])
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        conf = "/conf.html"
        cache = True
    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        conf = "/realdata.html"
        cache = False
        print("WHY YOU NOT WORK")

    encoding = "utf8"

    try:
        z = open(ad + c2onf, "r", encoding="utf8")
    except:
        if cache == True:
            import libs.lib_createcache

            libs.lib_createcache.createcache(ad, 25)
            z = open(ad + conf, "r", encoding="utf8")

        if cache == False:
            import libs.lib_createcache

            # lib_createcache.createcache(ad, 15)

            good_login = libs.lib_think.login(ad, x, False, False)
            if good_login == False:
                return False
            z = open(ad + conf, "r", encoding="utf8")

    soup = BeautifulSoup(z, "html.parser")
    try:
        name = soup.find("span", id="lblEmpName")
        # print(name)
    except:
        print("emp not found")
        return
    name = str.split(name.get_text(), ", ")
    # print(name, "wtfname")
    name = name[1] + " " + name[0]
    x["name"] = name
    import libs.lib_updateuserdata

    libs.lib_updateuserdata.updateuser(x, ad)

    ab = soup.find_all("tr")

    fullnj = []
    alldict = []
    olddict = []
    confirmable = []
    conf_bool = False
    from datetime import datetime

    for i in range(1, len(ab) - 1):
        nj = []
        nj2 = {}
        ax = ab[i].find_all("td")
        # print(ax)
        f3 = "False"
        canceled = False
        old = False
        if "dgR" in str(ax[13]):
            xx = str(ax[13])
            f = str.split(xx, '"')
            f3 = f[3]
            confirmable.append(f3)
            conf_bool = True
        can = ax[13]
        can2 = ax[0]
        # print(can2)
        if "Red" in str(can):
            # print ("OMG ITS RED")
            canceled = True

        show_date = datetime.strptime(ax[0].get_text(), "%m/%d/%Y")
        now = datetime.now()
        if show_date.date() < now.date():
            old = True

        thisdict = {
            "date": ax[0].get_text(),
            "time": ax[1].get_text(),
            "job": ax[2].get_text(),
            "show": ax[3].get_text(),
            "venue": ax[4].get_text(),
            "location": ax[5].get_text(),
            "client": ax[6].get_text(),
            "type": ax[7].get_text(),
            "pos": ax[8].get_text(),
            "details": ax[9].get_text(),
            "status": ax[10].get_text(),
            "notes": ax[11].get_text(),
            "timekeep": ax[12].get_text(),
            "plus": ax[13].get_text(),
            "canceled": canceled,
            "confirmid": "",
            "lunches": "",
            "endtime": "",
            "is_new": False,
            "confirable": f3,
            "old": old,
        }
        if "Turned Down" in thisdict["status"]:
            thisdict["canceled"] = True
        if old == False:
            alldict.append(thisdict)
            # print(old, "OLD")
        if old == True:
            olddict.append(thisdict)
            # print(old, "OLD")

    cconfirmables = {
        "confirmable": conf_bool,
        "num_shows": len(confirmable),
        "shows": confirmable,
    }

    from datetime import datetime

    now = datetime.now()
    s = {
        "name": name,
        "num_shows": len(alldict),
        "old_shows": olddict,
        "shows": alldict,
        "confirmable": conf_bool,
        "num_shows": len(confirmable),
        "confirmables": confirmable,
        "confirmables2": cconfirmables,
        "updated": str(now),
    }
    # print(olddict)

    # print(alldict)
    import json

    json_object = json.dumps(s, indent=4)
    if cache == True:
        x = open(ad + "/jason_show_cache_fake.json", "w")
    if cache == False:
        x = open(ad + "/jason_show_cache_real.json", "w")
    x.write(json_object)


def get_json_schedule(x, ad):

    # import libs.lib_think

    # print(x["usecache"], "usecache!!!")
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        print("USING CACHE DATA OK?")
        show = "jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        print("USING Real DATA OK?")
        show = "jason_show_cache_real.json"
        if (
            x["refreshreload"] == "True"
            or x["refreshreload"] == True
            or x["refreshreload"] == "true"
        ):
            # print("forcing new data", type(x["refreshreload"]))
            make_json_schedule(x, ad)
            # good_login = lib_think.login(ad, x, "True", App)
    data = get_json_schedule_2(x, ad, show)
    return data


def get_json_schedule_1(x, ad):

    # import libs.lib_think

    # print(x["usecache"], "usecache!!!")
    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        print("USING CACHE DATA OK?")
        show = "jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        print("USING Real DATA OK?")
        show = "jason_show_cache_real.json"
        if (
            x["refreshreload"] == "True"
            or x["refreshreload"] == True
            or x["refreshreload"] == "true"
        ):
            print("forcing new data", type(x["refreshreload"]))
            # make_json_schedule(x, ad)
            # good_login = lib_think.login(ad, x, "True", App)
    data = get_json_schedule_2(x, ad, show)
    return data


def get_json_schedule_2(x, ad, show):
    import json, os

    try:

        from datetime import datetime, timedelta

        nf = os.path.join(ad, show)
        with open(nf) as json_file:
            data = json.loa2d(json_file)
            # print(data)
            print("LOADED JSON FILE SUPER FAST")
    except:
        print("no " + show + "  Createing now")
        print("forcing new data", type(x["refreshreload"]))
        if x["refreshreload"] == True:
            make_json_schedule(x, ad)
        nf = os.path.join(ad, show)
        try:
            with open(nf) as json_file:
                data = json.load(json_file)
                # print(data)
                print("LOADED JSON FILE SUPER FAST on second try")
        except:
            make_json_schedule(x, ad)
            with open(nf) as json_file:
                data = json.load(json_file)
                # print(data)
                print("LOADED JSON FILE SUPER FAST on second try")

    return data


def just_get_json_schedule(x, ad):
    import json, os

    if x["usecache"] == "True" or x["usecache"] == True or x["usecache"] == "true":
        print("USING CACHE DATA OK?")
        show = "/jason_show_cache_fake.json"

    if x["usecache"] == "False" or x["usecache"] == False or x["usecache"] == "false":
        print("USING Real DATA OK?")
        show = "/jason_show_cache_real.json"

    nf = os.path.join(ad, show)

    nf = ad + "/" + show

    # print(nf, ad, "WTF MAN")

    with open(nf) as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":
    # parse("sch", "ad", False)
    from kivy.app import App

    ad = "C:/Users/kw/AppData/Roaming/demo3/"
    import lib_readuserdata

    x = lib_readuserdata.readuserdata("", ad, False)
    get_json_schedule(x, ad)
    # parsepayperiod, ("C:/Users/kw/AppData/Roaming/demo3/pp/")
