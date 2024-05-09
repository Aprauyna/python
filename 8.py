# #function and inputs

# def greet(name):   #here name is parameter
#     print(f"hello {name}")

# name=input("enter name\n")
# greet(name)        #here name is argument


# def details(name,location):
#     print(f"{name} and {location}")

# details("Arun","Pune")

############################################################################
# import math
# def pain_cal(height,width,cover):
#     num_cams=(height*width)/cover
#     # no_of_cans=round(num_cams)
#     no_of_cans=math.ceil(num_cams)
#     print(f"we need cans for painting {no_of_cans}")

# height=int(input("enter height\n"))
# width=int(input("enter width\n"))
# cover=int(input("enter cover\n"))
# pain_cal(height,width,cover)


#############################################################################

# import math

# def check_number(number):
#     if number%2==0:
#         print(f"{number} is prime")
#     else:
#         print(f"{number} is odd")

# even_odd=False
# while not False:
#     number=int(input("enter number to check even or odd for exit enter 0\n"))
#     if number==0:
#         exit(1)
#     check_number(number)

##################################################################################
#encryption

# def encryption(text,shift):
#     cipher_text=""
#     for char in text:
#         position=alphabet.index(char)
#         new_position=position+shift

#         cipher_text+=alphabet[new_position]
#     print(cipher_text)


# def decryption(text,shift):
#     cipher_text=""
#     for char in text:
#         position=alphabet.index(char)
#         new_position=position-shift

#         cipher_text+=alphabet[new_position]
#     print(cipher_text)


# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# direcction=input("enter 'encrypt' for encryption and 'decrypy' for decryption\n")
# text=input("enter your message\n").lower()
# shift=int(input("enter number of shfit\n"))

# if direcction=="encrypt":
#     encryption(text,shift)
# elif direcction=="decrypt":
#     decryption(text,shift)
# else:
#     print("invalid")
#     exit(1)

#################################################################################################
def enc_dec(text,shift,direcction):
    we_got=""
    if direcction=="decrypt":
        shift*=-1
    for letter in text:
        position=alphabet.index(letter)
        new_position=position+shift
        we_got+=alphabet[new_position]
    print(we_got)



alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direcction=input("enter 'encrypt' for encryption and 'decrypt' for decryption\n")
text=input("enter your message\n").lower()
shift=int(input("enter number of shfit\n"))

enc_dec(text,shift,direcction)




