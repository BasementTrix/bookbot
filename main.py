#!/usr/bin/env python3

from stats import word_count, character_freq

def get_book_text( file_path ) :
    with open( file_path ) as fp :
        book_text = fp.read()

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
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1

def main( book="books/frankenstein.txt" ) :

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

    
