# NLP Challenge

Category: AI Research

Points: 250

## Description
> A jaded attacker, who installed a malware on your computer, was able to access all your text files and a managed to encrypt them all. By analysing the timestamps, he used the last document you worked on and iterated over it sentence by sentence, and for each sentence used a pre-trained BERT model to create a 768D embedding vector which was persisted to permanent storage.
>
> The vector he created was computed using the 'bert-base-multilingual-uncased' model. The vector is an average of the second-to-last hidden layer outputs, over all tokens (including special ones).
>
> Subsequently, he erased the document from your hard-drive and kept a copy to himself. Knowing how significant the loss of the document is to you, he challenges you to solve a riddle to gain back access to your files.
>
> He provides you with a single feature vector (a 768d embedding), of a specific sentence in the document.
>
> **He guarantees that if you are able to find the actual sentence, he will unlock your hard drive.**
>
> Each sentence in the original document had a line number associated with it, you are to provide him with that number.
>
> A big hint to find this number is hidden in the first image file provided with this challenge. The second txt file is the BERT embedding.

**Files:** [hint\_-\_nlp.png](hint_-_nlp.png), [nlp_embedding.npy](nlp_embedding.npy)

## Solution


Original website used for scraping: https://quran.com/2

Since the website is lazy-loading, I downloaded the HTML file, `original_surah.html`.

To re-create the dataset, delete `surah.jl` and run
```bash script
scrapy runspider surah.py -o surah.jl
```

To find the solution, run
```
python solve.py
```

### The Hint

As an hint we're given a PNG image of the ISA logo, in black and white:

<div align="center">
    <img src="hint_-_nlp.png" width=400>
</div>

There doesn't seem to be anything interesting visible in the image, and the words in the logo and the agency name didn't give us the expected output, so we assumed that there might be some data *hidden* in the image. The art of hiding information in another medium is called steganography, it's a branch of cryptography and commonly appears in CTF (but not in this one). We went through some of the well known techniques of hiding data from images, such as hiding strings in the image's data, embedding files and hiding information in the LSB/MSB of the image, eventually we ran `stegsolve` on the image, which allows us to randomize the colors such that pixels with similar colors to the naked eye will have different colors, and got the following:     

<div align="center">
    <img src="hint_solved.bmp" width=400>
</div>

There are symbols in the middle of the logo! not only that but they are Arabic letters that makes the word البقرة (Al-Baqarah) which translates to "the cow".

