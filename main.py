#!/usr/bin/env python3

def word_count( input_text ) :
    words = input_text.split()
    num_words = len( words )
    return f"Found {num_words} total words"

def get_book_text( file_path ) :
    with open( file_path ) as fp :
        book_text = fp.read()

    return book_text

def main() :
    text = get_book_text( "books/frankenstein.txt" )
    
    print( word_count( text ) )

main()

    
