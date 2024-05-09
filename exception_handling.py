# Exception handling allows you to gracefully handle errors or exceptional situations 
# This helps your program continue running instead of crashing when an error occurs
# We can handle exceptions using the try, except, else, and finally blocks

# The try block contains the code that might raise an exception
# The except block catches specific exception types and provides a response
# The else block is executed if no exceptions occurred in the try block
# The finally block is always executed, whether an exception occurred or not


# try:
#     # Code that might raise an exception
#     result=10/0
# except ZeroDivisionError:
#     # Handle a specific exception type
#     print("Error:Division by zero")
# except Exception as e:
#     # Handle other exceptions (general case)
#     print("An error occurred:", str(e))
# else:
#     # Executed if no exceptions occurred in the try block
#     print("No exceptions occurred.")
# finally:
#     # Always executed, whether an exception occurred or not
#     print("Execution completed.")

##############################################
# Handling multiple exceptions
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Division by zero")
# except ValueError:
#     print("Error: Invalid input")
# except Exception as e:
#     print("An error occurred:", str(e))

################################################