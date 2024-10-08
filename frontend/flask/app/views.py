from flask import render_template, redirect, url_for, flash, request
from app import app
import paramiko
from functions import cmd
import time


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def navbar():
    return render_template('about.html')

@app.route('/showcow')
def showcow():
    stdout, stderr = cmd("cat cow.txt")
    return render_template('showcow.html', cow2=stdout, title="Show the cow in cat.txt")

@app.route('/fabrictest')
def fabrictest():
    output = connection.run("ls -ld /proc", hide = True).stdout.strip()
    return render_template('fabrictest.html', message=output, title="Test the fabric module")

@app.route('/exercises/lvl_1', methods=['GET', 'POST'])
def lvl_1():
    if request.method == "POST":
        stdout = cmd("check1.sh")
        return render_template('lvl_1.html', title="Level 1", task=stdout)
    else:
        return render_template('lvl_1.html', title="Level 1")

@app.route('/chapter1')
def ch1():
    return render_template('ch1.html', title="Chapter 1")

ch1ex1_count = 0
@app.route('/chapter1/ex1', methods=['GET', 'POST'])
def ch1_ex1():
    if request.method == "POST":
        stdout = cmd("ch1_ex1_check", "root")
        global ch1ex1_count
        ch1ex1_count += 1
        if ch1ex1_count > 10:
            ch1ex1_count = 0
        return render_template('ch1_ex1.html', title="Chapter 1, Exercise 1", task=stdout, count=ch1ex1_count)
    else:
        return render_template('ch1_ex1.html', title="Chapter 1, Exercise 1")

ch1ex2_count = 0
@app.route('/chapter1/ex2', methods=['GET', 'POST'])
def ch1_ex2():
    if request.method == "POST":
        stdout = cmd("ch1_ex2_check", "trainee")
        global ch1ex2_count
        ch1ex2_count += 1
        if ch1ex2_count > 10:
            ch1ex2_count = 0
        return render_template('ch1_ex2.html', title="Chapter 1, Exercise 2", task=stdout, count=ch1ex2_count)
    else:
        return render_template('ch1_ex2.html', title="Chapter 1, Exercise 2")

ch1ex3_count = 0
@app.route('/chapter1/ex3', methods=['GET', 'POST'])
def ch1_ex3():
    if request.method == "POST":
        stdout = cmd("ch1_ex3_check", "trainee")
        global ch1ex3_count
        ch1ex3_count += 1
        if ch1ex3_count > 10:
            ch1ex3_count = 0
        return render_template('ch1_ex3.html', title="Chapter 1, Exercise 3", task=stdout, count=ch1ex3_count)
    else:
        return render_template('ch1_ex3.html', title="Chapter 1, Exercise 3")

ch1ex4_count = 0
@app.route('/chapter1/ex4', methods=['GET', 'POST'])
def ch1_ex4():
    if request.method == "POST":
        stdout = cmd("ch1_ex4_check", "trainee")
        global ch1ex4_count
        ch1ex4_count += 1
        if ch1ex4_count > 10:
            ch1ex4_count = 0
        return render_template('ch1_ex4.html', title="Chapter 1, Exercise 4", task=stdout, count=ch1ex4_count)
    else:
        return render_template('ch1_ex4.html', title="Chapter 1, Exercise 4")

ch1ex5_count = 0
@app.route('/chapter1/ex5', methods=['GET', 'POST'])
def ch1_ex5():
    if request.method == "POST":
        stdout = cmd("ch1_ex5_check", "trainee")
        global ch1ex5_count
        ch1ex5_count += 1
        if ch1ex5_count > 10:
            ch1ex5_count = 0
        return render_template('ch1_ex5.html', title="Chapter 1, Exercise 5", task=stdout, count=ch1ex5_count)
    else:
        return render_template('ch1_ex5.html', title="Chapter 1, Exercise 5")

