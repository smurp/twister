twister
=======

a party game which calls out amusing commands


usage:
------
    e.g.
       twister.py 
          A game of twister where you keep track of whose turn it is.

       twister.py --wait 3 --players Alice,Bob --voice Alex
          A two player game with 3 seconds between turns, spoken by Alex.

       twister.py --voices Agnes,Cello
          Spoken randomly by Agnes and Cello

    
options:
--------
      -h, --help         show this help message and exit
      --doctest          perform doc tests
      --man              show the manual for this program
      -v, --verbose      be verbose in all things
      -V, --version      show version
      --wait=WAIT        the number of seconds between turns, default 4
      --players=PLAYERS  comma delimited list of players, eg Alice,Bob,Carol
      --voice=VOICE      specify one of Alex,Agnes or a random one will be used
      --speech=SPEECH    the speech command (for OSes other than OSX)
      --voices=VOICES    voices to randomly choose from, default: Alex,Agnes
