# Performance Test Scripts
## [SAFE](http://safe.cse.iitb.ac.in) Description
* **S**mart **A**uthenticated **F**ast **E**xams
* App-Server based system - Conducting exams in class using Smart Phone.  
## Project Description
* Created **scripts** for **performance testing** of **quiz functionality** in **SAFE** using **Locust**.
* **Scripts** to **create and add dummy users** in the **database** were also created.
* Scripts to **create and add dummy questions** was also provided.
* For more detailed description refer the **[report](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/blob/main/report.pdf)**
## Quiz Functionality APIs
![SAFE-Quiz-APIs](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/blob/main/pictures/quiz-api.png)

## Performance Test Demo
### Instructions for running Performance Test in [4.Attempt quiz](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/tree/main/4.Attempt%20quiz)
* Add the appropriate **Answers.py** and **credentianls.py** from the previous steps.
* Run ```$ python3 CourseCode.py``` : To provide the course Name. e.g. CS101
* Run ```$ python3 TestName.py``` : To provide the TestName . e.g. CS101.TZ
* Run ```$ locust -f SafeQuizAttempt.py``` : To run the actual performance test

### Performance Test Results
![Locust Perf Test](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/blob/main/pictures/perf-script.png)

## Impact
### Used to find a  bottleneck in SAFE backend Stack.
![Bottleneck component](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/blob/main/pictures/bottleneck.png)
### Performance Improvement
![Performance Improvement](https://github.com/jatin-jatin/Performance-Test-Script-SAFE-quiz-functionality/blob/main/pictures/improve.png)