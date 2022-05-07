# vCard-tools
A set of codes to help move contacts between smartphones and feature phones.  

Recently, I decided to set-up my feature phone into a secondary calling-only device. To make this happen, I wanted to transfer all my contacts from my google account into the feature phone. The feature phone I was using was Nokia Asha 205 (https://www.gsmarena.com/nokia_asha_205-5137.php) which I bought in April 2013.  

## Background to the solution:

My search with the query "Moving contacts from google to old Nokia phone" took me to some promising solutions (links pasted on the following lines)  
https://www.lambrospetrou.com/articles/nokia-symbian-s40-contacts-transfer/  
https://nokiapoweruser.com/how-to-import-contacts-on-nokia-215-220-225-230/   
https://talubu.wordpress.com/2017/08/09/how-to-import-contacts-to-nokia-3310-2017-215-220-222-225-230/  

And then I found this GitHub repository - https://github.com/patrickuhlmann/nokia3310contacts. But the solution required running a java script which I wasn't familiar with.

I tried running macros on MS Excel (Couldn't find the link to this solution)

And then I found this - https://gist.github.com/in4lio/1e16ead4ebe459919ae6551544cc3b22. This was a Python code, which I had some prior experience using.

By this stage I was getting a hang of what needed to be done.

## Suggested Workflow:  

(1) Export contacts from contacts.google.com as vCard format. The vCard file is same as the .vcf files (for all practical purposes with regards our problem.).  
(2) Split the multi-contact vCard file into multiple single-contact vcf files.  
(3) Format the single-contact vCard file into a format that nokia S40 devices use. This meant looking carefully for key differences between vCard Version 3.0 and 2.1.  
(4) Download and install the Nokia Suite software (which is an evolution of Nokia Ovi Suite and an even older Nokia PC Suite).  
(5) Connect the Nokia Asha 205 phone (via Bluetooth) to the Nokia Suite software and set up sync.  
(6) Backup existing contacts on the Nokia Asha 205 through the Nokia suite interface.  
(7) Delete all contacts from the Nokia Asha 205 phone and the computer. This is important as the Nokia Asha 205 phone has only limited storage and it is best to have a clean copy of the latest contacts without any duplicates.  
(8) Import the single contact formated vcf files into Nokia Suite.  
(9) Sync the contacts with the Nokia Asha 205 device.    

## Description of files:
*Expert tip* Run these codes in a separate folder with the associated vCard (or vcf) files as the output is saved in the same folder. Working in the separate folder means all output files are available in the same place.*  

**split.py** A script for splitting multi-contact single vCard file (input) to single contact multiple vcf files (Outputs).  
**vcf_formatter.py** A script for formatting (Overwrite) the single contact multiple vcf files (input) into version 2.1 single contact multiple vcf files (Output)  
**example_multicontact_vCard.vcf** An example export of 3 contacts from google contacts.   
**example-split-folder.zip** An example folder after executing the split.py program.  
**example-formatted-folder.zip** An example folder after executing vcf_formatter.py on a copy of the split files.  
**problematic_output_examples.zip** Folder with 3 files- an example problematic split file, actual formatted output, manual formmatted output.  
 
*Expert tip* Remember to make a copy of the unformatted vcf files in a separate folder before running vcf_formatter.py since the code overwrites the files being processed.

## Limitations
The vcf_formatter.py assumes a certain format of the input vcf files. But in my experience I noticed that not all the version 3.0 vcf files that I created from the single vCard were of the same formatting. This resulted in ommission of some contact details in the final output vcf files. I tried to manually format some vcf files. Examples of the files requiring manual processing are saved separately for reference and for improving the code. The contact details in these files are representative and not actuals.

## Update dated 07-May-2022
I have found an effective tool on the link https://sourceforge.net/projects/csv2vcfconverter/ that helps convert a csv file to the vcf2.1 format needed in old nokia phones.
