"""
    Silly Text Logos to display after a script ends.
    I made these on an online ascii art generator here: https://asciiartgen.now.sh/
    If 'Scottware' is a registered trade mark no infringment is intended.
    20190127 - pylint score of 10/10.
"""

from random import choice

LOGO = r"""
 _______ _______  _____  _______ _______ _  _  _ _______  ______ _______
 |______ |       |     |    |       |    |  |  | |_____| |_____/ |______
 ______| |_____  |_____|    |       |    |__|__| |     | |    \_ |______"""

LOGO2 = r"""
:::===  :::===== :::====  :::==== :::==== :::  ===  === :::====  :::====  :::=====
:::     :::      :::  === :::==== :::==== :::  ===  === :::  === :::  === :::     
 =====  ===      ===  ===   ===     ===   ===  ===  === ======== =======  ======  
    === ===      ===  ===   ===     ===    ===========  ===  === === ===  ===     
======   =======  ======    ===     ===     ==== ====   ===  === ===  === ========"""

LOGO3 = r"""
  .dBBBBP     dBBBP     dBBBBP  dBBBBBBP  dBBBBBBP     dBP   dBP  dBBBBBb   dBBBBBb     dBBBP 
  BP         dBP       dBP.BP     dBP       dBP       dBP   dBP        BB       dBP    dBP       
  `BBBBb    dBP       dBP.BP     dBP       dBP       dBPdBPdBP     dBP BB   dBBBBK    dBBP    
     dBP   dBP       dBP.BP     dBP       dBP       dBPdBPdBP     dBP  BB  dBP  BB   dBP      
dBBBBP'   dBBBBP    dBBBBP     dBP       dBP       dBBBBBBBP     dBBBBBBB dBP  dB'  dBBBBP"""

LOGO4 = r"""
  __                                        
 (_    _   _   _|_  _|_         _.  ._   _  
 __)  (_  (_)   |_   |_  \/\/  (_|  |   (/_ """

LOGO_INVENTORY = [LOGO, LOGO2, LOGO3, LOGO4]

def get_a_random_logo():
    """ Return a random Logo """
    return choice(LOGO_INVENTORY)

if __name__ == "__main__":
    print("Here are the logo's we currently have")
    for logo in LOGO_INVENTORY:
        print(logo)

    print("\nHere is a random logo: \n{}".format(get_a_random_logo()))
