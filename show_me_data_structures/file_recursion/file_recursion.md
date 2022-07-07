### in this task we visit all floders,

### in each folder we keep files in a list that maches a spesific patern,

### and we continiu the process deeeper in folders

### Time and Space complexity

### files = [file for file in files_and_folders if sfx in file] `->` `O(n)`

### folders = [folder for folder in files_and_folders if '.' not in folder] `->` `O(q)`

### for folder in folders:

### files.extend(find_files(suffix, path + '/' + folder))

### the above for loop `O(m * d) `

### so `O(n + q + m * d) => O(m*d)`
