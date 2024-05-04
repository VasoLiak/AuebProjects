#θεματα παρακατω ασκησεων: 1)onoma mias topo8esias, Gewgrafiko mikos, Gewgrafiko platos, Eidos topo8esias
#                          2)Apostasi meta3y topo88esiwn, stoixeia topo8esias, plisiesteri topo8esia
#                          3)Emfanizei string pou briskontai se fwliasmenes listes
#                          4)Emfanizei string pou briskontai se fwliasmenes listes
#                          5)Emfanizei string pou briskontai se fwliasmenes listes
#                          6)Epistrefei lista afairwntas fwliasmenes listes
#                          7)String me ola ta string pou periexoun 'cherry' sti field
#                          8)Epistrefei stoixeia topo8etwntas ta se fwliasmenes listes

#--------------------- Askisi 1 -----------------------

def location(name, lat, lon, type):
    """Kataskeuazei syn8eto dedomeno topo8esias (location).

    name -- onoma (str)
    lat -- gewfrafiko platos (se moires)
    lon -- gewgrafiko mikos (se moires)
    type -- eidos topo8esias (str)

    Epistrefei dedomeno pou anaparista tin topo8esia me onoma name h opoia
    brisketai sto gewgrafiko platos kai mikos lat kai lon antistoixa. To type
    einai string pou perigrafei to eidos tis topo8esias, p.x., 'monument',
    'bus station'.
    """
    return [name, lat, lon, type]


def name(loc):
    """Epistrefei to onoma mias topo8esias.

    loc -- topo8esia (typou location)

    Epistrefei to onoma (str) tis topo8esias loc.

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> name(monast)
    'Monastiraki'
    """
    return loc[0]

def longitude(loc):
    """Gewgrafiko mikos.

    loc -- dedomeno location

    Epistrefei gewgrafiko mikos tis topo8esias loc

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> longitude(monast)
    23.725947
    """
    return loc[2]
	
def lattitude(loc):
    """Gewgrafiko platos.

    loc -- dedomeno location

    Epistrefei gewgrafiko mikos tis topo8esias loc

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> lattitude(monast)
    37.976362
    """
    return loc[1]

def type(loc):
    """Eidos topo8esias.

    loc -- dedomeno location

    Epistrefei string pou perigrafei to eidos tis topo8esias loc, p.x.,
    'monument', 'bus station'.

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> type(monast)
    'square'
    """
    return loc[3]



#--------------------- Askisi 2 -----------------------

def distance(a, b):
    """Apostasi meta3y topo88esiwn.

    a -- topo8esia A (dedomeno typou location)
    b -- topo8esia B (dedomeno typou location)

    Epistrefei tin apostasi (Manhattan distance) 
    meta3y ths topo8esias A kai B se xiliometra.

    >>> aueb = location('AUEB', 37.994097, 23.732253, 'university campus')
    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> distance(aueb, monast)
    2.5224714882938657
    >>> distance(aueb, aueb)
    0.0
    """
    """ALLA3TE TON KWDIKA."""
    
    from math import pi, cos
    phi_m = pi/180 * (lattitude(a) + lattitude(b)) / 2
    k1 = 111.13209 - 0.56605 * cos(2*phi_m) + 0.00120 * cos(4*phi_m)
    k2 = 111.41513 * cos(phi_m) - 0.0945 * cos(3*phi_m) \
        + 0.00012*cos(5*phi_m)
    lat_dist = (lattitude(a) - lattitude(b)) * k1
    lon_dist = (longitude(a) - longitude(b)) * k2
    return abs(lon_dist) + abs(lat_dist)


def print_location(loc):
    """Emfanizei stoixeia topo8esias.

    loc -- dedomeno location

    Emfanizei stoixeia gia tin topo8esia loc opws sta paradeigmata:

    >>> monast = location('Monastiraki', 37.976362, 23.725947, 'square')
    >>> print_location(monast)
    Monastiraki (square) at coordinates 37.976362, 23.725947
    >>> print_location(location('North Pole', 90.0, 135.0, 'pole'))
    North Pole (pole) at coordinates 90.0, 135.0
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    print (name(loc), "(" + type(loc) + ")", "at coordinates" ,lattitude(loc) ,end=", ")
    print (longitude(loc))

def nearest_location(loc, loc_list, loc_type=None):
    """Epistrefei plisiesteri topo8esia.

    loc -- topo8esia (dedomeno typoy location)
    loc_list -- lista pou periexei topo8esies (dedomena location)
    loc_type -- eidos topo8esias (str)

    Epistrefei tin plisiesteri topo8esia stin loc apo autes pou briskonai sti
    lista loc_list tou eidous loc_type.

    Paradeigmata:
    >>> llist = [location('AUEB', 37.994097, 23.732253, 'university campus'),\
                  location('Acropolis', 37.971584, 23.725912, 'monument'), \
                  location('Syntagma', 37.975560, 23.734691, 'square'), \
                  location('National Garden', 37.973116, 23.736483, 'park'), \
                  location('Monastiraki', 37.976362, 23.725947, 'square')]
    >>> name(nearest_location(llist[2], llist, 'monument'))
    'Acropolis'
    >>> name(nearest_location(llist[1], llist, 'square'))
    'Monastiraki'
    >>> name(nearest_location(llist[2], llist))
    'National Garden'
    >>> name(nearest_location(llist[2], llist, 'square'))
    'Monastiraki'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    i=0
    if loc_type!= None:
        while i<=len(loc_list)-1:
            dis=distance(loc, loc_list[i])
            if loc_type== type(loc_list[i]):
                if loc_list[i] != loc:
                    y=dis
                    x=i
                elif loc_list[i] != loc and dis<y:
                    y=dis
                    x=1
            i= i+1
    else:
        while i<=len(loc_list)-1:
            dis=distance(loc,loc_list[i])
            if i== 0 and loc_list[i]!= loc:
                y=dis
                x=i
            elif loc_list[i]!= loc and dis<y:
                y=dis
                x=i
            i=i+1
    return loc_list[x]


