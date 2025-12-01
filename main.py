#!/usr/bin/env python3

from stats import word_count

def get_book_text( file_path ) :
    with open( file_path ) as fp :
        book_text = fp.read()

    return book_text

def main() :
    text = get_book_text( "books/frankenstein.txt" )
    
    print( word_count( text ) )

main()

    
