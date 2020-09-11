[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Tareas de administración del sistema operativo***)](03_Manipulando_fechas_de_archivos.md)

# 7.2 Manejo de carpetas

## Python Directory and Files Management


In this tutorial, you'll learn about file and directory management in Python, i.e. creating a directory, renaming it, listing all directories, and working with them.


## Python Directory

If there are a large number of files to handle in our Python program, we can arrange our code within different directories to make things more manageable.

A directory or folder is a collection of files and subdirectories. Python has the `os` module that provides us with many useful methods to work with directories (and files as well).


## Get Current Directory

We can get the present working directory using the `getcwd()` method of the `os` module.

This method returns the current working directory in the form of a string. We can also use the `getcwdb()` method to get it as bytes object.

```python
>>> import os
>>> os.getcwd()
'C:\\Program Files\\PyScripter'

>>> os.getcwdb()
b'C:\\Program Files\\PyScripter'
```

The extra backslash implies an escape sequence. The `print()` function will render this properly.

```python
>>> print(os.getcwd())
C:\Program Files\PyScripter
```


## Changing Directory

We can change the current working directory by using the `chdir()` method.

The new path that we want to change into must be supplied as a string to this method. We can use both the forward-slash `/` or the backward-slash `\` to separate the path elements.

It is safer to use an escape sequence when using the backward slash.

```python
>>> os.chdir('C:\\Python33')

>>> print(os.getcwd())
C:\Python33
```


## List Directories and Files

All files and sub-directories inside a directory can be retrieved using the `listdir()` method.

This method takes in a path and returns a list of subdirectories and files in that path. If no path is specified, it returns the list of subdirectories and files from the current working directory.

```python
>>> print(os.getcwd())
C:\Python33

>>> os.listdir()
['DLLs',
'Doc',
'include',
'Lib',
'libs',
'LICENSE.txt',
'NEWS.txt',
'python.exe',
'pythonw.exe',
'README.txt',
'Scripts',
'tcl',
'Tools']

>>> os.listdir('G:\\')
['$RECYCLE.BIN',
'Movies',
'Music',
'Photos',
'Series',
'System Volume Information']
```


## Making a New Directory

We can make a new directory using the `mkdir()` method.

This method takes in the path of the new directory. If the full path is not specified, the new directory is created in the current working directory.

```python
>>> os.mkdir('test')

>>> os.listdir()
['test']
```


## Renaming a Directory or a File

The `rename()` method can rename a directory or a file.

For renaming any directory or file, the `rename()` method takes in two basic arguments: the old name as the first argument and the new name as the second argument.

```python
>>> os.listdir()
['test']

>>> os.rename('test','new_one')

>>> os.listdir()
['new_one']
```


## Removing Directory or File

A file can be removed (deleted) using the `remove()` method.

Similarly, the `rmdir()` method removes an empty directory.

```python
>>> os.listdir()
['new_one', 'old.txt']

>>> os.remove('old.txt')
>>> os.listdir()
['new_one']

>>> os.rmdir('new_one')
>>> os.listdir()
[]
```

**Note**: The `rmdir()` method can only remove empty directories.

In order to remove a non-empty directory, we can use the `rmtree()` method inside the `shutil` module.

```python
>>> os.listdir()
['test']

>>> os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'

>>> import shutil

>>> shutil.rmtree('test')
>>> os.listdir()
[]
```

## Recorriendo directorios

`os.walk()`

**Description**
Python method walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.

**Following is the syntax for walk() method −**

```
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
Parameters
top − Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)
```

`topdown` − If optional argument topdown is True or not specified, directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.

`onerror` − This can show error to continue with the walk, or raise the exception to abort the walk.

`followlinks` − This visits directories pointed to by symlinks, if set to true.

`Return Value`
This method returns value.

### Example
The following example shows the usage of walk() method.

```python
# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
```

Let us run the above program, this will scan all the directories and subdirectories bottom-to-up.

## Setting File Modification Times

File modification times show when a file was last edited. This can sometimes be confused with creation time but these are very different. Creation time is normally held by the operating system and states when a file was created. This means if you download a file from the internet, the creation time will change and be the time it was downloaded. Thus the creation time isn't very helpful.

File modification time is different however as it is stored in the file. Even though the operating system still manages these, they can still be easily changed as opposed to creation time.

The modification date can be found by right-clicking on a file and selecting properties.

### Setting File Modification Times
First, you will want to import os, time and datetime.

```python 
import os 
import time
import datetime
```

You will now need to locate the file you want to edit and create a time object to set to the file. To create one, we will first break it down into its simpler parts.

```python 
fileLocation = r""
year = 2017
month = 11
day = 5
hour = 19
minute = 50
second = 0
```

`fileLocation` is a string and the rest of the variables above are integers.

Next, we will create our datetime object using the data given and then convert it to seconds since epoch; this is what will be stored.

```python
date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())
```

Now we can do a simple os.utime call passing the file and modification time to set the new times.

```python
os.utime(fileLocation, (modTime, modTime))
```

Now if you go back and check the modification date it should be changed.

Final Code

```python
import os
import time
import datetime

fileLocation = r""
year = 2017
month = 11
day = 5
hour = 19
minute = 50
second = 0

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

os.utime(fileLocation, (modTime, modTime))
```


[Contenidos](../Contenidos.md) \| [Anterior (1 Manejo de fechas y horas)](01_Fechas.md) \| [Próximo (3 Tareas de administración del sistema operativo***)](03_Manipulando_fechas_de_archivos.md)

