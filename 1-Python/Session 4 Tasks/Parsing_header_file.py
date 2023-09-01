import re

def parse_header_file(file_path):
    function_declarations = []
    
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Match function declarations using regular expression pattern
        pattern = r'\b[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^;]+\);'
        matches = re.findall(pattern, content)
        
        # Add matched function declarations to the list
        function_declarations.extend(matches)
    
    return function_declarations

file_path = '/home/mohamedashraf/LCD.h'  # Replace with the path to your header file
function_declarations = parse_header_file(file_path)

# Print the function declarations
for declaration in function_declarations:
    print(declaration)
