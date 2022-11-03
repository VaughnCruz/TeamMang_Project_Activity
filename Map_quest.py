from tkinter import *
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "xFSTtgGKQ97FOAa2o6PGwcIPcPGAclIE"
root = Tk()
root.geometry("1080x1920")
root.title("Map Quest Location")

heading = Label(text="Map Quest API", bg="#A47551",
                fg="white", font="Courier 20", width="350", height="3")
heading.pack()

#Starting Location Input 
LabelLocation = Label(text="Enter your Current Location: ",
                      font="Courier 13", fg="#333a56", anchor='nw')
LabelLocation.pack(pady=10)
orig = Entry(root, width=50, font=5)
orig.pack(pady=20)

#Destination Output
LabelDestination = Label(
    text="Enter your Destination Location: ", font="Courier 13", fg="#333a56")
LabelDestination.pack(pady=10)
dest = Entry(root, width=50, font=5)
dest.pack(pady=15)

#Funtion to clear inputs
def clear():
    orig.delete(0,END)
    dest.delete(0,END)

#Funtion to display directions 
def onClick():
    while True:

        url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
        print("URL ", (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:

            argument = "\nAPI Status: " + str(json_status) + " = A successful route call.\n"\
                "\n================================================================================="\
                + "\nDirections from: " + (orig.get()) + " to " + (dest.get())\
                + "\nTrip Duration: " + (json_data["route"]["formattedTime"])\
                + "\nKilometers: " + str("{:.2f}".format((json_data["route"]["distance"] * 1.6)))\
                + "\nFuel Used (Ltr): " + str("{:.3f}".format((json_data["route"]["fuelUsed"]*3.78)))\
                + "\n================================================================================="\
                + "\nDetailed Information of travel"\
                + "\nFrom country of: " + (json_data["route"]["locations"][0]["adminArea1"])\
                + "\nTo country of " + (json_data["route"]["locations"][1]["adminArea1"])\
                + "\nFrom the province of: " + (json_data["route"]["locations"][0]["adminArea3"])\
                + "\nTo the province of " + (json_data["route"]["locations"][1]["adminArea3"])\
                + "\n================================================================================="\
                + "\nGPS Coordinates"\
                + "\nCoordinates from starting location to destination GPS tracker"\
                + "\nGPS from starting location in Longitude is " + str(json_data["route"]["boundingBox"]["ul"]["lng"])\
                + "\nto destination Longitude of " + str(json_data["route"]["boundingBox"]["lr"]["lng"])\
                + "\n================================================================================="\
                + "\nGPS from starting location in Latitude is " + str(json_data["route"]["boundingBox"]["ul"]["lat"])\
                + "\nto destination Latitude of " + str(json_data["route"]["boundingBox"]["lr"]["lat"])\
                + "\n================================================================================="\

            myResult1 = Label(root, text=argument)
            myResult1.pack()
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                argument2 = ((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                myResult2 = Label(root, text=argument2,
                                  font="Courier 9", justify=LEFT)
                myResult2.pack()
        elif json_status == 402:
            argument3 = "********************************************"\
                + "Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."\
                + "**********************************************\n"
            myLabel3 = Label(root, text=argument3)
            myLabel3.pack()
        elif json_status == 611:
            argument4 = "********************************************"\
                + "Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations."\
                + "**********************************************\n"
            myLabel4 = Label(root, text=argument4)
            myLabel4.pack()
        else:
            argument5 = "**********************************************************************"\
                + "For Staus Code: " + str(json_status) + "; Refer to:"\
                + "https://developer.mapquest.com/documentation/directions-api/status-codes"\
                + "************************************************************************\n"
            myResult = Label(root, text=argument5)
            myResult.pack(pady=20)
        break

#Submit Button 
myButton = Button(root, text="Start",width=35, command=onClick, fg="#FFFFFF", bg="#D0B49F", font="Courier 10")
myButton.pack(pady=(15,5))

#Clear Button
button_clear = Button(root, text="Reset",width=35, command=clear, fg="#FFFFFF", bg="#D0B49F", font="Courier 10")
button_clear.pack(pady=(0,5))

#Quit Button
button_quit = Button(root, text="Exit",width=35, command=root.destroy, fg="#FFFFFF", bg="#D0B49F", font="Courier 10")
button_quit.pack()

root.mainloop() 
