import shelve
filename = "/home/strangequark/colorizeterrain.db"
CTDAT = shelve.open(filename)
Colors = {}
TM = []
DCI = {}
DCI_LTYPE = {'Flood':[], 'Land':[], 'Mount':[]}
DCI_NAMEIDS = {}
MM = {}
NCs = {}
maxindex = [1]
cflist = [.05,.1,.2,.3,.4,.5,.6,.7,1.0,-1.0]
flood = .1
mount = .9
fm = (flood,mount)
fmdiff = abs(flood - mount)
maxindex_s1 = [29]
Colors_s1 = {'Sand1':(252,252,220),'Sand2':(245,244,223), 'Sand3':(222,221,197),
             'Grass1':(205,237,173),'Grass2':(194,227,161),
             'Grass3':(174,207,140), 'Dirt':(247,235,178),'Dirt2':(232,221,172),
             'Dirt3':(209,200,157), 'Rock1':(245,242,230),'Rock2':(214,213,206),
             'Rock3':(181,178,167), 'Snow1':(250,249,247),'Snow2':(242,240,230),
             'Snow3':(232,232,232), 'Water1':(13,186,146),'Water2':(12,168,116),
             'Water3':(5,163,100), 'Iron1':(245,175,24), 'Iron2':(219,157,22),
             'Terracotta':(221,169,121), 'Sandstone':(242,237,218),
             'Charcoal':(147,145,146), 'Clay':(213,195,157),
             'OliveClay':(197,200,191), 'DesertSand':(221,190,146)}
