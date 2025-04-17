# Cloud & Database Systems: Project 1 showcase
# Bradley Antholz
# April 17th, 2025

##### note: screenshots of proof it works are in the pdf file above. A short description is provided for each, as well. Otherwise, the requirements for "GitHub repo link" and "project report" and "Proposed grade" are in this file.

##  Part 1: Project summary

#### This project was originally done with my own custom database, but I couldn't get that to work. So, I pivoted and used the DB provided in Lab 13 and decided to update it for this assignment. This was done over the course of several days, and shoutout to Morgan for troubleshooting some issues early on with me. 

#### I added four new things: Add Entry, Delete Entry, Update Entry and Top 10 Artists sorted by Track count. I used the previous labs for the outline of all four, and what took me the longest was debugging errors when running the live site (really, I had sooo many errors). I added some comments for clarity in flaskapp.py, but the one I wanted to highlight: I focused on Artist and Album because they were the easiest for both me and any users present. It's simple to memrize Taylor Swift, it is difficult to know the exact milliseconds of an album.

#### I incorportated DynamoDB right at the end of my project window, and for that I referenced old labs, specifically lab 9 question 2 (This time, without the syntax error). SQL is used to execute the query from Lab 13 and the new Top Artists section, which I just ripped the syntax from Lab 13. 

#### Setup/Run: Fairly straightforward, all radio buttons work and do what you want them to. I couldn't figure out why there was no message on the server saying that addition, deletion or update was successful, but everything else works flawlessly. CRUD doesn't call for display, so the added users are in the screenshots in the PDF. 


## Part 2: Challenges/Technologies used

#### Hooo boy was there a lot, mostly with assimilating old code with new code for the project. The screenshots show some of the issues, but for most of them I went to ChatGPT for an easy fix. For example, I kept getting this: The browser (or proxy) sent a request that this server could not understand. KeyError: 'name' and asked the model to help me understand why. I also wanted to make sure I got every part of the rubric down, so I asked it what was I missing too. Also, Morgan helped troubleshoot the errors before the checkpoint, which is what I emailed you about. Once I scrapped the DB I created, the errors stopped and it was pretty smooth. 

## Part 3: Grading

Grading Rubric (100 Points Total)
---
Part 1: Core Functionality (65 points): 58/65

- Website uses Flask and runs independently from VS Code (not relying on terminal interaction)
10/10
- Relational database (MySQL/RDS) is correctly used in the project
13/15
- Non-relational database (DynamoDB) is correctly used (e.g., user info stored/retrieved)
9/10
- Implements full CRUD operations (Create, Read, Update, Delete)
10/10
- Incorporates at least one SQL JOIN query
5/5
- Uses own RDS instance inside student’s VPC
3/5
- Uses own IAM account (e.g., ProjectOneUser)
5/5
- Application avoids storing credentials in public GitHub (e.g., creds.py is excluded via .gitignore)
5/5
---
### Justification: Not much to say for the 100%'s, but 1, I didn't use my own database and the RDS wouldn't work for me (made my life easier to just not deal with it); 2, Display user info is missing but I ran out of time and 3, I have no clue if using your RDS counts as "my own". 
---

Part 2: Code Quality and GitHub Submission (25 points): 23/25

- Code is organized across multiple files (e.g., flaskapp.py, dbCode.py)
8/10
- Good software practices (clear naming, comments, error handling with try/except, modular functions)
10/10
- GitHub repository is submitted with a clear commit history and a README file
5/5
---
### Justification: I don't have multiple files because I didn't feel a need to, everything fit well into flaskapp.py. That, and I didn't wanna mess up what I had. I think my variable naming is pretty clear and the README.md file is well done and organized. Not my first rodeo with GitHub.  
---
Part 3: Checkpoint Completion (10 points): 9/10

- Checkpoint submitted on time with a working Flask app that connects to RDS and renders dynamic data
9/10
---
### Justification: It didn't work and you gave me a 9/10. Don't see how I can get a 10 since I didn't change it
---

# Overall score: 58/65 + 23/25 + 9/10 = 90/100

### I think I did well on this project, obviously some areas could need improvement but given the constraints and my lack of expertise in python, I did well for what I have. 

---

