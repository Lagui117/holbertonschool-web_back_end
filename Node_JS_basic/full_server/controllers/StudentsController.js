import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    const databasePath = process.argv[2];
    
    readDatabase(databasePath)
      .then((fields) => {
        let output = 'This is the list of our students\n';
        
        // Sort fields alphabetically (case insensitive)
        const sortedFields = Object.keys(fields).sort((a, b) => 
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        
        sortedFields.forEach((field) => {
          const names = fields[field];
          output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        });
        
        response.status(200).send(output);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    
    const databasePath = process.argv[2];
    
    readDatabase(databasePath)
      .then((fields) => {
        const names = fields[major] || [];
        response.status(200).send(`List: ${names.join(', ')}\n`);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }
}

