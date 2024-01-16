import os
import mechanize
import ssl
import urllib
import string
import json
from bs4 import BeautifulSoup

try:
    import lib_enc
except:
    import libs.lib_enc


def check_fav_note(ad, note):
    f = "j_notes.json"

    try:
        o = open(ad + "/" + f)
        print("opened json file")
    except:
        print("cant find position list", os.getcwd())
        return {}
    data = json.load(o)
    o.close()
    for j in range(len(data)):
        if note == int(data[j]["num"]):
            return data[j]["star"]


def toggle_fav_note(ad, note):
    f = "j_notes.json"

    try:
        o = open(ad + "/" + f)
        print("opened json file")
    except:
        print("cant find position list", os.getcwd())
        return {}
    data = json.load(o)
    o.close()
    for j in range(len(data)):
        if note == int(data[j]["num"]):
            # print(data[j]["title"])
            if (data[j]["star"]) == True:
                (data[j]["star"]) = False
            else:
                (data[j]["star"]) = True
            print((data[j]["star"]), "star toggle saving")

    out_file = ad + "/j_notes.json"
    with open(out_file, "w") as ofile:
        json.dump(data, ofile, indent=4)
    ofile.close()


def get_notes(x, ad, search):
    f = "j_notes.json"
    # print
    # print(ad, "get positions", x)
    try:
        o = open(ad + "/" + f)
        print("opened json file")
    except:
        print("cant find position list", os.getcwd())
        return {}
    data = json.load(o)

    xx = [element for element in data if search.lower() in element["title"].lower()]
    if x["fav_notes"] == True:
        xxx = []
        for p in range(len(xx)):
            if xx[p]["star"] == True:
                xxx.append(xx[p])
        return xxx

    return xx


def make_notes(ad, city):
    import json

    l_notes = []

    conf = "/fullwebsite.html"
    z = open(ad + conf, "r", encoding="utf8")
    soup = BeautifulSoup(z, "html.parser")
    name = soup.find("span", id="lblFieldNotes")
    # print(name, type(name), len(name))
    # for z in name:
    # print(name[z])
    if name.has_attr("ul"):
        print(name["ul"])
    # print(name)
    name = name.find_all("li")
    # print(name, type(name), len(name))
    uu = "https://www.thinkrhino.com/employee/" + city["city"] + "/"
    for x in range(len(name)):
        d_notes = {}
        a = str.split(str(name[x]), '"')
        a = a[1]
        i = str.split(a, "=")
        print(name[x], a)
        d_notes.update({"title": name[x].text})
        d_notes.update({"url": uu + a})
        d_notes.update({"star": False})
        d_notes.update({"num": i[1]})

        l_notes.append(d_notes)

    # print(city["city"], l_notes)

    out_file = ad + "/j_notes.json"
    with open(out_file, "w") as ofile:
        json.dump(l_notes, ofile, indent=4)


def get_picture(pic):
    # print(pic)
    pic2 = str.split(pic, "/")
    pic2 = pic2[len(pic2) - 1]
    # print(pic2)

    bad = [
        "logo.png",
        "slider_01.jpg",
        "backtorhino_button_on.gif",
        "ad_gearwear_full2017.png",
    ]
    flag = True
    for z in range(len(bad)):
        # print(pic2, bad[z])
        if pic2 == bad[z]:
            flag = False
    if flag == True:
        # print(pic, "PICTURES DO YOU KNOW")
        return "https://www.thinkrhino.com/" + pic, pic2
    return ("", "")

    # aimg = AsyncImage(source='http://mywebsite.com/logo.png')


def word(text):
    print(type(text))
    text = str(text)
    print(text, "wtf")


def weird(z, id, ad):
    print(z, "hello")
    z2 = open(ad + "/fn/" + id + ".htm", "w")
    bad = [
        "UnhideWhenUsed=",
        "<w:LsdException",
        "mso-spacerun",
        "MsoNormal",
        "mso-style",
    ]
    for line in z.readlines():
        for y in range(len(bad)):
            if bad[y] in line:
                line = ""
        z2.write(line)
    z2.close()
    z2 = open(ad + "/fn/" + id + ".html", "r")
    return z2


