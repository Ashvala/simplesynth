Stupid Simple Synth!
=================

The idea is to write a really stupidly simple synth in python that can work over the command line.

Usage:
================

In order to get music, go into the source code and type in the list of notes you want

Usage example: 

note_list = [C,CSharp, Dsharp, E, Fsharp, G]

To indicate that a note should be played up an octave, multiply it by 2.

Example:

note_list = [C*2]

Going down an octave is a matter of dividing the note frequency by 2.

Example: 

note_list = [((C*4)/2)]



