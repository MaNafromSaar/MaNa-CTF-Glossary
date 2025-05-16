#!/usr/bin/env python3
"""
Cybersecurity Glossary Entry Tool

A simple tool to add, edit, and manage entries in the cybersecurity glossary.
"""

import json
import os
import sys
import argparse
from datetime import datetime

JSON_FILE = "glossary_data.json"

def load_glossary():
    """Load the glossary from the JSON file."""
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Creating new glossary file: {JSON_FILE}")
        return {"version": "1.0", "lastUpdated": datetime.now().strftime("%Y-%m-%d"), "entries": []}
    except json.JSONDecodeError:
        print("Error: Invalid JSON file. Please check the format.")
        sys.exit(1)

def save_glossary(glossary):
    """Save the glossary to the JSON file."""
    glossary["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(glossary, f, indent=2)

    print(f"Glossary saved to {JSON_FILE}")

def add_entry(glossary):
    """Add a new entry to the glossary."""
    print("\n=== Add New Glossary Entry ===\n")

    entry = {
        "resources": []
    }
    entry["term"] = input("Term: ").strip()

    # Check if the term already exists
    for existing in glossary["entries"]:
        if existing["term"].lower() == entry["term"].lower():
            overwrite = input("This term already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation cancelled.")
                return glossary
            # Remove the existing entry
            glossary["entries"] = [e for e in glossary["entries"] if e["term"].lower() != entry["term"].lower()]
            break

    entry["description"] = input("Description: ").strip()

    # Tags
    tags = input("Tags (comma-separated): ").strip()
    entry["tags"] = [tag.strip() for tag in tags.split(",") if tag.strip()]

    # Resources
    resources = []
    while True:
        url = input("Resource URL (or press Enter to finish): ").strip()
        if not url:
            break

        title = input("Resource title: ").strip()
        resources.append({"url": url, "title": title})

    entry["resources"] = resources

    # Add entry to glossary
    glossary["entries"].append(entry)
    print(f"\nEntry '{entry['term']}' added successfully!")

    # Sort entries alphabetically
    glossary["entries"] = sorted(glossary["entries"], key=lambda x: x["term"].lower())

    return glossary

def list_entries(glossary):
    """List all entries in the glossary."""
    print("\n=== Glossary Entries ===\n")

    if not glossary["entries"]:
        print("No entries in the glossary.")
        return

    for i, entry in enumerate(glossary["entries"], 1):
        print(f"{i}. {entry['term']}")

    print(f"\nTotal entries: {len(glossary['entries'])}")

def export_csv(glossary, output_file="cybersecurity_glossary.csv"):
    """Export the glossary to CSV format."""
    import csv

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write header
        writer.writerow(["Term", "Description", "Tags", "Resources"])

        # Write entries
        for entry in glossary["entries"]:
            resources = "; ".join([f"{r['title']} ({r['url']})" for r in entry["resources"]])
            writer.writerow([
                entry["term"],
                entry["description"],
                ", ".join(entry["tags"]),
                resources
            ])

    print(f"Glossary exported to {output_file}")

def update_html(glossary, template_file="cybersecurity_glossary_template.html", output_file="cybersecurity_glossary.html"):
    """Update the HTML file with the current glossary entries."""
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Template file {template_file} not found.")
        return

    # Process entries here and update the HTML
    # This is a basic implementation - would need to be customized

    print(f"HTML file updated: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Cybersecurity Glossary Tool")
    parser.add_argument('action', choices=['add', 'list', 'export-csv'],
                        help='Action to perform')
    parser.add_argument('--output', '-o', help='Output file for exports')

    args = parser.parse_args()

    glossary = load_glossary()

    if args.action == 'add':
        glossary = add_entry(glossary)
        save_glossary(glossary)
    elif args.action == 'list':
        list_entries(glossary)
    elif args.action == 'export-csv':
        output_file = args.output or "cybersecurity_glossary.csv"
        export_csv(glossary, output_file)

if __name__ == "__main__":
    main()
