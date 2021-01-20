import numpy as np
import torch
import jsonlines
from transformers import BertModel, BertTokenizer
from tqdm import tqdm


target_embedding = torch.from_numpy(np.load('nlp_embedding.npy'))
bert = BertModel.from_pretrained('bert-base-multilingual-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
sim = torch.nn.CosineSimilarity(dim=0)


def run_sentence(sent):
    tokenized = tokenizer(sent, return_tensors='pt')
    with torch.no_grad():
        outputs = bert(**tokenized, return_dict=True, output_hidden_states=True)
        # outputs.keys()
        embedded = outputs.hidden_states[-1].squeeze().mean(dim=0)
        assert embedded.size() == target_embedding.size()
        return embedded, sim(embedded, target_embedding)


def solve():
	max_sim = -1
	max_verse = None
	with jsonlines.open('surah.jl') as reader:
	    for obj in tqdm(reader, total=286):
	        line_num = obj['num']
	        verse = obj['line']
	        embedded, similarity = run_sentence(verse)
	        if similarity > max_sim:
	            max_sim = similarity
	            max_verse = (line_num, verse)
	print(f'Flag: {max_verse[0]}\nVerse: {max_verse[1]}')


solve()