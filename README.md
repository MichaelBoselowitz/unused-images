# Unused Image Cleaner

This is a python app to clean up unused image assets in a web codebase.

## How it works

It recursively parses the current working directory and will delete any files that are not mentioned in any files in the directories listed in the ```PATHS_TO_CHECK``` variable.

## Dependencies

- python @2.7.6
- sh @1.09
- grep @2.5.1-FreeBSD

## Installation

Place the script alongside the files to scan. Set the ```PATHS_TO_CHECK``` variable appropriately.

## Running

```python unused_images.py```
