#!/usr/bin/env python
# coding: utf-8

# In[1]:


def criar_contato(*args):
   print("Digite as informações do contato")
   info = {}
   for arg in args:
       info[arg] = input('Digite %s: ' % arg)
   return info


# In[2]:


def salvar_contato(**kwargs):
    arquivo = open('contatos.csv', 'a')
    arquivo.write(','.join(kwargs.values()))
    arquivo.write('\n')
    arquivo.flush()
    arquivo.close()
    


# In[ ]:


quantidade = input("Quantos contatos deseja cadastrar? ")
quantidade = int(quantidade)
campos = input("Digite os campos separados por vírgula: ")
campos = campos.split(',')
for i in range(quantidade):
    contato = criar_contato(*campos)
    salvar_contato(**contato)


# In[ ]:




