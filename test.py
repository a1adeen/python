import zipfile

#
# f = open('hii.txt' , 'w')
# f.write("hey")
# f.close()
#
# f_1 = open('hii_1' , 'w')
# f_1.write("hey")
# f_1.close()

#
# new_file = zipfile.ZipFile('zippp.zip' ,'w')
# new_file.write('hii.txt' , compress_type=zipfile.ZIP_DEFLATED)
# new_file.write('hii_1' , compress_type=zipfile.ZIP_DEFLATED)
# new_file.close()
#


# to extract
ext = zipfile.ZipFile('zippp.zip' ,  'r')
ext.extractall('o')
# did this