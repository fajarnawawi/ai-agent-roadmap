# Sample Projects to Test

Use these ideas to test your Virtual Software House implementation.

## Beginner Level

### 1. Simple Calculator
```
Create a command-line calculator that can perform basic arithmetic operations
(add, subtract, multiply, divide). Handle division by zero errors.
```

**Expected Features:**
- Four basic operations
- Error handling for division by zero
- Clean user input/output
- Unit tests for each operation

### 2. Todo List Manager
```
Build a todo list CLI app where users can add tasks, list all tasks,
mark tasks as complete, and remove tasks.
```

**Expected Features:**
- Add task with description
- List all tasks with status
- Mark task complete
- Remove task by ID
- Persistent storage (JSON file)

### 3. Temperature Converter
```
Create a tool that converts temperatures between Celsius, Fahrenheit, and Kelvin.
```

**Expected Features:**
- Convert between all three units
- Input validation
- Precise calculations
- Tests for all conversion formulas

## Intermediate Level

### 4. File Organizer
```
Build a script that organizes files in a directory by extension.
It should create folders for each file type and move files accordingly.
```

**Expected Features:**
- Scan directory for files
- Create folders by extension
- Move files safely (handle conflicts)
- Dry-run mode
- Undo functionality

### 5. CSV Data Analyzer
```
Create a tool that reads a CSV file and provides basic statistics
(mean, median, mode) for numerical columns.
```

**Expected Features:**
- Read CSV files
- Identify numerical columns
- Calculate statistics
- Handle missing data
- Output formatted report

### 6. Password Generator
```
Build a secure password generator with customizable length and character sets.
```

**Expected Features:**
- Configurable length
- Include/exclude: uppercase, lowercase, numbers, symbols
- Strength meter
- Copy to clipboard
- Generate multiple passwords

## Advanced Level

### 7. Web Scraper
```
Create a web scraper that extracts article titles and links from a news website
and saves them to a JSON file.
```

**Expected Features:**
- HTTP requests with error handling
- HTML parsing
- Data extraction
- JSON export
- Rate limiting
- Tests with mock HTTP responses

### 8. API Client
```
Build a client for a public API (e.g., GitHub, OpenWeather) that fetches data
and displays it in a formatted way.
```

**Expected Features:**
- API authentication (if needed)
- Multiple endpoints
- Error handling (rate limits, timeouts)
- Response caching
- Pretty-print output

### 9. Markdown to HTML Converter
```
Create a tool that converts Markdown files to HTML with support for
headings, links, lists, and code blocks.
```

**Expected Features:**
- Parse Markdown syntax
- Generate valid HTML
- Support common elements
- CSS styling option
- File I/O handling

## Expert Level

### 10. Mini Web Framework
```
Build a minimal web framework with routing, request/response handling,
and middleware support.
```

**Expected Features:**
- Route decorators
- GET/POST request handling
- Query parameters
- Middleware chain
- JSON responses
- Tests with mock requests

---

## Tips for Testing

1. **Start Simple:** Begin with beginner projects to validate the system works
2. **Iterate:** Run the same project multiple times, compare outputs
3. **Edge Cases:** Give vague requirements to test clarification
4. **Complexity:** Gradually increase project difficulty
5. **Evaluation:** Manually review the generated code quality

## Success Metrics

Your system is working well if it:
- ✅ Generates runnable code on first try (>70% of time)
- ✅ Writes tests that actually test the functionality
- ✅ Handles common edge cases
- ✅ Produces readable, documented code
- ✅ Completes beginner projects in 1-2 iterations
- ✅ Completes intermediate projects in 2-3 iterations
