mijn_prijzen = {"aardbei" : 3, "vanille" : 4, "chocolade" : 5}
aanbieding = mijn_prijzen["vanille"] * 0.8
reclame_tekst = f"{round(aanbieding,2)}"
reclame_tekst2 = f"vandaag in de aanbieding: vanille, 1 liter - slechts €{reclame_tekst}."
reclame_tekst3 = (f"vandaag in de aanbieding: vanille,, 1 liter - slechts €{reclame_tekst}.".upper())
reclame_tekst4 = reclame_tekst3
for el in reclame_tekst4:
    if len(reclame_tekst3) >= 5:
        print(el.upper())
    else:
        print(el.lower())