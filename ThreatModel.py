import json

# Define class STRIDEThreatModel
class STRIDEThreatModel:


    # Create init funtion as constructor of STRIDEThreatModel class. Will be called every time object of class is crrated
    def __init__(self):

        # Create threats dictionary as an object of class using the 6 STRIDE categories
        self.threats = {
            'Spoofing': [],
            'Tampering': [],
            'Repudiation': [],
            'Information Disclosure': [],
            'Denial of Service': [],
            'Elevation of Privilege': [],
        }
    