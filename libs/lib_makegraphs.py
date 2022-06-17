from kivy_garden.graph import Graph, BarPlot
from datetime import datetime


def make_matplot():
    pass


# def show_maker(ins,outs,shows):
#    return [[0,ins],[1,outs],2,shows]


def make_stats_pp(self, clabel, dd, newmax, y):
    if clabel == "1":
        from kivymd.uix.card import MDCard

        self.root.current_screen.ids["graphs"].add_widget(MDCard(text="wow"))
        print("wow")

    # import platform

    platformheight = 400

    from kivy.utils import platform

    # print(platform, "KIVY PLATFORM")
    if platform == "android":
        print("omg its android")

    if platform == "win":
        platformheight = 400

    # self.root.current = "stats"
    # self.root.set_current("stats")
    self.samples = y
    # print(len(dd), "lendd")
    self.graph = Graph(
        y_ticks_major=newmax / 3,
        x_ticks_major=y / 3,
        xmin=0,
        xmax=self.samples,
        ymin=0,
        ymax=newmax,
        draw_border=True,
        height=platformheight,
        xlabel=clabel,
        x_grid_label=True,
        y_grid_label=True,
    )
    self.root.current_screen.ids["graphs"].add_widget(self.graph)

    self.plot = BarPlot(color=self.theme_cls.primary_color, bar_spacing=0.5)
    self.graph.add_plot(self.plot)
    self.plot.bind_to_graph(self.graph)
    update_plot(self, dd)


def update_plot(self, dd):

    self.plot.points = [(dd[x][0], dd[x][1]) for x in range(len(dd))]


def parsepp(self, ad, type, finish, start):
    import os, glob
    import libs.lib_parse as lib_parse

    try:
        os.chdir(ad + "/pp")
    except:
        os.mkdir(ad + "/pp")
        os.chdir(ad + "/pp")
    x = 0
    listofdicks = []
    dd = []
    dd2 = []
    realdays = []
    realdays_max = 0
    month_max = 0
    days_ago_max = 0
    months_ago_max = 30
    ins = 0
    outs = 0
    shows = 0

    for file in glob.glob("*.html"):
        # print(file)
        # file2, junk = str.split(file, ".")
        file2 = file
        pp_date = datetime.strptime(file2, "%m-%d-%Y.html")

        # print(pp_date)
        try:
            print(start.date(), finish.date(), pp_date.date(), "STARTSSS")
        except:
            pass
        try:
            start = start.date()
        except:
            print("cannont convert start")

        try:
            finish = finish.date()
        except:
            print("cannont convert finish")

        try:
            pp_date = pp_date.date()
        except:
            print("cannont convert pp_date")

        # print(type(pp_date))
        # xx = type(start)
        # print(xx)
        """
        try:
            if start.date() < pp_date and pp_date < finish.date():
                flag = True
                start = start.date()
                finish = finish.date()
        except:
            pass
        """

        if start < pp_date and pp_date < finish:

            dd, days, ins2, outs2, shows2 = lib_parse.parsepayperiod(ad + "/pp/" + file)
            # print (days)
            ins = ins + ins2
            outs = outs + outs2
            shows = shows + shows2
            listofdicks.append(dd)
            x = x + 1
            if (dd["moneytotal"]) > month_max:
                month_max = dd["moneytotal"]
            z = [dd["ddelta"], dd["moneytotal"]]
            dd2.append(z)

            for z in range(len(days)):

                if days[z][1] > realdays_max:
                    realdays_max = days[z][1]
                if days[z][0] > days_ago_max:
                    days_ago_max = days[z][0]
                realdays.append(days[z])

        max_t = ins
        if outs > ins:
            max_t = outs
        if shows > max_t:
            max_t = shows

        #    return dd2,5000
    if 1 == 1:
        return (
            dd2,
            realdays,
            realdays_max,
            month_max,
            days_ago_max,
            months_ago_max,
            ins,
            outs,
            shows,
            max_t,
        )
