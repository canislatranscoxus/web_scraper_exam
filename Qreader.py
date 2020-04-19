'''----------------------------------------------------------------------------------------------------

 _______             _         _                                             _______                      
(_______)           (_)       (_)              _                            (_______)                     
 _       _____ ____  _  ___    _       _____ _| |_  ____ _____ ____   ___    _       ___ _   _ _   _  ___ 
| |     (____ |  _ \| |/___)  | |     (____ (_   _)/ ___|____ |  _ \ /___)  | |     / _ ( \ / ) | | |/___)
| |_____/ ___ | | | | |___ |  | |_____/ ___ | | |_| |   / ___ | | | |___ |  | |____| |_| ) X (| |_| |___ |
 \______)_____|_| |_|_(___/   |_______)_____|  \__)_|   \_____|_| |_(___/    \______)___(_/ \_)____/(___/ 

                                                                         /\ ___/\
   _____      ________________                                          /        \
  /  _  \    /  _  \__    ___/                                         /  ◣    ◢  \
 /  /_\  \  /  /_\  \|    |                                           /---      ---\  
/    |    \/    |    \    |                                                \  /
\____|__  /\____|__  /____|                                                 \/
        \/         \/         


description: this class is a Question reader. This class read an html file and extract the questions with 
             and the multiple options.


----------------------------------------------------------------------------------------------------'''

import csv
from bs4     import BeautifulSoup

from Qitem   import Qitem


class Qreader:

    def get_items( self, file_path ):
        i = 1
        try:

            d = {}
            with open( file_path ) as fp:
                soup = BeautifulSoup(fp)

                for q in soup.find_all('div'):

                    if q == None:
                        #print( 'Qreader.get_items(), q is None' )
                        continue
                    elif q.p == None:
                        #print( 'Qreader.get_items(), question number: {}, q.p is None'.format( i ) )
                        continue

                    qitem           = Qitem()
                    qitem.number    = i
                    qitem.question  = q.p.text
                    options         = q.find_all('li')
                    qitem.a         = options[ 0 ].text
                    qitem.b         = options[ 1 ].text
                    qitem.c         = options[ 2 ].text
                    qitem.d         = options[ 3 ].text
                    
                    d[ i ] = qitem 

                    #print( '\n {}. {}'.format( i, qitem.question ) )

                    ''' 
                    letter = 65
                    for opt in options:
                        print( '\n{}) {}'.format( chr( letter ), opt.text ) )
                        letter = letter + 1 
                    '''


                    i = i +1
                    '''if i == 5:
                        break
                    '''

            return d            
        except Exception as e:
            print( 'Qreader.get_items(), number:{}. error:{}'.format(i, e ) )
            raise


# -----------------------------------------------------------------------------------------------------
