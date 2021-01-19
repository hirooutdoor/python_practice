# %%
import numpy as np
# %%
a = np.array([1, 2, 3])

a

#%%
a.shape

a.ndim
# %%
b = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

b
# %%
print('Shape:', b.shape)
print('Rank:', b.ndim)
# %%
b.size
# %%
a = np.zeros((3, 5))

a
# %%
# 形を指定して、 0 ~ 1 の間の乱数で要素を埋めた ndarray を作る
e = np.random.random((4, 5))

e
# %%
# 3 から始まり 10 になるまで 1 ずつ増加する数列を作る（10 は含まない）
f = np.arange(3, 10, 1)

f
# %%
#上で作成した e という 4×5 行列を表す多次元配列から、1 行 2 列目の値を取り出す
val = e[0, 1]

val
# %%
center = e[1:3, 1:4]

center
# %%
