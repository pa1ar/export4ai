# export4ai script

## wtf is this?

Script that grabs all text from files in a folder, wraps it up, and preps it for AI. No more copy-paste nightmares.

https://github.com/user-attachments/assets/018d86d3-6a84-409f-ac7b-1f6b3eefab1f

## why care?

Need to feed text files to an external AI chatbot? This script does it in seconds. Helpful for iterative back-and-forth.  
Save time, look cool.

## usage

### **clone it:**
   - `git clone https://github.com/pa1ar/export4ai`

### **alias it:**
   - Add to `~/.zshrc` or `~/.bashrc`:
     ```bash
     alias 4aiexport='python /path/to/4aiexport.py'
     ```
   - Reload: `source ~/.zshrc` or `source ~/.bashrc`.

### **then use it**

Assuming you in the right folder (your project or whatever).

1. **basic:**
   - `4aiexport .` - Export all text files in the current dir.

2. **exclude junk:**
   - `4aiexport . -x node_modules -x README.md` - Skip these.

3. **specific files:**
   - `4aiexport file1.txt file2.py` - Just these.

## **tips**

- if you want to copy the output to clipboard, add `| pbcopy` at the end of the command
- you can modify the wrapping of the script in the `4aiexport.py` file to your liking 

That is all.
