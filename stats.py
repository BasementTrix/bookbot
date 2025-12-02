def word_count( input_text ) :
    words = input_text.split()
    num_words = len( words )
    return f"Found {num_words} total words"

## def char_sort( body_text ) :
    

def character_freq( input_text ) :
    char_freq = {}
    for i in range( 0, len(input_text) ) :
        this_char = input_text[ i ]
        this_char = this_char.lower()
        if this_char in char_freq :
            char_freq[ this_char ] += 1
        else :
            char_freq[ this_char ] = 1
    
    return char_freq 

