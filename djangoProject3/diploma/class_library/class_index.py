CORE_CLASSES = {
    "department": {
            "BIO": [
                {"code": 101,"type": "core","name": "Intro to Biology", "credits": 3, "pre_requisites": ""},
                {"code": 102,"type": "core","name": "Biology II", "credits": 3, "pre_requisites": "BIO 101, BIO 110"},
                {"code": 110,"type": "core","name": "Intro to Biology Lab", "credits": 1, "pre_requisites": ""},
                {"code": 120,"type": "core","name": "Biology II Lab", "credits": 1, "pre_requisites": ""},
                {"code": 201,"type": "core","name": "Advanced Biology", "credits": 3, "pre_requisites": "BIO 101, BIO 102"},
                {"code": 202,"type": "core","name": "Advanced Biology II", "credits": 3, "pre_requisites": "BIO 201"},
                {"code": 210, "type": "core", "name": "Advanced Biology Lab", "credits": 1, "pre_requisites": ""},
                {"code": 220, "type": "core", "name": "Advanced Biology II Lab", "credits": 1, "pre_requisites": ""},
                {"code": 301,"type": "core","name": "Cell Biology", "credits": 3, "pre_requisites": "BIO 201, BIO 202"},
                {"code": 302,"type": "core","name": "Cell Biology II", "credits": 3, "pre_requisites": "BIO 301"},
                {"code": 310, "type": "core", "name": "Cell Biology Lab", "credits": 1, "pre_requisites": ""},
                {"code": 320, "type": "core", "name": "Cell Biology II Lab", "credits": 1, "pre_requisites": ""},
            ],
            "CHM": [
                {"code": 101, "type": "core", "name": "Intro to Chemistry", "credits": 3,"pre_requisites": ""},
                {"code": 102, "type": "core", "name": "Chemistry II", "credits": 3,"pre_requisites": "CHM 101, CHM 110"},
                {"code": 110, "type": "core", "name": "Intro to Chemistry Lab", "credits": 1, "pre_requisites": ""},
                {"code": 120, "type": "core", "name": "Chemistry II Lab", "credits": 1,"pre_requisites": ""},
                {"code": 201, "type": "core", "name": "Advanced Chemistry", "credits": 3,"pre_requisites": "CHM 101, CHM 102"},
                {"code": 202, "type": "core", "name": "Advanced Chemistry II", "credits": 3,"pre_requisites": "CHM 201"},
                {"code": 201, "type": "core", "name": "Advanced Chemistry", "credits": 1,"pre_requisites": ""},
                {"code": 202, "type": "core", "name": "Advanced Chemistry II", "credits": 1,"pre_requisites": ""},
            ],
            "ENG": [
                {"code": 101, "type": "core", "name": "English I", "credits": 3,"pre_requisites": ""},
                {"code": 102, "type": "core", "name": "English II", "credits": 3,"pre_requisites": "ENG 101"},
                {"code": 201, "type": "core", "name": "Classical English", "credits": 3,"pre_requisites": "ENG 102"},
                {"code": 202, "type": "core", "name": "Contemporary English", "credits": 3,"pre_requisites": "ENG 201"},
            ],
            "HIS": [
                {"code": 101, "type": "core", "name": "American History I", "credits": 3,"pre_requisites": ""},
                {"code": 102, "type": "core", "name": "American History II", "credits": 3,"pre_requisites": "HIS 101"},
                {"code": 201, "type": "core", "name": "American History WWI", "credits": 3,"pre_requisites": "HIS 102"},
                {"code": 202, "type": "core", "name": "American History WWII", "credits": 3,"pre_requisites": "HIS 201"},
                {"code": 203, "type": "core", "name": "World History I", "credits": 3,"pre_requisites": "HIS 201"},
                {"code": 204, "type": "core", "name": "World History II", "credits": 3,"pre_requisites": "HIS 203"},
            ],
            "LIT": [
                {"code": 101, "type": "core", "name": "American Literature I", "credits": 3,"pre_requisites": ""},
                {"code": 102, "type": "core", "name": "American Literature  II", "credits": 3,"pre_requisites": "LIT 101"},
                {"code": 201, "type": "core", "name": "World Literature I", "credits": 3,"pre_requisites": "LIT 102"},
                {"code": 202, "type": "core", "name": "World Literature II", "credits": 3,"pre_requisites": "LIT 201"},
            ],
            "MTH": [
                {"code": 100, "type": "core", "name": "Algebra", "credits": 3, "pre_requisites": ""},
                {"code": 200, "type": "core", "name": "Geometry", "credits": 3, "pre_requisites": "MTH 100"},
                {"code": 300, "type": "core", "name": "Triggernometry", "credits": 3, "pre_requisites": "MTH 200"},
                {"code": 401, "type": "core", "name": "Calculus I", "credits": 4, "pre_requisites": "MTH 300"},
                {"code": 402, "type": "core", "name": "Calculus II", "credits": 4, "pre_requisites": "MTH 401"},
            ],
    }}


ELECTIVE_CLASSES = {
    "department": {
        "ART": [
            {"code": 101, "type": "elective", "name": "Art Studies I", "credits": 3, "pre_requisites": ""},
            {"code": 102, "type": "elective", "name": "Art Studies II", "credits": 3, "pre_requisites": "ART 101"},
            {"code": 201, "type": "elective", "name": "History of Modern Art", "credits": 3, "pre_requisites": "ART 102"},
            {"code": 202, "type": "elective", "name": "Contemporary Art Techniques", "credits": 3, "pre_requisites": "ART 201"}
        ],
        "GEO": [
            {"code": 101, "type": "elective", "name": "Geology I", "credits": 3, "pre_requisites": ""},
            {"code": 102, "type": "elective", "name": "Geology II", "credits": 3, "pre_requisites": "GEO 101"},
            {"code": 201, "type": "elective", "name": "Earth Materials", "credits": 3, "pre_requisites": "GEO 102"},
            {"code": 202, "type": "elective", "name": "Structural Geology", "credits": 3, "pre_requisites": "GEO 201"}
        ],
        "CS": [
            {"code": 101, "type": "elective", "name": "Introduction to Computer Science", "credits": 3, "pre_requisites": ""},
            {"code": 102, "type": "elective", "name": "Programming Fundamentals", "credits": 3, "pre_requisites": "CS 101"},
            {"code": 201, "type": "elective", "name": "Data Structures and Algorithms", "credits": 3, "pre_requisites": "CS 102"},
            {"code": 202, "type": "elective", "name": "Database Management Systems", "credits": 3, "pre_requisites": "CS 201"},
            {"code": 203, "type": "elective", "name": "Operating Systems", "credits": 3, "pre_requisites": "CS 201"}
        ],
        "PHS": [
            {"code": 101, "type": "elective", "name": "Introduction to Physical Fitness", "credits": 2, "pre_requisites": ""},
            {"code": 102, "type": "elective", "name": "Team Sports Fundamentals", "credits": 2, "pre_requisites": "PHS 101"},
            {"code": 201, "type": "elective", "name": "Advanced Personal Training", "credits": 2, "pre_requisites": "PHS 102"}
        ],

    }
}