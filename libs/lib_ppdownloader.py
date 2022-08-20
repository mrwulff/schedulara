import os
import mechanize
import ssl
import urllib
import string


def open_files():
    f = os.listdir("pp")
    print(f)
    print(type(f))
    print(len(f))
    for i in range(1):
        # for i in range(len(f)):

        print(f[i])
        a = open("pp/" + f[i], "r")
        for line in a.readlines():
            # print (line)
            if 'cell-noborder">' in line:
                print(line)


def doublefake():
    global browser
    global response
    print("doublefake")

    url = "http://127.0.0.1:8000/list.html"
    url = urllib.parse.unquote(url)
    br = mechanize.Browser()

    br.set_handle_robots(False)
    br.set_handle_equiv(False)

    br.open(url)

    aa = "test2.html"

    g = find_paychecks(str(aa))

    for i in range(len(g)):
        # print (g[i][1])
        try:
            mm = open(g[i][1] + ".htm1l", "r")
            print(g[i][1] + "opened successful")
        except:
            print(g[i][1] + "opened failed")

            br.select_form(name="ctl00")
            control_a = br.form.find_control("__EVENTARGUMENT")
            control_vs = br.form.find_control("__VIEWSTATE")

            control_g = br.form.find_control("__VIEWSTATEGENERATOR")
            control_va = br.form.find_control("__EVENTVALIDATION")

            br.select_form(name="ctl00")

            control_t = br.form.find_control("__EVENTTARGET")

            control_t.readonly = False

            control_t.value = g[i][1]

            response = br.response()
            aa = response.get_data()
            aaa = open(g[i][1] + ".html", "wb")
            aaa.write((aa))
            aaa.close()


def find_paychecks(a, ad):
    print("find_paychecks")
    print(a)
    b = open(ad + "/" + a, "r")
    c = []
    for line in b.readlines():
        c.append(line)
    g = []
    print(len(c))
    for d in range(len(c)):
        if 'aystub" href="javascript' in c[d]:
            # print (c[d],'FOUND ONE BOSS!')
            print(c[d])

            e = str.split(c[d], "'")
            url = e[1]
            f = str.split(c[d + 1], ">")
            # print (len(f))
            if len(f) > 3:
                # print (f[2])
                date, junk = str.split(f[2], "<")
                date = str.replace(date, "/", "-")
                links = (url, date)
                g.append(links)
    return g


def thinkpp(x, ad):
    print("thinkpp", x)
    import libs.lib_enc

    # USERNAME
    import ssl

    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    ssl._DEFAULT_CIPHERS = "DES-CBC3-SHA"

    # PE_LOGIN = 'http://www.thinkrhino.com/employee/lasvegas/'
    PE_LOGIN = "https://www.thinkrhino.com/employee/lasvegas/index.aspx"
    PE_COUNTRIES = "payperiods.aspx"

    pp = "test2.html"
    try:
        aaa = open(ad + "/" + pp, "wb")
    except:
        os.mkdir(ad + "/pp")
        aaa = open(ad + "/" + pp, "wb")
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    browser.open(PE_LOGIN)

    browser.select_form(name="ctl00")
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = libs.lib_enc.r_password(x["password"])
    # print (browser)
    # print browser.title

    res = browser.submit()

    aa = res.get_data()
    # print (aa)

    res = browser.open(PE_COUNTRIES)

    aa = res.read()
    # print (aa)

    aaa.write((aa))
    aaa.close()
    g = find_paychecks(pp, ad)

    browser.select_form(name="ctl00")
    found = 0
    for z in range(len(g)):
        # for z in range(2):
        try:
            aaa = open(ad + "/pp" + "/" + g[z][1] + ".html", "r")
            print("found " + g[z][1])
            found = found + 1
        except:
            try:
                aaa = open(ad + "/pp" + "/" + g[z][1] + ".html", "wb")
            except:
                os.mkdir(ad + "/pp")
                aaa = open(ad + "/pp" + "/" + g[z][1] + ".html", "wb")

            browser.select_form(name="ctl00")

            control_t = browser.form.find_control("__EVENTTARGET")
            control_t.readonly = False
            # control_t.value='dgResults$ctl02$btn_Paystub'
            control_t.value = g[z][0]
            # print (g[z][0], type(g[z][0]),'gz')
            # print (type(g[z][0]))
            # control_t.value=g[z][0]
            # print (control_t.value,type(control_t.value),'value')

            res = browser.submit()

            request = browser.request
            # print (request.header_items())

            aa = res.get_data()

            aaa.write((aa))
            print("Downloaded from server " + g[z][1])
            aaa.close()
            browser.open(PE_COUNTRIES)
    return len(g), len(g) - found


def get_files():
    # print('getting files from live site')
    # think()

    # doublefake()

    think()
    open_files()


def main():
    get_files()


# main()
