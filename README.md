# export4ai script

## wtf is this?

Script that grabs all text from files in a folder, wraps it up, and preps it for AI. No more copy-paste nightmares.

[live action](export4ai_demo.mp4)

## why care?

Need to feed text files to an external AI chatbot? This script does it in seconds. Helpful for iterative back-and-forth.  
Save time, look cool.

## usage

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

That is all.
