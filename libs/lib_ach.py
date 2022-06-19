def list_ach(ad):
    import json

    f = open(ad + "/testtest22.json")
    data = json.load(f)
    print(data["children"][0])
    print(len(data["children"]))
    return data["children"]


def make_ach(ad):
    import json

    response_json = {}
    response_json["name"] = "ach"

    # where your children list will go
    children = []

    size = 500  # or whatever else you want

    # For each item in your original list

    # children.append({"name": "name", "size": size})
    # children.append({"name": "name", "size": size})

    ach_name = "Test"
    ach_disc = "This is just a test"
    achieved = "False"
    date_achieved = "0"
    ach_level = 5
    ach_color = "Black"
    ach_shows = dict()
    ach_extra = "none"
    ach_hidden = "False"
    ach_progress = 0
    ach_icon = "lock-alert"
    ach_graph_disc = []

    # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    hats = {
        "name": "Wear The Hat",
        "disc": "Work 10 different Positions",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 10,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": "Positions:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "account-cowboy-hat",
        "ach_graph_disc": ["Percent:", "Position:", "###:"],
    }

    grind = {
        "name": "Hustle and Grind",
        "disc": "Work 14 days in a Row",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 10,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": "Dates:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "calendar-sync",
        "ach_graph_disc": ["###:", "Date:"],
    }
    ach = [hats, grind]

    for iii in range(len(ach)):
        children.append(ach[iii])

    for i in range(10):
        tot_ach = {
            "name": ach_name + " " + str(i),
            "disc": ach_disc,
            "achieved": achieved,
            "date_achieved": date_achieved,
            "ach_level": ach_level,
            "ach_color": ach_color,
            "ach_shows": ach_shows,
            "ach_extra": ach_extra,
            "ach_hidden": ach_hidden,
            "ach_progress": ach_progress,
            "ach_icon": ach_icon,
            "ach_graph_disc": ach_graph_disc,
        }

        children.append(tot_ach)

    response_json["children"] = children

    json_object = json.dumps(response_json, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


def longestrun(myList):
    sett = set()
    size = 1
    for ind, elm in enumerate(myList):
        print("bigger")
        if ind > 0:
            if elm == myList[ind - 1]:
                size += 1
            else:
                sett.update([size])
                size = 1
    sett.update([size])
    return max(sett)


def check_hats(self, ad):
    print("checking hats")
    import datetime
    import libs.lib_makegraphs as lib_makegraphs

    new_start = datetime.datetime.now()
    new_finish = datetime.datetime.now() - datetime.timedelta(days=10365)
    h, h2, days = lib_makegraphs.parsepp(
        self,
        ad,
        "hats",
        new_start,
        new_finish,
    )
    import json
    from collections import Counter

    # print(Counter(h2))
    days.sort()
    import itertools

    print(days)
    xx = longestrun(days[0])
    print(xx, "whtdcfuck")
    # for i in range(len(days)):
    #    print(days[i][0])

    f = open(ad + "/testtest22.json")
    data = json.load(f)
    # print(data["children"][0], "data0")
    data["children"][0]["ach_shows"] = Counter(h2)
    data["children"][0]["ach_progress"] = len(h)
    if len(h) > 14:
        if data["children"][0]["achieved"] == "False":
            data["children"][0]["date_achieved"] = str(datetime.date.today())

        data["children"][0]["achieved"] = "True"

    json_object = json.dumps(data, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


if __name__ == "__main__":
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # list_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    check_hats("", "C:/Users/kw/AppData/Roaming/demo3/")
