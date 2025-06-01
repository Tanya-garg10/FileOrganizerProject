🧾 USER GUIDE: File Organizer Script

📌 Overview
This user guide provides step-by-step instructions on how to use the Python File Organizer Script to automatically sort files in a selected directory based on their type (e.g., documents, images, videos, others).

🛠️ Requirements
•	Python 3 installed
•	Basic understanding of using a terminal or command prompt
•	Script file: file_organizer.py

📁 Supported File Categories
Category	         Extensions
Documents	     .pdf, .docx, .txt, .pptx, .xlsx
Images	         .jpg, .jpeg, .png, .gif, .bmp
Videos	         .mp4, .avi, .mov, .mkv
Others	         All other file types

🚀 How to Run the Script
1.	Open Terminal / Command Prompt
2.	Navigate to Script Folder
3.	Run the Script
4.	Input the Directory Path

🧪 Example Before and After

📂 Before Running Script:
All files are scattered inside the folder:
test_files/
│
├── notes.txt
├── report.pdf
├── image.jpg
├── video.mp4
├── unknown.xyz
📂 After Running Script:
Files are sorted automatically into:
test_files/
│
├── Documents/
│   └── notes.txt, report.pdf
├── Images/
│   └── image.jpg
├── Videos/
│   └── video.mp4
├── Others/
│   └── unknown.xyz

📸 Screenshots
Add screenshots in the /screenshots/ folder to demonstrate the file arrangement before and after.

🔧 Troubleshooting
•	Directory not found?
Make sure the path is correct and surrounded by quotes if it contains spaces.
•	Nothing happens?
Ensure there are files in the selected folder and the script is run using Python 3.

👨‍💻 Author
•	Name: Tanya Garg
•	Internship Project – Python Automation
•	Organization: Infotact Solutions

