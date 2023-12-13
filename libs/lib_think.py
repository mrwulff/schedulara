def login(ad, x, ios, App):
    import mechanize
    import ssl
    import libs.lib_enc

    if ios == True:
        app = App.get_running_app()
        ad = app.user_data_dir
    # print (x)

    print("using real data")
    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    print("using real data66")

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_COUNTRIES = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"

    # USERNAME = c.text
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # aaa=open(dir_path+'/test2.html','wb')
    # global browser
    browser = mechanize.Browser()

    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    # print (PE_LOGIN,'PE_LOGIN')
    if 1 == 1:
        # try:
        browser.open(PE_LOGIN)
        print("browser=open")
    # except:
    print("using real data669")
    #    return False
    browser.select_form(name="ctl00")
    # print (x['username'],x['password'])
    # print (type(x['username']),type(x['password']))
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = browser["mypassword"] = libs.lib_enc.r_password(
        x["password"]
    )

    res = browser.submit()

    res = browser.open(PE_COUNTRIES)

    aa = res.get_data()  # HTML source of the page
    # print (aa)
    b2 = open(ad + "/realdata.html", "wb")
    print("using real data66")

    b2.write(aa)

    b2.close()
    print("login success")
    return True
    # except:
    #    print ('login failed')
    #    return False


def openbrowser(ad, x, ios, App):
    import ssl
    import os
    import mechanize
    import libs.lib_enc

    ssl.verify = False

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_SCHEDULE = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"

    dir_path = os.path.dirname(os.path.realpath(__file__))
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

    res = browser.submit()

    res = browser.open(PE_SCHEDULE)
    return browser


def login_basic(ad, x, App):
    import mechanize
    import ssl
    import libs.lib_enc

    app = App.get_running_app()
    ad = app.user_data_dir
    # print (x)

    print("using real data")
    ssl.verify = False
    ssl._create_default_https_context = ssl._create_unverified_context
    print("using real data66")

    PE_LOGIN = "https://www.thinkrhino.com/employee/" + x["city"] + "/index.aspx"
    PE_COUNTRIES = "https://www.thinkrhino.com/employee/" + x["city"] + "/Schedule.aspx"
    print("using real data67")
    # USERNAME = c.text
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # aaa=open(dir_path+'/test2.html','wb')
    # global browser
    browser = mechanize.Browser()
    print("using real data68")

    browser.set_handle_robots(False)
    browser.set_handle_equiv(False)
    print("using real data69")
    browser.addheaders = [
        (
            "User-agent",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1",
        )
    ]
    print(PE_LOGIN, "PE_LOGIN")
    if 1 == 1:
        # try:
        browser.open(PE_LOGIN)
        print("browser=open")
    # except:
    print("using real data669")
    #    return False
    browser.select_form(name="ctl00")
    # print (x['username'],x['password'])
    # print (type(x['username']),type(x['password']))
    browser["emailaddress"] = x["username"]
    browser["mypassword"] = browser["mypassword"] = libs.lib_enc.r_password(
        x["password"]
    )

    res = browser.submit()

    res = browser.open(PE_COUNTRIES)

    aa = res.get_data()  # HTML source of the page
    # print (aa)
    b2 = open(ad + "/realdata.html", "wb")
    print("using real data66")

    b2.write(aa)

    b2.close()
    print("login success")
    return True
    # except:
    #    print ('login failed')
    #    return False
