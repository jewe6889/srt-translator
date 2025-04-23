# SRT Translator

A simple tool to translate subtitle files (.srt) into different languages using GoogleTranslator.

## Features

- Translate SRT subtitle files to any supported language
- Preserves subtitle timing and formatting
- Easy command-line interface
- Supports all major operating systems (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- Required Python packages (automatically installed with the setup instructions below):
  - deep-translator
  - pysrt

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/srt-translator.git
cd srt-translator
```

### 2. Create a virtual environment (recommended)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python translate_srt.py input_file.srt -l target_language
```

- `input_file.srt`: Path to the SRT file you want to translate
- `-l target_language`: Target language code (e.g., "es" for Spanish, "fr" for French)

### Examples

Translate subtitles to Spanish:
```bash
python translate_srt.py doja.srt -l es
```

Translate subtitles to French and specify output file:
```bash
python translate_srt.py doja.srt -l fr -o doja_french.srt
```

### Platform-Specific Instructions

#### Windows
```
python translate_srt.py path\to\subtitles.srt -l es
```

#### macOS/Linux
```
python3 translate_srt.py path/to/subtitles.srt -l es
```

Or make the script executable first:
```
chmod +x translate_srt.py
./translate_srt.py path/to/subtitles.srt -l es
```

## Supported Languages

The translator supports over 100 languages. Some common language codes:

- English: `en`
- Spanish: `es`
- French: `fr`
- German: `de`
- Italian: `it`
- Japanese: `ja`
- Korean: `ko`
- Chinese (Simplified): `zh-CN`
- Russian: `ru`

For a full list of supported languages and their codes, check the [Google Translate supported languages](https://cloud.google.com/translate/docs/languages).