ch1ex6_count = 0
@app.route('/chapter1/ex6', methods=['GET', 'POST'])
def ch1_ex6():
    if request.method == "POST":
        stdout = cmd("ch1_ex6_check", "trainee")
        global ch1ex6_count
        ch1ex6_count += 1
        if ch1ex6_count > 10:
            ch1ex6_count = 0
        return render_template('ch1_ex6.html', title="Chapter 1, Exercise 6", task=stdout, count=ch1ex6_count)
    else:
        return render_template('ch1_ex6.html', title="Chapter 1, Exercise 6")

ch1ex7_count = 0
@app.route('/chapter1/ex7', methods=['GET', 'POST'])
def ch1_ex7():
    if request.method == "POST":
        stdout = cmd("ch1_ex7_check", "trainee")
        global ch1ex7_count
        ch1ex7_count += 1
        if ch1ex7_count > 10:
            ch1ex7_count = 0
        return render_template('ch1_ex7.html', title="Chapter 1, Exercise 7", task=stdout, count=ch1ex7_count)
    else:
        return render_template('ch1_ex7.html', title="Chapter 1, Exercise 7")

ch1ex8_count = 0
@app.route('/chapter1/ex8', methods=['GET', 'POST'])
def ch1_ex8():
    if request.method == "POST":
        stdout = cmd("ch1_ex8_check", "trainee")
        global ch1ex8_count
        ch1ex8_count += 1
        if ch1ex8_count > 10:
            ch1ex8_count = 0
        return render_template('ch1_ex8.html', title="Chapter 1, Exercise 8", task=stdout, count=ch1ex8_count)
    else:
        return render_template('ch1_ex8.html', title="Chapter 1, Exercise 8")

@app.route('/chapter1/complete')
def ch1_complete():
    return render_template('ch1_complete.html', title="Chapter 1 complete")

@app.route('/linux')
def linux():
    return render_template('linux.html', title="Linux machine")

@app.route('/chapter2')
def ch2():
    return render_template('ch2.html', title="Chapter 2")

ch2ex1_count = 0
@app.route('/chapter2/ex1', methods=['GET', 'POST'])
def ch2_ex1():
    if request.method == "POST":
        stdout = cmd("ch2_ex1_check", "trainee")
        global ch2ex1_count
        ch2ex1_count += 1
        if ch2ex1_count > 10:
            ch2ex1_count = 0
        return render_template('ch2_ex1.html', title="Chapter 2, Exercise 1", task=stdout, count=ch2ex1_count)
    else:
        return render_template('ch2_ex1.html', title="Chapter 2, Exercise 1")

ch2ex2_count = 0
@app.route('/chapter2/ex2', methods=['GET', 'POST'])
def ch2_ex2():
    if request.method == "POST":
        stdout = cmd("ch2_ex2_check", "trainee")
        global ch2ex2_count
        ch2ex2_count += 1
        if ch2ex2_count > 10:
            ch2ex2_count = 0
        return render_template('ch2_ex2.html', title="Chapter 2, Exercise 2", task=stdout, count=ch2ex2_count)
    else:
        return render_template('ch2_ex2.html', title="Chapter 2, Exercise 2")

ch2ex3_count = 0
@app.route('/chapter2/ex3', methods=['GET', 'POST'])
def ch2_ex3():
    if request.method == "POST":
        stdout = cmd("ch2_ex3_check", "trainee")
        global ch2ex3_count
        ch2ex3_count += 1
        if ch2ex3_count > 10:
            ch2ex3_count = 0
        return render_template('ch2_ex3.html', title="Chapter 2, Exercise 3", task=stdout, count=ch2ex3_count)
    else:
        return render_template('ch2_ex3.html', title="Chapter 2, Exercise 3")

ch2ex4_count = 0
@app.route('/chapter2/ex4', methods=['GET', 'POST'])
def ch2_ex4():
    if request.method == "POST":
        stdout = cmd("ch2_ex4_check", "trainee")
        global ch2ex4_count
        ch2ex4_count += 1
        if ch2ex4_count > 10:
            ch2ex4_count = 0
        return render_template('ch2_ex4.html', title="Chapter 2, Exercise 4", task=stdout, count=ch2ex4_count)
    else:
        return render_template('ch2_ex4.html', title="Chapter 2, Exercise 4")

