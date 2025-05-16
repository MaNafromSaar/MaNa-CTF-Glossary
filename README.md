# Cybersecurity Glossary

A community-driven, tag-based cybersecurity glossary focused on terms relevant to CTF competitions, exploitation, and cybersecurity concepts.

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Glossary-blue)
![Tags](https://img.shields.io/badge/Tag--based-Organization-green)

## 🌟 Features

- **Tag-based organization**: No rigid categories, search across all related tags
- **Multiple views**: Table, card, and alphabetical formats for easy reference
- **Searchable**: Full text search across all entries and tags
- **Responsive design**: Works on mobile and desktop devices
- **Multiple resource and tool links**: Each entry can have multiple reference links and related tools
- **Easy contribution**: Simple JSON-based storage for community contributions

## 📚 Using the Glossary

The glossary has three different views:

1. **Table View**: Default view with all terms in a table format. Best for quickly scanning many entries.
2. **Card View**: Visual card-based layout for each term. Provides a more detailed view of each entry.
3. **A-Z View**: Traditional alphabetical organization with entries grouped by first letter. Ideal for browsing the glossary like a dictionary.

### Tag Filtering

You can filter the glossary by clicking on tags in the tag filter section at the top of the page. Multiple tag selection filters for entries that contain ALL selected tags.

### Search Functionality

The search box allows you to quickly find terms by searching across:
- Term names
- Descriptions
- Tags
- Resources

## 🛠️ Adding New Entries

### Quick Start

Get started quickly with the setup script:

```bash
cd glossary
./setup.sh
```

This will ensure all scripts are executable and ready to use.

### Using the Interactive Manager (Recommended)

The easiest way to manage the glossary is using the included Python manager script:

```bash
cd glossary
./glossary.py
```

This interactive tool provides a simple menu system to:
- Add new entries
- Edit existing entries
- Delete entries
- Search for terms
- Export to HTML
- List all entries

### Command-Line Usage

You can also use direct commands for quick operations:

```bash
# Add a new entry
./glossary.py add

# Edit an entry (will prompt for which one or search)
./glossary.py edit

# Search for terms
./glossary.py search exploit

# Generate HTML output
./glossary.py export

# List all entries
./glossary.py list

# Display help
./glossary.py help
```

### Manual JSON Editing

If you prefer manual editing, you can directly modify the `glossary_data.json` file. Each entry should follow this format:

```json
{
  "term": "Your Term",
  "description": "Description of the term",
  "tags": ["tag1", "tag2", "tag3"],
  "resources": [
    {
      "title": "Resource Title",
      "url": "https://resource-url.com"
    },
    {
      "title": "Another Resource",
      "url": "https://another-url.com"
    },
    {
      "title": "Tool: Related Tool",
      "url": "https://tool-url.com",
      "type": "tool"
    }
  ],
  "letter": "Y"  // First letter for alphabetical sorting
}
```

Note: To add a tool link, prefix the title with "Tool: " and add a "type": "tool" property.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Add/edit entries using the Python manager or by directly editing the JSON
3. Submit a pull request

### Contribution Guidelines

- Ensure the term doesn't already exist (unless you're improving an existing entry)
- Provide a clear, concise description
- Add relevant tags (at least 2-3)
- Include at least one legitimate resource link
- Follow the existing JSON structure

## 📦 Repository Contents

### Core Files
- `cybersecurity_glossary.html` - The main HTML interface with tag filtering and multiple views
- `glossary_data.json` - The JSON data file containing all entries
- `glossary_manager.py` - Python library for managing entries and generating HTML

### User Tools
- `glossary.py` - Main interactive entry point for managing the glossary
- `setup.sh` - Quick setup script to prepare the environment
- `add_entry.py` - Legacy utility for adding entries (use `glossary.py` instead)

### Documentation
- `README.md` - This documentation
- `.gitignore` - List of files to ignore in version control

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- All contributors who have added terms and resources
- The cybersecurity community for continuous knowledge sharing
- CTF organizers whose challenges inspire many of these entries
- Focus on improving the quality and accuracy of the glossary
- Follow established formats and conventions
