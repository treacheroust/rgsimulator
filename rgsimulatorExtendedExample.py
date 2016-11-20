# This example shows how you can add additional behavior to rgsimulator without mucking with the base rgsimulator code.
# This is done by creating a derived class which inherits from the base rgsimulator classes.
# For example, this can be used to add new key binding with custom behavior.

from rgsimulatorUI import SimulatorUI as BaseSimulatorUI
from rgsimulator import Simulator as BaseSimulator

class SimulatorUI(BaseSimulatorUI):
    def __init__(self, settings):
        BaseSimulatorUI.__init__(self, settings)
        # Add custom behavior here ...

class Simulator(BaseSimulator):
    def __init__(self, player1_path, player2_path, uiClass):
        BaseSimulator.__init__(self, player1_path, player2_path, SimulatorUI)
        # Add custom code here ...


if __name__ == "__main__":

    from rgsimulator import parseArguments
    args = parseArguments()

    p1_path = args.player
    p2_path = args.player2

    s = Simulator(p1_path, p2_path, SimulatorUI)
    s.run()
