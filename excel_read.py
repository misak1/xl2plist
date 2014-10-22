#!/usr/bin/python
# -*- coding: utf-8 -*- 

import codecs
import xlrd # <- 別途インストール

if __name__ == "__main__":

    book = xlrd.open_workbook('test_book.xls')
    
    sheet_1 = book.sheet_by_index(0)
#    for col in range(sheet_1.ncols):
#        print "----------------------------"
#        for row in range(sheet_1.nrows):
#            print sheet_1.cell(row,col).value

### for iOS
    plist_header = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>''' + "\n"

    plist_footer = '''</dict>
</plist>''' + "\n"
    f = open('images.plist', 'w')
    f = codecs.lookup('utf_8')[-1](f)
    f.write(plist_header)
    for row in range(sheet_1.nrows):
        key = "\t" + u'<key>' + sheet_1.cell(row,0).value + '</key>' + "\n"
        val = "\t" + u'<string>' + sheet_1.cell(row,1).value + '<string>' + "\n"
        f.write(key)
        f.write(val)
    f.write(plist_footer)
    f.close() # ファイルを閉じる
    
### for Android
    f = open('images.properties', 'w')
    f = codecs.lookup('utf_8')[-1](f)
    for row in range(sheet_1.nrows):
        key = u'' + sheet_1.cell(row,0).value +"="
        val = u'' + sheet_1.cell(row,1).value + "\n"
        f.write(key)
        f.write(val)
    f.close() # ファイルを閉じる

