# TF 1.X

- [What does variable reuse mean in TensorFlow?](https://medium.com/@hideyuki/what-does-variable-reuse-mean-in-tensorflow-40e86535026b)
  ```
  Here is the summary
  - reuse means sharing the same variable between different objects
  - If you want to share a variable, the second time you refer to that, you need to explicitly specify “reuse=True” in the variable scope of the variable that you wants to reuse, or
  - set the variable scope to “reuse=tf.AUTO_REUSE”
  ```
