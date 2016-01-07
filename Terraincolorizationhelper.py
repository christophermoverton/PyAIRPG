Colors = {}
TM = []
DCI = {}
DCI_LTYPE = {}
MM = {}
NCs = {}
maxindex = [1]

def DoYouWantToKeep():
    keep = False
    ans = raw_input("Do you want to keep this? [Y/N]")
    if ans == "y" or ans == "Y":
        keep = True
    return keep

def ColorInputMenu(Colors=Colors):
    a1 = True
    while a1:
        ans=raw_input("Please add a color name:")
        colorname = ans
        a2 = True
        rcolorval = 0
        bcolorval = 0
        gcolorval = 0
        while a2:
            ans=raw_input("Please add a Red color value (RGB) (0-255 integer per channel) format: \n")
            rcolorval = ans
            try:
                rcolorval = int(rcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Green color value (RGB) (0-255 integer per channel) format: \n")
            gcolorval = ans
            try:
                gcolorval = int(gcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Blue color value (RGB) (0-255 integer per channel) format: \n")
            bcolorval = ans
            try:
                bcolorval = int(bcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        colorval = (rcolorval,gcolorval,bcolorval)
        print("""You entered """, colorname, """ for the color name.""")
        print("""You entered """, colorval, """ color values.""")
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    Colors[colorname] = colorval
    return colorname

def ColorChangeMenu(Colors=Colors):
    a1 = True
    abort = False
    while a1:
        ans=raw_input("What color do you want to change?: ")
        colorname = ans
        if not str(ans) in Colors:
            print("Color is not found.")
            print("Here is a list of the known Colors")
            print(list(Colors.keys()))
            ans = raw_input("Try again? [Y/N]: ")
            if ans == "N" or ans == "n":
                a1 = False
                abort = True
            continue
        colorname = str(ans)    
        a2 = True
        rcolorval = 0
        bcolorval = 0
        gcolorval = 0
        while a2:
            ans=raw_input("Please add a Red color value (RGB) (0-255 integer per channel) format: \n")
            rcolorval = ans
            try:
                rcolorval = int(rcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Green color value (RGB) (0-255 integer per channel) format: \n")
            gcolorval = ans
            try:
                gcolorval = int(gcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Blue color value (RGB) (0-255 integer per channel) format: \n")
            bcolorval = ans
            try:
                bcolorval = int(bcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        colorval = (rcolorval,gcolorval,bcolorval)
        print("""You entered """, colorname, """ for the color name.""")
        print("""You entered """, colorval, """ color values.""")
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    if not abort:
        Colors[colorname] = colorval
    else:
        colorname = "No color input"
    return colorname

def DeleteColorMenu(Colors=Colors):
    a1 = True
    abort = False
    while a1:
        ans=raw_input("What color do you want to delete?: ")
        colorname = ans
        if not str(ans) in Colors:
            print("Color is not found.")
            print("Here is a list of the known Colors")
            print(list(Colors.keys()))
            ans = raw_input("Try again? [Y/N]: ")
            if ans == "N" or ans == "n":
                a1 = False
                abort = True
            continue
        colorname = str(ans)    

        print("""You want to delete """, colorname, """ for the color name.""")
        
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    if not abort:
        del Colors[colorname]
    else:
        colorname = "No color input"
    return colorname
    
def ColorMenu(Colors=Colors):
    ans=True
    while ans:
        print ("""
        1.List Colors dictionary
        2.List Color names.
        3.How many colors are there?
        4.Input a color
        5.Delete a color(the color's name need be specified exactly).
        6.Change a color value(the color's name need be specified exactly).
        7.Go to Main Menu
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1": 
            print(Colors) 
        elif ans=="2":
            print(list(Colors.keys())) 
        elif ans=="3":
            print("There are ",len(Colors)," Colors")
        elif ans=="4":
            colorname = ColorInputMenu()
            print("""Color name: """, colorname, """ added.""")
        elif ans=="5":
            colorname = DeleteColorMenu()
            print("""Deleted: """, colorname)
        elif ans=="6":
            colorname = ColorChangeMenu()
            print(colorname, " changed.")
        elif ans=="7":
          print("\n Going back to the main menu!")
          ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")

def incrementMaxIndex(maxindex = maxindex):
    maxindex[0] += 1
    
def NamegetMenu():
    ans = raw_input("Please add a name: /n")
    return str(ans)

def LandtypeGetMenu():
    ans=True
    while ans:
        print ("""
        Choose the following Landtype:
        1.Flood
        2.Land
        3.Mountain
        4.None (quit)
        """)    
        ans=raw_input("What landtype? ") 
        if ans=="1": 
            ans = False
            landtype = 'Flood'
        elif ans=="2":
            ans = False
            landtype = 'Land'
        elif ans=="3":
            ans = False
            landtype = 'Mount'
        elif ans=="4":
            ans = False
            landtype = 'abort'
    return landtype

def TypeGetMenu():
    ans=True
    while ans:
        print ("""
        Choose the following Threshold Type:
        1.Height
        2.Normal (gradient/slope)
        3.HeightThreshold 
        4.None (quit)
        """)    
        ans=raw_input("What Threshold Type? ") 
        if ans=="1": 
            ans = False
            ttype = 'height'
        elif ans=="2":
            ans = False
            ttype = 'normal'
        elif ans=="3":
            ans = False
            ttype = 'heightT'
        elif ans=="4":
            ans = False
            ttype = 'abort'
    return ttype

def FractalMenu():
    fractal = False
    ans = raw_input("Fractal? [Y/N]")
    if ans == 'Y' or ans == 'y':
        fractal = True
    return fractal

def DoYouWantToQuit():
    ans = raw_input("Do you want to quit? [Y/N]")
    toquit = False
    if ans == 'Y' or ans == 'y':
        toquit = True
    return toquit

def FractalMenu2():
    a1 = True
    abort = False
    while a1:
        a2 = True
        while a2:
            ans=raw_input("Please enter a NSize (value) this is zoom level [from 0.00001 to 10000]: \n")
            nsize = ans
            try:
                nsize = float(nsize)
                a2 = False
            except:
                print("Not a valid nsize.")
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
                continue
            if not 10000 >= nsize >= .0000001:
                print("Not a valid nsize.")
                a2 = True
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
        a2 = True
        if not a1:
            break
        while a2:
            ans=raw_input("Please enter a NBasis type [integer from 0 to 9]: \n")
            nbasis = ans
            try:
                nbasis = int(nbasis)
                a2 = False
            except:
                print("Not a valid Nbasis value.")
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
                continue
            if not 0 <= nbasis <= 9:
                print("Not a valid Nbasis value.")
                a2 = True
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
        a2 = True
        if not a1:
            break
        while a2:
            ans=raw_input("Please enter a lacunarity value [float from .01 to 6.000, typical value is 2.0]: \n")
            lacunarity = ans
            try:
                lacunarity = float(lacunarity)
                a2 = False
            except:
                print("Not a valid lacunarity value.")
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
                continue
            if not .01 <= lacunarity <= 6.0:
                print("Not a valid lacunarity value.")
                a2 = True
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
        a2 = True
        if not a1:
            break
        while a2:
            ans=raw_input("Please enter a depth value [integer from 1 to 16, typical value is 3]: \n")
            depth = ans
            try:
                depth = int(depth)
                a2 = False
            except:
                print("Not a valid depth value.")
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
                continue
            if not 1 <= depth <= 16:
                print("Not a valid depth value.")
                a2 = True
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
        a2 = True
        if not a1:
            break
        while a2:
            ans=raw_input("Please enter a dimension value [float from .01 to 2.0, typical value is 1.0]: \n")
            dimension = ans
            try:
                dimension = float(dimension)
                a2 = False
            except:
                print("Not a valid depth value.")
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
                continue
            if not .01 <= dimension <= 2.0:
                print("Not a valid depth value.")
                a2 = True
                if DoYouWantToQuit():
                    abort = True
                    a1 = False
                    a2 = False
        if not a1:
            break
        returndict = {'nbasis':nbasis,'nsize':nsize, 'lacunarity':lacunarity,
                      'depth':depth, 'dimension': dimension}
        print("""You entered """, returndict, """ for the fractal values.""")
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    if not abort:
        return returndict
    else:
        return {'abort':'abort'}

def setColorPosition(tmcolorsdict):
    a1 = True
    pos = None
    while a1:
        ans = raw_input("Enter the position of the color [float from 0 to 1]: ")
        try:
            pos = float(ans)

            
            if pos in tmcolorsdict:
                print("Color position already in TM Colors dictionary.")
                pos = None
                if DoYouWantToQuit():
                    break
            if not 0.0 <= pos <= 1.0:
                print("Color position is not valid.  Needs to be a float between 0 and 1. ")
                pos = None
                if DoYouWantToQuit():
                    break
            else:
                a1 = False
        except:
            print("Not a valid entry.")
            if DoYouWantToQuit():
                break
    return pos

def getColorNameMenu(tmcolorsdict, Colors=Colors):
    a1 = True
    tmcolorvalues = list(tmcolorsdict.values())
    returnstr = ""
    while a1:
        ans = raw_input("Enter the name of the color: ")
        if not str(ans) in Colors:
            print("Not a valid color in the Colors dictionary.")
            returnstr = ""
            if DoYouWantToQuit():
                break
        else:
            if Colors[str(ans)] in tmcolorvalues:
                print("Color already in TMColorsdict.")
                if DoYouWantToKeep():
                    returnstr = str(ans)
                    a1 = False
                else:
                    if DoYouWantToQuit():
                        break
            else:
                returnstr = str(ans)
                a1 = False
    return returnstr

def getColorValue(tmcolorsdict):
    a1 = True
    colorval = (None,None,None)
    while a1:
        a2 = True
        tmcolorvalues = list(tmcolorsdict.values())
        rcolorval = 0
        bcolorval = 0
        gcolorval = 0

        while a2:
            ans=raw_input("Please add a Red color value (RGB) (0-255 integer per channel) format: \n")
            rcolorval = ans
            try:
                rcolorval = int(rcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Green color value (RGB) (0-255 integer per channel) format: \n")
            gcolorval = ans
            try:
                gcolorval = int(gcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Blue color value (RGB) (0-255 integer per channel) format: \n")
            bcolorval = ans
            try:
                bcolorval = int(bcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        colorval = (rcolorval,gcolorval,bcolorval)
        if colorval in tmcolorvalues:
            print("Color already in TMColorsdict.")
            if DoYouWantToKeep():
                a1 = False
            else:
                if DoYouWantToQuit():
                    break
        else:
            a1 = False
        print("""You entered """, colorval, """ color values.""")
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    
    return colorval

def TMColorInputMenu(tmcolorsdict, Colors=Colors):
    a1 = True
    while a1:
        print ("""
        1.Add existing color from Colors Dictionary
        2.Show colors from Colors Dictionary
        3.Input manually an RGB color value
        4.Show TM colors and positions (in dictionary form)
        5.Abort/Done (go to previous TM color menu)
        """)
        ans=raw_input("What would you like to do? ")
        if ans == "1":
            colorname = getColorNameMenu(tmcolorsdict)
            if colorname != "":
                pos = setColorPosition(tmcolorsdict)
                if not pos == None:
                    tmcolorsdict[pos] = Colors[colorname]
                else:
                    print("Not able to add color entry.")
            else:
                print("Not able to add color entry.")
        elif ans == "2":
            print(Colors)
        elif ans == "3":
            colorval = getColorValue(tmcolorsdict)
            if colorval[0] == None:
                print("Not able to add color entry.")
            else:
                pos = setColorPosition(tmcolorsdict)
                if not pos == None:
                    tmcolorsdict[pos] = colorval
                else:
                    print("Not able to add color entry.")
        elif ans == "4":
            print(tmcolorsdict)
        elif ans == "5":
            print("Leaving TM Color Input menu.")
            a1 = False

def TMDeleteColorMenu(tmcolorsdict, Colors=Colors):
    a1 = True
    abort = False
    colorname = ""
    while a1:
        print("Here are the the tm colors: ")
        print(tmcolorsdict)
        ans=raw_input("What color do you want to delete? [by position]: ")
        bcolorval = ans
        try:
            bcolorval = int(bcolorval)
        except:
            print("Not a valid colorvalue.")
            ans = raw_input("Try again? [Y/N]: ")
            if ans == "N" or ans == "n":
                a1 = False
                abort = True
            continue    

        print("""You want to delete """, bcolorval)
        
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    if not abort:
        colorname += str(bcolorval)
        colorname += " "
        colorname += str(tmcolorsdict[bcolorval])
        del tmcolorsdict[bcolorval]
    else:
        colorname = "None"
    return colorname

def TMColorChangeMenu(tmcolorsdict, Colors=Colors):
    a1 = True
    abort = False
    changePos = False
    while a1:
        print("Here are the TM Colors: ")
        print(tmcolorsdict)
        ans=raw_input("What color do you want to change? [by position]: ")
        colorpos = ans
        try:
            colorpos = float(colorpos)
        except:
            print("Not a valid color position.")
            ans = raw_input("Try again? [Y/N]: ")
            if ans == "N" or ans == "n":
                a1 = False
                abort = True
            continue
        
        if not colorpos in tmcolorsdict:
            print("Color position is not found.")

            ans = raw_input("Try again? [Y/N]: ")
            if ans == "N" or ans == "n":
                a1 = False
                abort = True
            continue
        ans = raw_input("Do you want to change the position of this color:? [Y/N] \n")
        if ans == "Y" or ans == "y":
            changePos = True
            pos = setColorPosition(tmcolorsdict)
            if not pos == None:
                colorpos2 = pos
        a2 = True
        rcolorval = 0
        bcolorval = 0
        gcolorval = 0
        while a2:
            ans=raw_input("Please add a Red color value (RGB) (0-255 integer per channel) format: \n")
            rcolorval = ans
            try:
                rcolorval = int(rcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Green color value (RGB) (0-255 integer per channel) format: \n")
            gcolorval = ans
            try:
                gcolorval = int(gcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        a2 = True
        while a2:
            ans=raw_input("Please add a Blue color value (RGB) (0-255 integer per channel) format: \n")
            bcolorval = ans
            try:
                bcolorval = int(bcolorval)
                a2 = False
            except:
                print("Not a valid colorvalue.")
                continue
        colorval = (rcolorval,gcolorval,bcolorval)
        if not changePos:
            print("""You entered """, colorpos, """ for the color position.""")
        else:
            print("""You entered """, colorpos, """ for the old color position to be changed.""")
            print("""You entered """, colorpos2, """ for the new color position.""")
        print("""You entered """, colorval, """ color values.""")
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            a1 = False
    if not abort:
        if not changePos:
            tmcolorsdict[colorpos] = colorval
            colorname = str(colorpos)
            colorname += " "
            colorname += str(colorval)
        else:
            del tmcolorsdict[colorpos]
            tmcolorsdict[colorpos2] = colorval
            colorname = str(colorpos)
            colorname += "removed and updated to "
            colorname += str(colorpos2)
            colorname += " "
            colorname += str(colorval)            
    else:
        colorname = "None"
    return colorname

def TMColorsMenu(tmcolorsdict, Colors = Colors):
    ans=True
    while ans:
        print ("""
        1.List TM Colors
        2.How many TM colors are there?
        3.Input TM colors
        4.Delete a TM color(by color position key).
        5.Change a TM color value(by color position key).
        6.Done updating.
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1": 
            print(tmcolorsdict) 
        elif ans=="2":
            print(len(tmcolorsdict)) 

        elif ans=="3":
            TMColorInputMenu(tmcolorsdict)
            print("Left the TM Color input menu.")
        elif ans=="4":
            color = TMDeleteColorMenu(tmcolorsdict)
            print("""Deleted: """, color)
        elif ans=="5":
            color = TMColorChangeMenu(tmcolorsdict)
            print(color, " changed.")
        elif ans=="6":
          print("\n Going back to the main menu!")
          ans = False
          if len(tmcolorsdict) <= 1:
              print("You should add more colors (at least 2)!")
              if not DoYouWantToQuit():
                  ans = True
        elif ans !="":
          print("\n Not Valid Choice Try again")

def AreYouSureQuit():
    ans = raw_input("Are you sure you want to quit? [Y/N]")
    toquit = False
    if ans == 'Y' or ans == 'y':
        toquit = True
    return toquit

def GetTBpositionMenu():
    a1 = True
    pos = None
    while a1:
        ans = raw_input("Enter the position[float from 0 to 1]: ")
        try:
            pos = float(ans)

            if not 0.0 <= pos <= 1.0:
                print("Color position is not valid.  Needs to be a float between 0 and 1. ")
                pos = None
                if DoYouWantToQuit():
                    break
            else:
                a1 = False
        except:
            print("Not a valid entry.")
            if DoYouWantToQuit():
                break
    return pos    

def TMInputMenu(Colors=Colors, TM = TM, maxindex = maxindex):
    a1 = True
    tmdat = {}
    rtmdat = {}
    while a1:
        tmindex = maxindex
        NamegetMenu()
        a2 = True
        while a2:
            landtype = LandtypeGetMenu()
            if landtype == 'abort':
                if AreYouSureQuit():
                    a2 = False
                    a1 = False
                    break
            else:
                tmdat['Landtype']=landtype
                a2 = False
                    
        if not a1:
            break
        a2 = True
        while a2:
            ttype = TypeGetMenu()
            if ttype == 'abort':
                if AreYouSureQuit():
                    a2 = False
                    a1 = False
                    break
            else:
                tmdat['Type'] = ttype
                tmdat['ThreshType'] = ttype
                a2 = False
                    
        if not a1:
            break
        fractal = FractalMenu()
        if fractal:
            tmdat['Fractal'] = True
            a2 = True
            while a2:
                fractaldict = FractalMenu2()
                if 'abort' in fractaldict:
                    if AreYouSureQuit():
                        a2 = False
                        a1 = False
                        break
                else:
                    for fdkey in fractaldict:
                        tmdat[fdkey] = fractaldict[fdkey]
                    a2 = False
        else:
            tmdat['Fractal'] = False
        if not a1:
            break
        tmcolorsdict = {}
        TMColorsMenu(tmcolorsdict)
        col=[]
        tmckeys = list(tmcolorsdict.keys())
        tmckeys.sort()
        for tmckey in tmckeys:
            col.append([tmcolorsdict[tmckey],tmckey])
        tmdat['Colors'] = col
        a2 = True
        while a2:
            print ("First TBracket entry position this should be a lower value relative a second entry.")
            tbrackpos1 = GetTBpositionMenu()
            if tbrackpos1 == None:
                print("No entry.")
                if DoYouWantToQuit():
                    a1 = False
                    break
            else:
                print("Second TBracket entry position this should be > first.")
                tbrackpos2 = GetTBpositionMenu()
                if tbrackpos2 == None:
                    print("No 2nd entry.")
                    if DoYouWantToQuit():
                        a1 = False
                        break
                else:
                    if tbrackpos1 > tbrackpos2:
                        print("2nd entry greater than the first.")
                        print("We'll swap these.")
                        tbrackpos2a = tbrackpos1
                        tbrackpos1 = tbrackpos2
                        tbrackpos2 = tbrackpos2a
                    tmdat['TBracket'] = [tbrackpos1,tbrackpos2]
                    a2 = False
        if not a1:
            break
        if ttype == 'heightT':
            a2 = True
            while a2:
                print ("First TBracket2 entry position this should be a lower value relative a second entry.")
                tbrackpos3 = GetTBpositionMenu()
                if tbrackpos3 == None:
                    print("No entry.")
                    if DoYouWantToQuit():
                        a1 = False
                        break
                else:
                    print("Second TBracket2 entry position this should be > first.")
                    tbrackpos4 = GetTBpositionMenu()
                    if tbrackpos4 == None:
                        print("No 2nd entry.")
                        if DoYouWantToQuit():
                            a1 = False
                            break
                    else:
                        if tbrackpos3 > tbrackpos4:
                            print("2nd entry greater than the first.")
                            print("We'll swap these.")
                            tbrackpos4a = tbrackpos3
                            tbrackpos3 = tbrackpos4
                            tbrackpos4 = tbrackpos4a
                        tmdat['TBracket2'] = [tbrackpos3,tbrackpos4]
                        a2 = False
        if not a1:
            break            
        tmdat["id"] = maxindex[0]
        print("""You entered """, tmdat)
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            rtmdat = tmdat.copy()
            incrementMaxIndex()
            a1 = False
            
    return rtmdat

def DeleteTM(TM=TM):
    a1 = True
    while a1:
        if len(TM) == 0:
            print("Nothing to delete in TM since it is empty!")
            break
        ans = raw_input("Please enter the index value: ")
        try:
            ans = int(ans)
            if 0<= ans <= len(TM)-1:
                print("Deleting...", TM[ans])
                del TM[ans]
                a1 = False
            else:
                print("Invalid entry.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False

def DeleteTMMenu(TM=TM):
    ans=True
    while ans:
        print ("""
        1.List Threshold Modules by Index
        2.Delete a TM (by Index).
        3.Go back to previous Menu.
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1":
            for i,t in enumerate(TM):
                print("Index:")
                print(i)
                print("TM: ")
                print(t)
        elif ans =="2":
            DeleteTM()
        elif ans =="3":
            ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")            

def TMMenu(TM=TM):
    ans=True
    while ans:
        print ("""
        1.List Threshold Module dictionary
        2.List Threshold Module names.
        3.How many TMs are there?
        4.Input a TM
        5.Delete a TM.
        6.Change a TM.
        7.Go to Main Menu
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1": 
            print(TM) 
        elif ans=="2":
            namelist = []
            for key in TM:
                val = [key,TM[key]['Name']]
                namelist.append(val)
            
        elif ans=="3":
            print("There are ",len(TM)," TMs")
        elif ans=="4":
            tmdat = TMInputMenu()
            if len(tmdat) == 0:
                print("TM Data input aborted!")
            else:
                TM.append(tmdat)
                print("TM Data input received and added.")
##            print("""TM name: """, tmname, """ added.""")
        elif ans=="5":
            DeleteTMMenu()
        elif ans=="6":
##            tmname = TMChangeMenu()
            print("Nothing changed.")
        elif ans=="7":
          print("\n Going back to the main menu!")
          ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")
          
print('Welcome to the Terrain colorization assistant!')
print("Let's go ahead and add some terrain colors!")
def MainMenu():
    ans=True
    while ans:
        print ("""
        1.Add/Modify Colors dictionary
        2.Add/Modify Threshold dictionary
        3.Add/Modify Direct Color Input dictionary
        4.Add/Modify Mixer Modules dictionary
        5.Add/Modify Node Chains dictionary
        6.Set Flood/Mount stage
        7.Exit/Quit
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1": 
    ##      print("\n Student Added")
            ColorMenu()
            print("Leaving Color Menu...")
        elif ans=="2":
            TMMenu()
    ##      print("\n Student Deleted") 
        elif ans=="3":
            print("not there yet.")
        elif ans=="4":
    ##      print("\n Goodbye")
            print("not there yet.")
        elif ans=="5":
            print("not there yet.")
        elif ans=="7":
            print("\n Goodbye")
            ans = False
        elif ans !="":
            print("\n Not Valid Choice Try again")
MainMenu()
