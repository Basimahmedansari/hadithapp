import streamlit as st
import requests
API_KEY = "$2y$10$dDP1R6YfJLgBXP18GRki1eAvDYugo60EuZhJAnk7dr1ORLCJs7O8S"
st.title("📚 Hadith Nabawi ﷺ")
import streamlit as st

st.title("Hadith App")

books = {
    "Sahih Bukhari": "sahih-bukhari",
    "Sahih Muslim": "sahih-muslim",
    "Al-Tirmidhi": "al-tirmidhi"
}

book = st.selectbox("Select Book", books.keys())

bookSlug = books[book]

meriHbooks = requests.get(
    f"https://hadithapi.com/api/books?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e"
)
allBooksdata = meriHbooks.json()["books"]

options = []
for b in allBooksdata:
    options.append(f"{b['bookName']} | {b['bookSlug']}")

itemBook = st.selectbox("Choose Hadith Book", options)

bookSlug = itemBook.split(" | ")[1]

st.text("Selected Book: " + bookSlug)

merihadithsChapters = requests.get(
    f"https://hadithapi.com/api/{bookSlug}/chapters?apiKey==$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e")

chapterResponse = merihadithsChapters.json()
if "chapters" not in chapterResponse:
    st.error(chapterResponse)
    st.stop()

allChapterdata = chapterResponse["chapters"]

optionsChap = []

for c in allChapterdata:
    optionsChap.append(
        f"{c['chapterNumber']} | {c['chapterArabic']} | {c['chapterUrdu']}"
    )
itemchap = st.selectbox("Choose Chapter", optionsChap)

chapterNO = itemchap.split(" | ")[0]
hadith = requests.get(
    f"https://hadithapi.com/api/hadiths?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e&book={bookSlug}&chapter={itemchap}&paginate={100000}")

hadithResponse = hadith.json()

if "hadiths" not in hadithResponse:
    st.error(hadithResponse)
    st.stop()
allHadith = hadithResponse["hadiths"]["data"]
for a in allHadith:
    st.subheader(f"Hadith No. {a['hadithNumber']}")
    st.info(a["hadithArabic"])
    st.success(a["hadithUrdu"])
    st.warning(a["hadithEnglish"])





