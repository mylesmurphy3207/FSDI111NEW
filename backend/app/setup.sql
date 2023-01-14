CREATE TABLE task ( 
    id INTEGER PRIMARY KEY, 
    summary VARCHAR(1024),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);




INSERT INTO task (
    summary, 
    description,
) VALUES (  
    "Take out the trash",
    "Take the trash out to the dumpster by the driveway"
);

INSERT INTO task (
    summary, 
    description
) VALUES ( 
    "Wash the car",
    "Either take the car to the car wash or do it yourself"
);

INSERT INTO task (
    summary, 
    description
) VALUES (
    "Prepare lunch",
    "Make a wholesome meal"
);