ch2ex5_count = 0
@app.route('/chapter2/ex5', methods=['GET', 'POST'])
def ch2_ex5():
    if request.method == "POST":
        stdout = cmd("ch2_ex5_check", "trainee")
        global ch2ex5_count
        ch2ex5_count += 1
        if ch2ex5_count > 10:
            ch2ex5_count = 0
        return render_template('ch2_ex5.html', title="Chapter 2, Exercise 5", task=stdout, count=ch2ex5_count)
    else:
        return render_template('ch2_ex5.html', title="Chapter 2, Exercise 5")

ch2ex6_count = 0
@app.route('/chapter2/ex6', methods=['GET', 'POST'])
def ch2_ex6():
    if request.method == "POST":
        stdout = cmd("ch2_ex6_check", "trainee")
        global ch2ex6_count
        ch2ex6_count += 1
        if ch2ex6_count > 10:
            ch2ex6_count = 0
        return render_template('ch2_ex6.html', title="Chapter 2, Exercise 6", task=stdout, count=ch2ex6_count)
    else:
        return render_template('ch2_ex6.html', title="Chapter 2, Exercise 6")

ch2ex7_count = 0
@app.route('/chapter2/ex7', methods=['GET', 'POST'])
def ch2_ex7():
    if request.method == "POST":
        stdout = cmd("ch2_ex7_check", "trainee")
        global ch2ex7_count
        ch2ex7_count += 1
        if ch2ex7_count > 10:
            ch2ex7_count = 0
        return render_template('ch2_ex7.html', title="Chapter 2, Exercise 7", task=stdout, count=ch2ex7_count)
    else:
        return render_template('ch2_ex7.html', title="Chapter 2, Exercise 7")

ch2ex8_count = 0
@app.route('/chapter2/ex8', methods=['GET', 'POST'])
def ch2_ex8():
    if request.method == "POST":
        stdout = cmd("ch2_ex8_check", "trainee")
        global ch2ex8_count
        ch2ex8_count += 1
        if ch2ex8_count > 10:
            ch2ex8_count = 0
        return render_template('ch2_ex8.html', title="Chapter 2, Exercise 8", task=stdout, count=ch2ex8_count)
    else:
        return render_template('ch2_ex8.html', title="Chapter 2, Exercise 8")

ch2ex9_count = 0
@app.route('/chapter2/ex9', methods=['GET', 'POST'])
def ch2_ex9():
    if request.method == "POST":
        stdout = cmd("ch2_ex9_check", "trainee")
        global ch2ex9_count
        ch2ex9_count += 1
        if ch2ex9_count > 10:
            ch2ex9_count = 0
        return render_template('ch2_ex9.html', title="Chapter 2, Exercise 9", task=stdout, count=ch2ex9_count)
    else:
        return render_template('ch2_ex9.html', title="Chapter 2, Exercise 9")

ch2ex10_count = 0
@app.route('/chapter2/ex10', methods=['GET', 'POST'])
def ch2_ex10():
    if request.method == "POST":
        stdout = cmd("ch2_ex10_check", "trainee")
        global ch2ex10_count
        ch2ex10_count += 1
        if ch2ex10_count > 10:
            ch2ex10_count = 0
        return render_template('ch2_ex10.html', title="Chapter 2, Exercise 10", task=stdout, count=ch2ex10_count)
    else:
        return render_template('ch2_ex10.html', title="Chapter 2, Exercise 10")

@app.route('/chapter2/complete')
def ch2_complete():
    return render_template('ch2_complete.html', title="Chapter 2 complete")

@app.route('/chapter3')
def ch3():
    return render_template('ch3.html', title="Chapter 3")

