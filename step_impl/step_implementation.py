from getgauge.python import step 
from getgauge.python import data_store
import os
from decleration import globalValues
from decleration import fileOperation
import math 
import webbrowser


@step("Summ of <num1> and <num2> is <num3>")
def summ_of_and_is(num1, num2, num3):
    actual = int(num1) + int(num2)
    expected =  int(num3)
    assert actual == expected 

@step("If <sentance> contains <word>")
def if_contains(sentence, word):
    value1 = sentence.__contains__(word)
    assert value1 == True


@step("Open terminal")
def open_terminal():
    os.system("gnome-terminal 'sudo apt-get update'") 
  
@step("Test multiple values <table>")
def test_multiple_values(table):
    actual = [table.get_column_values_with_name("num1")]
    expected = [table.get_column_values_with_name("num2")]
    assert actual == expected 
  

@step("Sample products to test table <table>")
def sample_products_to_test_table(table):
    Product = table.get_column_values_with_name("Product")
    Description = table.get_column_values_with_name("Description")
    if Product != "":
        #print(Product)
        #print(Description)
        assert Product != ""
        assert Description != ""
        apple = globalValues.appleCost
        assert apple == 4
           

 
@step("test if <num1> divide by <num2> works")
def test_somthing(num1, num2):
    int(num1) / int(num2)
 

# @step("Test values <num1> plus <num2> equal <num3>.")
# def jdljrb(a, b, c):
#     sum = a+b
#     print(sum)
    
 
# @step("Test values from the table<table:specs/values.csv>")
# def test_values_from_the_table(table:specs/values.csv):
#     assert False, "Add implementation code"


@step("Use entities in <file> for the test.")
def set_entities(file):
    file = fileOperation.check_file_param(file)
    entities = file.split("\n")[0:] 
    assert "University" in entities


@step("Compare the response from the file <file>")
def compare_the_response_from_the_file(file):
    split = file.split("\n")[1]
    responce = split.split(",")[0]
    piValue = split.split(",")[1] 
    assert float(piValue) == math.pi
 
@step("Open <url> this in browser")
def open_this_in_browser(arg1):
    webbrowser.open(arg1) 
 
@step("Write <text> in this file <file>")
def Write_in_this_file(text, file):
    with open(file, 'w') as f:
        f.write(text)
        f.close()
    f= open(file, 'r')
    print(f.read())    
       
@step("Check if this file <file> contains <arg1>")
def check_if_this_file_contains(file, arg1):
    f= open(file, 'r')
    text = f.read().replace("\n"," ")
    f.close()
    value1 = text.__contains__(arg1)
    assert value1 == True
    print("File contains: " + arg1)


@step("Delete this file <filePath>")
def delete_this_file(filePath):
    os.remove(filePath)
    if os.path.exists(filePath):
         print ("File exist")
    else:
        print ("File has been deleted")
    
