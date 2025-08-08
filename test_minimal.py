#!/usr/bin/env python3

# Minimal test to isolate the bus error
import sys
import os

if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

print("Testing basic imports...")

try:
    from tkinter import *
    print("✓ tkinter imported successfully")
except Exception as e:
    print(f"✗ tkinter import failed: {e}")
    sys.exit(1)

try:
    import customtkinter
    print("✓ customtkinter imported successfully")
except Exception as e:
    print(f"✗ customtkinter import failed: {e}")
    sys.exit(1)

try:
    from RuleBased import RuleBased
    print("✓ RuleBased imported successfully")
except Exception as e:
    print(f"✗ RuleBased import failed: {e}")
    sys.exit(1)

print("Creating minimal GUI...")

try:
    root = customtkinter.CTk()
    print("✓ CustomTkinter window created")
    
    root.title("Caselist Maker")
    root.geometry("600x600")
    print("✓ Window configured")
    
    # Add variables like main.py
    result_text = ""
    rule_algo = RuleBased("")
    print("✓ Variables created")
    
    # Add header frame like main.py
    header_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
    header_frame.pack(fill="x", padx=20, pady=10)
    print("✓ Header frame created")
    
    # Add settings function like main.py
    def open_settings():
        settings_window = customtkinter.CTkToplevel(root)
        settings_window.title("Settings")
        settings_window.geometry("500x600")
        settings_window.transient(root)
        settings_window.grab_set()
        print("Settings window opened")
    
    print("✓ Settings function created")
    
    # Add settings button like main.py
    settings_button = customtkinter.CTkButton(
        master=header_frame, 
        text="⚙️", 
        command=open_settings,
        width=40,
        height=30,
        font=customtkinter.CTkFont(size=16)
    )
    settings_button.pack(side="left")
    print("✓ Settings button created")
    
    # Add title label like main.py
    title_label = customtkinter.CTkLabel(
        master=header_frame, 
        text="Debate Disclosure Processor", 
        font=("Arial", 16, "bold")
    )
    title_label.pack(side="left", padx=(20, 0))
    print("✓ Title label created")
    
    # Add instruction label like main.py
    instruction_label = customtkinter.CTkLabel(master=root, text="Paste your disclosure text below:")
    instruction_label.pack(pady=5)
    print("✓ Instruction label created")
    
    # Test: Replace CTkTextbox with regular tkinter Text widget
    import tkinter as tk
    text_input = tk.Text(master=root, width=60, height=10)
    text_input.pack(pady=10)
    print("✓ Text input created (using tkinter Text)")
    
    # Add button frame like main.py
    button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
    button_frame.pack(pady=15)
    print("✓ Button frame created")
    
    # Add result display components like main.py
    result_label = customtkinter.CTkLabel(master=root, text="Results will appear here:")
    result_label.pack(pady=(20, 5))
    print("✓ Result label created")
    
    # Test: Also replace result display with regular tkinter Text
    result_display = tk.Text(master=root, width=60, height=6)
    result_display.pack(pady=5)
    print("✓ Result display created (using tkinter Text)")
    
    # Add processing functions like main.py
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
    
    # Add buttons like main.py
    rule_button = customtkinter.CTkButton(master=button_frame, text="Rule-based", command=run_rule_based)
    rule_button.pack(side=RIGHT, padx=5)
    print("✓ Rule button created")
    
    llm_button = customtkinter.CTkButton(master=button_frame, text="LLM-based", command=run_llm_based)
    llm_button.pack(side=LEFT, padx=5)
    print("✓ LLM button created")
    
    print("Starting mainloop...")
    root.mainloop()
    
except Exception as e:
    print(f"✗ GUI creation failed: {e}")
    import traceback
    traceback.print_exc()
