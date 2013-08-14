#!/usr/bin/python
__version__='0.1.0'
__doc__ = """
twister.py speaks random things aloud like `Dave put your right foot on blue`
"""
import sys
import os
import random
import time

default_voices = 'Alex,Agnes'
default_wait = 4

def choose(lst):
    return random.choice(lst)

def play(options):
    players = options.players.split(',') or []
    tmpl = "%(speech_command)s    " \
        "%(player)s put your %(side)s %(extremity)s on %(color)s"
    player = ""
    player_idx = 0
    while True:
        if players:
            player = players[player_idx]
            if player:
                player += ',' 
            player_idx += 1
            if player_idx == len(players):
                player_idx = 0
        voice = options.voice
        if options.voice:
            voice = options.voice
        else:
            voice = choose(options.voices.split(','))
        if options.speech:
            speech_command = options.speech
        else:
            speech_command = "say --voice %(voice)s" % locals()
        side = choose(['left','right'])
        color = choose(['green','red','yellow','blue'])
        extremity = choose(['hand','foot'])
        sentence = tmpl % locals()
        print sentence
        os.system(sentence)
        time.sleep(options.wait)


if __name__ == "__main__":        
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "--doctest",
        action = 'store_true',
        help = "perform doc tests")
    parser.add_option(
        "--man",
        action = 'store_true',
        help = "show the manual for this program")
    parser.add_option(
        "-v","--verbose",
        action = 'store_true',
        help = "be verbose in all things")
    parser.add_option(
        "-V","--version",
        action = 'store_true',
        help = "show version")
    parser.add_option(
        "--wait",
        type="int",
        default = default_wait,
        help = "the number of seconds between turns, default %s" % default_wait)
    parser.add_option(
        "--players",
        default = "",
        help = "comma delimited list of players, eg Alice,Bob,Carol")
    parser.add_option(
        "--voice",
        #default = default_voices.split(',')[0],
        help = "specify one of %(default_voices)s or a random one will be used" % locals())
    parser.add_option(
        "--speech",
        help = "the speech command (for OSes other than OSX)")
    parser.add_option(
        "--voices",
        default = default_voices,
        help = "voices to randomly choose from, default: %s" % default_voices)
    parser.version = __version__
    parser.usage =  """
    e.g.
       %prog 
          A game of twister where you keep track of whose turn it is.

       %prog --wait 3 --players Alice,Bob --voice Alex
          A two player game with 3 seconds between turns, spoken by Alex.

       %prog --voices Agnes,Cello
          Spoken randomly by Agnes and Cello

    """
    (options,args) = parser.parse_args()
    show_usage = True
    
    if options.doctest:
        show_usage = False
        import doctest
        doctest.testmod(verbose=options.verbose)
        sys.exit()
    if options.version:
        show_usage = False
        if options.verbose:
            print __cvs_id__
        else:
            print parser.version
        sys.exit()
    if options.man:
        show_usage = False
        import pydoc
        pydoc.help(__import__(__name__))
        sys.exit()
    if show_usage:
        parser.print_usage()

    play(options)
