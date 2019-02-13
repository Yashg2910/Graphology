def summary(msg):
    sum = ""
    baseline_sum = get_baseline_sum(msg["Baseline_Angle"])
    margin_sum = get_margin_sum(msg["Top_margin"])
    size_sum = get_letter_size_sum(msg["Letter_Size"])
    line_sum = get_line_spacing_sum(msg["Line_Spacing"])
    word_sum = get_word_spacing_sum(msg["Word_Spacing"])
    pressure_sum = get_pressure_sum(msg["Pen_Pressure"])
    slant_sum = get_slant_angle_sum(msg["Slant"])

    sum = "#" +baseline_sum+margin_sum+size_sum+line_sum+ word_sum+ pressure_sum+ slant_sum
    return sum

def get_baseline_sum(base_angle):

    sum = ""

    if base_angle == "DESCENDING":
        sum = "Pessimistic, mental tiredness"
    elif base_angle == "ASCENDING":
        sum = " Optimistic, hopefulness, cheerfulness, Active, Excitability"
    elif base_angle == "STRAIGHT":
        sum = "Balanced, stable, realism, disciplined"
    sum = sum+" #"
    return sum

def get_margin_sum(top_margin):
    sum = ""
    if top_margin == "MEDIUM OR BIGGER":
        sum = "courageous, self-disciplined, balanced"
    elif top_margin == "NARROW":
        sum = "Insecure and devotes onself completely"
    sum = sum + " #"
    return sum

def get_letter_size_sum(letter_size):
    sum = ""
    if letter_size == "BIG":
        sum = "extroversion and overindulgence"
    elif letter_size == "SMALL":
        sum = "seclusion and shyness"
    elif letter_size == "MEDIUM":
        sum = "c"
    sum = sum + " #"
    return sum

def get_line_spacing_sum(line_spacing):
    sum = ""
    if line_spacing == "BIG":
        sum = "a"
    elif line_spacing == "SMALL":
        sum = "b"
    elif line_spacing == "MEDIUM":
        sum = "c"
    sum = sum + " #"
    return sum

def get_word_spacing_sum(word_spacing):
    sum = ""
    if word_spacing == "BIG":
        sum = "discrimination, independence, good taste, exclusiveness, snobbery, pride"
    elif word_spacing == "SMALL":
        sum = " inability to be alone, poor taste, friendliness."
    elif word_spacing == "MEDIUM":
        sum = ""
    sum = sum + " #"
    return sum

def get_pressure_sum(pen_pressure):
    sum = ""
    if pen_pressure == "HEAVY":
        sum = "Energetic, active, anxious, vigorous, angry, alert, punctuate"
    elif pen_pressure == "LIGHT":
        sum = "calmness, passivity, lack of energy"
    elif pen_pressure == "MEDIUM":
        sum = "Feelings not very intense"
    sum = sum + " #"
    return sum

def get_slant_angle_sum(slant_angle):

    sum = ""
    if slant_angle == "EXTREMELY RECLINED":
        sum = " Fear of future, defensive, early rejection"
    elif slant_angle == "A LITTLE OR MODERATELY RECLINED":
        sum = "Relective, independent, not sympathetic, difficulty in adapting and expressing emotions"
    elif slant_angle == "A LITTLE INCLINED":
        sum = "Expressive , confidence in conviction, freedom of thoughts, extrovert, future orientation"
    elif slant_angle == "MODERATELY INCLINED":
        sum = "Expressive , confidence in conviction, freedom of thoughts, extrovert, future orientation"
    elif slant_angle == "EXTREMELY INCLINED":
        sum = "lack of self-control, impulsive, unrestrained, intense, expressive, low frustration tolerance"
    elif slant_angle == "STRAIGHT":
        sum = "head controls over heart, independent, emotional nature, works independently"
    elif slant_angle == "IRREGULAR":
        sum = "Emotionally unstable"
    sum = sum + ""
    return sum