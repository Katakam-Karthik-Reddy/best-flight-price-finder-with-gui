dic = {}

#f = open('Airport_list.txt', 'r')

def loadAirports():
        file = open('Airport_list.txt', 'r')
        for line in file:
            list = line.split(',')
            list[1] = list[1].replace('\n', "")
            dic[list[0]] = list[1]



#cityinput = input("Enter the city name: ")
def getAirportCode(cityname):
    try:
        return dic[cityname]
    except:
        print("key not found, plz check spelling")
        return ""



