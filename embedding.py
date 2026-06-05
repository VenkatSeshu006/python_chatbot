from google import genai
import numpy as np

client = genai.Client(api_key=" ")


def normalise_l2(cut_dim):
    x=np.array(cut_dim)
    if x.ndim == 1:
        norm = np.linalg.norm(x)
        if x.ndim==0:
            return x
        return x/norm
    else:
        norm=np.linalg.norm(x,2,axis=1,keepdims =True)
        return np.where(norm==0,x,x/norm)


response = client.embedding.create(
    input="cat"
    model="text-embedding-3-small"
    )

cut_dim = response.data[0].embedding[:7]
norm_dim=normalise_l2(cut_dim)
print(norm_dim)