#--------------------- Askisi 3 -----------------------

def pick_cherries_only():
    """Emfanizei string pou briskontai se fwliasmenes listes.

    Prepei na exei to akolou8o apotelesma:

    >>> pick_cherries_only()
    cherry1
    cherry2
    cherry3
    cherry4
    Yay!!!
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    fruits = ['cherry1', 'orange', \
              ['grape', 'cherry2', ['cherry3'], 'banana'], \
              None, 'cherry4', [[['Yay!!!']]]]

    print(fruits[0])
    print(fruits[2][1])
    print(fruits[2][2][0])
    print(fruits[4])
    print(fruits[5][0][0][0])
        

#--------------------- Askisi 4 -----------------------

def pick_cherries_onebyone():
    """Emfanizei string pou briskontai se fwliasmenes listes.

    Prepei na exei to akolou8o apotelesma:

    >>> pick_cherries_onebyone()
    cherry1
    cherry2
    cherry3
    cherry4
    last cherry
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]

    print(cherry_field[0])
    cherry_field[0]='cherry2' 
    print(cherry_field[0])
    cherry_field[0]='cherry3' 
    print(cherry_field[0])
    cherry_field[0]='cherry4'
    print(cherry_field[0])
    cherry_field[0]='last cherry' 
    print(cherry_field[0]) 


#--------------------- Askisi 5 -----------------------

def pick_cherries(field):
    """Emfanizei string pou briskontai se fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. (Opws kai h cherry_field sto swma ths synarthshs 
    pick_cherries_onebyone()).

    Leitoyrgei opws i pick_cherries_onebyone, omws gia au8aireta polles
    fwliasmenes listes stin field.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> pick_cherries(cherry_field)
    cherry1
    cherry2
    cherry3
    cherry4
    last cherry
    >>> pick_cherries(['Hello', ['world', None]])
    Hello
    world
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    ls = field
    if ls != None:
        print(ls[0])
    else:
        return
    
    while ls[1] != None:
        ls = ls[1]
        print(ls[0]) 

#--------------------- Askisi 6 -----------------------

def flatten(field):
    """Epistrefei lista afairwntas fwliasmenes listes.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. (Opws kai h cherry_field sto swma ths synarthshs 
    pick_cherries_onebyone()).

    Epistrefei nea lista pou periexei ola ta string pou briskontai sti
    field, xwris omws na periexontai se fwliasmenes listes.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> flatten(cherry_field)
    ['cherry1', 'cherry2', 'cherry3', 'cherry4', 'last cherry']
    >>> flatten(['Hello', ['world', None]])
    ['Hello', 'world']
    >>> flatten(['Lone cherry', None])
    ['Lone cherry']
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    ls = field
    if ls[1] is None:
        return [ls[0]]
    n_ls = [ls[0]]
    return n_ls + flatten(ls[1]) 

#--------------------- Askisi 7 -----------------------

def cherry_string(field):
    """String me ola ta string pou periexoun 'cherry' sti field.

    field -- lista me fwliasmena string. Ka8e lista exei dyo stoixeia: 
    to prwto einai string kai to deutero einai eite lista ths idias 
    morfhs 'h None. 
    (Opws kai h cherry_field sto swma ths synarthshs pick_cherries_onebyone()).

    Epistrefei string pou exei proel8ei apo synenwsh olwn twn string
    pou periexontai sti field kai periexoun th le3h 'cherry'.

    Paradeigmata:

    >>> cherry_field = ['cherry1', ['cherry2', ['cherry3', ['cherry4', ['last cherry', None]]]]]
    >>> cherry_string(cherry_field)
    'cherry1cherry2cherry3cherry4last cherry'
    >>> cherry_string(['Hello', ['cherry', None]])
    'cherry'
    >>> cherry_string(['Hello', ['first cherry', ['world', ['last cherry', None]]]])
    'first cherrylast cherry'
    """
    """ SYMPLHRWSTE TA KENA APO KATW."""
    from functools import reduce
    from operator import add
    return reduce(add,(flatten(field)[i] for i in range(len(flatten(field))) if 'cherry' in flatten(field)[i]))

#--------------------- Askisi 8 -----------------------

def unflatten(ls):
    """Epistrefei stoixeia topo8etwntas ta se fwliasmenes listes.

    ls -- lista pou ta stoixeia tis einai string.

    Epistrefei lista me fwliasmena string, opws to orisma ths synarthshs 
    cherry string. Mia tetoia lista exei dyo stoixeia: to prwto einai
    string kai to deutero einai eite lista ths idias morfhs 'h None.

    Paradeigmata:

    >>> unflatten(['Hello', 'world'])
    ['Hello', ['world', None]]
    >>> unflatten(['Hello'])
    ['Hello', None]
    >>> unflatten(['No', 'more', 'cherries', 'please!'])
    ['No', ['more', ['cherries', ['please!', None]]]]
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""
    unflatten_list = None
    for i in reversed(ls):
        unflatten_list = [i, unflatten_list]
    return unflatten_list 
