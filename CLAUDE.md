# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI training dummy data repository that provides various dummy datasets for AI training and education purposes. The repository contains Excel/CSV data, text files, and a data generation script in Python.

## Common Commands

### Data Generation
```bash
# Activate virtual environment (if exists)
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows

# Generate all dummy data
python generate_dummy_data.py
```

### Python Dependencies
The data generation script requires:
- pandas
- numpy
- openpyxl
- faker

Install with: `pip install pandas numpy openpyxl faker`

## Repository Structure

```
/
├── data/                 # Main data storage directory
│   ├── excel/           # Excel/CSV files (student scores, sales data)
│   └── text/            # Text files (meeting transcripts)
├── assets/              # Website assets for GitHub Pages
├── guides/              # User guides and documentation
├── _data/               # Metadata storage
│   └── metadata.json    # Detailed information about datasets
├── generate_dummy_data.py  # Python script to generate dummy data
└── venv/                # Python virtual environment (if created)
```

## Key Data Files

### Excel/CSV Data
1. **student_scores.xlsx/csv**: 12,000 records of student test scores across 5 subjects
2. **sales_data.xlsx/csv**: 5,000 records of product purchase history

### Text Data
- **meeting_transcript_*.txt**: Meeting transcriptions for NLP tasks

### Metadata
- **_data/metadata.json**: Contains detailed information about each dataset including columns, row counts, file formats, and tags

## Architecture Notes

- The project is designed to be hosted on GitHub Pages for easy distribution
- Data is generated using Python with Faker library for realistic Japanese names
- All data is completely fictional and safe for training purposes
- The repository supports both Excel and CSV formats for wider compatibility