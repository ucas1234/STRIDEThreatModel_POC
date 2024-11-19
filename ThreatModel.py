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
    
    # Create function which will add the details of each threat to the threat category and append risk score
    def add_threat(self, threat_type, description, component, likelihood, impact, mitigations):
        # Loop to check if the threat type that has been specified exists in the threats dictionary and create new threat object with all the attributes we need.
        if threat_type in self.threats:
            threat = {
                'description': description,
                'component': component,
                'likelihood': likelihood,
                'impact': impact,
                'mitigations': mitigations
            }
            # Use calculate_risk_score score function to calculate risk score using likelihood * impact
            risk_score = self.calculate_risk_score(likelihood, impact)
            # Add this risk score to our threat object as  new string attribute and append to list of threats associated with the specified threat_type
            threat['risk_score'] = risk_score
            self.threats[threat_type].append(threat)
        # Handle error if the specified threat_type is not in the 6 STRIDE threat categories dictionary.
        else:
            print("This is not a valid threat type. Please choose a valid threat category from the STRIDE model")


    # Create function to calculate the risk score
    def calculate_risk_score(self, likelihood, impact)
        


