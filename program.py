inventory = []
name = input("Vad är ditt namn?")

greeting = "Välkommen, [name]. Du drack lite för mycket igår, och när du börjar vakna till, inser du att du befinner dig på en okänd plats."
print(greeting)
input("Tryck ENTER för att fortsätta..")

print("Du anser att du bör göra någonting innan någonting dåligt sker.")
choice = input("Vad gör du? [titta runt]/[gå tillbaka till sömns]").lower()
if "gå tillbaka till sömns" in choice:
    print("Du försöker gå tillbaka till sömns, men du kan för någon anledning inte somna om. Därför bestämmer du dig för att titta runt istället.")
    input("Tryck ENTER för att fortsätta..")
    
print("Du sätter dig upp, och ser att det mörka rummet du nu befinner dig i är likt en gammal fängelsehåla.")
print("De grova stenväggarna ger hålan en klaustrofobisk känsla, och utrymmet är endast stort nog för en person.")
print("Luften är fuktig och tung, det känns som att frisk luft aldrig kommer ner hit.")
input("Tryck ENTER för att fortsätta")
print("Du tittar ner på det våta stengolvet som du nyss sovit på, och du märker en nyckel vid sidan om dig.")
print("Du tar upp den och lägger den fickan")
print("Nyckel skaffad!")
inventory.append("nyckel")    

