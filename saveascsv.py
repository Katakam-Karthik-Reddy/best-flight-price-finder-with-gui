import pandas as pd


def saveascvs(path, flights1, flights2):
    try:
        name = []
        start = []
        end = []
        duration = []
        stops = []
        price = []


        name.append("flight data for easymytrip")
        start.append("")
        end.append("")
        duration.append("")
        stops.append("")
        price.append("")

        for f in flights1:
            name.append(f.flightname)
            start.append(f.starttime)
            end.append(f.endtime);
            duration.append(f.totaljourneytime)
            stops.append(f.totalstops)
            price.append(f.price)
        
        name.append("flight data for ixigo")
        start.append("")
        end.append("")
        duration.append("")
        stops.append("")
        price.append("")

        for f in flights2:
            name.append(f.flightname)
            start.append(f.starttime)
            end.append(f.endtime);
            duration.append(f.totaljourneytime)
            stops.append(f.totalstops)
            price.append(f.price)

        dic = { "name": name, "starttime": start, "endtime": end, "flightduration": duration, "totalstops": stops, "price": price}

        dt = pd.DataFrame(dic)
        #path = os.path.dirname(path)
        fullpath = path+ "/flightsdata.csv"
        #print(fullpath)

        #dt.to_csv(os.path.join(path,"flightsdata.csv"))
        dt.to_csv(fullpath)
        return fullpath
    except(OSError):
        return ""
