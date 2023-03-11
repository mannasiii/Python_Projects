# Python program to create
# a pdf file


from fpdf import FPDF


# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 15)

# create a cell
pdf.cell(200, 10, txt = "कुसुमाग्रज(वि.वा. शिरवाडकर) ",
		ln = 1, align = 'C')

# add another cell
pdf.cell(200, 10, txt = " कोलंबसाचे गर्वगीत हे कुसुमाग्रज तथा वि.वा. शिरवाडकरांनी लिहिलेली एक कविता आहे. ही त्यांच्या विशाखा काव्यसंग्रहात आहे. "
         "मार्ग आमुचा रोधू न शकतीना धनना दारा घराची वा वीतभर कारा ,"
        "मानवतेचे निशाण मिरवू महासागरात, जिंकुनी खंड खंड सारा"
         "चला उभारा शुभ्र शिडे ती गर्वाने वरती, कथा या खुळ्या सागराला
"अनंत अमुची ध्येयासक्ती अनंत अन् आशा किनारा तुला पामराला!"
		,ln = 2, align = 'C')

# save the pdf with name .pdf
pdf.output("py.pdf")
