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


description: This is the main webscraper script. Here we create instances of Question reader and Answer reader,
             then extract the data of the html files and create a new html with questions and answers.
----------------------------------------------------------------------------------------------------'''
import csv
from Qreader   import Qreader
from Areader   import Areader
from Qa_writer import Qa_writer

class Webscraper_amz:
    d              = None

    # file paths
    questions_html = '' 
    answers_html   = ''
    qa_csv         = ''
    html_path      = ''

    def to_csv( self  ):
        try:
            with open( self.qa_csv, 'w',  newline='') as f:
                writer = csv.writer( f  )

                for key, q in self.d.items():
                    s = [ q.number, q.question, q.a, q.b, q.c, q.d, q.correct_answer, q.explanation ]
                    #print( s )
                    writer.writerow( s )        

        except Exception as e:
            print( 'Webscraper_amz.to_csv(), error:{}'.format( e ) )
            
    def print_qa( self ):
        try:
            for key, q in self.d.items():
                #s = '{}.{}. A){} B){} C){} D{} *** Exp:{} '.format( q.number, q.question[ : 10 ], q.a[ : 10], q.b[ : 10], q.c[ : 10], q.d[ : 10], q.explanation[ : 10] )
                print ( '{}. {} '.format( q.number, q.question[ : 30 ] ) )
                print( '\tA) {} \n\tB) {} \n\tC) {} \n\tD) {} '.format( q.a, q.b, q.c, q.d ) )
                print( q.correct_answer )
                print( q.explanation )
                print( '\n' )

        except Exception as e:
            print( 'Webscraper_amz.print_qa(), error:{}'.format( e ) )
                

    def run( self, questions_html, answers_html, qa_csv=None, html_path=None, topic=None ):
        try:
            self.questions_html = questions_html 
            self.answers_html   = answers_html    
            self.qa_csv         = qa_csv
            self.html_path      = html_path
            self.topic          = topic

            qreader  = Qreader()
            areader  = Areader()
            qawriter = Qa_writer()

            self.d   = {}
            self.d   = qreader.get_items( questions_html )
            
            #print( 'webscraper.run(), d size: {}'.format( len( self.d ) )  )

            areader.get_items( answers_html, self.d  )
            qawriter.to_html( self.d, html_path, self.topic )

        except Exception as e:
            print( 'Webscraper_amz.run(), error:{}'.format( e ) )


    def __init__(self ):
        #print( 'webscraper created' )
        None

questions_html = '/home/ali/aws_test/1_questions.html'
answers_html   = '/home/ali/aws_test/1_answers.html'
qa_csv         = '/home/ali/aws_test/1.csv'
html_path      = '/home/ali/aws_test/1.html'

