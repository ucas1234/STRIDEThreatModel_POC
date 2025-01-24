import json
from enum import Enum

# Define class and use Enum for the likelihood and impact
class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

# Define class STRIDEThreatModel
class STRIDEThreatModel:


    # Create init funtion as constructor of STRIDEThreatModel class. Will be called every time object of class is crrated
    def __init__(self):

        # Create threats dictionary as an object of class using the 6 STRIDE categories
        self.threatCategories = {'Spoofing': [], 'Tampering': [], 'Repudiation': [], 'Information Disclosure': [], 'Denial of Service': [], 'Elevation of Privilege': []}

    # Create function that validates imputs
    def get_valid_input(self, prompt, valid_range):
        while True:
            try:
                # Convert users input into a integer
                choice = (int(input(prompt)))
                if choice not in valid_range:
                    print(f"Please enter a number between {valid_range.start} and {valid_range.stop - 1 }.")
                else:
                    return choice
            except ValueError:
                print("Invalid input. Please enter a number.")

    
    # Create function which will add the details of each threat to the threat category and append risk score
    def add_threat(self, threat_category, description, component, likelihood, impact, mitigations):
        # Loop to check if the threat type that has been specified exists in the threats dictionary and create new threat object with all the attributes we need.
        if threat_category in self.threatCategories:
            threat = {'threat_category': threat_category,'description': description, 'component': component,'likelihood': likelihood, 'impact': impact, 'mitigations': mitigations}
            # Use calculate_risk_score score function to calculate risk score using likelihood * impact
            risk_score = self.calculate_risk_score(likelihood, impact)
            # Add this risk score to our threat object as  new string attribute and append to list of threats associated with the specified threat_category
            threat['risk_score'] = risk_score
            self.threatCategories[threat_category].append(threat)
        # Handle error if the specified threat_category is not in the 6 STRIDE threat categories dictionary.
        else:
            print(f"This is not a valid threat category {threat_category}. Please choose a valid threat category from the STRIDE model")


    # Create function to calculate the risk score
    def calculate_risk_score(self, likelihood, impact):
        
        return likelihood.value * impact.value
    

    # Create function to display the list of "threat_category"'s from our self.threatCategories dictionary
    def display_threat_categorys(self):
        print("\nSelect a threat category from the list:")

        # Use python .list() function to convert the threat_category keys 
        # from self.threatCategories dictionary into a list of strings ofkeys stored 
        # as threat_categorys variable
        # Use the python .keys() function to retrieve all the keys from self.threatCategories dictionary.
        threat_categorys = list(self.threatCategories.keys())

        # Use index variable to loop to iterate over the threat_category in the threat_categorys list, incrementing 
        # value until end of list
        for index, threat_category in enumerate(self.threatCategories.keys(), start = 1):

            # Print the index number to screen followed by threat type for each threat type from self.threatCategories dictionary
            # Use .f to conver the variable vlaues into a string
            print(f"{index}. {threat_category}")

            # Return threat_thyes to be used in other functions
    
        return list(self.threatCategories.keys())

        

    # Create a function that displays individual threats associated with threat_category selected
    def display_individual_threats(self, threat_category):

        # Use .get(threat_category, []) to get the list of threats for chosen threat types from our self.threatCategories dictionary
        threats = self.threatCategories.get(threat_category, [])

        # Check if our threats list if empty, if it is print error message
        if not threats:
            print(f"No threats available for the {threat_category} category.")
            return []
        print(f"\nSelect a threat from the '{threat_category}' category:")
        
        # Use index variable to loop to iterate over the list of individual threats until end of list is reached
        for index, threat in enumerate(threats, start = 1):
            # Print to screen the index number followed by a . then the threat description from the threat dictionary for each threat.
            print(f"{index}. {threat['description']}")
        
        # Return threats so they can be used by other functions
        return threats

    # Create function that takes the selected threat as an input parameter then displays all of its attributes
    def view_threat_details(self, selected_threat):
        print("\n ----- Threat Details -----")
        print(f"Type: {selected_threat['threat_category']}")
        print(f"Description: {selected_threat['description']}")
        print(f"Component: {selected_threat['component']}")
        print(f"Likelihood: {selected_threat['likelihood'].name}") # We use .name to get just the name of the enum without Severity. before it 
        print(f"Impact: {selected_threat['impact'].name}") # We use .name to get just the name of the enum without Severity. before it 
        print(f"Risk Score: {selected_threat['risk_score']}")
        # Final print is a list of multiple mitigations. Use the .join() function to concatinate comma seperated strings
        print(f"Mitigations: {', '.join(selected_threat['mitigations'])}")

    
    # Create function to load in the threats listed in our .json file
    def load_threats_from_json(self, json_file):
        # Error handle json file opening with try: and except block
        try:
            with open(json_file, 'r') as file: # the "as file" part is used to assign the opened file object to a variable called file to perform operations on it.
                # Use .load() python function which is part of the json module. It converts json-encoded string to a python data structure.
                threats_data = json.load(file)
                for threat in threats_data:
                    threat_category = threat['threat_category']
                    description = threat['description']
                    component = threat['component']
                    likelihood = threat['likelihood']
                    impact = threat['impact']
                    mitigations = threat['mitigations']

                    #  Convert likelihood and impact to Severity enum

                    try:
                        likelihoodEnum = Severity[likelihood.upper()] # Convert our likelihood string from json into Severity Enum
                        impactEnum = Severity[impact.upper()] # Convert our impact string from JSON into Severity Enum
                    
                    except KeyError:
                        print(f"Error: Invalid likelihood or impact value '{likelihood}' or '{impact}' for threat: {threat}")
                        continue
                    if threat_category and description and component:
                        self.add_threat(threat_category, description, component, likelihoodEnum, impactEnum, mitigations)
                    else:
                        print(f"Missing data for threst: {threat}")
        except FileNotFoundError:
            print(f"Error: The file {json_file}  was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode the JSON file.")

    # Create a function that allows the user to choose a threat category and view individual threats in that category
    def interactive_menu(self):
        while True:
            print("\nPlease choose an option:")
            print("1. View Threat Categories")
            print("2. Exit")
            choice = input("Enter choice (1-2): ")
            # If the user chooses option 1 (View Threat Categories), show available threat categories.
            if choice == '1':
                threat_categories = self.display_threat_categorys()
                # Use out get_valid_input function to ensure that the input is between 1 and lenght of our threat category list
                selected_category_index = self.get_valid_input(f"Select a threat category (1-{len(threat_categories)}): ", range(1, len(threat_categories) + 1)) - 1
                # Retrieve the selected category from the threat_categories list using the index selected
                selected_category = threat_categories[selected_category_index]
                # Display list of individual threats in the category selected
                threats = self.display_individual_threats(selected_category)
                if threats:
                    # If there are threats in that category use input validation again with indexing for list of individual threats 
                    selected_threat_index = self.get_valid_input(f"Select a threat (1-{len(threats)}): ", range(1, len(threats) + 1)) - 1
                    # Retrieve selected individual threat threats list using the index selected
                    selected_threat = threats[selected_threat_index]
                    # Display all of the details of the individual threat
                    self.view_threat_details(selected_threat)
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose again.")


# ---------------- Main program below -----------------------


# Checks if the script is being run directly (as opposed to being imported as a module). If it is being run directly, the following code is executed.
if __name__ == "__main__":
    
    # Create a new object from the class StrideThreatModel() called threat_model
    threat_model = STRIDEThreatModel()

    # Next load our thrEATS FROM json into the threat_model object
    threat_model.load_threats_from_json('threats.json')

    # Start up user interactive menu
    threat_model.interactive_menu()



        
                        







                
