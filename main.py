#!/usr/bin/env python3

import sys
from stats import word_count, character_freq

def get_book_text( file_path ) :
    try: 
        with open( file_path ) as fp :
            book_text = fp.read()
    except FileNotFoundError :
        print( f"Cannot open the file '{file_path}'." )
        usage()

    return book_text

def report_sort( entry ) :
    return entry[ "num" ]

def book_report( char_freq ) :
    report_text = []
    for key in sorted( char_freq ) :
        report_text.append( { "char": key,  "num": char_freq[ key ] } )
        # print( key )

    report_text.sort( key=report_sort, reverse=True )

    for line in report_text :
        key = line[ "char" ]
        val = line[ "num" ]
        print( f"{key}: {val}" )

def usage() :
    print( "Usage: python3 main.py <path_to_book>" )
    sys.exit(1)
    
def main() :

    if len( sys.argv ) != 2 :
        usage()
    else :
        book = sys.argv[1]
        
    text = get_book_text( book )
    letter_counts = character_freq( text )
    
    print(  "============ BOOKBOT ============" )
    print( f"Analyzing book found at {book}..." )
    print(  "----------- Word Count ----------" )
    print(  "Found " + str( word_count( text ) ) + " total words" )
    print(  "--------- Character Count -------" )
    book_report( letter_counts )
    print(  "============= END ===============" )

main()

    
