# study-grouper [Smart Group Formation System]

A Python-based tool that automatically forms small, balanced groups using location proximity and digital skill level.

Originally built to organize MSc study groups more efficiently, this system uses real-world constraints like distance and technical proficiency to create practical, well-balanced teams


**Setup & Requirements (Installation Instructions at Bottom)**
Requirements

1. Python 3.x

2. pandas

3. requests

4. Google Maps API key


**Features**

Forms mini-groups of max 5 people

Ensures members live within 12 km of each other

Guarantees at least 2 “Digital Natives” per group

Uses Google Maps API for distance calculations

Accepts data from an Excel file

Outputs groups using student surnames


**The tool expects an Excel file with the following columns:**

1. Column Name	Description
2. Surname	Student's surname
3. Location	Address or GPS-friendly location
4. IT Experience	e.g., "Digital Native: Grew up in the digital age, highly proficient with technology."

**How It Works (High-Level)**

1. Reads student data from Excel

2. Separates Digital Natives from others

3. Builds groups starting with at least 2 Digital Natives

4. Adds nearby members (≤12 km)

5. Stops at 5 members per group

6. Outputs the final groups
   

** Example Use Cases**
This system can be adapted for:

🎓 Study & project groups

🏢 Workplace team formation

🚑 Emergency response teams

🌍 Community & NGO programs

🎤 Event & hackathon groups

🏃 Local sports or fitness groups

Anywhere you need small, local, skill-balanced teams.

**Install Instructions**

Install dependencies:
1. **pip install pandas requests**

2. 🔑 Google Maps API

Create an API key at:
https://developers.google.com/maps

Add your key to the script:

**API_KEY = "YOUR_API_KEY_HERE"**

3. Running the Project
   
   **python group_creator.py**

**Project Structure
**
/smart-grouping
│
├── group_creator.py
├── students.xlsx
├── README.md


**Contributing**

Feel free to:

Fork the repo

Improve the algorithm

Optimize performance

Add visualization

Improve distance logic

Extend use cases

Pull requests are welcome!

📜 License

Open-source for learning, experimentation, and community use.

Author

Built by JKQ
MSc Digital Forensics & Cybersecurity
Cybersecurity | Python | Problem Solving




