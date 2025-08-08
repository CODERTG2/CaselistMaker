#!/usr/bin/env python3

# Absolute minimal tkinter test
import sys
import os

if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

print("Minimal tkinter test...")

try:
    import tkinter as tk
    print("✓ tkinter imported")
    
    root = tk.Tk()
    print("✓ window created")
    
    root.title("Test")
    root.geometry("300x200")
    print("✓ window configured")
    
    label = tk.Label(root, text="Hello World")
    label.pack()
    print("✓ label created")
    
    # Try without mainloop first
    root.update()
    print("✓ update() works")
    
    # Try very short mainloop
    root.after(1000, root.quit)  # Quit after 1 second
    print("✓ Starting 1-second mainloop...")
    
    root.mainloop()
    print("✓ Mainloop completed")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
