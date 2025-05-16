#!/usr/bin/env python3
"""
Cybersecurity Glossary Manager
------------------------------
A tool for managing and updating the cybersecurity glossary entries.
"""

import json
import os
import re
import sys
from datetime import datetime


class GlossaryManager:
    """Manages the cybersecurity glossary entries and HTML generation."""

    def __init__(self, data_file='glossary_data.json', html_file='cybersecurity_glossary.html'):
        """Initialize the GlossaryManager with the specified data and HTML files."""
        self.data_file = data_file
        self.html_file = html_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Load glossary data from the JSON file."""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            print(f"✅ Successfully loaded data from {self.data_file}")
            print(f"   - {len(self.data['entries'])} entries found")
            print(f"   - Version: {self.data['version']}")
            print(f"   - Last updated: {self.data['lastUpdated']}")
        except FileNotFoundError:
            print(f"❌ Data file {self.data_file} not found.")
            self.data = {"version": "1.0", "lastUpdated": datetime.now().strftime('%Y-%m-%d'), "entries": []}
            print("💡 Created new empty glossary data structure.")
        except json.JSONDecodeError:
            print(f"❌ Error parsing JSON from {self.data_file}. The file might be corrupted.")
            sys.exit(1)

    def save_data(self):
        """Save glossary data to the JSON file."""
        self.data["lastUpdated"] = datetime.now().strftime('%Y-%m-%d')
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
            print(f"✅ Successfully saved data to {self.data_file}")
        except IOError as e:
            print(f"❌ Error saving data: {e}")
            sys.exit(1)

    def generate_html(self):
        """Generate HTML file from the glossary data."""
        try:
            # This is a simplified version - a full implementation would use the template
            # from the existing HTML file and replace only the data parts
            print(f"⚠️ HTML generation would update {self.html_file}")
            print("💡 To actually generate HTML, implement this method based on your HTML template.")
        except Exception as e:
            print(f"❌ Error generating HTML: {e}")

    def add_entry(self):
        """Interactive method to add a new entry to the glossary."""
        print("\n📝 Adding a new glossary entry")
        print("-----------------------------")

        # Get term
        term = input("Term: ").strip()
        if not term:
            print("❌ Term cannot be empty.")
            return

        # Check if term already exists
        for entry in self.data["entries"]:
            if entry["term"].lower() == term.lower():
                print(f"❌ Term '{term}' already exists in the glossary.")
                return

        # Get description
        description = input("Description: ").strip()
        if not description:
            print("❌ Description cannot be empty.")
            return

        # Get tags
        tags_input = input("Tags (comma-separated): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        if not tags:
            print("❌ At least one tag is required.")
            return

        # Get resources
        resources = []
        print("\nAdd resources (documentation, tutorials, etc.):")
        while True:
            resource_title = input("Resource title (or press Enter to finish): ").strip()
            if not resource_title:
                break

            resource_url = input("Resource URL: ").strip()
            if not resource_url:
                print("❌ Resource URL cannot be empty.")
                continue

            resources.append({"title": resource_title, "url": resource_url})

        # Get tools
        print("\nAdd related tools:")
        while True:
            tool_name = input("Tool name (or press Enter to finish): ").strip()
            if not tool_name:
                break

            tool_url = input("Tool URL: ").strip()
            if not tool_url:
                print("❌ Tool URL cannot be empty.")
                continue

            # Add tool as a special type of resource
            resources.append({"title": f"Tool: {tool_name}", "url": tool_url, "type": "tool"})

        # Determine the first letter for alphabetical sorting
        # Remove special characters for proper alphabetical sorting
        letter = re.sub(r'[^a-zA-Z0-9]', '', term)[0].upper() if re.sub(r'[^a-zA-Z0-9]', '', term) else term[0].upper()

        # Create new entry
        new_entry = {
            "term": term,
            "description": description,
            "tags": tags,
            "resources": resources,
            "letter": letter
        }

        # Add entry to data and save
        self.data["entries"].append(new_entry)
        self.save_data()
        print(f"✅ Successfully added new entry: '{term}'")

    def edit_entry(self):
        """Interactive method to edit an existing entry."""
        print("\n✏️ Edit a glossary entry")
        print("---------------------")

        # List all entries for selection
        print("Available entries:")
        for i, entry in enumerate(self.data["entries"]):
            print(f"{i+1}. {entry['term']}")

        try:
            selection = int(input("\nEnter entry number to edit (or 0 to cancel): "))
            if selection == 0:
                return
            if selection < 1 or selection > len(self.data["entries"]):
                print("❌ Invalid selection.")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        entry = self.data["entries"][selection-1]
        print(f"\nEditing: {entry['term']}")

        # Edit each field
        new_term = input(f"Term [{entry['term']}]: ").strip()
        if new_term:
            entry["term"] = new_term

        new_desc = input(f"Description [{entry['description']}]: ").strip()
        if new_desc:
            entry["description"] = new_desc

        tags_str = ", ".join(entry["tags"])
        new_tags = input(f"Tags [{tags_str}]: ").strip()
        if new_tags:
            entry["tags"] = [tag.strip() for tag in new_tags.split(",") if tag.strip()]

        # Edit resources
        print("\nCurrent resources and tools:")
        for i, resource in enumerate(entry["resources"]):
            resource_type = "Tool" if resource.get("type") == "tool" else "Resource"
            print(f"{i+1}. [{resource_type}] {resource['title']} - {resource['url']}")

        print("\nOptions: (a)dd resource, (t)ool, (e)dit existing, (d)elete, or (s)kip")
        action = input("Action: ").lower()

        if action == 'a':
            resource_title = input("Resource title: ").strip()
            resource_url = input("Resource URL: ").strip()
            if resource_title and resource_url:
                entry["resources"].append({"title": resource_title, "url": resource_url})
        elif action == 't':
            tool_name = input("Tool name: ").strip()
            tool_url = input("Tool URL: ").strip()
            if tool_name and tool_url:
                entry["resources"].append({"title": f"Tool: {tool_name}", "url": tool_url, "type": "tool"})
        elif action == 'e':
            try:
                res_idx = int(input("Resource number to edit: ")) - 1
                if 0 <= res_idx < len(entry["resources"]):
                    resource_title = input(f"Resource title [{entry['resources'][res_idx]['title']}]: ").strip()
                    resource_url = input(f"Resource URL [{entry['resources'][res_idx]['url']}]: ").strip()
                    if resource_title:
                        entry["resources"][res_idx]["title"] = resource_title
                    if resource_url:
                        entry["resources"][res_idx]["url"] = resource_url
            except ValueError:
                print("❌ Please enter a valid number.")
        elif action == 'd':
            try:
                res_idx = int(input("Resource number to delete: ")) - 1
                if 0 <= res_idx < len(entry["resources"]):
                    del entry["resources"][res_idx]
            except ValueError:
                print("❌ Please enter a valid number.")

        # Update letter if term changed
        if new_term:
            letter = re.sub(r'[^a-zA-Z0-9]', '', new_term)[0].upper() if re.sub(r'[^a-zA-Z0-9]', '', new_term) else new_term[0].upper()
            entry["letter"] = letter

        # Save changes
        self.save_data()
        print(f"✅ Successfully updated entry: '{entry['term']}'")

    def delete_entry(self):
        """Interactive method to delete an existing entry."""
        print("\n🗑️ Delete a glossary entry")
        print("-----------------------")

        # List all entries for selection
        print("Available entries:")
        for i, entry in enumerate(self.data["entries"]):
            print(f"{i+1}. {entry['term']}")

        try:
            selection = int(input("\nEnter entry number to delete (or 0 to cancel): "))
            if selection == 0:
                return
            if selection < 1 or selection > len(self.data["entries"]):
                print("❌ Invalid selection.")
                return
        except ValueError:
            print("❌ Please enter a valid number.")
            return

        entry = self.data["entries"][selection-1]
        confirm = input(f"⚠️ Are you sure you want to delete '{entry['term']}'? (y/n): ").lower()
        if confirm == 'y':
            self.data["entries"].pop(selection-1)
            self.save_data()
            print(f"✅ Successfully deleted entry: '{entry['term']}'")
        else:
            print("❌ Deletion cancelled.")

    def list_entries(self):
        """List all entries in the glossary."""
        print("\n📋 Glossary Entries")
        print("----------------")

        if not self.data["entries"]:
            print("No entries found.")
            return

        for entry in sorted(self.data["entries"], key=lambda x: x["term"].lower()):
            print(f"\n📌 {entry['term']}")
            print(f"   Description: {entry['description']}")
            print(f"   Tags: {', '.join(entry['tags'])}")

            # Group and display resources and tools separately
            resources = [r for r in entry["resources"] if r.get("type") != "tool"]
            tools = [r for r in entry["resources"] if r.get("type") == "tool"]

            if resources:
                print("   📚 Resources:")
                for resource in resources:
                    print(f"     - {resource['title']}: {resource['url']}")

            if tools:
                print("   🔧 Tools:")
                for tool in tools:
                    # Strip "Tool: " prefix for cleaner display
                    tool_name = tool['title'].replace("Tool: ", "")
                    print(f"     - {tool_name}: {tool['url']}")


def main():
    """Main entry point of the script."""
    # Make sure we're looking for files in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    manager = GlossaryManager()

    while True:
        print("\n🔍 Cybersecurity Glossary Manager")
        print("===============================")
        print("1. Add a new entry")
        print("2. Edit an existing entry")
        print("3. Delete an entry")
        print("4. List all entries")
        print("5. Generate HTML")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if choice == 1:
                manager.add_entry()
            elif choice == 2:
                manager.edit_entry()
            elif choice == 3:
                manager.delete_entry()
            elif choice == 4:
                manager.list_entries()
            elif choice == 5:
                manager.generate_html()
            elif choice == 6:
                print("👋 Exiting. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n👋 Program interrupted. Exiting.")
            break


if __name__ == "__main__":
    main()
