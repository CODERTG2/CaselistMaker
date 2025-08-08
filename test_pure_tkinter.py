#!/usr/bin/env python3

# Test with pure tkinter to isolate CustomTkinter issues
import sys
import os

if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

print("Testing with pure tkinter...")

try:
    import tkinter as tk
    from tkinter import ttk
    print("✓ tkinter imported successfully")
except Exception as e:
    print(f"✗ tkinter import failed: {e}")
    sys.exit(1)

try:
    from RuleBased import RuleBased
    print("✓ RuleBased imported successfully")
except Exception as e:
    print(f"✗ RuleBased import failed: {e}")
    sys.exit(1)

print("Creating pure tkinter GUI...")

try:
    root = tk.Tk()
    print("✓ Tkinter window created")
    
    root.title("Caselist Maker")
    root.geometry("600x600")
    print("✓ Window configured")
    
    # Add variables
    result_text = ""
    rule_algo = RuleBased("")
    print("✓ Variables created")
    
    # Add header frame
    header_frame = tk.Frame(root)
    header_frame.pack(fill="x", padx=20, pady=10)
    print("✓ Header frame created")
    
    # Add settings function
    def open_settings():
        settings_window = tk.Toplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("500x600")
        settings_window.transient(root)
        settings_window.grab_set()
        print("Settings window opened")
    
    print("✓ Settings function created")
    
    # Add settings button
    settings_button = tk.Button(header_frame, text="⚙️", command=open_settings, width=3)
    settings_button.pack(side="left")
    print("✓ Settings button created")
    
    # Add title label
    title_label = tk.Label(header_frame, text="Debate Disclosure Processor", font=("Arial", 16, "bold"))
    title_label.pack(side="left", padx=(20, 0))
    print("✓ Title label created")
    
    # Add instruction label
    instruction_label = tk.Label(root, text="Paste your disclosure text below:")
    instruction_label.pack(pady=5)
    print("✓ Instruction label created")
    
    # Add text input
    text_input = tk.Text(root, width=60, height=10)
    text_input.pack(pady=10)
    print("✓ Text input created")
    
    # Add button frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=15)
    print("✓ Button frame created")
    
    # Add result display components
    result_label = tk.Label(root, text="Results will appear here:")
    result_label.pack(pady=(20, 5))
    print("✓ Result label created")
    
    result_display = tk.Text(root, width=60, height=6)
    result_display.pack(pady=5)
    print("✓ Result display created")
    
    # Add processing functions
    def run_rule_based():
        global rule_algo, result_text
        text = text_input.get("1.0", "end-1c")
        if not text.strip():
            result_display.delete("1.0", "end")
            result_display.insert("1.0", "Please enter some text.")
            return
        
        rule_algo.disclosure = text
        result_text = rule_algo.process()
        result_display.delete("1.0", "end")
        result_display.insert("1.0", result_text)
        print("Rule-based processing completed")
    
    def run_llm_based():
        result_display.delete("1.0", "end")
        result_display.insert("1.0", "LLM functionality temporarily disabled")
        print("LLM button clicked")
    
    print("✓ Processing functions created")
    
    # Add buttons
    rule_button = tk.Button(button_frame, text="Rule-based", command=run_rule_based)
    rule_button.pack(side="right", padx=5)
    print("✓ Rule button created")
    
    llm_button = tk.Button(button_frame, text="LLM-based", command=run_llm_based)
    llm_button.pack(side="left", padx=5)
    print("✓ LLM button created")
    
    # Add copy function
    def copy_result():
        global result_text
        if result_text:
            root.clipboard_clear()
            root.clipboard_append(result_text)
            print("Result copied to clipboard")
        else:
            print("No results to copy")
    
    copy_button = tk.Button(root, text="Copy Result", command=copy_result)
    copy_button.pack(pady=10)
    print("✓ Copy button created")
    
    print("Starting mainloop...")
    root.mainloop()
    print("✓ Mainloop completed normally")
    
except Exception as e:
    print(f"✗ GUI creation failed: {e}")
    import traceback
    traceback.print_exc()
