
def createcache(ad,numshows):
    print ('THISISIOS',ad)
    import datetime
    import random

    print (ad,'ccaa')


    x = datetime.datetime.now()
    t=(x.strftime("%m"))+'/'+(x.strftime("%d"))+'/'+(x.strftime("%Y"))
    todays=t
    x= (datetime.date.today() + datetime.timedelta(days=-1))
    t=(x.strftime("%m"))+'/'+(x.strftime("%d"))+'/'+(x.strftime("%Y"))
    yesterdays=t

    x22= (datetime.date.today() + datetime.timedelta(days=+1))
    t=(x22.strftime("%m"))+'/'+(x22.strftime("%d"))+'/'+(x22.strftime("%Y"))
    nexts=t

    x= (datetime.date.today() + datetime.timedelta(days=+10))
    t=(x.strftime("%m"))+'/'+(x.strftime("%d"))+'/'+(x.strftime("%Y"))
    confs=t

    cshow=['GEORGE STRAIT','VGK','NCAA','RANDOM','UFC 269',' VGK vs DAL','PBL Boxing','(TM) EMPIRE CLASSIC BASKETBALL']
    rven=['Dolby Theater','MGM Grand','T-Mobile Arena','Wynn','Mandalay Bay']
    rpos=['SH','L3','V3','A3']
    #numshows=3


    yesterday="""<tr>
            <td class="cell-noborder">"""+yesterdays+"""</td><td class="cell-noborder" style="width:10px;">07:00</td><td class="cell-noborder">24123</td><td class="cell-noborder">(GGA) PAPARAZZI</td><td class="cell-noborder">MGM GRAND GARDEN ARENA</td><td class="cell-noborder">MEET AT LOADING DOCK</td><td class="cell-noborder">MGM RESORTS</td><td class="cell-noborder">SHOW</td><td class="cell-noborder">HL</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder">Confirmed</td><td class="cell-noborder-wide">HARD HAT, VEST, GLOVES, FULL ANKLE STEEL/COMP BOOT; BRING PARKING STUB TO SUP ONSITE; ALL A3 ,L3, & V3 NEED TO BE CATWALK CAPABLE</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder-wide">&nbsp;</td>
        </tr>"""

    today="""<tr class="whiterow">
            <td class="cell-noborder">"""+todays+"""</td><td class="cell-noborder" style="width:10px;">06:00</td><td class="cell-noborder">24152</td><td class="cell-noborder">(TM) GEORGE STRAIT</td><td class="cell-noborder">T-MOBILE ARENA</td><td class="cell-noborder">LOADING DOCK</td><td class="cell-noborder">MGM RESORTS</td><td class="cell-noborder">IN</td><td class="cell-noborder">L</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder">Confirmed</td><td class="cell-noborder-wide">MASKS, HARD HATS, SAFETY VESTS, GLOVES, AND FULL ANKLE PROTECTIVE TOE BOOTS</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder-wide">&nbsp;</td>
        </tr>"""
    

    conf="""<tr>
            <td class="cell-noborder">"""+confs+"""</td><td class="cell-noborder" style="width:10px;">10:00</td><td class="cell-noborder">23976</td><td class="cell-noborder">(TM) IHEART 2021</td><td class="cell-noborder">T- MOBILE ARENA</td><td class="cell-noborder">T- MOBILE ARENA LOADING DOCK</td><td class="cell-noborder">MGM RESORTS</td><td class="cell-noborder">OUT</td><td class="cell-noborder">A3</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder">Tentative</td><td class="cell-noborder-wide">PPE: SAFETY VESTS, HARD HAT, PROTECTIVE ANKLE BOOTS, GLOVES; WEAR FACE MASK// RETURN PARKING STUB TO SUP</td><td class="cell-noborder">&nbsp;</td><td class="cell-noborder"><input type="submit" name="dgResults$ctl14$ctl03" value="Confirm" onclick="return confirm(&quot;You're confirming you can work the (TM) IHEART 2021 OUT call on 09/19/2021 at 10:00 ?&quot;);" /></td><td class="cell-noborder-wide">&nbsp;</td>
        </tr>"""
    headers="""        <tr class="resultsheader-wide">
            <td class="leftcell">Date</td><td class="leftcell">Time</td><td class="leftcell">Job #</td><td class="leftcell">Show</td><td class="leftcell">Venue</td><td class="leftcell">Location</td><td class="leftcell">Client</td><td class="leftcell">Type</td><td class="leftcell">Position</td><td class="leftcell">Details</td><td class="leftcell">Status</td><td class="leftcell-wide">Notes</td><td class="leftcell">TK/TL/SAF</td><td class="cell-noborder">&nbsp;</td><td class="leftcell">+</td>
        </tr>"""
    footers="""<tr>
            <td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td>
        </tr>"""
    print (ad,'thisisios')
    aaa=open(ad+'/conf.html','w')
    aaa.write('      <span id="lblEmpName" class="subheader">McDemo, Test</span>')
    aaa.write(headers)
    #aaa.write(yesterday)
    #aaa.write(today)
    for x in range(numshows):
        x22= (datetime.date.today() + datetime.timedelta(days=-2+x))
        t=(x22.strftime("%m"))+'/'+(x22.strftime("%d"))+'/'+(x22.strftime("%Y"))
        nexts=t
        next="""<tr>
            <td class="cell-noborder" style="background-color:Gray;">"""+nexts+"""</td><td class="cell-noborder" style="background-color:Gray;width:10px;">08:00</td><td class="cell-noborder" style="background-color:Gray;">24150</td><td class="cell-noborder" style="background-color:Gray;">"""+(random.choice(cshow))+""" </td><td class="cell-noborder" style="background-color:Gray;">"""+(random.choice(rven))+"""</td><td class="cell-noborder" style="background-color:Gray;">PARK MGM LAS VEGAS</td><td class="cell-noborder" style="background-color:Gray;">MGM RESORTS</td><td class="cell-noborder" style="background-color:Gray;">IN</td><td class="cell-noborder" style="background-color:Gray;">"""+(random.choice(rpos))+"""</td><td class="cell-noborder" style="background-color:Gray;">&nbsp;</td><td class="cell-noborder" style="background-color:Gray;">Confirmed</td><td class="cell-noborder-wide" style="background-color:Gray;">WORKING W/ JESSE</td><td class="cell-noborder" style="background-color:Gray;">&nbsp;</td><td class="cell-noborder-wide">&nbsp;</td>
        </tr><br>\n"""
        aaa.write(next)
    aaa.write(conf)
    aaa.write(footers)
    aaa.close()
    print ('omg it saved a fucking file')
    return ad

#createcache('')
