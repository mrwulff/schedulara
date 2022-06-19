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
    ach_level = 0
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
        "ach_level": 0,
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
        "ach_level": 0,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": "Dates:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "calendar-sync",
        "ach_graph_disc": ["###:", "Date:"],
    }

    hourly = {
        "name": "Celery man!",
        "disc": "Work 18 Hours on a single call",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 0,
        "ach_color": "Who's green, gets no overtime pay and snaps easily?",
        "ach_shows": ach_shows,
        "ach_extra": "Most Hours:",
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
        "ach_icon": "clock-time-four",
        "ach_graph_disc": ["Hours:", "Show", "Date:"],
    }

    ach = [hats, grind, hourly]

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

    size = 1
    max_size = 0
    listshows = []
    mshows = []
    for i in range(len(myList) - 1):
        # print(myList[i][0], myList[i + 1][0], myList[i][1])

        if myList[i + 1][0] - 1 == myList[i][0] or myList[i + 1][0] == myList[i][0]:
            if myList[i + 1][0] - 1 == myList[i][0]:

                size += 1
            # print("omg")
            listshows.append(myList[i])
        else:
            size = 1
            # print("fail")
            listshows = []
        # print(size)
        if max_size < size:
            # print(size)
            date = myList[i]
            max_size = size
            mshows = listshows

    return max_size, date, mshows


def check_hats(self, ad):
    print("checking hats")
    points = 0
    import datetime
    import libs.lib_makegraphs as lib_makegraphs

    new_start = datetime.datetime.now()
    new_finish = datetime.datetime.now() - datetime.timedelta(days=10365)
    h, h2, days, hours = lib_makegraphs.parsepp(
        self,
        ad,
        "hats",
        new_start,
        new_finish,
    )
    hours.sort(key=lambda x: x[0], reverse=True)
    top_hours = []
    # print(hours, "hourssss")
    if len(hours) > 5:
        for aaa in range(5):
            top_hours.append(hours[aaa])

    import json
    from collections import Counter

    # print(Counter(h2))
    days.sort()
    import itertools

    # print(days)
    xx, date, shows = longestrun(days)
    # print(xx, shows, "whtdcfuck")
    # for i in range(len(days)):
    #    print(days[i][0])

    f = open(ad + "/testtest22.json")
    data = json.load(f)

    ###hats
    data["children"][0]["ach_shows"] = Counter(h2)
    data["children"][0]["ach_progress"] = len(h)

    if len(h) > 10:
        if data["children"][0]["achieved"] == "False":
            data["children"][0]["date_achieved"] = str(datetime.date.today())

        data["children"][0]["achieved"] = "True"
        data["children"][0]["ach_level"] = 10

    ###hustle
    if len(shows) > 14:
        if data["children"][1]["achieved"] == "False":
            data["children"][1]["date_achieved"] = str(datetime.date.today())

        data["children"][1]["achieved"] = "True"
        data["children"][1]["ach_level"] = 10
    data["children"][1]["ach_shows"] = shows
    data["children"][1]["ach_progress"] = len(shows)

    ###hours_ach
    if hours[0][0] > 18:
        print("ach unlocked!!!")
        if data["children"][2]["achieved"] == "False":
            data["children"][2]["date_achieved"] = str(datetime.date.today())
        data["children"][2]["achieved"] = "True"
        data["children"][2]["ach_level"] = 10
        data["children"][2]["ach_shows"] = top_hours
        data["children"][2]["ach_progress"] = hours[0][0]

    json_object = json.dumps(data, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


if __name__ == "__main__":
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # list_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    check_hats("", "C:/Users/kw/AppData/Roaming/demo3/")
