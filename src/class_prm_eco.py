class prm_eco:
# --------------------- Constructor ----------------------------------------------------------------------------------    
    def __init__(self, r, ct, dt, occ, fix_om, var_om, var_f, var_co2):
        self._r   = r    # Discount rate
        self._ct  = ct   # Construction Time [y]
        self._dt  = dt   # Depreciation Time [y]
        self._occ = occ  # Overnight Construction Cost [€/MW]
        self._fix_om  = fix_om   # Fix OM cost [€/MW]
        self._var_om  = var_om   # var OM cost [€/MWh ouput]
        self._var_f   = var_f    # var fuel cost [€/MWh input]
        self._var_co2 = var_co2  # var carbon cost [€/MWh i]
        self._tic  = self.calculate_tic()  # Total Investment Costs [€/MW]
        self._idc  = self.calculate_idc()  # Interest During Construction [€/MW]
        self._acap = self.calculate_acap() # Annual CAPEX [€/MW/y]
# --------------------- End Of Constructor ---------------------------------------------------------------------------    

    # Calculate Total Investment Cost
    def calculate_tic(self):
        # Source : Haeseleer (2013) p39 (!! bracket error => IDC = TIC - OCC !!)
        # And Considering uniform construction cost profile to simplify...
        return self._occ / self._ct * ( (1 + self._r) / self._r ) * ( (1 + self._r)**self._ct - 1)
    
    # Calculate Interest During Construction Costs
    def calculate_idc(self):
        return self._tic - self._occ

    # Calculate Annual CAPEX cost
    def calculate_acap(self):
        # Source : Footnote Hansen & Percebois - Energie pXX
        return self._tic * ( (self._r*(1+self._r)**self._dt) / ((1+self._r)**self._dt - 1) ) 

# --------------------- GET/SET methods -------------------------------------------------------------------------------

    # Get methods
    def get_r(self):
        return self._r
    
    # Set methods
    def set_r(self, r):
        self._r = r
        # Recalculate IDC after updating cash_flows
        self._tic  = self.calculate_tic()
        self._idc  = self.calculate_idc()
        self._acap = self.calculate_acap()

# --------------------- PRINT methods ---------------------------------------------------------------------------------

    def Print(self):
        print()
        print('--------------------------------------------')
        print('--- Eco parameters -------------------------')
        print('--------------------------------------------')
        print(f"discount rate : {self._r}")
        print('--------------------------------------------')
        print(f"construction time : {self._ct} y")
        print(f"depreciation time : {self._dt} y ")
        print('--------------------------------------------')
        print(f"Overnight Construction Cost :  {self._occ} €/MW")
        print(f" -> Interest During Construction : {self._idc} €/MW")
        print(f" -> Total Investment Costs :       {self._tic} €/MW")
        print(f" -> Annual CAPEX :                 {self._acap} €/MW/y")
        print('--------------------------------------------')
        print(f"fix_om:  {self._fix_om} €/MW/y")
        print(f"var_om:  {self._var_om} €/MWh")
        print(f"var_f:   {self._var_f} €/MWhi")
        print(f"var_co2: {self._var_co2} €/MWh")
        print('--------------------------------------------')
        print()
    
