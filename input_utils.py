from chords import enharmonics

def input_normalisation(user_input):
    cleaned = user_input.title().replace(',', ' ').strip().split()
    # Convert enharmonics (A# → Bb, etc)
    normalized = [enharmonics.get(note, note) for note in cleaned]
    return list(set(normalized))