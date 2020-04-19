'''----------------------------------------------------------------------------------------------------

 _______             _         _                                             _______                      
(_______)           (_)       (_)              _                            (_______)                     
 _       _____ ____  _  ___    _       _____ _| |_  ____ _____ ____   ___    _       ___ _   _ _   _  ___ 
| |     (____ |  _ \| |/___)  | |     (____ (_   _)/ ___|____ |  _ \ /___)  | |     / _ ( \ / ) | | |/___)
| |_____/ ___ | | | | |___ |  | |_____/ ___ | | |_| |   / ___ | | | |___ |  | |____| |_| ) X (| |_| |___ |
 \______)_____|_| |_|_(___/   |_______)_____|  \__)_|   \_____|_| |_(___/    \______)___(_/ \_)____/(___/ 

                                                                         /\    /\
   _____      ________________                                          /  ----  \
  /  _  \    /  _  \__    ___/                                            ◣    ◢  
 /  /_\  \  /  /_\  \|    |                                                \  /
/    |    \/    |    \    |                                                 \/
\____|__  /\____|__  /____|                                                 
        \/         \/         

Unit test

----------------------------------------------------------------------------------------------------'''

from Qreader        import Qreader
from Areader        import Areader
from Webscraper_amz import Webscraper_amz

class My_ut:

    def read_questions( self ):
        q = Qreader()

        file_path = '/home/ali/aws_test/1_questions.html'
        csv_file_path = '/home/ali/aws_test/01.csv'

        d = q.get_items( file_path )
        #q.to_csv( d, csv_file_path )

    def read_answers( self ):
        a = Areader()

        file_path = '/home/ali/aws_test/1_answers.html'
        csv_file_path = '/home/ali/aws_test/01a.csv'

        d = {}
        a.get_items( file_path, d )
        #q.to_csv( d, csv_file_path )
        

    def print_qa( self ):
        '''

        '''

        questions_html = '/home/ali/aws_test/1_questions.html'
        answers_html   = '/home/ali/aws_test/1_answers.html'
        qa_csv         = '/home/ali/aws_test/1.csv'
        
        w              = Webscraper_amz( questions_html, answers_html, qa_csv )
        w.run()
        w.print_qa()

    def to_csv( self ):
        questions_html = '/home/ali/aws_test/1_questions.html'
        answers_html   = '/home/ali/aws_test/1_answers.html'
        qa_csv         = '/home/ali/aws_test/1.csv'
        
        w              = Webscraper_amz( )
        w.run( questions_html, answers_html, qa_csv, html_path, topic )
        w.to_csv()


    def to_html( self ):
        questions_html = '/home/ali/aws_test/1_questions.html'
        answers_html   = '/home/ali/aws_test/1_answers.html'
        qa_csv         = '/home/ali/aws_test/1.csv'
        html_path      = '/home/ali/aws_test/1.html'
        topic          = 'Chapter 1: Design Resilient Architectures'

        w              = Webscraper_amz(  )
        w.run( questions_html, answers_html, qa_csv, html_path, topic )

    def convert_all_to_html( self ):
        questions_html = '/home/ali/aws_test/#_questions.html'
        answers_html   = '/home/ali/aws_test/#_answers.html'
        qa_csv         = '/home/ali/aws_test/#.csv'
        html_path      = '/home/ali/aws_test/#.html'
        
        topics         = [ 'Chapter 1: Design Resilient Architectures'
        , 'Chapter 2: Define Performant Architectures'
        , 'Chapter 3: Specify Secure Applications and Architectures'
        , 'Chapter 4: Design Cost-Optimized Architectures'
        , 'Chapter 5: Define Operationally Excellent Architectures'
        ]

        w              = Webscraper_amz(  )
        for i in range( 1, 6 ):
            n = str(i).strip()

            w.run( questions_html.replace( '#', n )
            , answers_html.replace( '#', n )
            , qa_csv.replace( '#', n )
            , html_path.replace( '#', n )
            , topics[ i - 1] )




#----------------------------------------------------------------------------------

if __name__ == '__main__':
    my_ut = My_ut()

    #my_ut.read_questions()
    #my_ut.read_answers()
    #my_ut.print_qa()
    #my_ut.to_csv()
    #my_ut.to_html()
    my_ut.convert_all_to_html()

    print( '\n\n end.' )