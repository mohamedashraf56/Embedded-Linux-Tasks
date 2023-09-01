
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


