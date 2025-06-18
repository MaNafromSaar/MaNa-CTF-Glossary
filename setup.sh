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
if [ ! -f "glossary_data.json" ] || [ ! -f "cybersecurity_glossary.html" ]; then
  print_yellow "Please run this script from the glossary directory."
  exit 1
fi

# Make sure scripts are executable
chmod +x glossary.py 2>/dev/null
chmod +x glossary_manager.py 2>/dev/null
chmod +x add_entry.py 2>/dev/null

print_green "✅ Setup complete!"
print_blue ""
print_blue "To launch the dynamic HTML glossary, run:"
print_blue "   python3 -m http.server 8080"
print_blue "Then open: http://localhost:8080/cybersecurity_glossary.html"
print_blue ""

# Offer to start the server and open the browser
echo -n "Start webserver and open glossary in browser now? [Y/n]: "
read answer
if [[ "$answer" =~ ^[Nn] ]]; then
  print_blue "You can start the server manually anytime with: python3 -m http.server 8080"
  exit 0
fi

print_green "Starting Python webserver on port 8080..."
nohup python3 -m http.server 8080 > /dev/null 2>&1 &
SERVER_PID=$!
sleep 1

# Try to open in browser (prefer firefox, then chromium, then xdg-open)
if command -v firefox &> /dev/null; then
  firefox http://localhost:8080/cybersecurity_glossary.html &
elif command -v chromium &> /dev/null; then
  chromium http://localhost:8080/cybersecurity_glossary.html &
elif command -v xdg-open &> /dev/null; then
  xdg-open http://localhost:8080/cybersecurity_glossary.html &
else
  print_yellow "Could not detect a browser to open the glossary. Please open http://localhost:8080/cybersecurity_glossary.html manually."
fi

print_green "Glossary is now live at: http://localhost:8080/cybersecurity_glossary.html"
print_blue "(To stop the server, kill process $SERVER_PID or close the terminal)"
print_blue "==============================================="
