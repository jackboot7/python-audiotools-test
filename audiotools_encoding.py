# -*- config:utf-8 -*-

"""
Dummy project to test Python Audio Tools encoding capabilities.

"""


import audiotools

def print_progress (amount_processed, total_amount):
    print "%d%%" % (amount_processed * 100 / total_amount)


def encode(input_file, meta, progress=print_progress):

    input = audiotools.open(input_file)

    # Metadata for output files.
    meta = audiotools.MetaData( **meta)

    filename = u'%02d %s' % (meta.track_number, meta.track_name)
    # Convert input_file to output formats including metadata
    

    #   Conversion from WAV to MP3
    #   The COMPRESSION_MODE[10] corresponds to lame's "--preset
    #   insane" which is the same as lame's "-b 320" producing 320kbps
    #   mp3s. 
    #   
    input.convert((u'%s.mp3' % filename), 
                    audiotools.MP3Audio,
                    compression=audiotools.MP3Audio.COMPRESSION_MODES[10],
                    progress=progress).set_metadata(meta)


    #   Conversion from WAV to FLAC
    #   The COMPRESSION_MODE[8] corresponds to the most amount of
    #   compression but at the slowest compression speed
    #
    input.convert((u'%s.flac' % filename), 
                    audiotools.FlacAudio,
                    compression=audiotools.FlacAudio.COMPRESSION_MODES[8],
                    progress=progress).set_metadata(meta)

    #   Conversion from WAV to AAC
    #   Using the faac binary. The COMPRESSION_MODE[3] corresponds to
    #   the default value of the faac encoder,  averages at approx.
    #   120 kbps VBR for a normal stereo input file.
    #
    input.convert((u'%s.m4a' % filename),
                    audiotools.M4AAudio_faac,
                    compression=audiotools.M4AAudio_faac.COMPRESSION_MODES[3],
                    progress=progress).set_metadata(meta)



meta = {    'track_number':1,
            'track_name':u'Swords',
            'album_name':u'Conatus',
            'artist_name':u'Zola Jesus' }

encode('swords.wav', meta )
