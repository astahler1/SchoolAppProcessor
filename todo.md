# Development Todo List

## Day 1: Environment Setup (2 hours)

### Step 1: Install Windsurf
**Task**: Download and install Windsurf on your computer.

**Action**:
- Visit windsurf.com
- Download the installer for your OS (Windows or macOS)
- Follow the installation instructions

**Windsurf Prompt**: "Guide me to install Windsurf on [specify Windows or macOS, e.g., Windows 10]. Verify the installation is complete."

**Time**: 30 minutes

**Notes**: Ensure you have admin access to install software. Contact Windsurf support via their website if issues arise.

### Step 2: Set Up Project and Google Sheets API
**Task**: Create a Python project and configure the Google Sheets API.

**Action**:
- Open Windsurf and start a new project
- Use the prompt to set up Python, Tkinter, and required libraries
- Follow Windsurf's instructions to create a free Google Cloud account and enable the Sheets API
- Download API credentials (JSON file) and integrate them into the project

**Windsurf Prompt**: "Create a Python project 'SchoolAppProcessor' with Tkinter, pandas, gspread, and openpyxl for a desktop app. Set up the Google Sheets API with free credentials, providing step-by-step instructions for a beginner. Ensure no local data storage is configured."

**Time**: 1 hour

**Notes**: Save the API credentials securely; you'll need them for exporting to Google Sheets.

### Step 3: Verify Setup
**Task**: Confirm the project is ready for development.

**Action**:
- Run a simple test to ensure Python and libraries are installed
- Check that the Google Sheets API is accessible

**Windsurf Prompt**: "Test the 'SchoolAppProcessor' project to verify Python, Tkinter, pandas, gspread, and openpyxl are installed. Confirm Google Sheets API access by creating a test spreadsheet."

**Time**: 30 minutes

**Notes**: If errors occur, use Windsurf's error-fixing prompt or contact me for help.

## Day 2: Data Input and Formatting (3 hours)

### Step 4: Implement CSV Upload
**Task**: Build a GUI to upload a CSV file.

**Action**:
- Create a Tkinter window with a button to select a CSV file
- Load the CSV into memory using pandas
- Display a preview table in the GUI

**Windsurf Prompt**: "Create a Tkinter desktop app with a button to upload a CSV file containing: Parent Name, Home Phone, Work Phone, Cell Phone, Address, Email, Sibling Enrolled, Student Name, Date of Birth, Age, Gender, Present Grade, Present School, Applying Grade, Foster Youth, Homeless, Another Student. Load into memory with pandas and show a preview table."

**Time**: 1 hour

**Notes**: Test with a small CSV (see Appendix in PRD for format).

### Step 5: Test CSV Upload
**Task**: Verify the CSV upload works.

**Action**:
- Create a sample CSV with 5 records (use PRD's sample format)
- Upload it and check the preview table

**Windsurf Prompt**: "Test CSV upload with a 5-record sample. Display the data in the GUI table and fix any errors."

**Time**: 30 minutes

**Notes**: If the table doesn't display correctly, refine the prompt with "Add column headers to the GUI table."

### Step 6: Format Data for Google Sheet
**Task**: Process CSV data into Google Sheet tabs.

**Action**:
- Transform CSV data into the required format (10 tabs: TK, K, 1st–8th)
- Map fields per PRD (e.g., Sibling and WL, Additional Info)
- Ensure formatting (title case names, MM/DD/YYYY dates)
- Update the GUI preview to reflect formatted data

**Windsurf Prompt**: "Process the CSV into a Google Sheet with tabs for TK, K, 1st–8th grades. Columns: Lottery Number (blank), Random # (blank), Emp./Sibs (blank), City, Student Last Name, Student First Name, Phone, Alt. Phone, Sibling and WL (combine Sibling Enrolled, Another Student), Current ACA Sib. Enrollment Date (blank), Birth Date, Gender, Email, Address, Present School, Date Applied, Additional Info ('Foster Youth' or 'Homeless' if Yes). Exclude Who Student Lives With, Age. Format names in title case, dates in MM/DD/YYYY. Show a GUI preview table."

**Time**: 1 hour

**Notes**: Ensure City is extracted from Address; test parsing with varied formats.

### Step 7: Test Data Formatting
**Task**: Verify Google Sheet output and GUI preview.

**Action**:
- Upload the 5-record CSV
- Check the Google Sheet for correct tabs and columns
- Verify the GUI preview matches

**Windsurf Prompt**: "Test formatting with 5 records, verify Google Sheet has 10 tabs with correct columns and GUI preview matches."

**Time**: 30 minutes

**Notes**: If tabs are missing, use "Ensure all 10 grade tabs are created."

## Day 3: Red Flag Detection and Output (3 hours)

### Step 8: Implement Red Flag Detection
**Task**: Add logic to flag age/grade inconsistencies.

**Action**:
- Check four conditions (Birth Date vs. Age, Age vs. Present Grade, Age vs. Applying Grade, DOB vs. Applying Grade)
- Create a "Red Flags" tab with Student Name, Issue Description, Flag Code
- Highlight flagged rows in red in the GUI and Red Flags tab

**Windsurf Prompt**: "Check for: 1) Age vs. Date of Birth mismatch, 2) Age vs. Present Grade mismatch, 3) Age not one less than Applying Grade age, 4) Date of Birth vs. Applying Grade mismatch. Create a 'Red Flags' tab with: Student Name, Issue Description, Flag Code (e.g., 'AGE_DOB'). Highlight flagged rows in red in the GUI and Red Flags tab."

**Time**: 1 hour

**Notes**: Use age ranges from PRD (e.g., TK: 3–4 years for 2025).

### Step 9: Test Red Flag Detection
**Task**: Verify red flag logic and output.

**Action**:
- Create a CSV with known issues (e.g., DOB 01/01/2015, age 8, applying for TK)
- Check the Red Flags tab and GUI highlights

**Windsurf Prompt**: "Test with 5 records, including DOB 01/01/2015, age 8, applying for TK. Verify Red Flags tab and red highlights in GUI."

**Time**: 30 minutes

**Notes**: If flags miss issues, refine with "Adjust age calculation for leap years."

### Step 10: Implement Export Functionality
**Task**: Add export to Google Sheet and Excel.

**Action**:
- Add GUI buttons for Google Sheet and Excel export
- Ensure data is discarded after export
- Show a confirmation message

**Windsurf Prompt**: "Show a GUI table preview. Export as a Google Sheet with TK–8th and Red Flags tabs, or Excel file. Discard data after export, show confirmation."

**Time**: 1 hour

**Notes**: Test both export formats to ensure compatibility.

### Step 11: Test Export
**Task**: Verify export and data deletion.

**Action**:
- Upload a 10-record CSV
- Export as Google Sheet and Excel
- Confirm data is discarded (no residual files)

**Windsurf Prompt**: "Test export with 10 records, verify Google Sheet/Excel output and no residual data."

**Time**: 30 minutes

**Notes**: If data persists, use "Ensure all memory is cleared after export."
