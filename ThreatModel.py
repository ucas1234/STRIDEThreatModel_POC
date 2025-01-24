import json

# Define class STRIDEThreatModel
class STRIDEThreatModel:


    # Create init funtion as constructor of STRIDEThreatModel class. Will be called every time object of class is crrated
    def __init__(self):

        # Create threats dictionary as an object of class using the 6 STRIDE categories
        self.threatCategories = {
            'Spoofing': [],
            'Tampering': [],
            'Repudiation': [],
            'Information Disclosure': [],
            'Denial of Service': [],
            'Elevation of Privilege': [],
        }
    
    # Create function which will add the details of each threat to the threat category and append risk score
    def add_threat(self, threat_category, description, component, likelihood, impact, mitigations):
        # Loop to check if the threat type that has been specified exists in the threats dictionary and create new threat object with all the attributes we need.
        if threat_category in self.threatCategories:
            threat = {
                'description': description,
                'component': component,
                'likelihood': likelihood,
                'impact': impact,
                'mitigations': mitigations
            }
            # Use calculate_risk_score score function to calculate risk score using likelihood * impact
            risk_score = self.calculate_risk_score(likelihood, impact)
            # Add this risk score to our threat object as  new string attribute and append to list of threats associated with the specified threat_category
            threat['risk_score'] = risk_score
            self.threatCategories[threat_category].append(threat)
        # Handle error if the specified threat_category is not in the 6 STRIDE threat categories dictionary.
        else:
            print("This is not a valid threat type. Please choose a valid threat category from the STRIDE model")


    # Create function to calculate the risk score
    def calculate_risk_score(self, likelihood, impact):

        # Define the likelihood and impact disctionaries, assigning numeric inputs to strings
        likelihood_map = {'Low': 1, 'Medium': 2, 'High': 3}
        impact_map = {'Low': 1, 'Medium': 2, 'High': 3}

        #Use .get() function to search forvalue assicated with key in dictionary, return 0 if doesn't exist
        return likelihood_map.get(likelihood, 0) * impact_map.get(impact, 0)
    

    # Create functyion to display the list of "threat_category"'s from our self.threatCategories dictionary
    def display_threat_categorys(self):
        print("\nSelect a threat category from the list:")

        # Use python .list() function to convert the threat_category keys 
        # from self.threatCategories dictionary into a list of strings ofkeys stored 
        # as threat_categorys variable
        # Use the python .keys() function to retrieve all the keys from self.threatCategories dictionary.
        threat_categorys = list(self.threatCategories.keys())

        # Use index variable to loop to iterate over the threat_category in the threat_categorys list, incrementing 
        # value until end of list
        for index, threat_category in enumerate(threat_categorys, start = 1):

            # Print the index number to screen followed by threat type for each threat type from self.threatCategories dictionary
            # Use .f to conver the variable vlaues into a string
            print(f"{index}. {threat_category}")

            # Return threat_thyes to be used in other functions
    
        return threat_categorys

        

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
        print(f"Likelihood: {selected_threat['likelihood']}")
        print(f"Impact: {selected_threat['impact']}")
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
                    self.add_threat(threat_category, description, component, likelihood, impact, mitigations)
        except FileNotFoundError:
            print(f"Error: The file {json_file}  was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode the JSON file.")

    # Create a function that allows the user to choose a threat category and view individual threats in that category
    def interactive_menu(self):

        # Infinite loop which continuously shows the user menu options every time the loop runs
        while True:
            print("\nPlease choose an option:")
            print("1. View Threat Categories")
            print("2. Exit")

            choice = input("Enter choice (1-2): ")

            if choice == '1':

                # Get the list of threat types with our display_threat_categorys() function and set equal to threat_categorys variable
                threat_categorys = self.display_threat_categorys()

                # Handle errors with try except block
                try:

                    threat_category_choice = int(input(f"Select a threat category (1-{len(threat_categorys)}): ")) - 1 # -1 adjusts the selection value as list indiced in Py start at 0

                    if 0 <=threat_category_choice < len(threat_categorys):

                        # From threat_categorys list retrieve the specific thrat category choice by the number user input
                        selected_threat_category = threat_categorys[threat_category_choice]

                        # Call our display_individual_threats() functio, passing in our selected_threat_category to return a list of threats associated with this category
                        threats = self.display_individual_threats(selected_threat_category)

                        if threats: # Check there are any threats in list

                            # Handle errors with try excepclet block 
                            try:
                                threat_choice = int(input(f"Select a threat (1-{len(threats)}): ")) - 1
                                if 0 <= threat_choice < len(threats):
                                    
                                    # From the list of individual threats retrieve specific number that was input by the user as the threat choice
                                    selected_threat = threats[threat_choice]

                                    # Create new key value pair within our selected_threat object
                                    selected_threat['threat_category'] = selected_threat_category

                                    # Call our view_threat_details function and pass in the selected_threat
                                    self.view_threat_details(selected_threat)
                                
                                else:
                                    print("Invalid choice. Returning to threat categories.")
                            
                            # Use ValueError py function to catch exception if anythin other then an integer is input
                            except ValueError:
                                print("Invalid input. Please enter a number.")
                        else:
                            print("Invalid choice. Returning to main menu.")
                except ValueError:
                    print("Invalid input. Please enter a number")
            
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose again.")


# Main program is below
# Use the python __name__ variable which automatically assigned a value depending on how file is used
if __name__ == "__main__":

    # Create a new object which is part of the STRIDEThreatModel() class
    threat_model = STRIDEThreatModel()

    # Call out load json function and append to our newly created threat_model object
    threat_model.load_threats_from_json('threats.json')

    threat_model.interactive_menu()



        
                        







                
