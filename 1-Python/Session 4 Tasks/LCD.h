void LCD_Init(void);


void LCD_WriteChar(u8 ch);
void LCD_WriteString(u8*str);
void LCD_WriteNumber(s32 num);
void LCD_WriteBinary(u8 num);
void LCD_WriteHex(u8 num);
void LCD_setcursor(u8 line,u8 cell);
void LCD_Clear(void);
void LCD_ClearCell(u8 line , u8 cell,u8 num);
void LCD_WriteNumber_4D(u16 num);


void LCD_CustomChar(u8 loc,u8*pattern);
void LCD_setcursorString(u8 line,u8 cell ,u8*str);
