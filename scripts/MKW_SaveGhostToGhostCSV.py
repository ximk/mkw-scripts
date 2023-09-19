from dolphin import gui
import TTK_Lib

"""
MKW_SaveGhostToGhostCSV

This script takes the current ghost's inputs and write them to the ghost csv file
"""

def main() -> None:
    gui.add_osd_message("Script started")
    
    # Convert internal RKG to input list
    input_sequence = TTK_Lib.readFullDecodedRKGData(TTK_Lib.PlayerType.GHOST)
    
    if (input_sequence is None or len(input_sequence) == 0):
        gui.add_osd_message("No inputs read!")
        return
    
    TTK_Lib.writeToCSV(input_sequence, TTK_Lib.PlayerType.GHOST)

if __name__ == '__main__':
    main()