TM_s1 = [{'Landtype':'Land', 'Type': 'height',
          'TBracket':[flood,flood+fmdiff/4.0], 'Fractal': True,
        'Colors':[[Colors_s1['Sand1'],0],[Colors_s1['Sand2'],.5],
                  [Colors_s1['Sand3'],1.0]], 'Name': 'LLDFractal',
        'nsize': 100.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.0, 'id': 1, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'height',
         'TBracket':[flood,flood+fmdiff/4.0], 'Fractal': False,
        'Colors':[[Colors_s1['Sand1'],0],[Colors_s1['Sand2'],.5],
                  [Colors_s1['Sand3'],1.0]], 'Name': 'LLDFractal',
        'nsize': 100.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.0, 'id': 2, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'height',
          'TBracket':[flood,flood+fmdiff/4.0], 'Fractal': True,
        'Colors':[[Colors_s1['Sand1'],0],[Colors_s1['Sand2'],.5],
                  [Colors_s1['Sand3'],1.0]], 'Name': 'LLDFractal',
        'TBracket2': [-float('inf'),.2],
        'Cutoff':[float('inf'),flood+fmdiff/4.0],
        'nsize': 100.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.0, 'id': 11, 'ThreshType': 'heightT'},
        {'Landtype':'Land', 'Type': 'height',
          'TBracket':[flood,flood+fmdiff/4.0], 'Fractal': False,
        'Colors':[[Colors_s1['Sand1'],0],[Colors_s1['Sand2'],.5],
                  [Colors_s1['Sand3'],1.0]], 'Name': 'LLDFractal',
        'TBracket2': [-float('inf'),.2],
        'Cutoff':[float('inf'),flood+fmdiff/4.0],
        'nsize': 100.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.0, 'id': 12, 'ThreshType': 'heightT'},
        {'Landtype':'Land', 'Type': 'height',
         'TBracket':[flood+fmdiff/4.0,mount], 'Fractal': True,
        'Colors':[[Colors_s1['Dirt'],0],[Colors_s1['Dirt2'],.2],
                  [Colors_s1['Dirt3'],.4], [Colors_s1['Grass1'],.6],
                  [Colors_s1['Grass2'],.8], [Colors_s1['Grass3'],1.0]],
         'Name': 'LHDFractal',
        'nsize': 100.0, 'nbasis': 0, 'lacunarity':2.0,
        'depth':16, 'dimension':1.1, 'id': 3, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'height',
         'TBracket':[flood+fmdiff/4.0,mount], 'Fractal': False,
        'Colors':[[Colors_s1['Dirt'],0],[Colors_s1['Dirt2'],.2],
                  [Colors_s1['Dirt3'],.4], [Colors_s1['Grass1'],.6],
                  [Colors_s1['Grass2'],.8], [Colors_s1['Grass3'],1.0]],
         'Name': 'LHDFractal',
        'nsize': 100.0, 'nbasis': 0, 'lacunarity':2.0,
        'depth':16, 'dimension':1.1, 'id': 4, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'normal', 'TBracket':[.1,1], 'Fractal': True,
        'Colors':[[Colors_s1['Iron2'],0],[Colors_s1['Rock2'],.5],
                  [Colors_s1['Rock3'],1.0]], 'Name': 'LLRFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.1, 'id': 5, 'ThreshType': 'normal'},
        {'Landtype':'Land', 'Type': 'normal', 'TBracket':[.1,1], 'Fractal': True,
        'Colors':[[Colors_s1['Iron1'],0],[Colors_s1['Rock2'],.5],
                  [Colors_s1['Rock1'],1.0]], 'Name': 'LLHFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.1, 'id': 6, 'ThreshType': 'normal'},
        {'Landtype':'Flood', 'Type': 'height', 'TBracket':[0,flood],
         'Fractal': True,
        'Colors':[[Colors_s1['Water1'],0],
                  [Colors_s1['Water2'],.5],[Colors_s1['Water3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 7, 'ThreshType': 'height'},
        {'Landtype':'Flood', 'Type': 'height', 'TBracket':[0,flood],
         'Fractal': False,
        'Colors':[[Colors_s1['Water1'],0],
                  [Colors_s1['Water2'],.5],[Colors_s1['Water3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 8, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'height', 'TBracket':[0,flood],
         'Fractal': True, 'TBracket2': [-1,.2],
        'Colors':[[Colors_s1['Water1'],0],
                  [Colors_s1['Water2'],.5],[Colors_s1['Water3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 13, 'ThreshType': 'heightT'},
        {'Landtype':'Flood', 'Type': 'height', 'TBracket':[0,flood],
         'Fractal': False, 'TBracket2': [-1,.2],
        'Colors':[[Colors_s1['Water1'],0],
                  [Colors_s1['Water2'],.5],[Colors_s1['Water3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 14, 'ThreshType': 'heightT'},
        {'Landtype':'Mount', 'Type': 'height', 'TBracket':[mount,1.0],
         'Fractal': True,
        'Colors':[[Colors_s1['Snow1'],0],
                  [Colors_s1['Snow2'],.5],[Colors_s1['Snow3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 9, 'ThreshType': 'height'},
        {'Landtype':'Mount', 'Type': 'height', 'TBracket':[mount,1.0],
         'Fractal': False,
        'Colors':[[Colors_s1['Snow1'],0],
                  [Colors_s1['Snow2'],.5],[Colors_s1['Snow3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 10, 'ThreshType': 'height'},
        {'Landtype':'Land', 'Type': 'height', 'TBracket':[mount,1.0],
         'Fractal': True, 'TBracket2': [.2,-float('inf')],
        'Colors':[[Colors_s1['Snow1'],0],
                  [Colors_s1['Snow2'],.5],[Colors_s1['Snow3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 15, 'ThreshType': 'heightT'},
        {'Landtype':'Land', 'Type': 'height', 'TBracket':[mount,1.0],
         'Fractal': False, 'TBracket2': [.2,-float('inf')],
        'Colors':[[Colors_s1['Snow1'],0],
                  [Colors_s1['Snow2'],.5],[Colors_s1['Snow3'],1]],
         'Name': 'WLFractal',
        'nsize': 40.0, 'nbasis': 3, 'lacunarity':2.1,
        'depth':16, 'dimension':1.3, 'id': 16, 'ThreshType': 'heightT'}
         ]
MM_s1={17: {'id': 17, 'Landtype': 'Land', 'Ins': (1,2), 'Outs': 17, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': True},
       18: {'id': 18, 'Landtype': 'Land', 'Ins': (11,12), 'Outs': 18, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': False},
       19: {'id': 19, 'Landtype': 'Land', 'Ins': (3,4), 'Outs': 19, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': True},
       20: {'id': 20, 'Landtype': 'Land', 'Ins': (5,6), 'Outs': 20, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': False},
       21: {'id': 21, 'Landtype': 'Land', 'Ins': (0,20), 'Outs': 21, 'Type':
          'normal2', 'FactorType' : 'falloff', 'FactorVar': 'normalT',
          'TBracket' : [.1,1],
          'Factor':.5, 'Falloff':[.2,-1], 'MainOut': True},
       22: {'id': 22, 'Landtype': 'Flood', 'Ins': (7,8), 'Outs': 22, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': True},
       23: {'id': 23, 'Landtype': 'Mount', 'Ins': (9,10), 'Outs': 23, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': True},
       24: {'id': 24, 'Landtype': 'Land', 'Ins': (13,14), 'Outs': 24, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': False},
       25: {'id': 25, 'Landtype': 'Land', 'Ins': (15,16), 'Outs': 25, 'Type':
          'normal2', 'FactorType' : 'fixed', 'FactorVar': 'height',
          'Factor':.5, 'Falloff':0, 'MainOut': False},
       26: {'id': 26, 'Landtype': 'Land', 'Ins': (0,18), 'Outs': 26, 'Type':
          'normal2', 'FactorType' : 'falloff', 'FactorVar': 'heightT',
          'TBracket':[flood,flood+fmdiff/4.0],
          'Factor':.5, 'Falloff':[.2,-1], 'MainOut': True},
       27: {'id': 27, 'Landtype': 'Land', 'Ins': (0,24), 'Outs': 27, 'Type':
          'normal2', 'FactorType' : 'falloff', 'FactorVar': 'heightT',
          'TBracket':[0,flood],
          'Factor':.5, 'Falloff':[-1,.2], 'MainOut': True},
       28: {'id': 28, 'Landtype': 'Land', 'Ins': (0,25), 'Outs': 28, 'Type':
          'normal2', 'FactorType' : 'falloff', 'FactorVar': 'heightT',
          'TBracket':[mount,1],
          'Factor':.5, 'Falloff':[.2,-1], 'MainOut': True}
       }

NCs_s1 = {5:{'Chain':[20,21],'Dependencies':[-1]},
       1:{'Chain':[17],'Dependencies':[-1]},
       3:{'Chain':[19],'Dependencies':[-1]},
       7:{'Chain':[22],'Dependencies':[-1]},
       9:{'Chain':[23],'Dependencies':[-1]},
       11:{'Chain':[18,26],'Dependencies':[-1]},
       13:{'Chain':[24,27],'Dependencies':[-1]},
##       19:{'Chain':[22],'Dependencies':[-1]}
       15:{'Chain':[25,28],'Dependencies':[-1]}
       }

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
    ans = raw_input("Please add a name: ")
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
        name = NamegetMenu()
        tmdat['Name'] = name
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

def ChangeMore():
    ans = raw_input("Do you want to change more? [Y/N]")
    if ans == "Y" or ans == "y":
        return True
    else:
        return False

def InputValue(bounds,typ, name):
    a,b,c = bounds
    a1 = True
    ri = None
    str1 = "Please enter a value for "
    str1 += name
    str1 += "[a "
    str1 += typ
    str1 += " from "
    str1 += str(a)+" to "+str(b) + ". default is set at " + str(c)
    str1 += "]: "
    while a1:
        ans = raw_input(str1)
        try:
            if typ == 'float':
                ans = float(ans)
            elif typ == 'int':
                ans = int(ans)
            if a <= ans <= b:
                ri = ans
            else:
                print("Invalid input.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid input.")
            if DoYouWantToQuit():
                a1 = False
    return ri

def getTBMenu(tmdat,one = True):
    a2 = True
    twost = "2"
    while a2:
        str1 = "First TBracket"
        if not one:
            str1 += twost
        str1 += " entry position this should be a lower value relative a "
        str1 += "second entry: "
        print (str1)
        tbrackpos1 = GetTBpositionMenu()
        if tbrackpos1 == None:
            print("No entry.")
            if DoYouWantToQuit():
                break
        else:
            str1 = "Second TBracket"
            if not one:
                str1 += twost
            str1 += " entry position this be greater than the first: "
            print(str1)
            tbrackpos2 = GetTBpositionMenu()
            if tbrackpos2 == None:
                print("No 2nd entry.")
                if DoYouWantToQuit():
                    break
            else:
                if tbrackpos1 > tbrackpos2:
                    print("2nd entry greater than the first.")
                    print("We'll swap these.")
                    tbrackpos2a = tbrackpos1
                    tbrackpos1 = tbrackpos2
                    tbrackpos2 = tbrackpos2a
                if one:
                    print ("Updating TBracket")
                    tmdat['TBracket'] = [tbrackpos1,tbrackpos2]
                else:
                    print ("Updating TBracket2")
                    tmdat['TBracket2'] = [tbrackpos1,tbrackpos2]
                a2 = False

def TMChangeMenuKey(tmdat):
    a1 = True
    while a1:
        print(tmdat)
        ans = raw_input("Please enter the TM key: ")
        print(ans)
        ans = ans.strip()
        if ans in tmdat:
            if ans == 'LandType':
                landtype = LandtypeGetMenu()
                if landtype == 'abort':
                    if AreYouSureQuit():
                        a1 = False
                else:
                    str1 = "Changed LandType from "
                    str1 += tmdat['LandType']
                    str1 += " to "
                    str1 += landtype
                    print(str1)                    
                    tmdat['Landtype']=landtype
                    if not ChangeMore():
                        a1 = False
                    
            elif ans == 'Name':
                name = NamegetMenu()
                str1 = "Changed Name from "
                str1 += tmdat['Name']
                str1 += " to "
                str1 += name
                print(str1)
                tmdat['Name'] = name
                if not ChangeMore():
                    a1 = False
            elif ans == 'Type':
                ttype = TypeGetMenu()
                if ttype == 'abort':
                    if AreYouSureQuit():
                        a1 = False
                else:
                    str1 = "Changed Type from"
                    str1 += tmdat['Type']
                    str1 += " to "
                    str1 += ttype
                    print(str1)                    
                    tmdat['Type'] = ttype
##                    tmdat['ThreshType'] = ttype
                    if not ChangeMore():
                        a1 = False
            elif ans == 'Fractal':
                fractal = FractalMenu()
                if fractal and not tmdat['Fractal']:
                    tmdat['Fractal'] = True
                    a2 = True
                    while a2:
                        print("Adding Fractal values...")
                        fractaldict = FractalMenu2()
                        if 'abort' in fractaldict:
                            if AreYouSureQuit():
                                a1 = False
                                a2 = False
                        else:
                            for fdkey in fractaldict:
                                str1 = "Adding fractal key "
                                str1 += fdkey
                                str1 += " with value "
                                str1 += str(fractaldict[fdkey])
                                print(str1)
                                tmdat[fdkey] = fractaldict[fdkey]
                            a2 = False
                            if not ChangeMore():
                                a1 = False
                elif fractal and tmdat['Fractal']:
                    ('Fractal value remains true.  No change.')
                else:
                    tmdat['Fractal'] = False
            elif ans == 'nsize':
                bounds = (.01, 10000, 20.0)
                typ = "float"
                fname = "nsize"
                rv = InputValue(bounds,typ, fname)
                str1 = "Changed " + fname+ " from " + str(tmdat['nsize'])
                str1 += " to " + str(rv)
                print(str1)
                tmdat['nsize'] = rv
                if not ChangeMore():
                    a1 = False
            elif ans == 'nbasis':
                bounds = (0, 1, 0)
                typ = "int"
                fname = "nbasis"
                rv = InputValue(bounds,typ, fname)
                str1 = "Changed " + fname+ " from " + str(tmdat['nbasis'])
                str1 += " to " + str(rv)
                print(str1)
                tmdat['nbasis'] = rv
                if not ChangeMore():
                    a1 = False
            elif ans == 'lacunarity':
                bounds = (0.01, 6.0, 2.0)
                typ = "float"
                fname = "lacunarity"
                rv = InputValue(bounds,typ, fname)
                str1 = "Changed " + fname+ " from " + str(tmdat['lacunarity'])
                str1 += " to " + str(rv)
                print(str1)
                tmdat['lacunarity'] = rv
                if not ChangeMore():
                    a1 = False
            elif ans == 'depth':
                bounds = (1.0, 16.0, 6.0)
                typ = "float"
                fname = "depth"
                rv = InputValue(bounds,typ, fname)
                str1 = "Changed " + fname+ " from " + str(tmdat['depth'])
                str1 += " to " + str(rv)
                print(str1)
                tmdat['depth'] = rv
                if not ChangeMore():
                    a1 = False 
            elif ans == 'dimension':
                bounds = (0, 1, 0)
                typ = "float"
                fname = "dimension"
                rv = InputValue(bounds,typ, fname)
                str1 = "Changed " + fname+ " from " + str(tmdat['dimension'])
                str1 += " to " + str(rv)
                print(str1)
                tmdat['dimension'] = rv
                if not ChangeMore():
                    a1 = False
            elif ans == 'TBracket':
                getTBMenu(tmdat)
                if not ChangeMore():
                    a1 = False
            elif ans == 'TBracket2':
                getTBMenu(tmdat,one = False)
                if not ChangeMore():
                    a1 = False
            elif ans == 'Colors':
                tmcolorsdict = {}
                for color in tmdat['Colors']:
                    c, cpos = color
                    tmcolorsdict[cpos] = c
                TMColorsMenu(tmcolorsdict)
                col=[]
                tmckeys = list(tmcolorsdict.keys())
                tmckeys.sort()
                for tmckey in tmckeys:
                    col.append([tmcolorsdict[tmckey],tmckey])
                print("Updating colors...")
                tmdat['Colors'] = col
        else:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False    

def TMChangeMenuIndex(TM=TM):
    a1 = True
    while a1:
        if len(TM) == 0:
            print("Nothing to change in TM since it is empty!")
            a1 = False
            break
        ans = raw_input("Please enter the index value: ")
        try:
            ans = int(ans)
            if 0<= ans <= len(TM)-1:
                print("Loading TM change menu for...", TM[ans])
                tmdict = TM[ans]
                TMChangeMenuKey(tmdict)
                TM[ans] = tmdict
                a1 = False
            else:
                print("Invalid entry.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False

def TMChangeMenu(TM=TM):
    ans=True
    while ans:
        print ("""
        1.List Threshold Modules by Index
        2.Change a TM (by index).
        3.Go back to previous Menu.
        """)
        ans=raw_input("What would you like to do? ") 
        if ans == "1":
            for i,t in enumerate(TM):
                print("Index:")
                print(i)
                print("TM: ")
                print(t)
        elif ans == "2":
            TMChangeMenuIndex()
        elif ans == "3":
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
                val = key['Name']
                namelist.append(val)
            print(namelist)
            
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
            TMChangeMenu()
            ##print("Nothing changed.")
        elif ans=="7":
          print("\n Going back to the main menu!")
          ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")
          

def addLandTypeEntries(sindex, DCI_LTYPE = DCI_LTYPE):
    returnval = None
    a1 = True
    while a1:
        print("This is DCI_LTYPE (LandType) assistance.")
        ans = raw_input("How many LandTypes do you want to change this color to? (int)")
        try:
            ans = int(ans)
            if 1 <= ans <= 3:
                nlist = ["first", "second", "third"]
                landtypes = []
                for i in range(ans):
                    str1 = "Enter the " + nlist[i] +" LandType."
                    print(str1)
                    landtype = LandtypeGetMenu()
                    if landtype == 'abort':
                        print("No LandType selected.")
                    else:
                        landtypes.append(landtype)
                if len(landtypes)== 0:
                    print("No LandTypes entered exiting DCI_LTYPE assistance...")
                    break
                matchedsel = []
##                for ltsel in landtypes:
                for lt in DCI_LTYPE:
                    if sindex in DCI_LTYPE[lt]:
                        if lt in landtypes:
                            matchedsel.append(ltsel)
                            str1 = ltsel + " input LandType already exists"
                            str1 += "for the selected DCI key index."
                            str1 += "No changes being made for this."
                for ltsel in landtypes:
                    if not ltsel in matchedsel:
                        DCI_LTYPE[ltsel].append(sindex)
                        str1 = "Added DCI selection key " + sindex
                        str1 += " for LandType " + ltsel + "in the DCI_LTYPE."
                        print(str1)
                a1 = False
            else:
                print("You entered a number too small or too large.  Your entry should be between 1 and 3.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Unable to process request.")
            if DoYouWantToQuit():
                a1 = False

def DCIInputMenu(DCI=DCI, DCI_NAMEIDS=DCI_NAMEIDS, DCI_LTYPE=DCI_LTYPE,
                 Colors=Colors, maxindex = maxindex):
    a1 = True
    while a1:
        print ("""
        DCI Color Input Menu:
        1.Add existing color from Colors Dictionary
        2.Show colors from Colors Dictionary
        3.Input manually an RGB color value
        4.Show DCI data (in dictionary form)
        5.Abort/Done (go to previous DCI color menu)
        """)
        ans=raw_input("What would you like to do? ")
        if ans == "1":
            colorname = getColorNameMenu(DCI)
            if colorname != "":
                addLandTypeEntries(maxindex[0])
                DCI[maxindex[0]] = Colors[colorname]
                str1 = "You've added a new key: "
                str1 += maxindex + " and color "
                str1 += colorname
                print(str1)
                DCI_NAMEIDS[maxindex[0]] = colorname
                str1 = "DCI ID: "
                str1 += str(maxindex[0])
                str1 += " has been assigned with the name "
                str1 += colorname
                print(str1)
                incrementMaxIndex()
            else:
                print("Not able to add color entry.")
        elif ans == "2":
            print(Colors)
        elif ans == "3":
            print("A Color Name needs to be added for this entry.")
            colorname = NamegetMenu()
            colorval = getColorValue(DCI)
            if colorval[0] == None:
                print("Not able to add color entry.")
            else:
                landtype = LandtypeGetMenu()
                if landtype == 'abort':
                    print("Not able to add color entry.")
                else:
                    str1 = "DCI Land type chosen "
                    str1 += landtype
                    print(str1)                    
                    DCI_LTYPE[landtype].append(maxindex[0])
                    DCI[maxindex[0]] = colorval
                    str1 = "You've added a new key: "
                    str1 += str(maxindex[0]) + " and color "
                    str1 += colorname
                    print(str1)
                    DCI_NAMEIDS[maxindex[0]] = colorname
                    str1 = "DCI ID: "
                    str1 += str(maxindex[0])
                    str1 += " has been assigned with the name "
                    str1 += colorname
                    print(str1)
                    incrementMaxIndex()
        elif ans == "4":
            print(DCI)
            print(DCI_LTYPE)
            print(DCI_NAMEIDS)
        elif ans == "5":
            print("Leaving DCI Input menu.")
            a1 = False

def DeleteDCI(DCI=DCI, DCI_LTYPE=DCI_LTYPE, DCI_NAMEIDS=DCI_NAMEIDS):
    a1 = True
    while a1:
        if len(DCI) == 0:
            print("Nothing to delete in DCI since it is empty!")
            break
        ans = raw_input("Please enter the index value: ")
        try:
            ans = int(ans)
            if ans in DCI:
                str1 = "Deleting..."
                str1 += "index " + str(ans) + " color " + str(DCI[ans])
                print(str1)
                del DCI[ans]
                for lt in DCI_LTYPE:
                    if ans in DCI_LTYPE[lt]:
                        DCI_LTYPE[lt].remove(ans)
                del DCI_NAMEIDS[ans]
                a1 = False
            else:
                print("Invalid entry.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False

def DeleteDCIMenu(DCI=DCI):
    ans=True
    while ans:
        print ("""
        1.List DCI by Index
        2.Delete a DCI (by Index).
        3.Go back to previous Menu.
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1":
            for key in DCI:
                print("DCI Key:")
                print(key)
                print("DCI Value: ")
                print(DCI[key])
        elif ans =="2":
            DeleteDCI()
        elif ans =="3":
            ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")

        
def getDCIColor(DCI=DCI):
    print("DCI color change using existing Colors value.")
    print(DCI)
    ans = raw_input("Enter the DCI color index: ")
    try:
        ans = int(ans)
        if ans in DCI:
            ans2 = raw_input("Do you want to change the LandType entry(-ies)? [Y/N]")
            if ans2 == "Y" or ans2 == "y":
                addLandTypeEntries(ans)

            colorname = getColorNameMenu(DCI)
            if colorname != "":
                str1 = "For the existing DCI key: "
                str1 += ans + " you've changed the color from "
                str1 += DCI_NAMEIDS[ans] + " to " + colorname
                print(str1)
                DCI[ans] = Colors[colorname]
                DCI_NAMEIDS[ans] = colorname
                if not ChangeMore():
                    a1 = False
    except:
        print("Invalid entry")
        if DoYouWantToQuit():
            a1 = False

def getDCIColorRGBin(DCI=DCI):
    print("DCI color change using existing Colors value.")
    print(DCI)
    ans = raw_input("Enter the DCI color index: ")
    try:
        ans = int(ans)
        if ans in DCI:
            ans2 = raw_input("Do you want to change the LandType entry(-ies)? [Y/N]")
            if ans2 == "Y" or ans2 == "y":
                addLandTypeEntries(ans)

            print("A Color Name needs to be added for this entry.")
            colorname = NamegetMenu()
            print("A Color Value needs to be added for this entry.")
            colorval = getColorValue(DCI)
            if colorval[0] == None:
                print("Not able to add color entry.")
                if DoYouWantToQuit():
                    a1 = False
            else:
                str1 = "For the existing DCI key: "
                str1 += ans + " you've changed the color from "
                str1 += DCI_NAMEIDS[ans] + " to " + colorname
                print(str1)
                DCI[ans] = Colors[colorname]
                str1 = "You've changed the color value from "
                str1 = str(DCI[ans]) + " to " + str(colorval)
                print(str1)
                DCI_NAMEIDS[ans] = colorname
                DCI[ans] = colorval
                if not ChangeMore():
                    a1 = False
    except:
        print("Invalid entry")
        if DoYouWantToQuit():
            a1 = False

def DCIChangeMenu(DCI=DCI, Colors=Colors, maxindex = maxindex):
    a1 = True
    while a1:
        print ("""
        DCI Color Change Menu:
        1.Change existing color using Colors Dictionary
        2.Show colors from Colors Dictionary
        3.Change existing color inputting manually an RGB color value
        4.Show DCI data (in dictionary form)
        5.Abort/Done (go to previous DCI color menu)
        """)
        ans=raw_input("What would you like to do? ")
        if ans == "1":
            getDCIColor()
        elif ans == "2":
            print(Colors)
        elif ans == "3":
            getDCIColorRGBin()
        elif ans == "4":
            print(DCI)
            print(DCI_LTYPE)
            print(DCI_NAMEIDS)
        elif ans == "5":
            print("Leaving DCI Change menu.")
            a1 = False
        elif ans !="":
            print("\n Not Valid Choice Try again")

def DirectColorInputMenu(DCI = DCI):
    ans=True
    while ans:
        print ("""
        1.List DCI dictionary
        2.How many DCIs are there?
        3.Input a DCI
        4.Delete a DCI.
        5.Change a DCI.
        6.Go to Main Menu
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1":
            print(DCI)
        elif ans=="2":
            str1 = "There are "
            str1 += str(len(DCI))
            str1 += " colors in the DCI."
            print(str1)
        elif ans=="3":
            DCIInputMenu()
        elif ans=="4":
            DeleteDCIMenu()
        elif ans=="5":
            DCIChangeMenu()
        elif ans=="6":
            ans = False
        elif ans !="":
            print("\n Not Valid Choice Try again")

def MMTypeGetMenu():
    ans=True
    ttype = 'abort'
    while ans:
        print ("""
        Choose the following Mixing Module Type:
        1.Normal (Color Interpolation)
        2.Normal2 (Color Interpolation 2)
        3.Multiply
        4.Screen
        5.Overlay
        6.Hard light
        7.Soft light
        8.Vivid light
        9.Dodge
        10.Burn
        11.Difference
        12.Divide
        13.Darkenonly
        14.Lightenonly
        15.None (quit)
        """)    
        ans=raw_input("What Threshold Type? ") 
        if ans=="1": 
            ans = False
            ttype = 'normal'
        elif ans=="2":
            ans = False
            ttype = 'normal2'
        elif ans=="3":
            ans = False
            ttype = 'multiply'
        elif ans=="4":
            ans = False
            ttype = 'screen'
        elif ans=="5":
            ans = False
            ttype = 'overlay'
        elif ans=="6":
            ans = False
            ttype = 'hardlight'
        elif ans=="7":
            ans = False
            ttype = 'softlight'
        elif ans=="8":
            ans = False
            ttype = 'vividlight'
        elif ans=="9":
            ans = False
            ttype = 'dodge'
        elif ans=="10":
            ans = False
            ttype = 'burn'
        elif ans=="11":
            ans = False
            ttype = 'difference'
        elif ans=="12":
            ans = False
            ttype = 'divide'
        elif ans=="13":
            ans = False
            ttype = 'darkenonly'
        elif ans=="14":
            ans = False
            ttype = 'lightenonly'
        elif ans=="15":
            ans = False
            ttype = 'abort'
        elif ans !="":
            print("\n Not Valid Choice Try again")
    return ttype

def getMMInval(MM=MM, DCI=DCI, TM=TM):
    a1=True
    rval = None
    while a1:
        ans = raw_input("""
        MM In key?
        """)
        try:
            ans = int(ans)
            c1 = ans in MM
            c2 = ans in DCI
            tmidlist = []
            for tm in TM:
                tmidlist.append(tm['id'])
            c3 = ans in tmidlist
            c4 = ans == 0
            if c1 or c2 or c3 or c4:
                rval = ans
                a1 = False
            else:
                print("Unable to find a matching (existing) key.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid entry.  This must be a integer.")
            if DoYouWantToQuit():
                a1 = False
    return rval

def getMMInvals():
    ans = True
    rvals = (None,None)
    while ans:
        print("Enter first In key: ")
        r1 = getMMInval()
        if r1 != None:
            ans2 = True
            while ans2:
                r2 = getMMInval()
                if r2 != None:
                    str1 = "You entered (" + str(r1) +","+str(r2)+")"
                    str1 += "as In key values."
                    print(str1)
                    ans = raw_input("Is this correct? (Y/N)")
                    if ans == "Y" or ans == "y":
                        rvals = (r1,r2)
                        ans = False
                        break
                    else:
                        if DoYouWantToQuit():
                            ans = False
                            break
                        break
                else:
                    print("2nd Input key incorrectly.")
                    if DoYouWantToQuit():
                        ans = False
                        break
        else:
            print("First In key entered incorrectly.")
            if DoYouWantToQuit():
                break
    return rvals
        

def getMMInsMenu(MM=MM,DCI=DCI,TM=TM, DCI_NAMEIDS=DCI_NAMEIDS):
    ans=True
    rvals = (None,None)
    while ans:
        print("MM Ins input menu.")
        print("""
        1.List MM (Mixer Module) dictionary
        2.List DCI dictionary
        3.List TMs.
        4.Input Ins (by key).
        5.Tip on getting MM inputs setup properly.
        6.Go to Main Menu
        """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
              print(MM)
        elif ans == "2":
              print(DCI_NAMEIDS)
        elif ans == "3":
              print(TM)
        elif ans == "4":
              rvals = getMMInvals()
              ans = False
        elif ans == "5":
              str1 = "You should have generally have TMs and DCIs setup /n"
              str1 += "before inputting a new MM.  MMs are structured around /n"
              str1 += "colors having been provisioned either through  /n"
              str1 += "computation of a TM or through a DCI.  /n"
              str1 += "If a Color input key doesn't have a TM, DCI, or MM ID /n"
              str1 += " key associated, then  a key input will not work."
              print(str1)
        elif ans == "6":
              ans = False
    return rvals

def MMFactorVarGetMenu(ftype):
    ans=True
    ttype = None
    while ans:
        if ftype == 'variable':
            print ("""
            Choose the following MM FactorVar Type:
            1.Height
            2.Normal (gradient/slope)
            3.Height2 (Feathering on Land to other Landtype smoothing).
            4.None (quit)
            """)    
            ans=raw_input("What FactorVar Type? ") 
            if ans=="1": 
                ans = False
                ttype = 'height'
            elif ans=="2":
                ans = False
                ttype = 'normal'
            elif ans=="3":
                ttype = 'height2'
            elif ans=="4":
                ans = False
                ttype = 'abort'
            elif ans !="":
                print("\n Not Valid Choice Try again")
        elif ftype == 'falloff':
            print ("""
            Choose the following MM FactorVar Type:
            1.Height Threshold (Height falloff feather smoothing).
            2.Normal Threshold (Grad Slope falloff feather smoothing).
            3.None (quit)
            """)    
            ans=raw_input("What FactorVar Type? ") 
            if ans=="1": 
                ans = False
                ttype = 'heightT'
            elif ans=="2":
                ans = False
                ttype = 'normalT'
            elif ans=="3":
                ans = False
                ttype = 'abort'
            elif ans !="":
                print("\n Not Valid Choice Try again")

    return ttype

def MMgetFalloff(cflist=cflist):
    a1 = True
    rvals = (None,None)
    print("""
    Tip for setting falloff boundaries.  The cflist boundary key that you
    have chosen will set the threshold boundary distance measure from
    the lowest threshold boundary position for the first boundary key chosen,
    or the highest threshold boundary position for the second boundary measure.
    No falloff (feathering) for such boundary position can be set by choosing
    the value -1.0 .  Example:  You want to feather all positions on the
    lower boundary of the given MM threshold to positions that are at distance
    less than .1 from the threshold edge, but you don't want any feathering
    on the upper threshold boundary (remember: a threshold always has two edge
    boundary positions which is a lower and upper boundary).
    So the first value entered is .1 and the second is -1.
    """)
    while ans:
        print("Please enter a cubic function key value as shown or -1.0.")
        print(cflist)
        ans=raw_input("Enter first falloff boundary: ")
        try:
            ans = float(ans)
            if ans in cflist:
                a2 = True
                while a2:
                    print("Please enter a second boundary cubic function key or -1.0.")
                    print(cflist)
                    ans2 = raw_input("Enter the second falloff boundary: ")
                    try:
                        ans2 = float(ans)
                        if ans2 in cflist:
                            str1 = "You entered falloff boundaries of "
                            str1 += str(ans) + " and " + str(ans2)
                            print(str1)
                            ans3 = raw_input("Is this correct? (Y/N)")
                            if ans3 == "Y" or ans3 == "y":
                                rvals = (ans,ans2)
                            else:
                                if DoYouWantToQuit():
                                    a1 = False
                                    break
                        else:
                            print("Invalid entry.  Entry not found in cflist.")
                            if DoYouWantToQuit():
                                a1 = False
                                break
                    except:
                        print("Invalid entry.  This needs to be a float.")
                        if DoYouWantToQuit():
                            a1 = False
                            break
            else:
                print("Entered value is not in the cflist.")
                if DoYouWantToQuit():
                    a1 = False
                    break
        except:
            print("Invalid entry.  This needs to be a float.")
            if DoYouWantToQuit():
                ans = False
                break

def MMFactorTypeGetMenu():
    ans=True
    while ans:
        print ("""
        Choose the following MM FactorType:
        1.Fixed
        2.Variable
        3.Falloff.
        4.None (quit)
        """)    
        ans=raw_input("What FactorType? ") 
        if ans=="1": 
            ans = False
            ttype = 'fixed'
        elif ans=="2":
            ans = False
            ttype = 'variable'
        elif ans=="3":
            ans = False
            ttype = 'falloff'
        elif ans=="4":
            ans = False
            ttype = 'abort'
        elif ans !="":
            print("\n Not Valid Choice Try again")
    return ttype

def MMMainOutMenu():
    print("Main Out Menu")
    print("""
          This puts the MM color out to the main out of the CIOM.
          It is advised only doing this for the end of a given
          node chain or at the beginning of a node chain, but not
          going to the Main Out on intermediate Node chain Mixing Modules.
          """)
    ans = raw_input("MainOut?  [Y/N]")
    if ans == "Y" or ans == "y":
        return True
    else:
        return False

def MMInputMenu(MM = MM, maxindex = maxindex):
    a1 = True
    mmdat = {}
    rtmdat = {}
    while a1:
        mmindex = maxindex[0]
        name = NamegetMenu()
        mmdat['Name'] = name
        a2 = True
        while a2:
            landtype = LandtypeGetMenu()
            if landtype == 'abort':
                if AreYouSureQuit():
                    a2 = False
                    a1 = False
                    break
            else:
                mmdat['Landtype']=landtype
                a2 = False
                    
        if not a1:
            break
        a2 = True
        while a2:
            mtype = MMTypeGetMenu()
            if mtype == 'abort':
                if AreYouSureQuit():
                    a2 = False
                    a1 = False
                    break
            else:
                mmdat['Type'] = mtype
                a2 = False
                    
        if not a1:
            break
        a2 = False
        while a2:
            rvals = getMMInsMenu()
            if rvals[0] != None:
                  mmdat['Ins'] = rvals
            else:
              print("To quit MM input...")
              if DoYouWantToQuit():
                a1 = False
                break              
        if not a1:
            break
        a2 = False
        while a2:
            ftype = MMFactorTypeGetMenu()
            if ftype == 'abort':
                print("No valid FactorType inputed...")
                if DoYouWantToQuit():
                    a1 = False
                    break
            else:
                mmdat['FactorType'] = ftype
                a2 = False
        if not a1:
            break
        a2 = True
        if ftype != 'fixed':
            while a2:
                  fvtype = MMFactorVarGetMenu()
                  if fvtype == 'abort':
                      print("No Valid FactorVar type entered...")
                      if DoYouWantToQuit():
                        a1 = False
                        break
                  else:
                      mmdat['FactorVar'] = fvtype
                      a2 = False
        if not a1:
            break
        a2 = True
        if ftype == 'falloff':
            while a2:
                rfvals = MMgetFalloff()
                if rfvals[0] == None:
                    print("Needed falloff values have not been entered.")
                    if DoYouWantToQuit():
                        a1 = False
                        break
                else:
                    mmdat['Falloff'] = rfvals
                    break
        if not a1:
            break
        if ftype == 'fixed':
            while a2:
                bounds = (0.0,1.0,.5)
                tp = 'float'
                name = 'Factor'
                factorval = InputValue(bounds,tp, name)
                if factorval == None:
                    print("A needed factor value has not be entered.")
                    if DoYouWantToQuit():
                        a1 = False
                        break
                else:
                    mmdat['Factor'] = factorval
                    break
        
        if ftype == 'falloff':
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
                        mmdat['TBracket'] = [tbrackpos1,tbrackpos2]
                        a2 = False
        if not a1:
            break         
        mmdat["id"] = maxindex[0]
        mmdat['Outs'] = maxindex[0]
        if MMMainOutMenu():
            mmdat['MainOut'] = True
        else:
            mmdat['MainOut'] = False
        print("""You entered """, mmdat)
        ans = raw_input("Is this correct? (Y/N)")
        if ans == "Y" or ans == "y":
            MM[maxindex[0]] = mmdat.copy()
            incrementMaxIndex()
            a1 = False
            print("Successfully added MM module...")

def MMDeleteMenu(MM=MM):
    ans = True
    while ans:
        print("""
        Enter the MM key to delete.
        """)
        ans = raw_input("Which key to delete? ")
        try:
            ans = int(ans)
            if ans in MM:
                str1 = "Deleting " + str(MM[ans])
                print(str1)
                yans = raw_input("Is this correct? (Y/N)")
                if yans == "Y" or yans == "y":
                    del MM[ans]
                    break
                else:
                    if DoYouWantToQuit():
                        break
            else:
                print("Key not found in MM dictionary.")
                if DoYouWantToQuit():
                    break
        except:
            print("Invalid entry.  Needs to be an integer")
            if DoYouWantToQuit():
                break

def MMChangeMenuKey(mmdat):
    a1 = True
    while a1:
        print(mmdat)
        ans = raw_input("Please enter the TM key: ")
        print(ans)
        ans = ans.strip()
        if ans in MM:
            if ans == 'LandType':
                landtype = LandtypeGetMenu()
                if landtype == 'abort':
                    if AreYouSureQuit():
                        a1 = False
                else:
                    str1 = "Changed LandType from "
                    str1 += mmdat['LandType']
                    str1 += " to "
                    str1 += landtype
                    print(str1)                    
                    mmdat['Landtype']=landtype
                    if not ChangeMore():
                        a1 = False
                    
            elif ans == 'Name':
                name = NamegetMenu()
                str1 = "Changed Name from "
                str1 += mmdat['Name']
                str1 += " to "
                str1 += name
                print(str1)
                mmdat['Name'] = name
                if not ChangeMore():
                    a1 = False
            elif ans == 'Type':
                ttype = MMTypeGetMenu()
                if ttype == 'abort':
                    if AreYouSureQuit():
                        a1 = False
                else:
                    str1 = "Changed Type from"
                    str1 += mmdat['Type']
                    str1 += " to "
                    str1 += ttype
                    print(str1)                    
                    mmdat['Type'] = ttype
##                    tmdat['ThreshType'] = ttype
                    if not ChangeMore():
                        a1 = False

            elif ans == 'FactorType':
                if ftype == 'abort':
                    print("No valid FactorType inputed...")
                    if DoYouWantToQuit():
                        a1 = False
                        break
                else:
                    mmdat['FactorType'] = ftype
                    if ftype == 'fixed':
                        a2 = True
                        while a2:
                            bounds = (0.0,1.0,.5)
                            tp = 'float'
                            name = 'Factor'
                            factorval = InputValue(bounds,tp, name)
                            if factorval == None:
                                print("A needed factor value has not be entered.")
                                if DoYouWantToQuit():
                                    a1 = False
                                    break
                            else:
                                mmdat['Factor'] = factorval
                                break
                    elif ftype == 'falloff':
                        a2 = True
                        while a2:
                            rfvals = MMgetFalloff()
                            if rfvals[0] == None:
                                print("Needed falloff values have not been entered.")
                                if DoYouWantToQuit():
                                    a1 = False
                                    break
                            else:
                                mmdat['Falloff'] = rfvals
                                break
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
                                    mmdat['TBracket'] = [tbrackpos1,tbrackpos2]
                                    a2 = False
                            
                    if ftype != 'fixed':
                        a2 = True
                        while a2:
                              fvtype = MMFactorVarGetMenu()
                              if fvtype == 'abort':
                                  print("No Valid FactorVar type entered...")
                                  if DoYouWantToQuit():
                                    a1 = False
                                    break
                              else:
                                  mmdat['FactorVar'] = fvtype
                                  break
                    if not ChangeMore():
                        a1 = False                

            elif ans == 'TBracket':
                getTBMenu(mmdat)
                if not ChangeMore():
                    a1 = False

        else:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False    

def MMChangeMenuIndex(MM=MM):
    a1 = True
    while a1:
        if len(MM) == 0:
            print("Nothing to change in MM since it is empty!")
            a1 = False
            break
        ans = raw_input("Please enter the index value: ")
        try:
            ans = int(ans)
            if ans in MM:
                print("Loading MM change menu for...", MM[ans])
                mmdict = MM[ans]
                MMChangeMenuKey(mmdict)
                MM[ans] = mmdict
                a1 = False
            else:
                print("Invalid entry.")
                if DoYouWantToQuit():
                    a1 = False
        except:
            print("Invalid entry.")
            if DoYouWantToQuit():
                a1 = False

def MMChangeMenu(MM=MM):
    ans=True
    while ans:
        print ("""
        1.List Mixing Modules by Index
        2.Change a MM (by index).
        3.Go back to previous Menu.
        """)
        ans=raw_input("What would you like to do? ") 
        if ans == "1":
            for i,t in enumerate(MM):
                print("Index:")
                print(i)
                print("MM: ")
                print(t)
        elif ans == "2":
            MMChangeMenuIndex()
        elif ans == "3":
            ans = False
        elif ans !="":
          print("\n Not Valid Choice Try again")  

def MixerModuleMenu(MM = MM):
    ans=True
    while ans:
        print ("""
        1.List MM (Mixer Module) dictionary
        2.How many MMs are there?
        3.Input a MM (Mixer Module).
        4.Delete a MM.
        5.Change a MM.
        6.Go to Main Menu
        """)
        ans=raw_input("What would you like to do? ")
        if ans == "1":
            print(MM)
        elif ans == "2":
            print(len(MM))
        elif ans == "3":
            MMInputMenu()
        elif ans == "4":
            MMDeleteMenu()
        elif ans == "5":
            MMChangeMenu()
        elif ans == "6":
            ans = False
        elif ans !="":
            print("\n Not Valid Choice Try again")

##Colors = {}
##TM = []
##DCI = {}
##DCI_LTYPE = {'Flood':[], 'Land':[], 'Mount':[]}
##DCI_NAMEIDS = {}
##MM = {}
##NCs = {}
##maxindex = [1]
##cflist = [.05,.1,.2,.3,.4,.5,.6,.7,1.0,-1.0]
##flood = .1
##mount = .9
def SaveData(CTDAT=CTDAT,TM=TM,DCI=DCI,MM=MM,
             NCs=NCs,maxindex=maxindex,flood=flood,
             mount=mount,Colors=Colors,DCI_LTYPE=DCI_LTYPE,
             DCI_NAMEIDS=DCI_NAMEIDS):
    dat = {'TM':TM, 'DCI':DCI, 'MM':MM,'NCs':NCs, 'maxindex':maxindex,
           'flood':flood,'mount':mount, 'Colors':Colors,
           'DCI_LTYPE':DCI_LTYPE, 'DCI_NAMEIDS':DCI_NAMEIDS}
    ans = True
    while ans:
        ans = raw_input("Please enter the name of the data: ")
        if len(ans) == 0:
            print("A name is needed.")
            if DoYouWantToQuit():
                ans = False
        else:
            CTDAT[str(ans)] = dat
            str1 = "Successfully saved data to "
            str1 += str(ans) + "."
            print(str1)
            ans = False

def LoadData(CTDAT=CTDAT,TM=TM,DCI=DCI,MM=MM,
             NCs=NCs,maxindex=maxindex,fm=(flood,mount),
             Colors=Colors,DCI_LTYPE=DCI_LTYPE,
             DCI_NAMEIDS=DCI_NAMEIDS):
##    dat = {'TM':TM, 'DCI':DCI, 'MM':MM,'NCs':NCs, 'maxindex':maxindex,
##           'flood':flood,'mount':mount, 'Colors':Colors,
##           'DCI_LTYPE':DCI_LTYPE, 'DCI_NAMEIDS':DCI_NAMEIDS}
    ans = True
    while ans:
        print("Load Data Menu")
        ans = raw_input("Please enter the name of the data: ")
        if len(ans) == 0:
            print("A name is needed.")
            if DoYouWantToQuit():
                ans = False
        else:
            if str(ans) in CTDAT:
                dat = CTDAT[str(ans)]
                TM = dat['TM']
                DCI = dat['DCI']
                MM = dat['MM']
                NCs = dat['NCs']
                maxindex = dat['maxindex']
                fm[0] = dat['flood']
                fm[1] = dat['mount']
                Colors = dat['Colors']
                DCI_LTYPE = dat['DCI_LTYPE']
                DCI_NAMEIDS = dat['DCI_NAMEIDS']
                str1 = "Successfully loaded data from "
                str1 += str(ans) + "."
                print(str1)
                ans = False
            else:
                print("Data name not found.")
                if DoYouWantToQuit():
                    ans = False

def DeleteData(CTDAT=CTDAT):
    ans = True
    while ans:
        print("Delete Data Menu")
        ans = raw_input("Please enter the name of the data you want to delete: ")
        if str(ans) in CTDAT:
            str1 = "You entered " + str(ans)
            print(str1)
            ans2 = raw_input("Are you sure you want to delete this? [Y/N]")
            if ans2 == "Y" or ans2 == "y":
                del CTDAT[str(ans)]
                str1 = "Sucessefully deleted " + str(ans)
                print(str1)
                ans = False
            else:
                print("Aborted deleting data.")
                if DoYouWantToQuit():
                    ans = False
        else:
            print("Name not found in database.")
            if DoYouWantToQuit():
                ans = False

def LoadSaveDelData(CTDAT=CTDAT):
    ans=True
    while ans:
        print("Load/Save/Delete Menu")
        print("""
        1.List of Data names.
        2.Save Data
        3.Load Data
        4.Delete Data
        5.Back to Main Menu
        """)
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print(list(CTDAT.keys()))
        elif ans == "2":
            SaveData()
        elif ans == "3":
            LoadData()
        elif ans == "4":
            DeleteData()
        elif ans == "5":
            ans = False
        elif ans !="":
            print("\n Not Valid Choice Try again")

def LoadStarterTemplate(TM=TM,DCI=DCI,MM=MM,
                        NCs=NCs,maxindex=maxindex,
                        Colors=Colors,DCI_LTYPE=DCI_LTYPE,
                        DCI_NAMEIDS=DCI_NAMEIDS,Colors_s1=Colors_s1,
                        TM_s1=TM_s1,MM_s1=MM_s1,NCs_s1=NCs_s1,
                        maxindex_s1=maxindex_s1):
    for tm in TM_s1:
        TM.append(tm)
##    TM = TM_s1[0:len(TM_s1)]
    for mm in MM_s1:
        MM[mm] = MM_s1[mm]
##    MM = MM_s1.copy()
    for col in Colors_s1:
        Colors[col] = Colors_s1[col]
##    Colors = Colors_s1.copy()
    for ncs in NCs_s1:
        NCs[ncs] = NCs_s1[ncs]
##    NCs = NCs_s1.copy()
    for mi in maxindex_s1:
        maxindex[0] = mi
##    maxindex = maxindex_s1[0:len(maxindex_s1)]
##    print(TM)
##    print(MM)
##    print(Colors)
##    print(NCs)
##    print(maxindex)
    print("Finished loading Starter template")

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
        7.Tip for setting up Terrain Colorization
        8.Load/Save/Delete Data to Database
        9.Load Starter Template Colorization
        10.Exit/Quit
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
            DirectColorInputMenu()
        elif ans=="4":
            MixerModuleMenu()
        elif ans=="5":
            print("not there yet.")
        elif ans=="7":
            print("""
            The CIOM (Color Input Output Module) is responsible for a terrain
            pixels determined output 8 bit per channel RGB assignment.
            In a given interface, Node Chains are usually established primarily
            by Colors either having been set by Threshold Modules or
            directly inputted into the CIOM via DCI s.  Thus when working with
            Mixer Modules, it is likely the most sensisble to have TMs
            or DCIs firstly established before moving onto structuring
            Mixer Modules, and/or working with Node Chains themselves.
            A Node Chain menu wizard aids in auto detecting TMs and/or
            DCIs in structuring the basis of any Node Chains, though
            the development of these chains will be specified via the user
            given likely chains of Mixer Modules as desired.
            What differentiates a Mixer Module from a Threshold Module (TM)?
            A Threshold Module is a standalone non CIOM input color mixing
            system that provides a Color RGB output.
            TMs are like MMs in that users
            specify color inputs that will form the basis of any mixing
            of such color (whether given from fractal noising or any
            height or normal map threshold basis...that is with specified
            height ranges to color pixels or given by normal colorization values
            and so forth.  Colors assigned in the TM are not done via DCIs or
            through the CIOM but instead provided natively in the definition of
            the TM.  On the other hand, Mixer modules rely on
            Color inputs being provided through CIOM valid id channels.
            This is 'id' on the TM or the key value provided from the DCI,
            but otherwise, Mixer modules do not have any color specified input
            systems (native to the MM)
            and thus are always reliant upon some channel id specified
            input.  TMs and DCIs serve as the root of any node chain system.
            While MMs are secondary in the node chaining process.
            MMs can specify other MMs channel outs as inputs, but also
            TM ids or DCI ids, but themselves again are not standalones in
            in start of a node chain system since they cannot produce color
            firstly without input color from the CIOM.  Again TMs and DCIs
            can do this.
               Node Chains serve from TMs or DCIs firstly and then
            likely move to a sequence of chained MMs which culminate in a
            final MM output.  This chain output is likely read as the last
            injected MainOut written color value in the CIOM.
            Node chains can verify upon conditions specified through the
            basis of TMs set for any relevant heightmap position.
            Thus, if for instance, a land type pixel qualifies for
            normal Threshold Module, and also qualifies for inter land type
            feather mixing all relevant node chains set for these independent
            TMs will apply in the formation of such pixels color value
            in computing its mixing.  Another good way of thinking of TMs
            is that aside from mixing, they serve as the basis of testing
            conditions to see that a heightmap position qualifies for
            'feathering' or qualifies for normal 'rock' color texturing even
            before computing its given color value for all these specifications
            and then mixing them together to form a color output.
               In setting up a Mixer Module, valid inputs will be cross
            checked before an input Mixer Module is added.  Thus it is highly
            recommended sequentially setting up a pre sketched out design layout
            in order from one MM chained to the next MM.  Though a user
            can rearrange these MM channels later as desired in changing their
            input channels as necessary.
            Thus order of operations are likely as follows:
            1.  Establish a Colors dictionary.  This includes a likely
            range of mixing colors to be used.
            2.  Setup desired Threshold Modules for all landtypes.
            3.  Setup DCIs (if any) where Thresholding is only reserved
            to a given Landtype (i.e, you don't want to set up a TM to
            apply color mixing).
            4.  Setup MMs from TMs and DCIs, and then setup additional
            MMs from these MMs repeating iteratively this procedure
            going from one MM to the next until completing a desired chain.
            5. Run the Node Chain wizard in setting up the chains...this
            should be straightfoward since the brunt of work has already
            been done.  
            """)
        elif ans=="8":
            LoadSaveDelData()
        elif ans=="9":
            LoadStarterTemplate()
        elif ans=="10":
            print("\n Goodbye")
            ans = False
        elif ans !="":
            print("\n Not Valid Choice Try again")

print('Welcome to the Terrain colorization assistant!')
print("Let's go ahead and add some terrain colors!")
MainMenu()
CTDAT.close()
