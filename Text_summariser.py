import streamlit as st
import string

st.title("Text Summarizer!!")

text = st.text_area("Enter your text here and you will receive a summarized version of it.")

if st.button("Summarize"):
    if text:
        # Basic stopwords
        stopwords = set([
            "the","is","in","and","to","of","a","that","it","on","for","as",
            "with","was","were","be","by","this","are","or","an"
        ])

        # Clean words
        words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

        # Word frequency
        word_freq = {}
        for word in words:
            if word not in stopwords:
                word_freq[word] = word_freq.get(word, 0) + 1

        # Split sentences
        sentences = text.split(".")

        # Score sentences
        sentence_scores = {}
        for sentence in sentences:
            sentence_words = sentence.lower().split()
            score = 0
            for word in sentence_words:
                word = word.strip(string.punctuation)
                if word in word_freq:
                    score += word_freq[word]
            sentence_scores[sentence] = score

        # Get top sentences
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]

        # Keep original order
        ordered_summary = [s for s in sentences if s in top_sentences]

        summary = ". ".join(ordered_summary)

        st.write("### Summary:")
        st.write(summary)

    else:
        st.write("Please enter some text")
