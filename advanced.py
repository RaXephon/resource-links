# Source:  University of Pennsylvania - Biostatistics Faculty List
# A file is provided for use: faculty.csv

# Part 1 - regular expressions

# Use regular expressions to:
# a) find number of occurrences for each of degrees listed:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
# b) find how many different titles are there, and their frequencies:  Ex:  Assistant Professor, Professor
# c) search for email addresses and put them in a list.    
# d) How many different email domains are there (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.)

  REPLACE THIS WITH YOUR RESPONSE

# Part 2 - write to csv file
# a)  write email addresses from Part 1 to csv file

# bellamys@mail.med.upenn.edu
# warren@upenn.edu
# bryanma@upenn.edu

  REPLACE THIS WITH YOUR RESPONSE

# Part 3 - dictionary

# Create a dictionary in the below format:

faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
            }

  REPLACE THIS WITH YOUR RESPONSE

# Part 4

# The previous dictionary does not have the best design for keys.  
# Create a new dictionary as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }

  REPLACE THIS WITH YOUR RESPONSE

# Part 5
# looks like current dictionary is sorted by first name.  Sort by last name and print.

  REPLACE THIS WITH YOUR RESPONSE
