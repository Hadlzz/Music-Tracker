import pretty_midi

def get_tempo(midi_file):
    midi_data = pretty_midi.PrettyMIDI(midi_file)
    
    # Get tempo changes (times and BPM values)
    tempo_times, tempo_values = midi_data.get_tempo_changes()

    if len(tempo_values) == 1:
        return tempo_values[0]  # Return a single tempo if it doesn't change
    else:
        average_tempo = sum(tempo_values) / len(tempo_values)  # Average tempo for variable tempo
        return round(average_tempo, 2)

midi_file = "Laufey.mid"
tempo = get_tempo(midi_file)

print(f"The tempo of the piece is approximately {tempo} BPM")