ch3ex1_count = 0
@app.route('/chapter3/ex1', methods=['GET', 'POST'])
def ch3_ex1():
    if request.method == "POST":
        stdout = cmd("ch3_ex1_check", "trainee")
        global ch3ex1_count
        ch3ex1_count += 1
        if ch3ex1_count > 10:
            ch3ex1_count = 0
        return render_template('ch3_ex1.html', title="Chapter 3, Exercise 1", task=stdout, count=ch3ex1_count)
    else:
        return render_template('ch3_ex1.html', title="Chapter 3, Exercise 1")

ch3ex2_count = 0
@app.route('/chapter3/ex2', methods=['GET', 'POST'])
def ch3_ex2():
    if request.method == "POST":
        stdout = cmd("ch3_ex2_check", "trainee")
        global ch3ex2_count
        ch3ex2_count += 1
        if ch3ex2_count > 10:
            ch3ex2_count = 0
        return render_template('ch3_ex2.html', title="Chapter 3, Exercise 2", task=stdout, count=ch3ex2_count)
    else:
        return render_template('ch3_ex2.html', title="Chapter 3, Exercise 2")

ch3ex3_count = 0
@app.route('/chapter3/ex3', methods=['GET', 'POST'])
def ch3_ex3():
    if request.method == "POST":
        stdout = cmd("ch3_ex3_check", "trainee")
        global ch3ex3_count
        ch3ex3_count += 1
        if ch3ex3_count > 10:
            ch3ex3_count = 0
        return render_template('ch3_ex3.html', title="Chapter 3, Exercise 3", task=stdout, count=ch3ex3_count)
    else:
        return render_template('ch3_ex3.html', title="Chapter 3, Exercise 3")

ch3ex4_count = 0
@app.route('/chapter3/ex4', methods=['GET', 'POST'])
def ch3_ex4():
    if request.method == "POST":
        stdout = cmd("ch3_ex4_check", "trainee")
        global ch3ex4_count
        ch3ex4_count += 1
        if ch3ex4_count > 10:
            ch3ex4_count = 0
        return render_template('ch3_ex4.html', title="Chapter 3, Exercise 4", task=stdout, count=ch3ex4_count)
    else:
        return render_template('ch3_ex4.html', title="Chapter 3, Exercise 4")

ch3ex5_count = 0
@app.route('/chapter3/ex5', methods=['GET', 'POST'])
def ch3_ex5():
    if request.method == "POST":
        stdout = cmd("ch3_ex5_check", "trainee")
        global ch3ex5_count
        ch3ex5_count += 1
        if ch3ex5_count > 10:
            ch3ex5_count = 0
        return render_template('ch3_ex5.html', title="Chapter 3, Exercise 5", task=stdout, count=ch3ex5_count)
    else:
        return render_template('ch3_ex5.html', title="Chapter 3, Exercise 5")

ch3ex6_count = 0
@app.route('/chapter3/ex6', methods=['GET', 'POST'])
def ch3_ex6():
    if request.method == "POST":
        stdout = cmd("ch3_ex6_check", "trainee")
        global ch3ex6_count
        ch3ex6_count += 1
        if ch3ex6_count > 10:
            ch3ex6_count = 0
        return render_template('ch3_ex6.html', title="Chapter 3, Exercise 6", task=stdout, count=ch3ex6_count)
    else:
        return render_template('ch3_ex6.html', title="Chapter 3, Exercise 6")

ch3ex7_count = 0
@app.route('/chapter3/ex7', methods=['GET', 'POST'])
def ch3_ex7():
    if request.method == "POST":
        stdout = cmd("ch3_ex7_check", "trainee")
        global ch3ex7_count
        ch3ex7_count += 1
        if ch3ex7_count > 10:
            ch3ex7_count = 0
        return render_template('ch3_ex7.html', title="Chapter 3, Exercise 7", task=stdout, count=ch3ex7_count)
    else:
        return render_template('ch3_ex7.html', title="Chapter 3, Exercise 7")

ch3ex8_count = 0
@app.route('/chapter3/ex8', methods=['GET', 'POST'])
def ch3_ex8():
    if request.method == "POST":
        stdout = cmd("ch3_ex8_check", "trainee")
        global ch3ex8_count
        ch3ex8_count += 1
        if ch3ex8_count > 10:
            ch3ex8_count = 0
        return render_template('ch3_ex8.html', title="Chapter 3, Exercise 8", task=stdout, count=ch3ex8_count)
    else:
        return render_template('ch3_ex8.html', title="Chapter 3, Exercise 8")

