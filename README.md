# CaselistMaker

A Python tool for processing and extracting negative positions from debate team disclosures. This tool helps debate coaches and students organize and clean up caselist data by extracting individual positions from formatted disclosure text.

## Features

- **Rule-Based Processing**: Extracts negative positions from formatted disclosure text using regex patterns
- **Duplicate Removal**: Automatically removes duplicate positions while preserving original formatting
- **Text Cleaning**: Cleans up formatting issues like excessive dashes, colons, and spacing
- **Interactive Input**: Simple command-line interface for pasting disclosure data

## How It Works

The tool processes debate team disclosures by:
1. Taking multiline input of negative position disclosures
2. Parsing text between "1NC" and "2NR" markers
3. Extracting individual positions separated by commas
4. Cleaning up formatting inconsistencies
5. Removing duplicates and outputting unique positions

## Usage

### Current Rule-Based Version

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

## Upcoming Features

🚀 **Small Language Model Version Coming Soon!**

We're developing an enhanced version powered by a small language model that will provide:
- Improved text parsing and understanding
- Better handling of complex formatting variations
- Automatic categorization of position types
- Enhanced duplicate detection
- More intelligent text cleaning

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `re` module)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CODERTG2/CaselistMaker.git
   cd CaselistMaker
   ```

2. Run the script:
   ```bash
   python RuleBased.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
