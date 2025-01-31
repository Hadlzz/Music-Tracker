import pretty_midi


#note density function
def note_density(midi_file):
    MAXIMUM_DENSITY = 1
    MAXIMUM_DENSITY = 20

    #load the midi file
    midi_data = pretty_midi.PrettyMIDI("Laufey.mid")
    #extract duration from midi file
    duration = midi_data.get_end_time()
    print(duration)
    #extract the total number of notes in the midi file
    total_notes = sum(len(instrument.notes) for instrument in midi_data.instruments)
    print(total_notes)
    #calculate note density
    note_density = total_notes / duration

    normalized_density = ((note_density - MAXIMUM_DENSITY) /(MAXIMUM_DENSITY - MAXIMUM_DENSITY))* 10

    return normalized_density


midi_file = "Laufey.mid"
density = note_density(midi_file)
#round density to a whole number
density = int(density)

print("The Density Level out of ten for this piece is:" , density)

