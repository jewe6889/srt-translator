#!/usr/bin/env python3
import argparse
import re
import os
import sys
from deep_translator import GoogleTranslator
import pysrt

def translate_srt(input_file, output_file, target_language):
    """
    Translate SRT file to the target language.
    
    Args:
        input_file (str): Path to the input SRT file
        output_file (str): Path to save the translated SRT file
        target_language (str): Target language code (e.g., 'es' for Spanish)
    """
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
        
    # Check if file is srt
    if not input_file.lower().endswith('.srt'):
        print(f"Error: Input file '{input_file}' is not an SRT file.")
        sys.exit(1)
    
    # Initialize translator
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
    except Exception as e:
        print(f"Error initializing translator: {e}")
        print("Check if the language code is valid.")
        sys.exit(1)
    
    try:
        # Load the SRT file
        subs = pysrt.open(input_file)
        
        # Translate each subtitle
        for sub in subs:
            # Preserve timing tags and only translate text content
            sub.text = translator.translate(sub.text)
        
        # Save the translated file
        subs.save(output_file, encoding='utf-8')
        
        print(f"Translation completed. Saved to {output_file}")
        
    except Exception as e:
        print(f"Error during translation: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Translate SRT subtitle files to different languages.')
    parser.add_argument('input_file', help='Path to the input SRT file')
    parser.add_argument('-l', '--language', required=True, help='Target language code (e.g., "es" for Spanish)')
    parser.add_argument('-o', '--output', help='Path to save the translated SRT file')
    
    args = parser.parse_args()
    
    # If output file is not specified, create one in the same directory
    if not args.output:
        base_name = os.path.splitext(os.path.basename(args.input_file))[0]
        output_dir = os.path.dirname(args.input_file)
        args.output = os.path.join(output_dir, f"{base_name}_{args.language}.srt")
    
    translate_srt(args.input_file, args.output, args.language)

if __name__ == "__main__":
    main()