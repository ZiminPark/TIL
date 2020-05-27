# TF 1.X

- [What does variable reuse mean in TensorFlow?](https://medium.com/@hideyuki/what-does-variable-reuse-mean-in-tensorflow-40e86535026b)

  ```
  - reuse means sharing the same variable between different objects
  - If you want to share a variable, the second time you refer to that, you need to explicitly specify 
  “reuse=True” in the variable scope of the variable that you wants to reuse, or
  - set the variable scope to “reuse=tf.AUTO_REUSE”
  ```


# TF 2.X

- Want to get layer by its name. [(Similar Question)](https://stackoverflow.com/questions/48966281/get-intermediate-output-from-keras-tensorflow-during-prediction)

  => [Practice Code](https://github.com/ZiminPark/TIL/blob/master/tensorflow/code/get_layer_by_name.ipynb)
