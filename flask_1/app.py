from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of words to generate business names
# List of words to generate business names
words = [
    "Tech", "Innovate", "Solutions", "Digital", "Global", "Creative", "Web", "Design", "Consulting", "Group",
    "Smart", "Data", "Strategy", "Marketing", "Infinite", "Fusion", "Nexa", "Eco", "Pro", "Quantum",
    "Cloud", "Savvy", "Bright", "Logic", "Synergy", "Vision", "Strive", "Optimize", "Growth", "Edge",
    "Pioneer", "Discover", "Precision", "Success", "Momentum", "Insight", "Revolution", "Dynamic", "Synergy", "Inspire",
    "Agile", "Strategic", "Enhance", "Imagine", "Collaborate", "Invent", "Supreme", "Nexus", "Infinity", "Futurist",
    "Prosper", "Maximize", "Elevate", "Pathfinder", "Infinite", "Harmony", "Synergize", "Magnetic", "Paragon", "Vanguard",
    "Pinnacle", "Phenomenal", "Radiant", "Horizon", "Ethereal", "Apex", "Epic", "Catalyst", "Integrate", "Ambition",
    "Sustain", "Thrive", "Transcend", "Aim", "Connect", "Boost", "Ascend", "Horizon", "Evolv", "Impact",
    "Unify", "Global", "Spectrum", "Bliss", "Empower", "Spirit", "Immerse", "Fortify", "Stratos", "Novus",
    "Adapt", "Reimagine", "Echelon", "Influence", "Prospect", "Vertex", "Innovent", "Maxim", "Genesis", "Quasar",
    "Quest", "Globex", "Infini", "Envision", "Epicure", "Solstice", "Renova", "Spiritus", "Nexen", "Stellar",
    "Phenix", "Terra", "Omnium", "Uplift", "Etherean", "Infinity", "Revive", "Evolv", "Ephemeral", "Syntrix",
    "Quantix", "Venture", "Zenith", "Prism", "Fusion", "Metron", "Synthesis", "Optix", "Futurum", "Revera",
    "Zenovation", "Echelon", "Metrolinx", "Equinox", "Novelix", "Evolvix", "Aurora", "Nexicon", "Futurix", "Prima",
    "Infinitech", "Omniway", "Integrify", "Innovisio", "Evolvify", "Supernova", "Quasarix", "Omnixion", "Horizonix", "Solixus",
    "Upliftix", "Innoventure", "Phenixen", "Futuromix", "Harmonix", "Reverix", "Nexorion", "Synchronex", "Fusionix", "Echelonia",
    "Evolvixion", "Optilife", "Futurumix", "Innovia", "Optifuse", "Synthix", "Paragonix", "Evolva", "Harmonixus", "Integrix",
    "Solixify", "Upliftrix", "Innoventrix", "Innoviax", "Omnibiz", "Optixify", "Stratex", "Reverify", "Nexify", "Syntrixus",
    "Evolvixify", "Nexiway", "Fusionova", "Omniaxion", "Harmonify", "Echelonify", "Omnirise", "Innovafuse", "Innofix", "Novelify",
    "Evolvion", "Paragonova", "Evolvano", "Echelify", "Innoventova", "Synchronova", "Fusionixus", "Optisync", "Echelix", "Evolvia",
    "Epicify", "Innoventify", "Nexifyx", "Futurovix", "Harmonixify", "Reverixus", "Evolvixifyx", "Optilifex", "Futurumixify", "Innoviaxi",
    "Optifusify", "Synthixify", "Paragonixify", "Evolvafy", "Harmonixusify", "Integrixify", "Solixifyx", "Upliftrixify", "Innoventrixify", "Innoviaxy"
]

# Rest of the code remains the same

@app.route("/", methods=["GET", "POST"])
def generate_name():
    if request.method == "POST":
        business_name = generate_business_name()
    else:
        business_name = ""

    return render_template("index.html", business_name=business_name)

def generate_business_name():
    random_words = random.sample(words, random.randint(2, 4))
    return " ".join(random_words)

if __name__ == "__main__":
    app.run(debug=True)
