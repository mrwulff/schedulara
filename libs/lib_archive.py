def load(cd, ad,last,first):
    print("loading archive",first,last)
    import glob
    import json
    from datetime import datetime
    all_shows=[]
    z=(glob.glob(ad  + cd+"/*"))
    #print (z)
    for i in range(len(z)):
        with open(z[i]) as d:
            dictData = json.load(d)
            c= (dictData['date'])
            show_date = datetime.strptime(c, "%m/%d/%Y")
            show_date=show_date.date()
            #print (first,show_date,last)
            #print (type(first),type(show_date),type(last))
            if type(last)==int or type(last)==str:
                all_shows.append(dictData)
            else:
                if first<=show_date and show_date<=last:
                    all_shows.append(dictData)


    print (all_shows)
    return all_shows


if __name__ == "__main__":


    x=load("future_shows","C:/Users/kw/AppData/Roaming/demo3/",0,0)
    #print (x)