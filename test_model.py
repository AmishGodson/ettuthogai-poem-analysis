from ettuthogai_validator import validate_poem

ett_poem = "கார்வானம் கொண்டனைப் பொன்னேர் புதுமலர்த் தாரன்"
non_poem = "அறம் பொருள் இன்பம் வீடு அடைதல்"

print("Ettuthogai:", validate_poem(ett_poem))
print("Non-Ettuthogai:", validate_poem(non_poem))
