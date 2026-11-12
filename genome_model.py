from sklearn.tree import DecisionTreeClassifier

# Assignment training dataset
sequences = [
    "ATGCGATC",
    "ATGCGTAC",
    "GCGCGTAT",
    "GCGCGCGC"
]

groups = ["A", "A", "B", "B"]


# Extract DNA features
def extract_features(sequence):
    sequence = sequence.upper().strip()

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    length = len(sequence)
    gc_content = ((g + c) / length) * 100

    return [a, t, g, c, length, gc_content]


# Train the classifier
def train_model():
    X = [extract_features(s) for s in sequences]

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, groups)

    return model


model = train_model()


# Predict a new DNA sequence
def predict_sequence(sequence):
    sequence = sequence.upper().strip()

    if not sequence:
        raise ValueError("Please enter a DNA sequence.")

    if any(base not in "ATGC" for base in sequence):
        raise ValueError("Only A, T, G and C are allowed.")

    features = extract_features(sequence)

    prediction = model.predict([features])[0]

    return prediction, features