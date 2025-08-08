import sys
import os

if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

import tkinter as tk
from tkinter import ttk
from RuleBased import RuleBased

# Create main window
root = tk.Tk()
root.title("Caselist Maker")
root.geometry("600x600")

# Global variables
result_text = ""
rule_algo = RuleBased("")

# Header frame
header_frame = tk.Frame(root)
header_frame.pack(fill="x", padx=20, pady=10)

# Settings function
def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("500x400")
    settings_window.transient(root)
    settings_window.grab_set()
    
    # Center the window
    settings_window.update_idletasks()
    x = (settings_window.winfo_screenwidth() // 2) - (500 // 2)
    y = (settings_window.winfo_screenheight() // 2) - (400 // 2)
    settings_window.geometry(f"500x400+{x}+{y}")
    
    # Settings title
    settings_title = tk.Label(settings_window, text="Configuration Settings", font=("Arial", 18, "bold"))
    settings_title.pack(pady=20)
    
    # Regex section
    regex_frame = tk.LabelFrame(settings_window, text="Rule-Based Regex Pattern", font=("Arial", 12, "bold"))
    regex_frame.pack(fill="x", padx=20, pady=10)
    
    regex_entry = tk.Entry(regex_frame, width=60)
    regex_entry.pack(padx=10, pady=10)
    regex_entry.insert(0, rule_algo.regex_pattern)
    
    def save_regex():
        rule_algo.regex_pattern = regex_entry.get()
        save_regex_btn.config(text="Saved!")
        settings_window.after(2000, lambda: save_regex_btn.config(text="Save Regex"))
    
    save_regex_btn = tk.Button(regex_frame, text="Save Regex", command=save_regex)
    save_regex_btn.pack(pady=5)

# Settings button
settings_button = tk.Button(header_frame, text="⚙️", command=open_settings, width=3, font=("Arial", 14))
settings_button.pack(side="left")

# Title
title_label = tk.Label(header_frame, text="Debate Disclosure Processor", font=("Arial", 16, "bold"))
title_label.pack(side="left", padx=(20, 0))

# Instructions
instruction_label = tk.Label(root, text="Paste your disclosure text below:", font=("Arial", 12))
instruction_label.pack(pady=5)

# Text input
text_input = tk.Text(root, width=70, height=12, wrap=tk.WORD)
text_input.pack(pady=10, padx=20)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Result section
result_label = tk.Label(root, text="Results will appear here:", font=("Arial", 12, "bold"))
result_label.pack(pady=(20, 5))

result_display = tk.Text(root, width=70, height=8, wrap=tk.WORD)
result_display.pack(pady=5, padx=20)

# Processing functions
def run_rule_based():
    global rule_algo, result_text
    text = text_input.get("1.0", "end-1c")
    if not text.strip():
        result_display.delete("1.0", "end")
        result_display.insert("1.0", "Please enter some text.")
        return
    
    try:
        rule_algo.disclosure = text
        result_text = rule_algo.process()
        result_display.delete("1.0", "end")
        result_display.insert("1.0", result_text)
    except Exception as e:
        result_display.delete("1.0", "end")
        result_display.insert("1.0", f"Error: {str(e)}")

def run_llm_based():
    result_display.delete("1.0", "end")
    result_display.insert("1.0", "LLM functionality temporarily disabled")

# Buttons
rule_button = tk.Button(button_frame, text="Rule-based Processing", command=run_rule_based, 
                       bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5)
rule_button.pack(side="right", padx=5)

llm_button = tk.Button(button_frame, text="LLM-based Processing", command=run_llm_based,
                      bg="#2196F3", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5)
llm_button.pack(side="left", padx=5)

# Copy functionality
def copy_result():
    global result_text
    if result_text:
        root.clipboard_clear()
        root.clipboard_append(result_text)
        copy_button.config(text="Copied!")
        root.after(2000, lambda: copy_button.config(text="Copy Result"))
    else:
        copy_button.config(text="No results to copy")
        root.after(2000, lambda: copy_button.config(text="Copy Result"))

copy_button = tk.Button(root, text="Copy Result", command=copy_result, 
                       bg="#FF9800", fg="white", font=("Arial", 10, "bold"), pady=3)
copy_button.pack(pady=10)

# Status bar
status_label = tk.Label(root, text="Ready to process disclosure text", 
                       relief=tk.SUNKEN, anchor="w", font=("Arial", 9))
status_label.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root.mainloop()
