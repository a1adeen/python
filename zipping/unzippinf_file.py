import zipfile
import shutil

# # zipping and unzppping py files
# # file_1
# f = open('new.txt', 'w')
# f.write("hey")
# f.close()
# # file_2
# f_2 = open('new_2' , 'w')
# f.write('hey_2')
# f.close()


# for compressing files into zip file first we have to make one zip file
# byt this we can send the files into .zip file by creating one
z = zipfile.ZipFile('zip_1.zip' , 'w')
z.write('new.txt' , compress_type=zipfile.ZIP_DEFLATED)
z.write('new_2' , compress_type=zipfile.ZIP_DEFLATED)
z.close()


# to extract the file
extrct = zipfile.ZipFile("zip_1.zip" , 'r')
# hese we make the folder to keep the extracted files
extrct.extractall('extracted')



# to make the directry into a zipfolder
dir_to_zip = '/home/aladeen/Documents/GitHub cloned files/python/zipping/extracted'
out_file_name = 'nnew_dir'
shutil.make_archive(out_file_name , 'zip' , dir_to_zip)



# to extract the diectry by another way

shutil.unpack_archive('nnew_dir.zip' , 'final' , 'zip')


