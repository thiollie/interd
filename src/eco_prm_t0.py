# Technico-economic data for simulation @T0 

#######################################
# Economic data
#######################################

cost = {}
cost[start_year] = {}

# Overnight Cost [€/MW]
# Sources : 
#
#
cost[start_year]['occ'] = {}
cost[start_year]['occ']['nuclear'] = {'hist':0,     'refu':0.5e6, 'new' :5e6}
cost[start_year]['occ']['thermal'] = {'coal':2.5e6, 'ccgt':2e6,   'ocgt':1e6}
cost[start_year]['occ']['vre']     = {'wos' :2.5e6, 'wof' :2e6,   'pv'  :1e6}
cost[start_year]['occ']['hydro']   = {'ror' :2.5e6, 'lake':2e6,   'psh' :1e6}
# Interest During Construction [€/MW]
# Sources : 
#
#
# Total Construction Cost [€/MW]
# Sources : 
#
#











#######################################
# Technic data
#######################################

# efficiency thermal -> elec















# Data
data[sf_first_year] = {}

# Overnight Cost [€/MW]
data[sf_first_year]['cost occ'] = {'nuclear his':0, 'nuclear ref':0.5e6, 'nuclear new':5e6, 'coal':2.5e6, 'gt':1e6}
# Lifetime [years]
data[sf_first_year]['lifetime'] = {'nuclear new':60,  'coal':30,    'gt':30}

data[sf_first_year]['cost fix_cap'] = {}

data['cost fix_cap'][m] = data['cost occ'][m] * ( (r*(1+r)**data['lifetime'][m]) / ((1+r)**data['lifetime'][m] -1) )



     
data['cost fix_om']   = {'nuclear':7e4 , 'coal':2.0e4, 'gt':1.5e4}
data['cost var_om']   = {'nuclear':1.2 , 'coal':3.0,   'gt':0.4}
data['cost var_fuel'] = {'nuclear':6,    'coal':40,    'gt':100}

# Post Treatment
data['cost var'] = {}
data['cost fix'] = {}
for m in set_machines:
    data['cost fix'][m] = data['cost fix_om'][m] + data['cost fix_cap'][m] 
    data['cost var'][m] = data['cost var_om'][m] + data['cost var_fuel'][m] 

data['cost tot_U'] = {}
data['cost tot'] = {}
U = np.arange(1, 8761, 1)
for m in set_machines:
    data['cost tot_U'][m] = data['cost fix_cap'][m] + data['cost fix_om'][m] + (data['cost var_om'][m] + data['cost var_fuel'][m]) * U
    data['cost tot'][m]   = data['cost tot_U'][m] / U




#TO CHANGE
# cost_occ 'nuclear ref':5e6