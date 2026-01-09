const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1); // Skip header line

    const fields = {};
    let totalStudents = 0;

    students.forEach((line) => {
      if (line.trim() !== '') {
        const [firstname, , , field] = line.split(',');
        if (field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
          totalStudents += 1;
        }
      }
    });

    console.log(`Number of students: ${totalStudents}`);
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

