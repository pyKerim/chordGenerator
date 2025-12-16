from chords import enharmonics


def input_normalisation(user_input):
    cleaned = user_input.title().replace(',', ' ').strip().split()
    print(f"After title: {cleaned}")  # Debug line
    normalized = [enharmonics.get(note, note) for note in cleaned]
    print(f"After enharmonics: {normalized}")  # Debug line
    return list(set(normalized))
