# Text Summarizer (Streamlit App)

## Live Demo
Access the app here: https://text-summarizer-a.streamlit.app
(or)
[Live App](https://text-summarizer-a.streamlit.app)

A simple, intuitive **text summarization web app** built with **Streamlit**.
It generates a concise summary of any input text using a **frequency-based extractive summarization technique**.

---

## Features

* Easy-to-use web interface
* Extractive summarization (top important sentences)
* Fast processing with no external dependencies (no ML models required)
* Uses word frequency scoring to determine sentence importance

---

## How It Works

1. Removes punctuation and converts text to lowercase
2. Filters out common stopwords
3. Calculates word frequency
4. Scores each sentence based on word importance
5. Selects the top 3 highest-scoring sentences
6. Displays them in original order as the summary

---

## Installation

Clone this repository:

```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
```

Install dependencies:

```bash
pip install streamlit
```

---

## Running the App

```bash
streamlit run app.py
```

Then open your browser and go to:

```
http://localhost:8501
```

---

## Usage

1. Enter your text in the input box
2. Click on "Summarize"
3. View the generated summary

---

## Project Structure

```
text-summarizer/
│
├── app.py          # Main Streamlit app
├── README.md       # Project documentation
```

---

## Limitations

* Uses a basic algorithm, not deep learning
* Summary quality depends on word repetition
* Works best for structured paragraphs

---

## Future Improvements

* Add NLP libraries like NLTK or spaCy
* Implement abstractive summarization (AI-based)
* Allow user to select summary length
* Improve sentence splitting using NLP

---

## Contributing

Feel free to fork this repository and improve the project. Contributions are welcome.

---

## License

This project is open-source and available under the MIT License.

---

## Author

Developed by *Sneha Satapathy*

---

## If you like this project

Consider giving it a star on GitHub.
