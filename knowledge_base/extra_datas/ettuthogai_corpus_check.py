def corpus_match(poem_text):
    sangam_markers = [
        "மலர்", "கார்", "முல்லை", "காடு", "மழை",
        "தலைவி", "தலைவன்", "அகம்", "யானை", "மலை"
    ]

    for word in sangam_markers:
        if word in poem_text:
            return True

    return False
