#!/usr/bin/env python3
"""
Cybersecurity Glossary Entry Point
---------------------------------
Main script to manage the cybersecurity glossary.
"""

import sys
import os
from glossary_manager import GlossaryManager

def display_welcome():
    """Show welcome message and available commands."""
    print("\n🔐 CYBERSECURITY GLOSSARY MANAGER 🔐")
    print("===================================\n")
    print("Available commands:")
    print("  1. add    - Add new entries")
    print("  2. edit   - Edit existing entries")
    print("  3. delete - Remove entries")
    print("  4. search - Search for terms")
    print("  5. export - Generate HTML")
    print("  6. list   - List all entries")
    print("  7. help   - Display this help message")
    print("  8. exit   - Exit the program\n")

def main():
    """Main entry point for the glossary manager."""
    manager = GlossaryManager()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == 'add':
            manager.add_entry_interactive()
        elif command == 'edit':
            term = sys.argv[2] if len(sys.argv) > 2 else None
            manager.edit_entry_interactive(term)
        elif command == 'delete':
            term = sys.argv[2] if len(sys.argv) > 2 else None
            manager.delete_entry_interactive(term)
        elif command == 'search':
            term = sys.argv[2] if len(sys.argv) > 2 else None
            if term:
                manager.search_entries(term)
            else:
                print("Please specify a search term.")
        elif command == 'export':
            manager.generate_html()
        elif command == 'list':
            manager.list_all_entries()
        elif command == 'help':
            display_welcome()
        else:
            print(f"Unknown command: {command}")
            display_welcome()
    else:
        # Interactive mode
        display_welcome()

        while True:
            command = input("\nEnter command (or 'help' for commands): ").lower()

            if command in ['quit', 'exit', 'q']:
                break
            elif command == 'add' or command == '1':
                manager.add_entry_interactive()
            elif command == 'edit' or command == '2':
                manager.edit_entry_interactive()
            elif command == 'delete' or command == '3':
                manager.delete_entry_interactive()
            elif command == 'search' or command == '4':
                term = input("Enter search term: ")
                manager.search_entries(term)
            elif command == 'export' or command == '5':
                manager.generate_html()
                print("✅ HTML successfully generated.")
            elif command == 'list' or command == '6':
                manager.list_all_entries()
            elif command in ['help', '7', '?']:
                display_welcome()
            else:
                print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
