import requests
import json


def submit(name, score, ach, ad):
    # https://www.highscores.ovh/
    import hashlib

    print(name, score, ach)
    # appid = ["d6073280-f7af-4082-8b33-0356d7068f51"]
    # secret = ["073276b2-4940-40f0-87cc-7e4805382cd0"]
    # secret = ["8b1d0ff7-8176-4142-bbfc-06594a61de83"]
    # f = open(ad + "/ids22.json")
    try:
        f = open(ad + "/ids22.json")
    except:
        print("failed to get scoretables. downloading now")

        import libs.lib_ach

        libs.lib_ach.download_ach(ad)
        try:
            f = open(ad + "/ids22.json")
        except:
            print("failed to get scoretables(submit)")

        return "failed to get json"
    data = json.load(f)
    appid = data["children"][ach]["appid"]
    secret = data["children"][ach]["secret"]

    print(appid, secret)

    # print(data)
    pid = name

    check = str(pid) + "" + str(score) + "" + str(secret)
    check = check.encode()
    print(check)
    check2 = hashlib.md5(check)

    (check2) = check2.hexdigest()
    print(check2)

    url = (
        "https://www.highscores.ovh/api/highscore?appId="
        + appid
        + "&playerId="
        + str(pid)
        + "&playerName="
        + name
        + "&score="
        + str(score)
        + "&checksum="
        + str(check2)
    )
    print(url)
    x = requests.post(url)

    print(dir(x))
    sc = x.status_code

    if sc == 200:
        print("SUCCESS!!!")
    if sc != 200:
        print(sc, x, x.content, x.raw)

    # url = "https://www.highscores.ovh/api/highscore?appId=<appId>playerId=<payerId>&playerName=<playerName>&score=<score>&checksum=<checksum>"


def dl_score(name, ach, ad):
    import json

    try:
        f = open(ad + "/ids22.json")
    except:
        print("failed to get scoretables. trying to download")
        import libs.lib_ach

        libs.lib_ach.download_ach(ad)
        try:
            f = open(ad + "/ids22.json")
        except:
            print("failed to get scoretables (dlscore)")
            return "fail"

    data = json.load(f)
    appid = data["children"][ach]["appid"]

    # appid = ["d6073280-f7af-4082-8b33-0356d7068f51"]

    url = (
        "https://www.highscores.ovh/api/highscore?appId=" + appid + "&playerId=" + name
    )
    print(url)
    x = requests.get(url)
    sc = x.status_code
    print(sc)
    content = x.content

    content = content.decode("UTF-8")
    # print(content)
    content = json.loads(content)

    # with open(ad + "data.json", "w") as f:
    #    json.dump(content, f)

    json_object = json.dumps(content, indent=4)
    x = open(ad + "/scores" + str(ach) + ".json", "w")
    x.write(json_object)
    print("downloaded score table: " + str(ach))
    return "success"


def clamp(x):
    return max(0, min(x, 255))


def parse_score(name, ach, ad, color):
    try:

        f = open(ad + "/scores" + str(ach) + ".json")
    except:
        dl_score(name, ach, ad)
        f = open(ad + "/scores" + str(ach) + ".json")

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    # print(data)
    x = []
    y = []
    q = []
    num = 0
    # color = [0, 0, 0, 1]
    color0 = int(color[0] * 255)
    color1 = int(color[1] * 255)
    color2 = int(color[2] * 255)
    ip = data["currentPlayerScore"]
    print(ip, "ipipipip", data)
    newc = "#{0:02x}{1:02x}{2:02x}".format(clamp(color0), clamp(color1), clamp(color2))
    for i in data["topScores"]:
        x = [i["score"], i["playerName"], i["placement"]]
        # q = str(i["score"]) + "," + str(i["playerName"]), +"," + str(i["placement"])
        q.append(i["score"])
        if i["playerName"].lower() == name.lower():
            print("wtf" + i["playerName"], name + "wtf")

            q.append("[b][color=" + newc + "]" + i["playerName"] + "[/b][/color]")
        else:
            q.append(i["playerName"])

        if num == 0:
            q.append(["numeric-1-circle", [255 / 256, 165 / 256, 0, 1], ""])
        if num == 1:
            q.append(["numeric-2-circle", [100, 100, 100, 1], ""])
        if num == 2:
            q.append(["numeric-3-circle", [50, 127, 250, 1], ""])
        if num > 2:
            q.append(i["placement"])
        # print(x)
        y.append(x)
        num = num + 1

    try:
        x = [ip["score"], ip["playerName"], ip["placement"]]
        # print(x)
        # print(x)
        print(x[2], "wtf placement", x)

        if x[2] > 10:
            y.append(x)

            q.append(str(ip["score"]))
            q.append("[b][color=" + newc + "]" + ip["playerName"] + "[/b][/color]")
            q.append(str(ip["placement"]))
        print(y, "scoremofo")
        return y, str(x[2]), q
    except:
        return y, "fail", q


if __name__ == "__main__":
    ad = "C:/Users/kw/AppData/Roaming/demo3"
    # submit("kevin wulff bad", 0, 0)
    # dl_score("kevin wulff", 0, ad)
    # parse_score(
    #    "kevin wulff bad", 0, "C:/Users/kw/AppData/Roaming/demo3", [50, 127, 250, 1]
    # )
    # submit("kevin wulff", 300, 0, ad)
    pass
