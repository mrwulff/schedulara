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
    ach_shows = []
    ach_extra = "none"
    ach_hidden = "False"
    ach_progress = 0

    # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

    hats = {
        "name": "Wear The Hat",
        "disc": "Work 10 different Positions",
        "achieved": achieved,
        "date_achieved": date_achieved,
        "ach_level": 10,
        "ach_color": ach_color,
        "ach_shows": ach_shows,
        "ach_extra": ach_extra,
        "ach_hidden": ach_hidden,
        "ach_progress": ach_progress,
    }
    children.append(hats)

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
        }

        children.append(tot_ach)

    response_json["children"] = children

    json_object = json.dumps(response_json, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


def check_hats(self, ad):
    print("checking hats")
    import datetime
    import libs.lib_makegraphs as lib_makegraphs

    new_start = datetime.datetime.now()
    new_finish = datetime.datetime.now() - datetime.timedelta(days=10365)
    h, h2 = lib_makegraphs.parsepp(
        self,
        ad,
        "hats",
        new_start,
        new_finish,
    )
    import json

    f = open(ad + "/testtest22.json")
    data = json.load(f)
    print(data["children"][0], "data0")
    data["children"][0]["ach_shows"] = h
    data["children"][0]["ach_progress"] = len(h)
    if len(h) > 14:
        if data["children"][0]["achieved"] == "False":
            data["children"][0]["date_achieved"] = str(datetime.datetime.now().date)

        data["children"][0]["achieved"] = "True"

    json_object = json.dumps(data, indent=4)
    x = open(ad + "/testtest22.json", "w")
    x.write(json_object)


if __name__ == "__main__":
    # make_ach("C:/Users/kw/AppData/Roaming/demo3/")
    # list_ach("C:/Users/kw/AppData/Roaming/demo3/")
    make_ach("C:/Users/kw/AppData/Roaming/demo3/")