def get_single3(x, ad, title, link, id, browser):
    print(title, link, id, "these are the 3 field notes")
    try:
        aaa = open(ad + "/fn/" + id + ".html", "r")
    except:
        # need to download this file
        print(browser, "BROWSER!!")
        browser = dl_fieldnote(x, ad, link, browser, id)

    # aaa = open(ad + "/fn/" + id + ".html", encoding="utf8")
    # z = ""
    # for line in aaa.readlines():
    #    z = z + line

    z = open(ad + "/fn/" + id + ".html", encoding="utf8")
    2697
    dumb = ["356", "2697"]
    for yy in range(len(dumb)):
        if id == dumb[yy]:
            print("why")
            z = weird(z, id, ad)
    soup = BeautifulSoup(z, "html.parser")
    # word(BeautifulSoup(z2, "xml"))

    name = soup.find("div", attrs={"class": "content"})
    # name = soup.find("div")
    bad = [
        # "div",
        "a",
        # "font",
        "iframe",
        # "strong",
        "br",
        "font color",
    ]
    # attachment
    # attachment

    img = soup.find_all("img")
    # img = soup.find("a href", attrs={"class": "attachment"})
    pic = ""
    pic_url = ""

    for y in range(len(img)):
        # if "uploads" in img[y]:
        # print(img[y], "IMG do")
        pp = img[y]
        # print(dir(pp), type(pp), pp.text, "IMG do")
        im = pp.get("src")
        print(im, "pictures")
        pic_url2, pic2 = get_picture(im)
        if len(pic2) > len(pic):
            pic = pic2
            pic_url = pic_url2

    # print(name, "NAME!!!")
    for x in range(0, len(bad)):
        for s in name.select(bad[x]):
            s.extract()
    # print(name, "NAMETEXT")
    name = str(name)

    bs = [
        "<",
        "[",
        ">",
        "]",
        "strong",
        "b",
        "<br>",
        "\n",
        "<br/>",
        "",
        '[div class="content"]',
        "",
        '[span id="notes"]',
        "",
        "[p]",
        "",
        "[/p]",
        "\n",
        '[span id="title"]',
        "",
        '[font color="brown"]',
        "",
        "[/font]",
        "",
        "[/span]",
        "",
        '[div style="text-align: center;"]',
        "",
        '[font size="5"]',
        "",
        "[/div]",
        "\n",
        "[div]",
        "",
        '[hr size="2" width="100%"/]',
        "",
        '[div class="divider"]',
        "",
        "[dt]",
        "",
        "[/dt]",
        "",
        "[dd]",
        "",
        "[/dd]",
        "",
        '[div style="text-align: center; "]',
        "",
        '[span id="attachmentlabel"]',
        "",
        "Attached File:",
        "",
        "[ol]",
        "",
        "[li]",
        "",
        "[/ol]",
        "",
        "[/li]",
        "",
        '[font color="green"]',
        "",
        '[font size="4"]',
        "",
        '[blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;"]',
        "\n",
        "[/blockquote]",
        "\n",
        '[font color="orange"]',
        "",
        "*",
        "-",
        '[blockquote class="webkit-indent-blockquote" style="margin: 0 0 0 40px; border: none; padding: 0px;"]-',
        "",
        '[blockquote class="webkit-indent-blockquote" style="margin: 0 0 0 40px; border: none; padding: 0px;"]',
        "",
        '[div align="center"]',
        "",
        '[font color="#a52a2a"]',
        "",
    ]

    for x in range(0, len(bs), 2):
        # print(bs[x], "wtf2222")
        name = str.replace(name, bs[x], bs[x + 1])
    # print(name, "mnaas")
    return browser, name, pic_url, pic, ""


