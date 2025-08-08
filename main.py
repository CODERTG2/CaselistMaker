import sys
import os

if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'

from tkinter import *
import customtkinter
# import subprocess
from RuleBased import RuleBased
# from LLMBased import LLMBased
# import threading

# def ollama_pull():
#     try:
#         subprocess.run(["ollama", "pull", "llama3.2"], check=True)
    
#     except subprocess.CalledProcessError as e:
#         print(f"Command failed with exit code {e.returncode}")
#         print(f"Error output: {e.stderr}")

root = customtkinter.CTk()
root.title("Caselist Maker")
root.geometry("600x600")

result_text = ""

rule_algo = RuleBased("")
# llm_algo = LLMBased("")

header_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
header_frame.pack(fill="x", padx=20, pady=10)

def open_settings():
    settings_window = customtkinter.CTkToplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("500x600")
    settings_window.transient(root)
    settings_window.grab_set()
    
    settings_window.update_idletasks()
    x = (settings_window.winfo_screenwidth() // 2) - (500 // 2)
    y = (settings_window.winfo_screenheight() // 2) - (600 // 2)
    settings_window.geometry(f"500x600+{x}+{y}")
    
    settings_title = customtkinter.CTkLabel(
        master=settings_window, 
        text="Configuration Settings", 
        font=customtkinter.CTkFont(size=18, weight="bold")
    )
    settings_title.pack(pady=20)

    def save_regex_pattern(pattern):
        rule_algo.regex_pattern = pattern
        regex_save_button.configure(text="Saved!")
        settings_window.after(2000, lambda: regex_save_button.configure(text="Save Regex"))
    
    # def save_llm_prompt(prompt):
    #     llm_algo.prompt = prompt
    #     prompt_save_button.configure(text="Saved!")
    #     settings_window.after(2000, lambda: prompt_save_button.configure(text="Save Prompt"))
    
    regex_frame = customtkinter.CTkFrame(master=settings_window)
    regex_frame.pack(fill="x", padx=20, pady=10)
    
    regex_label = customtkinter.CTkLabel(
        master=regex_frame, 
        text="Rule-Based Regex Pattern:", 
        font=customtkinter.CTkFont(size=14, weight="bold")
    )
    regex_label.pack(anchor="w", padx=10, pady=(10, 5))
    
    regex_entry = customtkinter.CTkEntry(master=regex_frame, width=450)
    regex_entry.pack(padx=10, pady=(0, 5))
    regex_entry.insert(0, rule_algo.regex_pattern)
    
    regex_save_button = customtkinter.CTkButton(
        master=regex_frame, 
        text="Save Regex", 
        command=lambda: save_regex_pattern(regex_entry.get()),
        width=100
    )
    regex_save_button.pack(padx=10, pady=(0, 10))
    
    # # LLM Prompt Section
    # prompt_frame = customtkinter.CTkFrame(master=settings_window)
    # prompt_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # prompt_label = customtkinter.CTkLabel(
    #     master=prompt_frame, 
    #     text="LLM Prompt Template:", 
    #     font=customtkinter.CTkFont(size=14, weight="bold")
    # )
    # prompt_label.pack(anchor="w", padx=10, pady=(10, 5))
    
    # prompt_textbox = customtkinter.CTkTextbox(master=prompt_frame, width=450, height=150)
    # prompt_textbox.pack(padx=10, pady=(0, 5), fill="both", expand=True)
    # prompt_textbox.insert("1.0", llm_algo.prompt)
    
    # prompt_save_button = customtkinter.CTkButton(
    #     master=prompt_frame, 
    #     text="Save Prompt", 
    #     command=lambda: save_llm_prompt(prompt_textbox.get("1.0", "end-1c")),
    #     width=100
    # )
    # prompt_save_button.pack(padx=10, pady=(0, 10))

settings_button = customtkinter.CTkButton(
    master=header_frame, 
    text="⚙️", 
    command=open_settings,
    width=40,
    height=30,
    font=customtkinter.CTkFont(size=16)
)
settings_button.pack(side="left")

title_label = customtkinter.CTkLabel(
    master=header_frame, 
    text="Debate Disclosure Processor", 
    font=("Arial", 16, "bold")
)
title_label.pack(side="left", padx=(20, 0))

instruction_label = customtkinter.CTkLabel(master=root, text="Paste your disclosure text below:")
instruction_label.pack(pady=5)

text_input = customtkinter.CTkTextbox(master=root, width=450, height=150)
text_input.pack(pady=10)

button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(pady=15)

result_label = customtkinter.CTkLabel(master=root, text="Results will appear here:")
result_label.pack(pady=(20, 5))

result_display = customtkinter.CTkTextbox(master=root, width=450, height=100)
result_display.pack(pady=5)

def run_rule_based():
    print("running")
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
        

def run_llm_based():
    # global llm_algo, result_text
    # text = text_input.get("1.0", "end-1c")
    # if not text.strip():
    #     result_display.delete("1.0", "end")
    #     result_display.insert("1.0", "Please enter some text.")
    #     return

    result_display.delete("1.0", "end")
    result_display.insert("1.0", "LLM functionality temporarily disabled")
    
    # llm_algo.disclosure = text
    # result_text = llm_algo.process()
    # result_display.delete("1.0", "end")
    # result_display.insert("1.0", result_text)

rule_button = customtkinter.CTkButton(master=button_frame, text="Rule-based", command=run_rule_based)
rule_button.pack(side=RIGHT, padx=5)
llm_button = customtkinter.CTkButton(master=button_frame, text="LLM-based", command=run_llm_based)
llm_button.pack(side=LEFT, padx=5)

def copy_result():
    global result_text
    if result_text:
        root.clipboard_clear()
        root.clipboard_append(result_text)
        copy_button.configure(text="Copied!")
        root.after(2000, lambda: copy_button.configure(text="Copy Result"))
    else:
        copy_button.configure(text="No results to copy")
        root.after(2000, lambda: copy_button.configure(text="Copy Result"))

copy_button = customtkinter.CTkButton(master=root, text="Copy Result", command=copy_result, width=120)
copy_button.pack(pady=10)

# def start_ollama_thread():
#     threading.Thread(target=ollama_pull, daemon=True).start()

# root.after(2000, threading.Thread(target=ollama_pull).start())

if __name__ == "__main__":
    root.mainloop()