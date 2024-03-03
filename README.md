# NLP-A5
NLP assignment from AIT

**Kaung Htet Cho (st124092)**

Supplementry folder is not necessary for assignment

## Task1
### Train BERT from scratch

- training_data = Harry potter book 1 (https://github.com/bobdeng/owlreader/blob/master/ERead/assets/books/Harry%20Potter%20and%20the%20Order%20of%20the%20Phoenix.txt)
- vocab_size = 7485
- total_sentence = 6184
- encoder_layers = 6
- n_epochs = 10

Trained the base BERT model saved the bert_from_scratch.pth for later use in sentence-BERT

## Task2
### Sentence BERT 

1. Load the datasets (SNLI, MNLI) from hugging face
2. Load weight file from last trained BERT base model and took the output, and then implemented Objective loss function
3. Hyperparameters
    - n_epochs = 5
    - linear_scheduler_with_warmup

## Task3
### Evaluation and Analysis

1. Performance comparison 

| Model          | Training time | Training loss |
|----------------|-------------|---------------|
| BERT pretrained - uncased       |    50s        |   18.541     |    
| BERT from scratch |          54s   |     13.695       |  

2. Impact of Hyperparameters: We can manipulate the hyperparameters according to whatwe want, we can think of increasing bigger training dataset, number of epochs and encoder layers(6) to standard pretrained (12 layers) but we should leave the embedding size 768 unchanged because original BERT got the best results among many implementation
3. Challenges: Personal GPU which can have lower GPU memory can face CUDA out of Memory in inferencing the sentence BERT because it takes two long sentences


## Task4
### Text-similarity Development

The Website can be accessed on http://localhost:8000. User can type two different sentences and then my trained sentence bert model processed the objective function and shown the cosine similarity between the two sentences
