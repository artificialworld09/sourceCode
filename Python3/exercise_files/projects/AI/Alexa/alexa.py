import wikipedia # pip install wikipedia
from take import takecommand as tak
from translate import tran
from speak import speak as spk
from default import speak2 as sp

data=tak().lower()

if "how are you" in data:
    spk("मैं ठीक हूं सर")
elif "who are you" in data:
    spk("मैं एक कंप्यूटर प्रोग्राम हूँ, मेरा नाम एलेक्सा है")
elif "how old are you" in data:
    spk("मैं अठारह साल की हूँ सर")
elif "what is your name" in data:
    spk("मेरा नाम एलेक्सा है, आप मुझे कंप्यूटर कह सकते हैं सर")
elif "where are you from" in data:
    spk("मैं भारत से हूँ सर")
elif "who is your owner" in data:
    spk("अब्दुल जोहा सर मेरे मालिक हैं")
elif "will you marry me" in data:
    spk("मैं एक कंप्यूटर प्रोग्राम हूँ तो मैं आपसे शादी कैसे कर सकती हूँ")
elif "i love you" in data:
    spk("यह मेरी किस्मत है कि आप मुझसे प्यार करते हो, मुझे भी आपसे बहुत प्यार है")

elif 'wikipedia' in data:
    print("searching wikipedia")
    sp("विकिपीडिया पर खोजा जा रहा है")
    query=data.replace("wikipedia", "")
    result=wikipedia.summary(query, sentences=2)
    txt=tran(result)
    print("according to wikipedia")
    sp("विकिपीडिया के अनुसार")
    print(result)
    sp(txt)