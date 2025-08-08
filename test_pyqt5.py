#!/usr/bin/env python3

import sys
import os

# macOS compatibility fixes
if sys.platform == "darwin":
    os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = ''

try:
    from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
    from PyQt5.QtCore import QTimer
    
    print("✓ PyQt5 imported successfully")
    
    app = QApplication(sys.argv)
    print("✓ QApplication created")
    
    window = QMainWindow()
    window.setWindowTitle("Test")
    window.setGeometry(100, 100, 300, 200)
    
    label = QLabel("PyQt5 Test Success!", window)
    label.move(50, 50)
    
    print("✓ Window created")
    
    window.show()
    print("✓ Window shown")
    
    # Auto-close after 2 seconds
    QTimer.singleShot(2000, app.quit)
    
    print("✓ Starting event loop...")
    app.exec_()
    print("✓ Event loop completed successfully!")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
