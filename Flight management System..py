import datetime
flight = []
customer = []
balance = 0
password = "asad123"
def addflight(flg):
    while(True):
        print("---------------------------------------------------------------------------------------------------------------"
              "-----")
        while (True):  # Unique ID Loop
            while (True):  # Exception Loop
                try:
                    id = int(input("Enter Flight No.(Numbers Only!): "))
                    break
                except:
                    print("Please Enter Integer Data!")
            list = []
            if (len(flg) > 0):
                for i in range(0, len(flg) - 1, 9):
                    list.append(flg[i])
                # print(list)
                check1 = id in list
                if check1 == True:
                    print("Please Enter Unique ID!")
                else:
                    flg.append(id)
                    break
            else:
                flg.append(id)
                break
        flg.append(input("Enter Flight Route: "))
        while(True):   
            try:
                a = datetime.datetime.strptime(input("Enter Flight Time (HH:MM) : "), "%H:%M")
                T = a.strftime("%H:%M")
                break
            except:
                print("Please Enter Correct Time In HHMM Format")
        flg.append(T)
        print("\t Tickets!")
        while(True):
            try:
                flg.append(int(input("Enter Economy  Tickets: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("please Enter Integer Data!")
        while(True):
            try:
                flg.append(int(input("Enter Business Class Tickets: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("Please Enter Integer Data!")
        while(True):
            try:
                flg.append(int(input("Enter Fisrt Class Tickets: ")))
                break
            except:
                print("Please enter Integer Data!")
        while(True):
            try:
                flg.append(int(input("Enter Price: ")))
                break
            except:
                print("please Enter Integer Data!")
        while (True):  # Ask User To Repeat Loop
            check0 = input("Do You Continue (y/n): ")
            print("-----------------------------------------------------------------------------------------------------------"
                  "-----")
            if ((check0 == "n") or (check0 == "N")):
                return
            elif ((check0 == "y") or (check0 == "Y")):
                break
            else:
                print("Press (Y/N) !")


def view(flg):            # Display Function
    l = len(flg)  
    if l == 0:
        print("No Record Entered")
        print("---------------------------------------------------------------------------------------------------------------"
              "-----")
        return
    else:
        for a in range(0, len(flg), 9):
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            print("Flight No.: " + str(flg[a]) + " \t Flight  route: " + flg[a + 1] + " \t Flight Time: " + flg[a + 2] + "\n"
            "Economy Tickets: " + str(flg[a + 3]) + " \t E-Price: " + str(flg[a + 4]) +"\n"
            "Business Class Tickets: "  + str(flg[a + 5]) + " \t B-Price: " + str(flg[a + 6]) + "\n"
            "First Class Tickets : " + str(flg[a+7]) + " \t F-Price: " +str(flg[a + 8]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                  "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

def sortt(num):  # bubble sortting on list
    for i in range(len(num) - 9, 0, -9):
        # check = num[i]
        # print(check)
        for j in range(0, i, 9):
            # check2 = num[j]
            # print("j" + str(check2))
            if num[j] > num[j + 9]:
                temp = []
                temp = num[j:j + 9]
                num[j] = num[j + 9]
                num[j + 1] = num[j + 10]
                num[j + 2] = num[j + 11]
                num[j + 3] = num[j + 12]
                num[j + 4] = num[j + 13]
                num[j + 5] = num[j + 14]
                num[j + 6] = num[j + 15]
                num[j + 7] = num[j + 16]
                num[j + 8] = num[j + 17]
                num[j + 9] = temp[0]
                num[j + 10] = temp[1]
                num[j + 11] = temp[2]
                num[j + 12] = temp[3]
                num[j + 13] = temp[4]
                num[j + 14] = temp[5]
                num[j + 15] = temp[6]
                num[j + 16] = temp[7]
                num[j + 17] = temp[8]
    view(num)                            # Call Display Fuction After Sorting
    return (num)


def binary(flg):  # Binary Search On List Function
    flight1 = sortt(flg)  # Sorting Function Call
    # print(movie1)
     # index = -1
    # s = 0
    list1 = []
    for i in range(0, len(flight1) - 1, 9):  # Loop To Take Out ID Indexes
        list1.append(flight1[i])

    # print(list1)
    def search1(list, n):
        index = -1
        l = 0
        u = (len(list) - 1)
        while l <= u:
            mid = (l + u) // 2
            if list[mid] == n:
                index = mid * 9
                # print(index)
                return index
            else:
                if list[mid] < n:
                    l = mid + 1
                else:
                    u = mid - 1
        return index

    while (True):  # Exception Loop
        try:
            m = int(input("Enter Flight No. : "))
            break
        except:
            print("Please Enter Integer Data!")
    outindex = search1(list1, m)
    #print(outindex)
    if (search1(list1, m) != -1):
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - -")
        # print("Found on "+str(outindex)+ "index")

        print("Flight No.: " + str(flight1[outindex]) + " \t Flight Route: " + flight1[outindex + 1] + " \t Flight Time: " +flight1[outindex + 2] + "\n"
              "Economy Tickets: " + str(flight1[outindex + 3]) + " \t E-Price: " + str(flight1[outindex + 4]) + "\n"
              "Business Class Tickets: " + str(flight1[outindex + 5]) + " \t B-Price: " + str(flight1[outindex + 6]) + "\n"
              "First Class Tickets: " + str(flight1[outindex + 7]) + " \t F-Price: " + str(flight1[outindex + 8]))
    else:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - -")
        print("Not Found")

def edit(flight):
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
          "- - - - - - - - - - - - - - - -")
    while (True):  # Exception Loop
        try:
            i = int(input("Please Enter Flight No. You Want To Change:  "))
            break
        except:
            print("Please Enter Integer Data!")
    lista = []
    for f in range(0,len(flight)-1,9):
        lista.append(flight[f])
    check = i in lista
    if check == True:
        a = lista.index(i)
        a = a*9
        while (True):  # Loop Repeat Data Changing
            while (True):  # Exception Loop
                try:
                    menu = int(input(
                        "[1] Change flight No. \n [2] Change Flight Route. \n [3] Change Flight Time. \n [4] Change "
                        "Economy Tickets. \n [5] Change E-Price. \n [6] Change Business Class Tickets. \n [7] Change B-Price. \n"
                        " [8] Change First Class \n [9] F-Price. \n [0] BACK. \n "
                        "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                        "- - - - - - - - - - - - - - - - - - \n  :       "))
                    break
                except:
                    print("Please enter Integer Data!")
            if menu == 1:
                while (True):  # Unique ID Loop
                    while (True):  # Exception Loop
                        try:
                            id = int(input("Enter New Flight No. :  "))
                            break
                        except:
                            print("Please Enter Integer Data!")
                    list = []
                    for n in range(0, len(flight) - 1, 9):
                        list.append(flight[n])
                    check1 = id in list
                    if check1 == True:
                        print("Please Enter Unique ID!")
                    else:
                        if customer != 0:
                            for s in range(1, len(customer), 5):
                                 if i == customer[s]:
                                     customer[s] = id
                        flight[a] = id
                        break
                    
            elif menu == 2:
                flight[a + 1] = input("Enter New Flight Route :  ")
            elif menu == 3:
                flight[a + 2] = input("Enter New Flight Time:  ")
            elif menu == 4:
                while (True):
                    try:
                        flight[a + 3] = int(input("Enter New Economy Tickets:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 5:
                while(True):
                    try:
                        flight[a + 4] = int(input("Enter New E-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 6:
                while (True):
                    try:
                        flight[a + 5] = int(input("Enter New Business Class Tickets:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 7:
                while (True):
                    try:
                        flight[a + 6] = int(input("Enter New B-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 8:
                while (True):
                    try:
                        flight[a + 7] = int(input("Enter New First Class Tickets:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 9:
                while (True):
                    try:
                        flight[a + 8] = int(input("Enter New F-Price:  "))
                        break
                    except:
                        print("Please Enter Integer Data!")
            elif menu == 0:
                break
        # print(movie)
        view(flight)
        return flight
    else:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              "- - - - - - - - - - - - - - - - - -")
        print("Wrong ID")
        while (True):
            h = input("Do You Want Add New Record(y/n):    ")
            if ((h == "n") or (h == "N")):
                return
            elif ((h == "y") or (h == "Y")):
                addflight(flight)
                break
            else:
                print("Press (Y/N)!")
                
                
def delete():  # Deleting Record Function
    while (True):  # Deleting Menu Loop
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
              " - - - - - - - - - - - - - - - - - -")
        while (True):  # Exception Loop
            try:
                user = int(input(" [1] Delete Flight Record. \n [2] Delete All Record. \n [0] BACK \n "
                                 "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                 "- - - - - - - - - - - - - - - - - - \n   :  "))
                break
            except:
                print("Please Enter Integer Data!")
        if user == 2:
            flight.clear()
            #print(flight)
        elif user == 0:
            break
        elif user == 1:
            while (True):  # Repeating Deletion Task
                while (True):  # Exception Loop
                    try:
                        d = int(input("Enter Flight No. You Want To Delete:  "))
                        break
                    except:
                        print("Please Enter Interger Data!")
                listid = []
                for l in range(0,len(flight)-1,9):
                    listid.append(flight[l])
                check = d in listid
                if check == True:
                    while(True):      # deleting all boooking against Deleted flight Record
                        listi = []
                        for x in range(1,len(customer)-1,5):
                            listi.append(customer[x])
                        checki = d in listi 
                        if checki == True:
                            z = listi.index(d)
                            z = (z*5)+1
                            for r in range(0,5):
                                customer.pop(z-1)
                        else:
                            break
                    a = listid.index(d)
                    a = a*9
                    for i in range(0, 9):
                        flight.pop(a)
                elif check == False:
                    print("Wrong ID")
                while (True):
                    f = input("If You Want To delete Another Record Press [Y/N]:    ")
                    if ((f == "y") or (f == "Y")):
                        break
                    elif ((f == "n") or (f == "N")):
                        return
                    else:
                        print("Press (Y/N)!")                
                
                
def verify(customer, flight, balance):  # Function Verify Full Booking Record Entery
    while (True):
        while (True):
            booking = []
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - - - -")
            addcustomer(booking, flight, balance)
            if len(booking) < 5:
                print("Incomplete Booking Record(Try Again)!")
                break
            elif len(booking) == 5:
                customer.append(booking[0])
                customer.append(booking[1])
                customer.append(booking[2])
                customer.append(booking[3])
                customer.append(booking[4])
                print("Booking Successfull !")
                #print(customer)
                # print(movie)
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                      " - - - - - - - - - - - - - - - - - - - - -")
                break
        while True:
            check0 = input("Do You Want To Make Another Book (Y/N): ")
            if (check0 == "n") or (check0 == "N"):
                return
            elif (check0 == "y") or (check0 == "Y"):
                break
            else:
                print("Press (Y/N) !)")
def addcustomer(booking, flight, balance):  # Add Customers Booking in List
    while True:  # Appending Booking Loop
        while True:  # Unique ID Loop
            while True:  # Exception Loop
                try:
                    id = int(input("Enter Booking ID(Numbers Only!): "))
                    break
                except:
                    print("Please Enter Integer Data!")
            list = []
            if len(customer) > 0:
                for i in range(0, len(customer) - 1, 5):
                    list.append(customer[i])
                # print(list)
                check1 = id in list
                if check1 == True:
                    print("Please Enter Unique ID!")
                else:
                    booking.append(id)
                    break
            else:
                booking.append(id)
                break
        check3 = matchingid(booking, flight)
        booking.append(input("Enter Passport Number: "))
        #print(check3)
        if check3 != -1:
            while(True):
                while(True):
                    try:
                        tmenu = int(input(" [1] Economy tickets. \n [2] Business Class Tickets. \n [3] First Class Tickets."
                                          "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                          "- - - - - - - - - - - - - - - - - - \n   :        "))
                        break
                    except:
                        print("Please Enter Integer Data!")
                if tmenu == 1:
                    while(True):
                        print(" Available Economy Tickets: " + str(flight[check3+3]) + "\n Price: "+str(flight[check3+4]))
                        t = flight[check3+3]
                        while(True):
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0:
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):
                            c = (flight[check3 + 3] - ticket)
                            flight[check3 + 3] = c
                            booking.append(1)
                            booking.append(t)
                            balance = balance + (flight[check3+4]*t)
                            break
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break 
                elif tmenu == 2:
                    while(True):
                        print(" Available Business Tickets: " + str(flight[check3+5]) + "\n Price: "+str(flight[check3+6]))
                        t = flight[check3+5]
                        while(True):
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0:
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):
                            c = (flight[check3 + 5] - ticket)
                            flight[check3 + 5] = c
                            booking.append(2)
                            booking.append(t)
                            balance = balance + (flight[check3+4]*t)
                            break
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break
                elif tmenu == 3:
                    while(True):
                        print(" Available Economy Tickets: " + str(flight[check3+7]) + "\n Price: "+str(flight[check3+8]))
                        t = flight[check3+7]
                        while(True):
                            try:
                                ticket = int(input("Enter Tickets You Want :"))
                                break
                            except:
                                print("Please Enter Integer Data!")
                        if t == 0:
                            print("All Seats Booked! ")
                            break
                        elif (t >= ticket):
                            c = (flight[check3 + 7] - ticket)
                            flight[check3 + 7] = c
                            booking.append(3)
                            booking.append(t)
                            balance = balance + (flight[check3+4]*t)
                            break
                        else:
                            print("PLease Enter Aviable Number OF Tickets")
                    break
                else:
                    print("Please Choose Correct Option!")
        break
def matchingid(booking, inflight):  # Match Movie ID During Booking
    while (True):  # Unique ID Loop
        while (True):  # Exception Loop
            try:
                id = int(input("Enter Flight No. (Numbers Only!): "))
                break
            except:
                print("Please Enter Integer Data!")
        list = []
        # print("12")
        if len(inflight) > 0:
            for i in range(0, len(inflight) - 1, 9):
                list.append(inflight[i])
            #print(list)
            check1 = id in list
            # print("18")
            if check1 == False:
                print("Please Enter Correct ID: ")
            else:
                booking.append(id)
                fid = list.index(id)
                fid = fid*9
                print("23")
                return fid
        else:
            # print("27")
            print("No Movie Record Exist(Ask Admin To Add Movie Record.)!")
            return -1              
                
def vbooking():
    if len(customer) == 0:
        print("No Booking Has Been Made!")
    else:
        for i in range(0, len(customer) - 1, 5):  # loop To Filter Booking ID
            id = customer[i + 1]
            # print(id)
            list2 = []
            for j in range(0, len(flight) - 1, 9):
                list2.append(flight[j])
            # print(list2)
            a = list2.index(id)
            a = (a * 9)
            Ttype = customer[i + 3]
            if Ttype == 1:
                t = "Economy"
            elif Ttype == 2:
                t = "Business Class"
            elif Ttype == 3:
                t = "First Class"
            # print(a)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - ")
            print(
                " Booking ID: " + str(customer[i]) + "\n FlightNo. : " + str(customer[i + 1]) + " \t Flight Route: " + flight[
                 a + 1] + " \t Flight Time : " + flight[a + 2] + " \t Passport No. : " + str(customer[i + 2]) + "\n"
                 " Ticket Type: "+ t + " \t Ticket Booked: "+ str(customer[i + 4]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                  " - - - - - - - - - - - - - - ")                
def delbook():
    while (True):  # Outer Repeat Function Loop
        while (True):  # Exception Loop
            try:
                user = int(input("Enter Booking ID: "))
                break
            except:
                print("Please Enter Integer Data!")
        list1 = []
        for l in range(0, len(customer) - 1, 5):      # Loop To Filter Booking ID
            list1.append(customer[l])
        check = user in list1
        if check == False:
            print("No Booking Record Exist Against This ID!")
        else:
            a = list1.index(user)
            a = a*5                                  # mutiplying 5 to get original Index Number
            list3 = []
            for d in range(0, len(flight)-1, 9):     # Loop to filter flight No.
                list3.append(flight[d])
            #print(customer[(a * 3) + 1])
            b = list3.index(customer[a + 1])         # Adding 1 to Get Flight No. and then index
            b = b*9                                  # mutiplying 9 to get original Index Number
            ctype = customer[a + 3]
            t = customer[a + 4]
            if ctype == 1:                           # Economy Type
                flight[b + 3] += customer[a + 4]         # Adding delete ticket in flight record
                balance = balance - (flight[b + 4]*t)    # Deducting delete booking price from Balance
            elif ctype == 2:                         # Business class Type
                flight[b + 5] += customer[a + 4]         # Adding delete ticket in flight record
                balance = balance - (flight[b + 6]*t)    # Deducting delete booking price from Balance
            elif ctype == 3:                         # First Class Type
                flight[b + 7] += customer[a + 4]         # Adding delete ticket in flight record
                balance = balance - (flight[b + 8]*t)    # Deducting delete booking price from Balance
            #print(b)
            for i in range(0, 5):           # Loop Repeat 5 times to pop booking record of 5 indexes.
                customer.pop(a)                 
            print("Successfully Deleted! ")
        while (True):  # Ask User To Repeat Function
            repeat = input("Do You Delete Another Booking? (Y/N).")
            if ((repeat == "Y") or (repeat == "y")):
                break
            elif ((repeat == "n") or (repeat == "N")):
                return
            else:
                print("Press (Y/N) !")               
       
def CancelFlight():
    if (len(customer) == 0):
        print("No Booking Has Been Made Yet!")
    else:
        while(True):         # main LOOP
            while(True):     # Exceptional Loop
                try:
                    user = int(input("Enter Flight No. : "))
                    break
                except:
                    print("Please Enter Integer Data! ")
            list3 = []
            for d in range(0, len(flight)-1, 9):     # Loop to filter flight No.
                list3.append(flight[d])
            check = user in list3
            if check == False:
                print("Wrong Flight No.!")
            else:
                b = list3.index(user)
                b = b* 9
                while(True):                                       # Deleting all boooking against Deleted Flight Record
                    listi = []
                    for x in range(1, len(customer)-1, 5):
                        listi.append(customer[x])
                    checki = user  in listi 
                    if checki == True:
                        z = listi.index(user)
                        z = (z*5)
                        ctype = customer[z + 3]
                        t = customer[z + 4] 
                        if ctype == 1:                              # Economy Type
                            flight[b + 3] += customer[z + 4]         # Adding delete ticket in flight record
                            balance = balance - (flight[b + 4]*t)    # Deducting delete booking price from Balance
                        elif ctype == 2:                            # Business class Type
                            flight[b + 5] += customer[z + 4]         # Adding delete ticket in flight record
                            balance = balance - (flight[b + 6]*t)    # Deducting delete booking price from Balance
                        elif ctype == 3:                            # First Class Type
                            flight[b + 7] += customer[z + 4]         # Adding delete ticket in flight record
                            balance = balance - (flight[b + 8]*t)    # Deducting delete booking price from Balance
                        for r in range(0,3):
                            customer.pop(z)
                    else:
                        print("Successfully Deleted! ")
                        flight[b + 2] = "Cancelled"
                        break
            while(True):
                check0 = input("Do You Want To Cancel Another Flight (Y/N): ")
                if (check0 == "n") or (check0 == "N"):
                    return
                elif (check0 == "y") or (check0 == "Y"):
                    break
                else:
                    print("Press (Y/N) !)")      
       
       
       

while (True):  # Outer Main Loop
    print(
        "----------------------------------------------------------------------------------------------------------------------")
    while (True):  # Exception Loop
        try:
            outmenu = int(input(" [1] Admin View \n [2] Costumer View \n [0] Exit \n "
                                "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                                "- - - - - - - - - - - - - - - - - - \n : "))
            break
        except:
            print("please Enter Integer Data!")
    print(
        "----------------------------------------------------------------------------------------------------------------------")
    if outmenu == 1:  # Admin View
        while(True):
            pwd = input("Enter Password: ")
            if (pwd == password) :
                while (True):  # Menu Loop
                    print("-----------------------------------------------------------------------------------------------------------"
                          "-----")
                    while (True):  # Exception Loop
                        try:
                            menu = int(input(
                                " [1] Add Flight Record. \n [2] View Flight Record. \n [3] View Flight With SORTING. "
                                "\n [4] Search Flight Record By ID. \n [5] Edit Flight Record. \n [6] Delete Flight Record. \n [7] View Booking. \n "
                                "[8] Delete Booking. \n [9]Cancel Fight. \n [10] Balance. \n [0] BACK \n"
                                "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                                "- - - - - - - - - - - - - -  \n : "))
                            break
                        except:
                            print("Please Enter Integer Data!")
                    print("-----------------------------------------------------------------------------------------------------------"
                          "-----")
                    if menu == 1:
                        addflight(flight)
                        #print(flight)
                    elif menu == 2:
                        view(flight)
                    elif menu == 3:
                        sortt(flight)
                    elif menu == 4:
                        binary(flight)
                    elif menu == 5:
                        edit(flight)
                    elif menu == 6:
                        delete()
                    elif menu == 7:
                        vbooking()
                    elif menu == 8:
                        delbook()
                    elif menu == 9:
                        CancelFlight()
                    elif menu == 10:
                        print("Current Balance Is: " + str(balance))
                    elif menu == 0:
                        break
                    else:
                        print("Enter Correct Number! ")
                break
            else:
                print("Wrong Password!")
                print("-----------------------------------------------------------------------------------------------------------"
                      "-----")
    if outmenu == 2:  # User View
        while (True):
            print("-----------------------------------------------------------------------------------------------------------"
                  "----")
            while (True):  # Exception Loop
                try:
                    menu2 = int(input(" [1] View Flight Record \n [2] Add Booking \n [3] Veiw Bookings \n [0] Back \n"
                              "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
                              "- - - - - - - - - - - - - - \n :"))
                    break
                except:
                    print("Please Enter Integer Data!")
            print("------------------------------------------------------------------------------------------------------------"
                  "---")
            if menu2 == 1:
                view(flight)
            elif menu2 == 2:
                verify(customer, flight, balance)
            elif menu2 == 3:
                vbooking()
            elif menu2 == 0:
                break
            else:
                print("Enter Correct Number!")
    if outmenu == 0:  # Program Exit
        exit ()


    
    