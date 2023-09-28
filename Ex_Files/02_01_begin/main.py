RUN_INDENTED = True

def my_function():
    greet = "Hello"
    return greet

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(my_function())
print(message)

