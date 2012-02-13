# -*- config:utf-8 -*-

"""
Dummy project to test Python Audio Tools encoding capabilities.

"""


import audiotools

def print_progress (amount_processed, total_amount):
    print "%d%%" % (amount_processed * 100 / total_amount)


def encode(input_file, progress=print_progress, **kwargs):

    input = audiotools.open(input_file)
    filename = input_file.rsplit('.', 1)[0]

    # Metadata for output files.
    meta = audiotools.MetaData()
    meta.track_name =  'Swords'
    meta.artist_name = 'Zola Jesus'

    
    # Convert input_file to output formats including metadata
    

    #   Conversion from WAV to MP3
    #   The COMPRESSION_MODE[10] corresponds to lame's "--preset
    #   insane" which is the same as lame's "-b 320" producing 320kbps
    #   mp3s. 
    #   
    input.convert(filename+'.mp3', 
                    audiotools.MP3Audio,
                    compression=audiotools.MP3Audio.COMPRESSION_MODES[10],
                    progress=progress).set_metadata(meta)


    #   Conversion from WAV to FLAC
    #   The COMPRESSION_MODE[8] corresponds to the most amount of
    #   compression but at the slowest compression speed
    #
    input.convert(filename+'.flac', 
                    audiotools.FlacAudio,
                    compression=audiotools.FlacAudio.COMPRESSION_MODES[8],
                    progress=progress).set_metadata(meta)

    #   Conversion from WAV to AAC
    #   Using the faac binary. The COMPRESSION_MODE[3] corresponds to
    #   the default value of the faac encoder,  averages at approx.
    #   120 kbps VBR for a normal stereo input file.
    #
    input.convert(filename+'.m4a',
                    audiotools.M4AAudio_faac,
                    compression=audiotools.M4AAudio_faac.COMPRESSION_MODES[3],
                    progress=progress).set_metadata(meta)



encode('swords.wav')
