'''
    Shoutouts to Everyone
'''
import win32com.client

def pronounce_names(names):
    '''
        Function to pronounce names
    '''
    # Create the SAPI voice object
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    # Pronounce each name in the list
    for name in names:
        print(f"Pronouncing: {name}")
        speaker.Speak(name)

# List of names to pronounce
names_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Define an event handler class using snake_case argument names
class SpeechEvents:
    def OnStartStream(self, stream_number, stream_position):
        print(f"Speech started. Stream Number: {stream_number}, Stream Position: {stream_position}")

    def OnEndStream(self, stream_number, stream_position):
        print(f"Speech ended. Stream Number: {stream_number}, Stream Position: {stream_position}")

# Define the function to pronounce a list of names
def pronounce_names1(names):
    # Use DispatchWithEvents to bind the SAPI.SpVoice object to our event handler class
    speaker1 = win32com.client.DispatchWithEvents("SAPI.SpVoice", SpeechEvents)

    # Pronounce each name in the list
    for name in names:
        print(f"Speaking: '{name}'\n")
        speaker1.Speak(name)

# List of names to pronounce
names_list1 = ["Alice", "Bob", "Charlie", "David"]

# Call the function to pronounce the names
a= SpeechEvents()
pronounce_names(names_list)
pronounce_names1(names_list1)