def get_single(x, ad, title, link, id, browser):
    import os

    login = True
    reason = ""
    print(title, link, id, "these are the 3 field notes")
    try:
        aaa = open(ad + "/fn/" + id + ".html", "r")
        aaa.close()
        print("read fine")
    except:
        # need to download this file
        print(browser, "BROWSER!! downloading file cause reasons")
        browser = dl_fieldnote(x, ad, link, browser, id)

    # aaa = open(ad + "/fn/" + id + ".html", encoding="utf8")
    # z = ""
    # for line in aaa.readlines():
    #    z = z + line

    z = open(ad + "/fn/" + str(id) + ".html", encoding="utf8")
    toast_fail = ""
    zz = os.path.getsize(ad + "/fn/" + str(id) + ".html")
    print(zz, "size")
    for line in z.readlines():
        if "er your information be" in line:
            print("not logged in you dumbbb")
            # login failed
            login = False
            z.close()
            reason = "not logged in"
            toast_fail = toast_fail + reason
    if zz == 0:
        print("file failed to dl")
        #
        toast_fail = toast_fail + "broken file "
        login = False
    if login == False:
        browser = dl_fieldnote(x, ad, link, browser, id)
        print("file failed to dl")
    z.close()
    z = open(ad + "/fn/" + str(id) + ".html", encoding="utf8")

    dumb = ["356", "2697"]
    for yy in range(len(dumb)):
        if id == dumb[yy]:
            print("why")
            # z = weird(z, id, ad)
    soup = BeautifulSoup(z, "html.parser")
    # print(soup.text, "soup.text")
    # print(soup, "SOUP")
    # word(BeautifulSoup(z2, "xml"))

    name = soup.find("div", attrs={"class": "content"})
    # name = soup.find("div")
    # print(name.text, "NAMEEE")
    bad = [
        # "div",
        "a",
        # "font",
        "iframe",
        # "strong",
        "br",
        "font color",
    ]
    # attachment
    # attachment

    img = soup.find_all("img")
    # img = soup.find("a href", attrs={"class": "attachment"})
    pic = ""
    pic_url = ""

    for y in range(len(img)):
        # if "uploads" in img[y]:
        # print(img[y], "IMG do")
        pp = img[y]
        # print(dir(pp), type(pp), pp.text, "IMG do")
        im = pp.get("src")
        # print(im, "pictures")
        pic_url2, pic2 = get_picture(im)
        if len(pic2) > len(pic):
            pic = pic2
            pic_url = pic_url2

    # print(name, "NAME!!!")
    for x in range(0, len(bad)):
        for s in name.select(bad[x]):
            s.extract()
    # print(name, "NAMETEXT")
    name = str(name)

    bs = [
        "<",
        "[",
        ">",
        "]",
        "strong",
        "b",
        "<br>",
        "\n",
        "<br/>",
        "",
        '[div class="content"]',
        "",
        '[span id="notes"]',
        "",
        "[p]",
        "",
        "[/p]",
        "\n",
        '[span id="title"]',
        "",
        '[font color="brown"]',
        "",
        "[/font]",
        "",
        "[/span]",
        "",
        '[div style="text-align: center;"]',
        "",
        '[font size="5"]',
        "",
        "[/div]",
        "\n",
        "[div]",
        "",
        '[hr size="2" width="100%"/]',
        "",
        '[div class="divider"]',
        "",
        "[dt]",
        "",
        "[/dt]",
        "",
        "[dd]",
        "",
        "[/dd]",
        "",
        '[div style="text-align: center; "]',
        "",
        '[span id="attachmentlabel"]',
        "",
        "Attached File:",
        "",
        "[ol]",
        "",
        "[li]",
        "",
        "[/ol]",
        "",
        "[/li]",
        "",
        '[font color="green"]',
        "",
        '[font size="4"]',
        "",
        '[blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;"]',
        "\n",
        "[/blockquote]",
        "\n",
        '[font color="orange"]',
        "",
        "*",
        "-",
        '[blockquote class="webkit-indent-blockquote" style="margin: 0 0 0 40px; border: none; padding: 0px;"]-',
        "",
        '[blockquote class="webkit-indent-blockquote" style="margin: 0 0 0 40px; border: none; padding: 0px;"]',
        "",
        '[div align="center"]',
        "",
        '[font color="#a52a2a"]',
        "",
        '[p class="MsoNormal" style="margin: 0in;"]',
        "",
        '[p class="MsoNormal" style="margin: 0in 0in 0.0001pt; font-family: Cambria;"]',
        "",
        '[img src="/uploads/AC0opentp.jpg" width="450"/]',
        "",
        '[font face="Georgia" size="4"]',
        "",
        '[span style="font-family: Georgia; font-size: large;"]',
        "",
        '[font color="purple"]',
        "",
    ]

    for x in range(0, len(bs), 2):
        # print(bs[x], "wtf2222")
        name = str.replace(name, bs[x], bs[x + 1])
    # print(name, "mnaas")
    return browser, name, pic_url, pic, toast_fail


def dl_fieldnote(x, ad, note, browser, id):
    print("thinkpp", x)

    # USERNAME
    import ssl

    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    ssl._DEFAULT_CIPHERS = "DES-CBC3-SHA"

    PE_first = "https://www.thinkrhino.com/employee/lasvegas/index.aspx"
    PE_second = note

    pp = str(id) + ".html"
    try:
        aaa = open(ad + "/fn/" + pp, "wb")
    except:
        os.mkdir(ad + "/fn/")
        aaa = open(ad + "/fn/" + pp, "wb")
    # aaa.close()
    print(browser, "BROWSER!!!")
    if browser == "":
        print("logging in for real")
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.set_handle_equiv(False)
        browser.addheaders = [
            (
                "User-agent",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
            )
        ]
        browser.open(PE_first)

        try:
            browser.select_form(name="ctl00")
        except:
            browser.select_form(nr=0)
        browser["emailaddress"] = x["username"]
        try:
            browser["mypassword"] = libs.lib_enc.r_password(x["password"])
        except:
            browser["mypassword"] = lib_enc.r_password(x["password"])

        res = browser.submit()

        # aa = res.get_data()
        # print (aa)
    else:
        print(browser, "what is this thing even for")

    res = browser.open(PE_second)

    aa = res.read()
    # print (aa)

    aaa.write((aa))
    aaa.close()

    return browser


if __name__ == "__main__":
    bbb = {
        "title": "T-Mobile Arena",
        "url": "https://www.thinkrhino.com/employee/lasvegas/fieldnote.aspx?id=2659",
        "star": False,
        "num": "3041",
    }

    ##tma=2659
    ##fucked up 356

    # 2024=3041
    ad = "C://Users//twat//AppData//Roaming//demo3"
    # make_notes(ad, {"city": "lasvegas"})
    # x = get_notes(ad, "")
    # print(x)
    x = {
        "username": "kevincwulff@gmail.com",
        "password": "b'YmxpbmsxODI='",
        "city": "lasvegas",
    }
    get_single(x, ad, bbb["title"], bbb["url"], bbb["num"], "")
    # toggle_fav_note(ad, 3041)