ch3ex9_count = 0
@app.route('/chapter3/ex9', methods=['GET', 'POST'])
def ch3_ex9():
    if request.method == "POST":
        stdout = cmd("ch3_ex9_check", "trainee")
        global ch3ex9_count
        ch3ex9_count += 1
        if ch3ex9_count > 10:
            ch3ex9_count = 0
        return render_template('ch3_ex9.html', title="Chapter 3, Exercise 9", task=stdout, count=ch3ex9_count)
    else:
        return render_template('ch3_ex9.html', title="Chapter 3, Exercise 9")

ch3ex10_count = 0
@app.route('/chapter3/ex10', methods=['GET', 'POST'])
def ch3_ex10():
    if request.method == "POST":
        stdout = cmd("ch3_ex10_check", "trainee")
        global ch3ex10_count
        ch3ex10_count += 1
        if ch3ex10_count > 10:
            ch3ex10_count = 0
        return render_template('ch3_ex10.html', title="Chapter 3, Exercise 10", task=stdout, count=ch3ex10_count)
    else:
        return render_template('ch3_ex10.html', title="Chapter 3, Exercise 10")

@app.route('/chapter3/complete')
def ch3_complete():
    return render_template('ch3_complete.html', title="Chapter 3 complete")

@app.route('/chapter4')
def ch4():
    return render_template('ch4.html', title="Chapter 4")

ch4ex1_count = 0
@app.route('/chapter4/ex1', methods=['GET', 'POST'])
def ch4_ex1():
    if request.method == "POST":
        stdout = cmd("ch4_ex1_check", "trainee")
        global ch4ex1_count
        ch4ex1_count += 1
        if ch4ex1_count > 10:
            ch4ex1_count = 0
        return render_template('ch4_ex1.html', title="Chapter 4, Exercise 1", task=stdout, count=ch4ex1_count)
    else:
        return render_template('ch4_ex1.html', title="Chapter 4, Exercise 1")

ch4ex2_count = 0
@app.route('/chapter4/ex2', methods=['GET', 'POST'])
def ch4_ex2():
    if request.method == "POST":
        stdout = cmd("ch4_ex2_check", "trainee")
        global ch4ex2_count
        ch4ex2_count += 1
        if ch4ex2_count > 10:
            ch4ex2_count = 0
        return render_template('ch4_ex2.html', title="Chapter 4, Exercise 2", task=stdout, count=ch4ex2_count)
    else:
        return render_template('ch4_ex2.html', title="Chapter 4, Exercise 2")

ch4ex3_count = 0
@app.route('/chapter4/ex3', methods=['GET', 'POST'])
def ch4_ex3():
    if request.method == "POST":
        stdout = cmd("ch4_ex3_check", "trainee")
        global ch4ex3_count
        ch4ex3_count += 1
        if ch4ex3_count > 10:
            ch4ex3_count = 0
        return render_template('ch4_ex3.html', title="Chapter 4, Exercise 3", task=stdout, count=ch4ex3_count)
    else:
        return render_template('ch4_ex3.html', title="Chapter 4, Exercise 3")

ch4ex4_count = 0
@app.route('/chapter4/ex4', methods=['GET', 'POST'])
def ch4_ex4():
    if request.method == "POST":
        stdout = cmd("ch4_ex4_check", "trainee")
        global ch4ex4_count
        ch4ex4_count += 1
        if ch4ex4_count > 10:
            ch4ex4_count = 0
        return render_template('ch4_ex4.html', title="Chapter 4, Exercise 4", task=stdout, count=ch4ex4_count)
    else:
        return render_template('ch4_ex4.html', title="Chapter 4, Exercise 4")

