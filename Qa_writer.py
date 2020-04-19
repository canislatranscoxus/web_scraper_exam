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

description:

----------------------------------------------------------------------------------------------------'''

import os

class Qa_writer:

    header = ''
    footer = ''

    qa_template = '''
    <li class="essay">
    <div class="question">
    <p><span epub:type="pagebreak" role="doc-pagebreak" id="Page_54"></span>{}</p>
    <ol id="c02-list-0001" type="A">
    <li>{}</li>
    <li>{}</li>
    <li>{}</li>
    <li>{}</li>
    </ol></div>
    </li>
    <button class="accordion">answer</button>
    <div class="panel">
    <p>{}
    </p>
    </div>
    '''

    qa_templateX = '''
    <li class="essay">
    <div class="question">
    <p><span epub:type="pagebreak" role="doc-pagebreak" id="Page_54"></span>{}</p>
    <ol id="c02-list-0001" type="A">
    <li>A</li>
    <li>B</li>
    <li>C</li>
    <li>D</li>
    </ol></div>
    </li>
    <button class="accordion">answer</button>
    <div class="panel">
    <p>#explanation
    </p>
    </div>
    '''

    def to_html( self, d, html_path, topic ):
        try:
            '''print( '\n\n' )
            print( '\n\n Qawriter.to_html() ... begin' )
            print( 'html_path: {}'.format( html_path) ) '''


            with open( html_path, 'w'  ) as f:
                f.write( self.header.replace( '#topic', topic ) )

                #print( 'Qa_writer.to_html(), ... dictionary has {} elements'.format( len( d ) ) )

                s = self.qa_template
                for key, q in d.items():
                    #print( '{} *** {} **** '.format( q.number, q.question ) )

                    s = self.qa_template.format( q.question, q.a, q.b, q.c, q.d, q.explanation )
                    f.write ( s )


                #print( 'writing footer...' )
                #print( self.footer )
                f.write( self.footer )

            print( 'Qa_writer.to_html(), file created: {}'.format( html_path ) )

        except Exception as e:
            print( 'Qa_writer.to_html(), error:{}'.format( e ) )

    def __init__( self ):
        dir = '/home/ali/prg/web_scraper_exam'
        header_path = os.path.join( dir, 'header.txt')
        footer_path = os.path.join( dir, 'footer.txt')
        

        try:
            with open( header_path, 'r' ) as h:
                self.header = h.read()

            with open( footer_path, 'r' ) as f:
                self.footer = f.read()

        except Exception as e:
            print( 'Qa_writer.__init__(), error:{}'.format( e ) )
