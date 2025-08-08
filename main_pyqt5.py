#!/usr/bin/env python3

import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QTextEdit, QPushButton, QDialog, 
                             QLineEdit, QFrame, QMessageBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QClipboard

from RuleBased import RuleBased

class SettingsDialog(QDialog):
    def __init__(self, parent, rule_algo):
        super().__init__(parent)
        self.rule_algo = rule_algo
        self.setWindowTitle("Settings")
        self.setFixedSize(500, 300)
        self.setModal(True)
        
        # Center the dialog
        parent_geo = parent.geometry()
        x = parent_geo.x() + (parent_geo.width() - 500) // 2
        y = parent_geo.y() + (parent_geo.height() - 300) // 2
        self.move(x, y)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Configuration Settings")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Regex section
        regex_label = QLabel("Rule-Based Regex Pattern:")
        regex_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(regex_label)
        
        self.regex_entry = QLineEdit()
        self.regex_entry.setText(self.rule_algo.regex_pattern)
        self.regex_entry.setStyleSheet("padding: 8px; font-size: 12px;")
        layout.addWidget(self.regex_entry)
        
        # Save button
        self.save_button = QPushButton("Save Regex")
        self.save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.save_button.clicked.connect(self.save_regex)
        layout.addWidget(self.save_button)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)
    
    def save_regex(self):
        self.rule_algo.regex_pattern = self.regex_entry.text()
        self.save_button.setText("Saved!")
        QTimer.singleShot(2000, lambda: self.save_button.setText("Save Regex"))

class CaselistMaker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rule_algo = RuleBased("")
        self.result_text = ""
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Caselist Maker - Debate Disclosure Processor")
        self.setGeometry(100, 100, 700, 700)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header_layout = QHBoxLayout()
        
        # Settings button
        self.settings_button = QPushButton("⚙️")
        self.settings_button.setFixedSize(40, 40)
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                border: 1px solid #ccc;
                border-radius: 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)
        self.settings_button.clicked.connect(self.open_settings)
        header_layout.addWidget(self.settings_button)
        
        # Title
        title_label = QLabel("Debate Disclosure Processor")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        main_layout.addLayout(header_layout)
        
        # Instructions
        instruction_label = QLabel("Paste your disclosure text below:")
        instruction_label.setFont(QFont("Arial", 12))
        main_layout.addWidget(instruction_label)
        
        # Text input
        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(200)
        self.text_input.setStyleSheet("""
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 4px;
                padding: 8px;
                font-size: 12px;
            }
            QTextEdit:focus {
                border-color: #4CAF50;
            }
        """)
        main_layout.addWidget(self.text_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.rule_button = QPushButton("Rule-based Processing")
        self.rule_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 12px 24px;
                font-weight: bold;
                border-radius: 4px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.rule_button.clicked.connect(self.run_rule_based)
        button_layout.addWidget(self.rule_button)
        
        self.llm_button = QPushButton("LLM-based Processing")
        self.llm_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 12px 24px;
                font-weight: bold;
                border-radius: 4px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        self.llm_button.clicked.connect(self.run_llm_based)
        button_layout.addWidget(self.llm_button)
        
        main_layout.addLayout(button_layout)
        
        # Results section
        result_label = QLabel("Results will appear here:")
        result_label.setFont(QFont("Arial", 12, QFont.Bold))
        main_layout.addWidget(result_label)
        
        self.result_display = QTextEdit()
        self.result_display.setMaximumHeight(150)
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("""
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 4px;
                padding: 8px;
                font-size: 12px;
                background-color: #f9f9f9;
            }
        """)
        main_layout.addWidget(self.result_display)
        
        # Copy button
        self.copy_button = QPushButton("Copy Result")
        self.copy_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                padding: 8px 16px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #e68900;
            }
        """)
        self.copy_button.clicked.connect(self.copy_result)
        main_layout.addWidget(self.copy_button)
        
        # Status bar
        self.status_label = QLabel("Ready to process disclosure text")
        self.status_label.setStyleSheet("""
            QLabel {
                color: #666;
                font-size: 10px;
                padding: 5px;
                border-top: 1px solid #ddd;
            }
        """)
        main_layout.addWidget(self.status_label)
        
        central_widget.setLayout(main_layout)
    
    def open_settings(self):
        dialog = SettingsDialog(self, self.rule_algo)
        dialog.exec_()
    
    def run_rule_based(self):
        text = self.text_input.toPlainText().strip()
        if not text:
            self.result_display.setText("Please enter some text.")
            return
        
        try:
            self.rule_algo.disclosure = text
            self.result_text = self.rule_algo.process()
            self.result_display.setText(self.result_text)
            self.status_label.setText("Rule-based processing completed!")
            QTimer.singleShot(3000, lambda: self.status_label.setText("Ready to process disclosure text"))
        except Exception as e:
            self.result_display.setText(f"Error: {str(e)}")
            self.status_label.setText("Processing failed!")
            QTimer.singleShot(3000, lambda: self.status_label.setText("Ready to process disclosure text"))
    
    def run_llm_based(self):
        self.result_display.setText("LLM functionality temporarily disabled")
        self.status_label.setText("LLM processing not available")
        QTimer.singleShot(3000, lambda: self.status_label.setText("Ready to process disclosure text"))
    
    def copy_result(self):
        if self.result_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(self.result_text)
            self.copy_button.setText("Copied!")
            self.status_label.setText("Result copied to clipboard!")
            QTimer.singleShot(2000, lambda: self.copy_button.setText("Copy Result"))
            QTimer.singleShot(3000, lambda: self.status_label.setText("Ready to process disclosure text"))
        else:
            self.copy_button.setText("No results to copy")
            QTimer.singleShot(2000, lambda: self.copy_button.setText("Copy Result"))

def main():
    # macOS compatibility
    if sys.platform == "darwin":
        os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look
    
    # Set application-wide stylesheet for a modern look
    app.setStyleSheet("""
        QMainWindow {
            background-color: #f5f5f5;
        }
        QLabel {
            color: #333;
        }
    """)
    
    window = CaselistMaker()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
