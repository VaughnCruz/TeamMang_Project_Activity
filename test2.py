import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "GnNc8nFpuHMZitizAMSnQIzZVl0cmeTG"

while True:
    orig = input("(quit or q to quit) Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("(quit or q to quit) Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:

        # Information about the location
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Detailed Information of travel") # Header for starting location
        print("=============================================")
        print("From country of "+ (json_data["route"]["locations"][0]["adminArea1"]),"To country of "+(json_data["route"]["locations"][1]["adminArea1"])) #Country base starting to destination
        print("From the province of "+ (json_data["route"]["locations"][0]["adminArea3"]),"To the province of "+(json_data["route"]["locations"][1]["adminArea3"])) #Province base starting to destination
        #END

        # GPS coordinates
        print("\n=============================================")
        print("Coordinates from starting location to destination GPS tracker") # Header for GPS location
        print("=============================================")
        print("GPS from starting location in Longitude is " + str(json_data["route"]["boundingBox"]["ul"]["lng"]),
        "to destination Longitude of " + str(json_data["route"]["boundingBox"]["lr"]["lng"])) # Longitude Coordinates
        print("---------------------------------------------")
        print("GPS from starting location in Latitude is " + str(json_data["route"]["boundingBox"]["ul"]["lat"]),
        "to destination Latitude of " + str(json_data["route"]["boundingBox"]["lr"]["lat"])) #Latitude Coordinates
        # END

        # Direction from origin to destination
        print()
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("=============================================")
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
         # END 

    
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")

    elif json_status == 611:
        print("******************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("********************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")