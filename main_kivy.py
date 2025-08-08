#!/usr/bin/env python3

import sys
import os

# Kivy imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard

# Import our processing classes
from RuleBased import RuleBased

class CaselistApp(App):
    def __init__(self):
        super().__init__()
        self.rule_algo = RuleBased("")
        self.result_text = ""
        
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header with settings and title
        header_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        
        # Settings button
        settings_btn = Button(text='⚙️', size_hint_x=None, width=50, 
                             background_color=[0.8, 0.8, 0.8, 1])
        settings_btn.bind(on_press=self.open_settings)
        header_layout.add_widget(settings_btn)
        
        # Title
        title_label = Label(text='Debate Disclosure Processor', 
                           font_size=20, bold=True, color=[0, 0, 0, 1])
        header_layout.add_widget(title_label)
        
        main_layout.add_widget(header_layout)
        
        # Instructions
        instruction_label = Label(text='Paste your disclosure text below:', 
                                 size_hint_y=None, height=30, color=[0, 0, 0, 1])
        main_layout.add_widget(instruction_label)
        
        # Text input
        self.text_input = TextInput(multiline=True, size_hint_y=0.4,
                                   background_color=[1, 1, 1, 1],
                                   foreground_color=[0, 0, 0, 1])
        main_layout.add_widget(self.text_input)
        
        # Buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=20)
        
        rule_btn = Button(text='Rule-based Processing', 
                         background_color=[0.3, 0.7, 0.3, 1])
        rule_btn.bind(on_press=self.run_rule_based)
        button_layout.add_widget(rule_btn)
        
        llm_btn = Button(text='LLM-based Processing', 
                        background_color=[0.2, 0.6, 0.9, 1])
        llm_btn.bind(on_press=self.run_llm_based)
        button_layout.add_widget(llm_btn)
        
        main_layout.add_widget(button_layout)
        
        # Results label
        result_label = Label(text='Results will appear here:', 
                           size_hint_y=None, height=30, 
                           bold=True, color=[0, 0, 0, 1])
        main_layout.add_widget(result_label)
        
        # Result display
        self.result_display = TextInput(multiline=True, readonly=True, size_hint_y=0.3,
                                       background_color=[0.95, 0.95, 0.95, 1],
                                       foreground_color=[0, 0, 0, 1])
        main_layout.add_widget(self.result_display)
        
        # Copy button
        self.copy_btn = Button(text='Copy Result', size_hint_y=None, height=40,
                              background_color=[1, 0.6, 0, 1])
        self.copy_btn.bind(on_press=self.copy_result)
        main_layout.add_widget(self.copy_btn)
        
        # Status bar
        self.status_label = Label(text='Ready to process disclosure text', 
                                 size_hint_y=None, height=30, color=[0.5, 0.5, 0.5, 1])
        main_layout.add_widget(self.status_label)
        
        return main_layout
    
    def open_settings(self, instance):
        # Create settings popup
        content = BoxLayout(orientation='vertical', spacing=10)
        
        # Title
        title = Label(text='Configuration Settings', font_size=18, bold=True,
                     size_hint_y=None, height=40, color=[0, 0, 0, 1])
        content.add_widget(title)
        
        # Regex section
        regex_label = Label(text='Rule-Based Regex Pattern:', 
                           size_hint_y=None, height=30, color=[0, 0, 0, 1])
        content.add_widget(regex_label)
        
        self.regex_input = TextInput(text=self.rule_algo.regex_pattern, 
                                    multiline=False, size_hint_y=None, height=40,
                                    background_color=[1, 1, 1, 1],
                                    foreground_color=[0, 0, 0, 1])
        content.add_widget(self.regex_input)
        
        # Buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        save_btn = Button(text='Save Regex', background_color=[0.3, 0.7, 0.3, 1])
        save_btn.bind(on_press=self.save_regex)
        button_layout.add_widget(save_btn)
        
        close_btn = Button(text='Close', background_color=[0.7, 0.3, 0.3, 1])
        button_layout.add_widget(close_btn)
        
        content.add_widget(button_layout)
        
        # Create popup
        self.settings_popup = Popup(title='Settings', content=content, 
                                   size_hint=(0.8, 0.6))
        close_btn.bind(on_press=self.settings_popup.dismiss)
        
        self.settings_popup.open()
    
    def save_regex(self, instance):
        self.rule_algo.regex_pattern = self.regex_input.text
        self.status_label.text = 'Regex pattern saved!'
        Clock.schedule_once(self.reset_status, 2)
    
    def reset_status(self, dt):
        self.status_label.text = 'Ready to process disclosure text'
    
    def run_rule_based(self, instance):
        text = self.text_input.text.strip()
        if not text:
            self.result_display.text = "Please enter some text."
            return
        
        try:
            self.rule_algo.disclosure = text
            self.result_text = self.rule_algo.process()
            self.result_display.text = self.result_text
            self.status_label.text = 'Rule-based processing completed!'
            Clock.schedule_once(self.reset_status, 3)
        except Exception as e:
            self.result_display.text = f"Error: {str(e)}"
            self.status_label.text = 'Processing failed!'
            Clock.schedule_once(self.reset_status, 3)
    
    def run_llm_based(self, instance):
        self.result_display.text = "LLM functionality temporarily disabled"
        self.status_label.text = 'LLM processing not available'
        Clock.schedule_once(self.reset_status, 3)
    
    def copy_result(self, instance):
        if self.result_text:
            Clipboard.copy(self.result_text)
            self.copy_btn.text = 'Copied!'
            self.status_label.text = 'Result copied to clipboard!'
            Clock.schedule_once(self.reset_copy_button, 2)
            Clock.schedule_once(self.reset_status, 3)
        else:
            self.copy_btn.text = 'No results to copy'
            Clock.schedule_once(self.reset_copy_button, 2)
    
    def reset_copy_button(self, dt):
        self.copy_btn.text = 'Copy Result'

if __name__ == '__main__':
    CaselistApp().run()
