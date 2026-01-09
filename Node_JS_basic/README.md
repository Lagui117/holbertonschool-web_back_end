# Node JS Basic

This project covers the fundamentals of Node.js, including basic JavaScript execution, file system operations, HTTP servers, and Express.js framework.

## Learning Objectives

- How to run JavaScript using Node.js
- How to use Node.js modules
- How to use specific Node.js files to execute code
- How to read and write files using the Node.js fs module
- How to use process.stdin, process.stdout, and process.stderr
- How to create HTTP servers using Node.js http module
- How to create HTTP servers using Express.js
- How to organize a complex HTTP server using Express.js with ES6 syntax

## Requirements

- All files are executed on Ubuntu 20.04 LTS using Node.js (version 14.x or higher)
- All files end with a new line
- Code is verified against lint using ESLint
- For the full_server project, Babel is used for ES6 support

## Project Structure

```
Node_JS_basic/
├── 0-console.js                    # Basic console output function
├── 1-stdin.js                      # Process stdin example
├── 3-read_file_async.js            # Asynchronous file reading
├── 4-http.js                       # Basic HTTP server
├── 5-http.js                       # HTTP server with routing
├── 6-http_express.js               # Express.js server
├── full_server/                    # Complete Express server
│   ├── controllers/
│   │   ├── AppController.js        # Homepage controller
│   │   └── StudentsController.js   # Students controller
│   ├── routes/
│   │   └── index.js                # Route definitions
│   ├── utils.js                    # Database utility functions
│   └── server.js                   # Main server file
├── .babelrc                        # Babel configuration
└── package.json                    # Node.js dependencies
```

## Tasks

### 0. Executing basic javascript with Node JS
**File:** `0-console.js`

Create a function named `displayMessage` that prints a string argument to STDOUT.

**Usage:**
```bash
node 0-main.js
```

### 1. Using Process stdin
**File:** `1-stdin.js`

Create a program that:
- Displays a welcome message
- Reads user input from stdin
- Displays the user's name
- Shows a closing message when the program ends

**Usage:**
```bash
node 1-stdin.js
# or
echo "John" | node 1-stdin.js
```

### 3. Reading a file asynchronously with Node JS
**File:** `3-read_file_async.js`

Create a function `countStudents` that:
- Accepts a file path as argument
- Reads the database file asynchronously
- Returns a Promise
- Throws an error if the database is not available
- Logs the number of students and groups them by field

**Usage:**
```bash
node 3-main.js database.csv
```

### 4. Create a small HTTP server using Node's HTTP module
**File:** `4-http.js`

Create a simple HTTP server that:
- Listens on port 1245
- Displays "Hello Holberton School!" for any endpoint

**Usage:**
```bash
node 4-http.js
curl localhost:1245
```

### 5. Create a more complex HTTP server using Node's HTTP module
**File:** `5-http.js`

Create an HTTP server that:
- Listens on port 1245
- Returns "Hello Holberton School!" for `/` endpoint
- Returns student list for `/students` endpoint
- Accepts database filename as command-line argument

**Usage:**
```bash
node 5-http.js database.csv
curl localhost:1245
curl localhost:1245/students
```

### 6. Create a small HTTP server using Express
**File:** `6-http_express.js`

Create an Express server that:
- Listens on port 1245
- Displays "Hello Holberton School!" for `/` endpoint
- Shows "Cannot GET /path" for undefined routes

**Usage:**
```bash
npm install express
node 6-http_express.js
curl localhost:1245
```

### 8. Organize a complex HTTP server using Express
**Directory:** `full_server/`

Create a complete Express server with:
- Controllers for handling requests
- Routes for URL routing
- Utility functions for database operations
- ES6 syntax with Babel support

**Structure:**
- `full_server/utils.js` - Database reading utility
- `full_server/controllers/AppController.js` - Homepage controller
- `full_server/controllers/StudentsController.js` - Students controller
- `full_server/routes/index.js` - Route definitions
- `full_server/server.js` - Main server file

**Endpoints:**
- `GET /` - Returns "Hello Holberton School!"
- `GET /students` - Returns list of all students grouped by field
- `GET /students/:major` - Returns list of students in a specific major (CS or SWE)

**Usage:**
```bash
# Install dependencies
npm install express babel-cli babel-preset-env nodemon

# Run the server
npm run dev
# or
babel-node --presets babel-preset-env ./full_server/server.js ./database.csv

# Test endpoints
curl localhost:1245
curl localhost:1245/students
curl localhost:1245/students/CS
curl localhost:1245/students/SWE
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd holbertonschool-web_back_end/Node_JS_basic
```

2. Install dependencies (for Express projects):
```bash
npm install
```

## Database Format

The CSV database file should have the following format:
```
firstname,lastname,age,field
Johann,Kerbler,20,CS
Arielle,Garzon,21,CS
...
```

## Error Handling

- File not found: Returns "Cannot load the database"
- Invalid major parameter: Returns "Major parameter must be CS or SWE"
- Empty lines in CSV are automatically filtered out

## Author

Holberton School

## License

ISC



