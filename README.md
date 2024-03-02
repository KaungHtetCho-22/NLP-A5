# NLP-A5
NLP assignment from AIT

**Kaung Htet Cho (st124092)**

## Table of Contents
1. [Task1](#Task1)
2. [Task2](#Task2)
3. [Task3](#Task3)
4. [Task4](#Task4)


## Task1
### Train BERT from scratch

- training_data = Harry potter book 1 (https://github.com/bobdeng/owlreader/blob/master/ERead/assets/books/Harry%20Potter%20and%20the%20Order%20of%20the%20Phoenix.txt)
- vocab_size = 7485
- total_sentence = 6184
- encoder_layers = 6

Trained the base BERT model saved the bert_from_scratch.pth for later use in sentence-BERT

## Task2
### Sentence BERT 

1. Load the datasets (SNLI, MNLI) from hugging face
2. Load weight file from last trained BERT base model and took the output, done Objective function

## Task3
### Evaluation and Analysis

1. Evaluation of sentence transformer model: 
2. Performance comparison
3. Impact of Hyperparameters: 
4. Challenges: Personal GPU which can have lower GPU memory can face CUDA out of Memory in inferencing the sentence BERT

## Task4
### Text-similarity Development

The Website can be accessed on http://localhost:8000. User can type two different sentences and then my trained sentence bert model processed the objective function and shown the cosine similarity between the two sentences
