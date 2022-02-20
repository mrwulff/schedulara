from kivy_garden.graph import Graph, BarPlot
from datetime import datetime


def make_stats_pp(self,clabel,dd,newmax,y):
    
    print ('wtfhello')
    self.root.current = "stats"
    self.samples = y
    print (len(dd),'lendd')
    self.graph = Graph(y_ticks_major=newmax/3,
                        x_ticks_major=y/3,
                        xmin=0, xmax=self.samples,
                        ymin=0, ymax=newmax,
                        draw_border=True,
                        height=200,
                        
                        
                        xlabel=clabel,
                        
                        x_grid_label=True, y_grid_label=True)
    self.root.current_screen.ids["graphs"].add_widget(self.graph)

    self.plot = BarPlot(color=self.theme_cls.primary_color,bar_spacing=.5)
    
    self.graph.add_plot(self.plot)
    self.plot.bind_to_graph(self.graph)
    update_plot(self,dd)

def update_plot(self,dd):

    self.plot.points = [(dd[x][0],dd[x][1]) for x in range(len(dd))]

def parsepp(self,ad,type):
    import os, glob
    import lib_parse
    print ('dumbdumb',ad)
    try:
        os.chdir(ad+'/pp')
    except:
        os.mkdir(ad+'/pp')
        os.chdir(ad+'/pp')
    x=0
    listofdicks=[]
    dd=[]
    dd2=[]
    realdays=[]
    realdays_max=0
    month_max=0
    days_ago_max=0
    months_ago_max=30
    for file in glob.glob("*.html"):
        #print (file)
        dd,days=lib_parse.parsepayperiod(ad+'/pp/'+file)
        #print (days)
        listofdicks.append(dd)
        x=x+1
        #print (dd['moneytotal'])
        if (dd['moneytotal'])>month_max:
            month_max=(dd['moneytotal'])
        z=[dd['ddelta'],dd['moneytotal']]
        print (z,'wtf')
        #z=[x,dd['ddelta']]
        dd2.append(z)

        for z in range(len(days)):
            #print (days[z])

            if days[z][1]>realdays_max:
                realdays_max=days[z][1]
            if days[z][0]>days_ago_max:
                days_ago_max=days[z][0]
            realdays.append(days[z])

        #print (realdays_max)
    #if type=='check':

    #    return dd2,5000
    if 1==1:
        return dd2,realdays,realdays_max,month_max,days_ago_max,months_ago_max