class prm_tech:
# --------------------- Constructor -----------------------------------------------------------------------------------
    def __init__(self, P=None, E=None, avail=None, Emax=1, Emin=0, rup=1, rdo=1):
        self._P = P if P is not None else 0                     # Capacity installed [MW]  
        self._E = E if E is not None else [0] * 8760             # Energy produced for each 8760 time steps in a year
        self._avail = avail if avail is not None else [0] * 8760 # Availabilité of techno for each 8760 time steps in a year
                                                                 # 0 means all units are off
                                                                 # 1 means all units are full operationnal
        self._Emax = Emax # Maximum of energy/power on 1 hour
        self._Emin = Emin # Minimum of energy/power on 1 hour
        self._rup  = rup  # Ramping up dynamic [0,1]
                          # 0 means not flexible up
                          # 1 means 100%Pn/h
        self._rdo  = rdo # Ramping down dynamic [0,1]
                          # 0 means not flexible down
                          # 1 means 100%Pn/h

        # Check if _P is null or a positive number
        if not self.is_valid_P():
            raise ValueError("_P should be null or a positive number (int or float)")
        # Check if E is a list of 8760 floats
        if not self.is_valid_E():
            raise ValueError("[ERROR] E should be a list of 8760 positive or null numbers...")
# --------------------- End Of Constructor ----------------------------------------------------------------------------

    # Check if arguments are valid
    def is_valid_E(self):
        return isinstance(self._E, list) and len(self._E) == 8760 and all(x >= 0 for x in self._E) and all(isinstance(x, (int, float)) for x in self._E)

    def is_valid_P(self):
        return self._P is None or (isinstance(self._P, (int, float)) and self._P >= 0)

    def is_valid_avail(self):
        return isinstance(self._avail, list) and len(self._avail) == 8760 and all(x >= 0 for x in self._avail) and all(x <= 1 for x in self._avail)

# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_P(self):
        return self._P
    def get_E(self):
        return self._E
    def get_avail(self):
        return self._avail
    def get_Emax(self):
        return self._Emax
    def get_Emin(self):
        return self._Emin
    def get_rup(self):
        return self._rup
    def get_rdo(self):
        return self._rdo
    
    # Set methods
    def set_P(self, P):
        self._P = P
    def set_E(self, E):
        self._E = E
    def set_avail(self, avail):
        self._avail = avail
    def set_Emax(self, Emax):
        self._Emax = Emax
    def set_Emin(self, Emin):
        self._Emin = Emin
    def set_rup(self, rup):
        self._rup = rup
    def set_rdo(self, rdo):
        self._rdo = rdo

# --------------------- PRINT methods ---------------------------------------------------------------------------------

    def Print(self):
        print()
        print('--------------------------------------------')
        print('--- Technical parameters -------------------')
        print('--------------------------------------------')
        print(f" -> Installed Capacity : {self._P} MW")
        print('--------------------------------------------')
        print(f" -> Energy Production [MWh] :")
        print(np.array(self._E))
        print('--------------------------------------------')
        print()
