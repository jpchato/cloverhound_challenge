"""
    Welcome applicants!
    The point of this little test is to help us determine your skillset.
    On the job it will be very common that you are handed an unfamiliar codebase
    and instructed to debug and determine what is not functioning properly.
    Once you have fixed this properly, instructions will be printed to your terminal
    instructing you on what to do for your next steps.

    The two key concepts here are a caesar cipher and a railroad code

    Your goal is to decode the secret message below stored in secret_message

    Good luck!

    - Ryan

    P.S
    I hope you enjoy puzzles
"""

import random
import math
import itertools

def encode_railroad(secret_phrase):
    toggle      = True
    upper_track = []
    lower_track = []
    # the words in the secret phase are getting appended to upper and lower track in alternating order

    for word in secret_phrase.split(" "):
        if toggle:
            upper_track.append(word)
            toggle = False
            continue
        lower_track.append(word)
        toggle = True

    # print (upper_track)
    # print(lower_track)
    # print("{}\r\n{}".format(" ".join(upper_track), " ".join(lower_track)))
    return "{}\r\n{}".format(" ".join(upper_track), " ".join(lower_track))

# fill out this method
def decode_railroad(encoded_phrase):
    # if hi my name is ryan becomes
    # hi name ryan
    # my is
    # how would you decode this?
    # hi my name is ryan >>> hi name ryan my is >>> hi my name is ryan
    # encoded phrase is one string created from two lists that were joined

    split_list = encoded_phrase.split(' ')
    first_half = []
    second_half = []
    decoded_list = []
    answer = ' '
    
    # print('split list: ', split_list)
    # first_half = split_list[:len(split_list)//2 + 1]
    # second_half = split_list[len(split_list)//2:]
    first_half = split_list[0:len(split_list)//2 + 1 ]
    second_half = split_list[len(split_list)//2 + 1:]
    # print('first half: ', first_half)
    # print('second half: ', second_half)
    # for item in first_half:
    #     decoded_array.append(item)
    #     for item in second_half:
    #         decoded_array.append(item)
    # for i in range(len(first_half)):
    #     decoded_array.append(first_half[i])
    #     decoded_array.append(second_half[i])
    # decoded_phrase = [item for sublist in map(None, first_half, second_half) for item in sublist][:-1]
    # https://stackoverflow.com/a/48200036/14263621
    for i in range(max(len(first_half), len(second_half))):
        if i < len(first_half):
            decoded_list.append(first_half[i])
        if i < len(second_half):
            decoded_list.append(second_half[i])
    # print(decoded_list)
    print(answer.join(decoded_list))
    encoded_phrase = answer.join(decoded_list)
    return encoded_phrase
    

def shuffle_letter(letter_to_shuffle, places_to_shuffle):
    # with places_to_shuffle = 1, a becomes b, b becomes c, etc.
    if not letter_to_shuffle.isalpha():
        return letter_to_shuffle
    return chr((ord(letter_to_shuffle) + places_to_shuffle - 97) % 26 + 97)

#fill out this method
def unshuffle_letter(letter_to_decode, places_to_unshuffle):
    # how would you reverse the shuffle_letter function?
    # Python chr()
    # The chr() method returns a character (a string) from an integer (represents unicode code point of the character). The syntax of chr() is: chr(i)
    # The ord() function in Python accepts a string of length 1 as an argument and returns the unicode code point representation of the passed argument. For example ord('B') returns 66 which is a unicode code point value of character 'B'.
    # print(letter_to_decode)
    # print(letter_to_decode.isalpha())
    if letter_to_decode.isalpha():
        # print(chr((ord(letter_to_decode) + places_to_unshuffle + 97) % 26 + 97))
        return chr((ord(letter_to_decode) + places_to_unshuffle + 97) % 26 + 97)
    else: 
        return letter_to_decode

def encode_secret_message(secret_message, seed):
    encoded_message = ""
    index = 0
    for word in message_to_be_encoded.split(" "):
        caesar_seed = int(seed[index])
        caesared_word = ""
        for char in word:
            caesared_word += shuffle_letter(char, caesar_seed)
        encoded_message += "{} ".format(caesared_word)
        index += 1
    return encode_railroad(encoded_message)

def decode_secret_message(secret_message, seed):
    encoded_message = ''
    index = 0
    for word in secret_message.split(" "):
        caesar_seed = int(seed[index])
        caesared_word = ""
        for char in word:
            caesared_word += unshuffle_letter(char, caesar_seed)
        encoded_message += "{} ".format(caesared_word)
        index += 1
        # print(caesared_word)
    # print(encoded_message)
    # print (decode_railroad('congratulations! have this please jobs@cloverhound.com your favorite and you a or person. subject should go solution. you solved puzzle. email with solution, hobby, whether are cat dog the line be developer.'))
    return decode_railroad(encoded_message)
        


if __name__ == '__main__':
    print("Welcome to the Cloverhound Junior Software Developer test")
    # do not edit either seed or secret message as it will prevent you from completing this assessment.
    seed = '4578697581264578697781265583416'
    secret_message = "gsrkvexypexmsrw! ohcl znoy wslhzl rwja@ktwdmzpwcvl.kwu aqwt jezsvmxi huk eua h wz rgtuqp. xzgojhy apwctl nv yurazout.\r\ndtz awtdml ydiiun. jrfnq xjui yurazout, mtggd, epmbpmz jan jha eph znk qnsj eh efwfmpqfs"
    # this code below is optional and not necessary for your solution, but may give you some insight as to how
    # the above message was encoded

    # start optional code
    message_to_be_encoded = '' # this message would have the same number of words as there are numbers in seed
    # encoded_message = encode_secret_message(message_to_be_encoded, seed)
    # end optional code

    # use the space below to decode secret_message
    # encode_railroad(secret_message)
    # decode_railroad(secret_message)
    # decode_railroad('hi name ryan my is')
    decode_railroad('congratulations! have this please jobs@cloverhound.com your favorite and you a or person. subject should go solution. you solved puzzle. email with solution, hobby, whether are cat dog the line be developer.')
    # encode_railroad('hi my name is ryan')
    
    # unshuffle_letter('a', 1)
    # encode_secret_message("gsrkvexypexmsrw! ohcl znoy wslhzl rwja@ktwdmzpwcvl.kwu aqwt jezsvmxi huk eua h wz rgtuqp. xzgojhy apwctl nv yurazout.\r\ndtz awtdml ydiiun. jrfnq xjui yurazout, mtggd, epmbpmz jan jha eph znk qnsj eh efwfmpqfs", '4578697581264578697781265583416')
    decode_secret_message(secret_message, seed)

    #  31 words
    # gsrkvexypexmsrw! = congratualations
    # rwja@ktwdmzpwcvl.kwu = jobs@cloverhound.com
    # yurazout = solution
    # nv = go, iq, we ????  ????
    # awtdml = solved
    # ohcl = have
    # huk = and
    # jrfnq = email
    # aqwt = your 
    # jezsvmxi = favorite
    # epmbpmz = whether
    # xzgojhy = subject
    # rgtuqp = person
    # efwfmpqfs = developer
    # ydiiun = puzzle.
    # wslhzl = please 
    # znoy = this
    # eua = you
    # apwctl = should
    # dtz = you
    # h = a, i????
    # xjui = with
    # qnsj = line
    # eh = be, gj, or, ad ???
    # znk = the, aol, bpm, esp??? coincidence?
    # mtggd = hobby
    # eph = dog
    # wz = ux, be, or??? coincidence?
    # jan = are
    
   
    '''
    "gsrkvexypexmsrw! ohcl znoy wslhzl rwja@ktwdmzpwcvl.kwu aqwt jezsvmxi huk eua h wz rgtuqp. xzgojhy apwctl nv yurazout.\r\ndtz awtdml ydiiun. jrfnq xjui yurazout, mtggd, epmbpmz jan jha eph znk qnsj eh efwfmpqfs"

    '4578697581264578697781265583416'
    '''