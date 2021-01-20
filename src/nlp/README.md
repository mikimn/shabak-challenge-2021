
# NLP Challenge

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