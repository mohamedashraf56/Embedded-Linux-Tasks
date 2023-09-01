#this is LCD init C func in 4bits mode 
def generate_init_function():
    init_function = """
void LCD_Init(void)
{
	/init in 4mode/
	_delay_ms(50);
	writeIns(0x02);//screen on 2line 4bit 5*7 mode
	writeIns(0x28);
	writeIns(0x0c);//0x0ccursor off ,0x0e on ,0x0f cursor blink
	writeIns(0x01);//clear screen
	_delay_ms(1);//because clear screen need 2ms
	writeIns(0x06);//increase DDRAM address with no shift
}
"""
    return init_function

# Generate the init function
init_code = generate_init_function()

# Write the generated code to a C file
file_path = '/home/mohamedashraf/file.c'  # Replace with the actual path to your C file
with open(file_path, 'a') as file:
    file.write(init_code)

print(f"init function generated and added to '{file_path}'.")
