CREATE TABLE notes (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   title VARCHAR(45),
   subtitle VARCHAR(45),
   body VARCHAR(512),
   date TIMESTAMP DATE DEFAULT (datetime('now','localtime'))
   );

INSERT INTO notes (
   title,
   subtitle,
   body
   ) VALUES (
   "Test",
   "An example for the table",
   "A long description explaining the meaning of the note"
   );
