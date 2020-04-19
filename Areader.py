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

description: this class is Answers reader. This class read an html file and extract the answers and 
             explanation.
----------------------------------------------------------------------------------------------------'''

import csv
import re

from bs4     import BeautifulSoup
from Qitem   import Qitem

class Areader:

    def get_items( self, file_path, d = None ):
        i = 1
        try:
            if d == None:
                print( 'Areader.get_items(). d is empty' )

                d = {}

            with open( file_path ) as fp:
                soup    = BeautifulSoup(fp)
                answers = soup.find( 'ol' )
                pattern = re.compile( '(\w(,\s\w)*\.).*' )

                for a in answers.find_all( 'li' ):

                    qitem = None
                    if i in d:
                        qitem = d[ i ]
                    else:
                        qitem           = Qitem()
                        qitem.number    = i

                    s = pattern.search( a.text )
                    if s != None:
                        qitem.correct_answer = s.group( 1 )

                    qitem.explanation   = a.text
                    
                    #print( '\n\n {}. {} \n{}'.format( i, qitem.question, qitem.explanation ) )

                    i = i + 1
                    '''if i == 5:
                        break
                    '''
                    
                    
            return d            
        except Exception as e:
            print( 'Areader.get_items(), number:{}. error:{}'.format(i, e ) )
                
# ---------------------------------------------------------------------------------------------------------


