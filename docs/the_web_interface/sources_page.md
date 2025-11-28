# Sources Page

This page gives users a full workspace for managing **Kleio source files** inside Timelink. It combines file browsing, translation, importing, status tracking, and error reviews into one interface. A scheduled job refreshes the files' status every 5 minutes so the dashboard always reflects the current system state.

![alt text](sources_page.png)


---

## Features

### Kleio File browsing

- A built-in file explorer shows folders and `.cli` files inside the Timelink home directory.
- Users can click through folders, open subdirectories, and view file details.

### File Translation and Import Status

Each file displays:

- Its status (translated, pending, warnings, etc...)
- Its translation report (warnings and errors)
- Its import report (not imported, queued, errors)
- A user can additionally click the `.cli` file directly to observe its contents.

The sidebar summarizes:

- How many files need translation/import  
- How many have warnings or errors  
- What’s queued for import/translation and what is running on the background
- Items that need reviewing.


### Translating and importing files

Users can select one or more files at once and run translation and/or import on the selected files easily, which triggers a job running on the background according to the selected option.

Once done, the results can be seen by clicking the file's import/translation status directly, or by clicking the Translation/Importer output tabs.


---

## Main Sections

### **Files**
The interactive explorer for browsing, selecting, translating, and importing Kleio files.

### **Repository**
Placeholder area for future repository-related features. (see [Roadmap](web_roadmap.md))

### **Translation Output**
Shows translation results and error reports.

### **Importer Output**
Shows importer results and error summaries.

### **Help**
Explains the translation/import pipeline and how to interpret errors.

---

### [Back to Page Index](inside_app.md)