# coding:utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from init import *
class AttrNetwork(nn.Module):
    def __init__(self):
        super(AttrNetwork,self).__init__()
        self.num_layers = 1  # 隐藏层的层数
        self.hidden_size = 50  # 隐藏层的维度
        self.embeding_size = 100  # 词向量的长度
        self.num_classes = 149 # 罪名数量
        self.attr_size = 10 #attr数量
        self.lstm = nn.LSTM(self.embeding_size,
                            self.hidden_size, self.num_layers)
        self.fc = nn.Linear(self.hidden_size,self.attr_size)
        
    def forward(self,inputs):
        lstm_hidden, (h, c) = self.lstm(inputs)
        out = self.fc(h)
        return out

def main():
    word2id, word_embeddings, attr_table, x_train, y_train, y_attr_train, x_test, y_test, y_attr_test, x_val, y_val, y_attr_val, namehash, length_train, length_test, length_val = load_data_and_labels_fewshot()
    network=AttrNetwork()
    optimizer = optim.Adam(network.parameters(), lr=0.001)
    loss_count = 0
    best_loss = np.inf
    train_len = len(x_train)
    for i in range(train_len):
        word_list = x_train[i]
        x = np.array([])
        for word in word_list:
            x = np.append(x,word_embeddings[word])
        x = torch.tensor(x).reshape(500, 1, 100)
        crime_pred = network(x.float()).reshape(-1)

        label = np.argmax(y_train[i])
        crime_attr = torch.tensor(attr_table[label]).float().reshape(-1)
        crime_attr[crime_attr>1]=0.5
        loss = F.mse_loss(crime_pred,crime_attr)
        loss_count+=loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if i%100==0 and i>=100:
            ave_loss = loss_count/100
            loss_count=0
            print(ave_loss)
            if ave_loss<best_loss:
                best_loss=ave_loss
                torch.save(network, "../pth/test_model")
    for i in range(10):
        word_list = x_test[i]
        x = np.array([])
        for word in word_list:
            x = np.append(x,word_embeddings[word])
        x = torch.tensor(x).reshape(500, 1, 100)
        crime_pred = network(x).reshape(-1)
        crime_pred[crime_pred>0.5]=1
        crime_pred[crime_pred<=0.5]=0
        label = np.argmax(y_train[i])
        crime_attr = torch.tensor(attr_table[label]).float().reshape(-1)
        print(crime_pred,label,crime_attr)
    
if __name__ == "__main__":
    main()