ch4ex5_count = 0
@app.route('/chapter4/ex5', methods=['GET', 'POST'])
def ch4_ex5():
    if request.method == "POST":
        stdout = cmd("ch4_ex5_check", "trainee")
        global ch4ex5_count
        ch4ex5_count += 1
        if ch4ex5_count > 10:
            ch4ex5_count = 0
        return render_template('ch4_ex5.html', title="Chapter 4, Exercise 5", task=stdout, count=ch4ex5_count)
    else:
        return render_template('ch4_ex5.html', title="Chapter 4, Exercise 5")

ch4ex6_count = 0
@app.route('/chapter4/ex6', methods=['GET', 'POST'])
def ch4_ex6():
    if request.method == "POST":
        stdout = cmd("ch4_ex6_check", "trainee")
        global ch4ex6_count
        ch4ex6_count += 1
        if ch4ex6_count > 10:
            ch4ex6_count = 0
        return render_template('ch4_ex6.html', title="Chapter 4, Exercise 6", task=stdout, count=ch4ex6_count)
    else:
        return render_template('ch4_ex6.html', title="Chapter 4, Exercise 6")

ch4ex7_count = 0
@app.route('/chapter4/ex7', methods=['GET', 'POST'])
def ch4_ex7():
    if request.method == "POST":
        stdout = cmd("ch4_ex7_check", "trainee")
        global ch4ex7_count
        ch4ex7_count += 1
        if ch4ex7_count > 10:
            ch4ex7_count = 0
        return render_template('ch4_ex7.html', title="Chapter 4, Exercise 7", task=stdout, count=ch4ex7_count)
    else:
        return render_template('ch4_ex7.html', title="Chapter 4, Exercise 7")

ch4ex8_count = 0
@app.route('/chapter4/ex8', methods=['GET', 'POST'])
def ch4_ex8():
    if request.method == "POST":
        stdout = cmd("ch4_ex8_check", "trainee")
        global ch4ex8_count
        ch4ex8_count += 1
        if ch4ex8_count > 10:
            ch4ex8_count = 0
        return render_template('ch4_ex8.html', title="Chapter 4, Exercise 8", task=stdout, count=ch4ex8_count)
    else:
        return render_template('ch4_ex8.html', title="Chapter 4, Exercise 8")

@app.route('/chapter4/complete')
def ch4_complete():
    return render_template('ch4_complete.html', title="Chapter 4 complete")

@app.route('/chapter5')
def ch5():
    return render_template('ch5.html', title="Chapter 5")

ch5ex1_count = 0
@app.route('/chapter5/ex1', methods=['GET', 'POST'])
def ch5_ex1():
    if request.method == "POST":
        stdout = cmd("ch5_ex1_check", "trainee")
        global ch5ex1_count
        ch5ex1_count += 1
        if ch5ex1_count > 10:
            ch5ex1_count = 0
        return render_template('ch5_ex1.html', title="Chapter 5, Exercise 1", task=stdout, count=ch5ex1_count)
    else:
        return render_template('ch5_ex1.html', title="Chapter 5, Exercise 1")

ch5ex2_count = 0
@app.route('/chapter5/ex2', methods=['GET', 'POST'])
def ch5_ex2():
    if request.method == "POST":
        stdout = cmd("ch5_ex2_check", "trainee")
        global ch5ex2_count
        ch5ex2_count += 1
        if ch5ex2_count > 10:
            ch5ex2_count = 0
        return render_template('ch5_ex2.html', title="Chapter 5, Exercise 2", task=stdout, count=ch5ex2_count)
    else:
        return render_template('ch5_ex2.html', title="Chapter 5, Exercise 2")

ch5ex3_count = 0
@app.route('/chapter5/ex3', methods=['GET', 'POST'])
def ch5_ex3():
    if request.method == "POST":
        stdout = cmd("ch5_ex3_check", "trainee")
        global ch5ex3_count
        ch5ex3_count += 1
        if ch5ex3_count > 10:
            ch5ex3_count = 0
        return render_template('ch5_ex3.html', title="Chapter 5, Exercise 3", task=stdout, count=ch5ex3_count)
    else:
        return render_template('ch5_ex3.html', title="Chapter 5, Exercise 3")


