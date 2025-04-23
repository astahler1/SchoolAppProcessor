Product Requirements Document (PRD): School Application Data Processor

1. Overview
1.1 Purpose
The School Application Data Processor is a desktop application designed to streamline the processing of student application data for a school. It will:
Accept a CSV file exported from the school's website containing application data.
Format the data into a Google Sheet with tabs for each grade level (TK–8th), eliminating unnecessary fields and mapping specific fields to designated columns.
Detect red flags related to age and grade inconsistencies, highlighting them in a separate tab.
Export the results as a Google Sheet (or Excel) without storing data locally to ensure security.
Serve as a proof-of-concept to demonstrate time savings for office staff, with plans for future refinements.

1.2 Background
The school currently collects student application data via a website, exporting it as a CSV file. Office admins manually process this data into a Google Sheet with grade-level tabs, which is time-consuming and error-prone. Common issues include mismatches between age, date of birth, and grade levels. This app automates the process, improving efficiency and accuracy.

1.3 Goals
Build a simple, cross-platform (Windows/macOS) desktop app in 5–10 hours using free tools.
Ensure ease of use for non-technical office admins withminimal IT support.
Prioritize security by avoiding local data storage and complying with FERPA.
Create a proof-of-concept to justify further development (e.g., adding passwords, more features).

1.4 Stakeholders
Primary Users: Office administrators who process student applications.
Developer: Novice user with minimal coding knowledge, using Windsurf's AI.
School Leadership: Approves potential budget for future enhancements based on proof-of-concept.

2. Requirements
2.1 Functional Requirements
2.1.1 Data Input
Description: Users upload a CSV file exported from the school's website via a graphical user interface (GUI).
CSV Fields:
Parent Name, Who Student Lives With, Home Phone, Work Phone, Cell Phone, Address, Email, Sibling Currently Enrolled (Y/N), Student Name, Date of Birth, Age, Gender, Present Grade, Present School, Applying Grade, Foster Youth (Y/N), Homeless/Unhoused (Y/N), Another Student (Y/N).
Process: Load CSV into memory using pandas, display a preview table in the GUI.

2.1.2 Data Formatting
Description: Transform CSV data into a Google Sheet with 10 tabs (TK, K, 1st–8th grades).
Columns per Tab:
Lottery Number (blank), Random # (blank), Emp./Sibs (blank), City (extracted from Address), Student Last Name, Student First Name, Phone (Home or Cell), Alt. Phone (Work or Cell), Sibling and WL (combine Sibling Enrolled, Another Student), Current ACA Sib. Enrollment Date (blank), Birth Date, Gender, Email, Address, Present School, Date Applied (today's date), Additional Info (include "Foster Youth" or "Homeless" if Yes).

Formatting Rules:
- Eliminated Fields: Who Student Lives With (completely), Age (used only for red flags).
- Mapped Fields:
  - Sibling and WL: Combine Sibling Currently Enrolled and Another Student
  - Additional Info: Include "Foster Youth" or "Homeless" if respective fields are Yes
  - Split Student Name into First and Last Name
  - Extract City from Address
  - Phone: Prefer Home Phone, fallback to Cell
  - Alt. Phone: Prefer Work Phone, fallback to Cell
  - Dates: MM/DD/YYYY format
  - Names: Title case

2.1.3 Red Flag Detection
Description: Identify inconsistencies in age and grade data, flagging them in a separate tab.
Conditions:
- Birth Date vs. Age: Age doesn't match Date of Birth
- Age vs. Present Grade: Age doesn't align with typical grade age
- Age vs. Applying Grade: Age is not one less than the typical age for the grade applied for
- DOB vs. Applying Grade: DOB doesn't align with typical age for applying grade

Typical Age Ranges (2025, applying for current/next year):
- TK: 3–4 years (DOB ~09/02/2020–09/01/2021)
- K: 4–5 years (DOB ~09/02/2019–09/01/2020)
- 1st: 5–6 years, ..., 8th: 12–13 years

Output:
"Red Flags" tab with columns: Student Name, Issue Description, Flag Code

2.1.4 Output
Description: Export formatted data and red flags as a Google Sheet, with an Excel file option.
- Display: GUI table preview before export
- Storage: No local storage; data processed in memory, exported, then discarded

2.1.5 User Interface
Description: Simple Tkinter GUI with:
- Button to upload CSV
- Preview table for formatted data, with red highlights for flagged rows
- Buttons to export as Google Sheet or Excel
- Confirmation message after export

2.2 Non-Functional Requirements
2.2.1 Security
- No Local Storage: Process data in memory, discard after export
- FERPA Compliance: Restrict to authorized users, document data use
- Future: Option to add password authentication

2.2.2 Performance
Process CSVs with up to 100 records in <10 seconds

2.2.3 Usability
- Intuitive GUI for non-technical users
- Simple installation (one-click executable)

2.2.4 Compatibility
Cross-platform: Windows and macOS

2.3 Constraints
- Time: 5–10 hours for proof-of-concept
- Budget: Free tools (Python, Tkinter, pandas, gspread, openpyxl)
- Skill Level: Novice developer using Windsurf's AI
- IT Support: Minimal, requiring simple installation and use
- Future Refinements: Password, additional red flags, notifications

3. Technical Specifications
3.1 Tech Stack
- Language: Python 3.x
- GUI Framework: Tkinter
- Libraries: pandas, gspread, openpyxl
- Storage: None (in-memory processing)

3.2 Development Environment
- Google Sheets API: Free credentials via Google Cloud Console

3.3 Deployment
- Packaging: PyInstaller for Windows/macOS executables
- Distribution: Copy executable to two computers via USB/email

4. Development Plan
4.1 Timeline
Total: 5–10 hours over 4 days
- Day 1 (2 hours): Environment setup, Google Sheets API configuration
- Day 2 (3 hours): Data Input, Data Formatting
- Day 3 (3 hours): Red Flag Detection, Output
- Day 4 (1–2 hours): Testing, packaging, user guide

4.2 Tasks
Detailed implementation tasks for:
- Data Input (2 hours)
- Data Formatting (2 hours)
- Red Flag Detection (2 hours)
- Output (1–2 hours)
- Packaging and Documentation (1 hour)

4.3 Testing Plan
- Input: Test CSV upload with 10 records
- Formatting: Verify Google Sheet tabs/columns
- Red Flags: Test with errors
- Output: Confirm export, data deletion

5. Future Enhancements
- Password authentication
- Additional red flags (e.g., missing Email)
- Email notifications for red flags

6. Risks and Mitigations
- Google Sheets API setup complexity
- Age calculation errors
- Cross-platform issues
- User adoption challenges

7. Appendices
7.1 Sample CSV Format
```csv
Parent Name,Who Student Lives With,Home Phone,Work Phone,Cell Phone,Address,Email,Sibling Enrolled,Student Name,Date of Birth,Age,Gender,Present Grade,Present School,Applying Grade,Foster Youth,Homeless,Another Student
Jane Doe,Parents,555-1234,555-5678,555-9012,123 Main St, City1, CA 12345,jane@example.com,Yes,John Doe,01/01/2020,5,Male,K,School A,1st,No,No,Yes
```

7.2 Sample Google Sheet Output
Tab: TK
Columns: Lottery Number, Random #, Emp./Sibs, City, Student Last Name, Student First Name, Phone, Alt. Phone, Sibling and WL, Current ACA Sib. Enrollment Date, Birth Date, Gender, Email, Address, Present School, Date Applied, Additional Info
