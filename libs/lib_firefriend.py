def view_chat(App, gg, x):
    # print(App, gg, x)
    from datetime import datetime

    now = datetime.now()

    from firebase_admin import db
    import firebase_admin
    from datetime import datetime

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")
    chat_exists_flag = False
    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already logged into db")

    s = gg["date"] + " " + gg["job"] + " " + x["city"]

    ref = db.reference("/chat/" + s)

    z = ref.get()
    try:
        print(len(z))
        chat_exists_flag = True
        # return z
    except:
        "no chat file"
        return []
    logs = []
    for key, value in z.items():

        # print(key, value)
        for key2, value2 in value.items():
            nt, junk = str.split(value2["Time"], ".")
            # print(key2, value2)
            q = {"name": key2, "date": nt, "message": value2["Message"]}
            logs.append(q)
            # print(len(logs),wtf)
    # print(logs)
    return logs


def try_add_chat(App, gg, x, test_message):
    # print(App, gg, x)
    from datetime import datetime

    now = datetime.now()

    from firebase_admin import db
    import firebase_admin
    from datetime import datetime

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")
    chat_exists_flag = False
    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already logged into db")

    s = gg["date"] + " " + gg["job"] + " " + x["city"]

    ref = db.reference("/chat/" + s)

    z = ref.get()
    try:
        # print(len(z))
        chat_exists_flag = True
    except:
        "no chat file"

    book = {
        x["name"]: {
            "Message": test_message,
            "Time": str(now),
        },
    }
    ref.push(book)
    toast = "Check In Success"
    return toast


def try_add_show(App, gg, x):

    if 1 == 2:
        from faker import Faker

        faker = Faker()

        x["name"] = faker.name()
        x["email"] = faker.email()

    from firebase_admin import db
    import firebase_admin
    from datetime import datetime

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")
    show_exists_flag = False
    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already logged into db")

    s = gg["date"] + " " + gg["job"] + " " + x["city"]

    ref = db.reference("/shows/" + s)
    z = ref.get()
    try:
        print(len(z))
        show_exists_flag = True
    except:
        "no show file"

    flag_checkedin = False
    name_list = []
    name_list_flat = []
    junk = []
    if show_exists_flag == True:
        for key, value in z.items():
            # print(key, value)
            for key, value2 in value.items():
                # print(key, value2)
                old_update = datetime.strptime(value2["Init"], "%Y-%m-%d %H:%M:%S.%f")
                newtime = old_update.strftime("%m/%d %H:%M")
                data = {
                    "name": key,
                    "date": value2["Init"],
                    "Position": value2["Position"],
                    "Time": value2["Time"],
                    "Type": value2["Type"],
                    "Email": value2["email"],
                }
                name_list.append(data)
                data_list = (
                    key,
                    value2["Init"],
                    value2["Position"],
                    value2["Time"],
                    value2["Type"],
                )
                junk.append(key)

                junk.append(value2["Position"])
                junk.append(value2["Time"])
                junk.append(newtime)
                junk.append(value2["Type"])

                name_list_flat.append(data_list)
                # name_list.append(data)
                if x["name"] == key:
                    flag_checkedin = True
                    # print ('Already Checked In)

    if flag_checkedin == True:
        t = "Already Checked In"
        # print("Already Checked In")
        return junk, t, name_list
    if flag_checkedin == False:
        print("Trying to check in")
        t = add_show(App, gg, x)
        try_add_show(App, gg, x)
        # print("Check in Success")


def add_show(App, gg, x):

    import firebase_admin
    from datetime import datetime

    now = datetime.now()

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")

    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already init")
    s = gg["date"] + " " + gg["job"] + " " + x["city"]

    from firebase_admin import db

    ref = db.reference("/shows/" + s)
    book = {
        x["name"]: {
            "Time": gg["time"],
            "Type": gg["type"],
            "Position": gg["pos"],
            "Init": str(now),
            "email": str(x["username"]),
        },
    }
    ref.push(book)
    toast = "Check In Success"
    return toast


def update_user_profile(x):
    from firebase_admin import db
    import firebase_admin
    from datetime import datetime

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")
    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already logged into db")
    u = str.replace(x["username"], "@", ".at.")
    u = str.replace(u, ".", "-")
    ref = db.reference("/users/" + u)

    user = {
        x["name"]: {
            "Pic": x["button4"],
            "bio": x["bio"],
            "NickName": x["nick"],
            "Phone": str(x["phone"]),
            "City": str(x["city"]),
        },
    }

    ref.set(user)
    toast = "Update Success"
    return toast


def get_profile(user):

    from firebase_admin import db
    import firebase_admin
    from datetime import datetime

    databaseURL = "https://schedulara-default-rtdb.firebaseio.com"
    cred_obj = firebase_admin.credentials.Certificate("sc.json")
    show_exists_flag = False
    try:
        default_app = firebase_admin.initialize_app(
            cred_obj, {"databaseURL": databaseURL}
        )
    except:
        print("already logged into db")

    # s = gg["date"] + " " + gg["job"] + " " + x["city"]

    u = str.replace(user, "@", ".at.")
    u = str.replace(u, ".", "-")
    ref = db.reference("/users/" + u)
    z = ref.get()
    return z
