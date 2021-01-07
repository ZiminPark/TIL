


### 1. Want to get layer by its name. [(Similar Question)](https://stackoverflow.com/questions/48966281/get-intermediate-output-from-keras-tensorflow-during-prediction)

  => [Practice Code](https://github.com/ZiminPark/TIL/blob/master/tensorflow/code/get_layer_by_name.ipynb)

### 2. [Text Generation with RNN](https://github.com/ZiminPark/TIL/blob/master/tensorflow/code/text_generation.ipynb)
- many-to-many 연습용
```python
def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)  # sequences : tf.data.Dataset
```

### 3. Indexing by tf.gather_nd
```python
# tf.gather_nd docs: https://www.tensorflow.org/api_docs/python/tf/gather_nd
# tf.stack docs: https://www.tensorflow.org/api_docs/python/tf/stack

tar = tf.constant([[0,2,1], [2,3,1]])
indexer = tf.constant([[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]]])
beta = tf.random.normal([2,3,5])

step = 3
bsz = 2

step_range = [tf.range(step)] * bsz
step_range = tf.stack(step_range, 0)
print(step_range)

bdx = [tf.range(bsz)] * step
bdx = tf.stack(bdx, 1)
print(bdx)

indexer = tf.stack([bdx, step_range, tar], axis=-1)
print(indexer)

print(tf.gather_nd(beta, indexer))
```


# TF 1.X

- [What does variable reuse mean in TensorFlow?](https://medium.com/@hideyuki/what-does-variable-reuse-mean-in-tensorflow-40e86535026b)

  ```
  - reuse means sharing the same variable between different objects
  - If you want to share a variable, the second time you refer to that, you need to explicitly specify 
  “reuse=True” in the variable scope of the variable that you wants to reuse, or
  - set the variable scope to “reuse=tf.AUTO_REUSE”
  ```
