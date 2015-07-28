<br />
## Advanced Python    

###Q9. [Regular Expressions, Dictionary, Writing to CSV File](q9_python/q9_advanced.py)
This question has multiple parts, and will take **20-40 hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv]((q9_python/faculty.csv))
 

###Part I - Regular Expressions

Use regular expressions to:

a) Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

>> REPLACE THIS WITH YOUR RESPONSE

b) Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

>> REPLACE THIS WITH YOUR RESPONSE

c) Search for email addresses and put them in a list.  Print the list of email addresses.

>> REPLACE THIS WTIH YOUR RESPONSE

d) Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

>> REPLACE THIS WTIH YOUR RESPONSE


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
