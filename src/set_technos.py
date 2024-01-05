# Set of available technologies in simulation

set_techno = {}

##########################################################
# Nuclear
##########################################################
set_techno['nuclear'] = []
set_techno['nuclear'].append('hist') # historic nuclear
set_techno['nuclear'].append('refu') # refurbishment nuclear
set_techno['nuclear'].append('new') # new nuclear

##########################################################
# Thermal
##########################################################
set_techno['thermal'] = []
set_techno['thermal'].append('coal')
set_techno['thermal'].append('ccgt') # combined cycle gas turbine (CCGT)
set_techno['thermal'].append('ocgt') # open cycle gas turbine (OCGT)

##########################################################
# Variable Renewable Energy
##########################################################
set_techno['vre'] = []
set_techno['vre'].append('wos')
set_techno['vre'].append('wof')
set_techno['vre'].append('pv')

##########################################################
# Hydro
##########################################################
set_techno['hydro'] = []
set_techno['hydro'].append('ror')
set_techno['hydro'].append('lake')
set_techno['hydro'].append('psh')

##########################################################
# Print
##########################################################

print()

print('----------------------------------------------')
print('--- access : set_techno[\'label\']')
print('----------------------------------------------\n')

for label, data in set_techno.items():

    print('***********')
    print(label)
    print('***********n')
    print(data)
    print()
    

print('----------------------------------------------')
print()