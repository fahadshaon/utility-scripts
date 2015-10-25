# SQL Database Extract script


A python script to extract single database info from a multi-database MySQL dump 
generated from phpMyAdmin. 

Commands available are
 
- `list` - Lists all the database in a dump file.
- `extract` - Extracts a database from a dump file. 

Usage
 
    python sql_db_extract.py [-h] {list,extract} ...
    
List 

    python sql_db_extract.py list [-h] file_path
        
Extract

    python sql_db_extract.py extract [-h] file_path database output_dir



# LICENSE 

The MIT License (MIT)

Copyright (c) 2015 Fahad Shaon <fahad.shaon@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
