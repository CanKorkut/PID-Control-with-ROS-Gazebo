
# coding: utf-8

class pid:
    def __init__(self):
        self.P_value=0.0
        self.I_value=0.0
        self.D_value=0.0
        self.kp=0.05
        self.ki=0.002
        self.kd=0.002
        self.Derivator=0
        self.Integrator=0
        self.Integrator_Max=500
        self.Integrator_Min=-500
        self.set_point=200.0
        self.error=0.0
    def update(self,current_value):
        self.error=self.set_point - current_value
        if self.error <0:
            self.error = 0
        try:
            self.P_value=self.kp*self.error
        except ZeroDivisionError:
            self.P_value=0.0
        self.D_value=self.kd*(self.error-self.Derivator)
        self.Derivator=self.error
        self.Integrator=self.Integrator+self.error
        if self.Integrator > self.Integrator_Max:
            self.Integrator_Max=self.Integrator_Max
        elif self.Integrator < self.Integrator_Min:
            self.Integrator_Min=self.Integrator_Min
        self.I_value = self.Integrator*self.ki
        PID = self.P_value + self.I_value + self.D_value
        return PID
    def setPoint(self,set_point):
        self.set_point=set_point
        self.Integrator=0
        self.Derivator=0

    def setIntegrator(self,Integrator):
        self.Integrator=Integrator

    def setDerivator(self,Derivator):
        self.Derivator = Derivator

    def setKp(self,Kp):
        self.kp=Kp

    def setki(self,Ki):
        self.ki=Ki

    def setkd(self,Kd):
        self.kd=Kd

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator

