
## Virtual Environment Setup (Linux Mint)

```
1. mkdir new_project && cd new_project
2. sudo apt install python3-venv    # ONE TIME SYSTEM SETUP
3. python3 -m venv venv             # Creates ./venv/
4. source venv/bin/activate         # Prompt MUST show: (venv)
5. pip install --upgrade pip        # Always first
6. pip install your_packages_here   # Project-specific
7. python your_script.py            # Runs in isolation
8. deactivate                       # Exit when done
```


## VS Code Integration

```
9.  code .                           # Open project
10. Ctrl+Shift+P → "Python: Select Interpreter"
11. Choose: ./venv/bin/python        # Status bar MUST show this path
12. F5 to run/debug
```


## Verification Checklist (RUN THESE EXACTLY)

```bash
dpkg -l | grep python3-venv         # [OK] if installed
which python                        # MUST: .../new_project/venv/bin/python
pip list                            # Shows ONLY venv packages
```