ch5ex4_count = 0
@app.route('/chapter5/ex4', methods=['GET', 'POST'])
def ch5_ex4():
    if request.method == "POST":
        stdout = cmd("ch5_ex4_check", "trainee")
        global ch5ex4_count
        ch5ex4_count += 1
        if ch5ex4_count > 10:
            ch5ex4_count = 0
        return render_template('ch5_ex4.html', title="Chapter 5, Exercise 4", task=stdout, count=ch5ex4_count)
    else:
        return render_template('ch5_ex4.html', title="Chapter 5, Exercise 4")

ch5ex5_count = 0
@app.route('/chapter5/ex5', methods=['GET', 'POST'])
def ch5_ex5():
    if request.method == "POST":
        stdout = cmd("ch5_ex5_check", "trainee")
        global ch5ex5_count
        ch5ex5_count += 1
        if ch5ex5_count > 10:
            ch5ex5_count = 0
        return render_template('ch5_ex5.html', title="Chapter 5, Exercise 5", task=stdout, count=ch5ex5_count)
    else:
        return render_template('ch5_ex5.html', title="Chapter 5, Exercise 5")

ch5ex6_count = 0
@app.route('/chapter5/ex6', methods=['GET', 'POST'])
def ch5_ex6():
    if request.method == "POST":
        stdout = cmd("ch5_ex6_check", "trainee")
        global ch5ex6_count
        ch5ex6_count += 1
        if ch5ex6_count > 10:
            ch5ex6_count = 0
        return render_template('ch5_ex6.html', title="Chapter 5, Exercise 6", task=stdout, count=ch5ex6_count)
    else:
        return render_template('ch5_ex6.html', title="Chapter 5, Exercise 6")

ch5ex7_count = 0
@app.route('/chapter5/ex7', methods=['GET', 'POST'])
def ch5_ex7():
    if request.method == "POST":
        stdout = cmd("ch5_ex7_check", "trainee")
        global ch5ex7_count
        ch5ex7_count += 1
        if ch5ex7_count > 10:
            ch5ex7_count = 0
        return render_template('ch5_ex7.html', title="Chapter 5, Exercise 7", task=stdout, count=ch5ex7_count)
    else:
        return render_template('ch5_ex7.html', title="Chapter 5, Exercise 7")

ch5ex8_count = 0
@app.route('/chapter5/ex8', methods=['GET', 'POST'])
def ch5_ex8():
    if request.method == "POST":
        stdout = cmd("ch5_ex8_check", "trainee")
        global ch5ex8_count
        ch5ex8_count += 1
        if ch5ex8_count > 10:
            ch5ex8_count = 0
        return render_template('ch5_ex8.html', title="Chapter 5, Exercise 8", task=stdout, count=ch5ex8_count)
    else:
        return render_template('ch5_ex8.html', title="Chapter 5, Exercise 9")

@app.route('/chapter5/complete')
def ch5_complete():
    return render_template('ch5_complete.html', title="Chapter 5 complete")

@app.route('/restore')
def restore():
    return render_template('restore.html', title="Restore contents")

@app.route('/ch1_restore')
def ch1_restore():
    cmd("ch1_restore", "trainee")
    return render_template('ch1_restore.html', title="Chapter 1 restored")

@app.route('/ch2_restore')
def ch2_restore():
    cmd("ch2_restore", "trainee")
    return render_template('ch2_restore.html', title="Chapter 2 restored")

@app.route('/ch3_restore')
def ch3_restore():
    cmd("ch3_restore", "trainee")
    return render_template('ch3_restore.html', title="Chapter 3 restored")

@app.route('/ch4_restore')
def ch4_restore():
    cmd("ch4_restore", "root")
    return render_template('ch4_restore.html', title="Chapter 4 restored")

@app.route('/ch5_restore')
def ch5_restore():
    cmd("ch5_restore", "root")
    return render_template('ch5_restore.html', title="Chapter 5 restored")