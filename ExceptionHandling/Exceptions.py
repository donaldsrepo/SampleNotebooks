def TestTouch():
    import os
    fail = 0
    
    # correct path, no errors
    #RootPath="/DataScience/SampleNotebooks/ExceptionHandling" correct path
    # incorrect path, causes error
    RootPath="/DataScience/SampleNotebooks/ExceptionHandling_error"
    
    # specific OS command error handling
    try:
        from pathlib import Path
        Path(RootPath+"/test.json").touch()
    except OSError:
        print ("Creation of the file failed")
    else:
        print ("Successfully created the file ")
    finally:
        print("Finished json create file command")
    
    # handle normal or common exceptions
    try:
        from pathlib import Path
        Path(RootPath+"/test.json").touch()
    except Exception as e:
        print('errno =',e.errno)
        print('message =',str(e))
        fail = fail + 1
    else:
        print ("Successfully created the file ")
    finally:
        print("Finished json create file command")
    
    # handle all exceptions
    try:
        from pathlib import Path
        Path(RootPath+"/test.json").touch()
    except BaseException as e:
        print('errno =',e.errno)
        print('message =',str(e))
        fail = fail + 1
    else:
        print ("Successfully created the file ")
    finally:
        print("Finished json create file command")
    
    if (fail == 2):
        print("BOTH exception handlers caught this error")
    elif (fail == 1):
        print("ONE exception handler caught this error")
    else:
        print("NO errors found")
    return fail
        
        
# if you run this package using python Exceptions.py
if __name__ == '__main__':
    print("running this package directly on command line")

TestTouch()

# setup some simple unit testing    
def test_touch(): 
    # use the Exceptions.py package remotely 
    TestTouch()
    assert TestTouch() == 2