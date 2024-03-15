import streamlit as st
import tkinter as tk
from tkinter import filedialog
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
# Set up tkinter
root = tk.Tk()
root.title("tester")
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
st.title('Folder Picker')
st.write('Please select a folder:')
clicked = st.button('Folder Picker')
if clicked:
    folderName = st.text_input('Selected folder:', filedialog.askdirectory(master=root))
    for root, dirs, files in os.walk(folderName):
        for name in files:
            local_file_path = os.path.join(root, name)
            st.write("File:", local_file_path)
#             print("inside files: ")
#             print("gcs_blob_path: ", gcs_blob_path)
        for directory in dirs:
            local_dir_path = os.path.join(root, directory)
            
 
#             print("inside dirs: ")
#             print("gcs_blob_path: ", gcs_blob_path)
            st.write(f"Uploaded folder {local_dir_path}")