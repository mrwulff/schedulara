def get_positions(ad, search):
    import os
    import shutil
    import json

    f = "position_list.json"
    # print
    # print(ad, "get positions")
    try:
        o = open(ad + "/" + f)
        print("opened json file")
    except:
        pass
        print("cant find position list", os.getcwd())
        shutil.copyfile(f, ad + "/" + f)
        o = open(ad + "/" + f)
        print("opened json file")
    data = json.load(o)
    # print(
    #    data["positions"], len(data["positions"]), type(data["positions"]), "DATATATA"
    # )
    # xx = filter(lambda person: person["abv"] == "V", data)

    xx = [element for element in data["positions"] if search.lower() in element["all"]]
    print(len(xx), search, "xx", len(data["positions"]))
    return xx


def edit(ad):
    import json

    f = "position_list.json"
    f2 = "poslist.json"
    # print
    # print(ad, "get positions")

    o = open(ad + "/" + f)
    data = json.load(o)["positions"]
    for i in range(len(data)):
        print(data[i])
        data[i]["all"] = data[i]["abv"] + " " + data[i]["description"]
        data[i]["all"] = data[i]["all"].lower()
    print(data)
    with open(f2, "w") as ofile:
        json.dump(data, ofile, indent=4)


if __name__ == "__main__":
    # get_positions("C://Users//twat//schedulara", "")
    edit("C://Users//twat//schedulara")
