
#def print_format_table(): 
 
#    for style in range(8):
#        for fg in range(30,38): 
#            s1 = ''
#            for bg in range(40,48):
#                format = ';'.join([str(style), str(fg), str(bg)]) 
#                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#            print(s1) 
#       print('\n')
#print_format_table()
"""
def write_colourful_text(string, style, foreground, background):
    string = 'RAINBOW'
    for style in range(0,8):
        for foreground in range(40,48):
            s = ''
            for background in range(40,48):
                format = ';'.join([str(style), str(foreground), str(background)])
                s += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s)
        print('\n')

write_colourful_text(string, style, foreground, background)
"""

import sys
BOLD = 1
FG_GREEN = 32
BG_DARKBLUE = 44

def print_colorful_text(string, style, foreground, background):
	s1 = ''
	format = ';'.join([str(style), str(foreground), str(background)])
	s1 += '\x1b[%sm %s \x1b[0m' % (format, string)
	if (string != "RAINBOW" or string != "W"):
		print (s1, end = "")
	else:
		print (s1)
"""
def main(argv):
	print_colorful_text("R ", 2, 36, 40)
	print_colorful_text("A ", 0, 37, 40)
	print_colorful_text("I ", 0, 33, 40)
	print_colorful_text("N ", 0, 32, 40)
	print_colorful_text("B ", 0, 36, 40)
	print_colorful_text("O ", 0, 34, 40)
	print_colorful_text("W", 0, 35, 40)
	print_colorful_text("RAINBOW", BOLD, FG_GREEN, BG_DARKBLUE)
	print ("\n")

main(sys.argv)
"""