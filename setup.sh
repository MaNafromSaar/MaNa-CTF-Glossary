#!/bin/bash
# Quick setup script for the Cybersecurity Glossary

# Print colorful messages
print_green() {
  echo -e "\e[32m$1\e[0m"
}

print_blue() {
  echo -e "\e[34m$1\e[0m"
}

print_yellow() {
  echo -e "\e[33m$1\e[0m"
}

# Welcome message
print_blue "==============================================="
print_blue "   Cybersecurity Glossary - Quick Setup"
print_blue "==============================================="
print_blue ""

# Check for Python3
if ! command -v python3 &> /dev/null; then
  print_yellow "Python 3 is not installed. Please install it to use the glossary manager."
  exit 1
fi

# Check if we're in the right directory
if [ ! -f "glossary_data.json" ] || [ ! -f "glossary_manager.py" ]; then
  print_yellow "Please run this script from the glossary directory."
  exit 1
fi

# Make sure scripts are executable
chmod +x glossary.py
chmod +x glossary_manager.py
chmod +x add_entry.py

print_green "✅ Setup complete! You can now use the glossary with:"
print_green "   ./glossary.py"

print_blue ""
print_blue "Quick commands:"
print_blue "   ./glossary.py add    - Add a new entry"
print_blue "   ./glossary.py search - Search for terms"
print_blue "   ./glossary.py export - Generate HTML output"
print_blue ""
print_blue "   or run without arguments for interactive mode:"
print_blue "   ./glossary.py"
print_blue ""
print_blue "Open the HTML file to view the glossary:"
print_blue "   cybersecurity_glossary.html"
print_blue "==============================================="
