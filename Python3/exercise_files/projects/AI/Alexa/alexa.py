import wikipedia # pip install wikipedia
from take import takecommand as tak
from speak import speak as spk
from default import speak2 as sp

data=tak().lower()

if "alexa how are you" in data:
    spk("मैं ठीक हूं सर")
elif "who are you" in data:
    spk("मैं एक कंप्यूटर प्रोग्राम हूँ, मेरा नाम एलेक्सा है")
elif "how old are you" in data:
    spk("मैं अठारह साल की हूँ सर")
elif "what is your name" in data:
    spk("मेरा नाम एलेक्सा है, आप मुझे कंप्यूटर कह सकते हैं सर")
elif "where are you from" in data:
    spk("मैं भारत से हूँ सर")

elif 'wikipedia' in data:
    print("searching wikipedia")
    sp("searching wikipedia")
    query=data.replace("wikipedia", "")
    result=wikipedia.summary(query, sentences=2)
    print("according to wikipedia")
    sp("according to wikipedia")
    sp(result)
    print(result)