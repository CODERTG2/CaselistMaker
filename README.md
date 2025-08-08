# CaselistMaker

A comprehensive Python application for processing and extracting negative positions from debate team disclosures. This tool helps debate coaches and students organize and clean up caselist data by extracting individual positions from formatted disclosure text.

## 📥 Download

Get started quickly with our ready-to-use installers:

| Platform | Download | Requirements |
|----------|----------|--------------|
| 🪟 **Windows** | [CaselistMaker-Setup-v1.0.0.exe](./installers/CaselistMaker-Setup-v1.0.0.exe) | Windows 10+ |
| 🍎 **macOS** | [CaselistMaker.dmg](./installers/CaselistMaker.dmg) | macOS 10.14+ |

*No Python installation required for the installers above.*

## Features

### Core Processing
- **Rule-Based Processing**: Extracts negative positions from formatted disclosure text using regex patterns
- **LLM-Based Processing**: Advanced AI-powered processing using Ollama and Llama 3.2 for improved accuracy
- **Dual Processing Options**: Choose between fast rule-based or intelligent LLM processing
- **Duplicate Removal**: Automatically removes duplicate positions while preserving original formatting
- **Text Cleaning**: Cleans up formatting issues like excessive dashes, colons, and spacing

### User Interface
- **Modern GUI Application**: User-friendly PyQt5-based graphical interface
- **Interactive Input**: Easy-to-use text input area for pasting disclosure data
- **Real-time Processing**: Visual feedback during processing with status updates
- **Copy to Clipboard**: One-click copying of processed results
- **Settings Panel**: Customizable processing options and LLM prompt configuration

### Installation & Distribution
- **Cross-Platform Installers**: Ready-to-use installers for Windows and macOS
- **Standalone Application**: No need for Python installation on end-user machines
- **Automatic Ollama Integration**: Guided setup for LLM capabilities
- **Background Model Management**: Automatic model downloading and management

## How It Works

The tool processes debate team disclosures through two methods:

### Rule-Based Processing
1. Takes multiline input of negative position disclosures
2. Parses text between "1NC" and "2NR" markers using regex patterns
3. Extracts individual positions separated by commas
4. Cleans up formatting inconsistencies
5. Removes duplicates and outputs unique positions

### LLM-Based Processing
1. Uses Ollama with Llama 3.2 model for intelligent text analysis
2. Automatically identifies 1NC, 2NC, 1NR, and 2NR arguments
3. Applies advanced natural language processing for better accuracy
4. Handles complex formatting variations and context understanding
5. Provides more reliable duplicate detection and categorization

## Usage

### GUI Application (Recommended)

1. Launch the CaselistMaker application:
   - **From installer**: Use desktop shortcut or start menu
   - **From source**: Run `python main.py`

2. Application workflow:
   - Copy negative positions from the wiki
   - Paste disclosure text into the input area
   - Choose processing method:
     - **Rule-based**: Fast, regex-based processing
     - **LLM-based**: AI-powered processing (requires Ollama)
   - Click "Copy Result" to copy processed positions to clipboard

3. **LLM Setup** (for AI processing):
   - The app will prompt to install Ollama if not detected
   - Ollama enables advanced AI-powered text processing
   - Models are downloaded automatically in the background

### Command-Line Version (Legacy)

1. Run the script:
   ```bash
   python RuleBased.py
   ```

2. Follow the workflow:
   - Copy negative positions from the wiki
   - Paste into a Google Sheet (remove any unwanted rows)
   - Copy the specific column or round report from sheets
   - Paste into the terminal when prompted
   - Press Enter twice to process
   - Individual positions will be printed

### Example Input Format
```
1NC Topicality, Disadvantage A, Counterplan B, Kritik C 2NR
```

### Example Output
```
Topicality
Disadvantage A
Counterplan B
Kritik C
```

## Technical Details

### Architecture
- **GUI Framework**: PyQt5 for cross-platform desktop application
- **Processing Engine**: Dual-mode processing (Rule-based + LLM)
- **AI Integration**: Ollama with Llama 3.2 model
- **Packaging**: PyInstaller for standalone executables

### Building from Source
The project includes build configurations for creating installers:
- **Windows**: Inno Setup script (`installer.iss`)
- **macOS**: DMG packaging
- **Cross-platform**: PyInstaller spec file (`main.spec`)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Install development dependencies: `pip install PyQt5 pyinstaller`
3. Make your changes
4. Test with both processing methods
5. Submit a pull request

## License

This project is open source and available under the MIT License.
