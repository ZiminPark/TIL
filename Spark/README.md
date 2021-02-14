## 1. Spark 입문 T아카데미 [영상](https://www.youtube.com/playlist?list=PL9mhQYIlKEhf23_3QIqQvsa_06CyTZGdl)
- Hadoop, Zepplin, Spark, Kafka에 대한 간단한 개념 설명
- Driver and Executor
- Streaming 관련 오버뷰
- 간단한 Spark 관련 코드, DAG, Transform and Action
- Job, Stage, Task, Shuffle
- Structured API: SparkSQL, DataFrame, Datasets 그리고 Planning, Optimization 설명 / RDD와 뭐가 다른지

## 2. [Table Partition](https://developer.hpe.com/blog/Ql2DXNL4rmhWB8AEDMQz/tips-and-best-practices-to-take-advantage-of-spark-2x)
- 테이블을 저장할 때 parquet으로 파티셔닝하여 저장할 수 있다.
- RDD에서 말하는 파티셔닝이랑은 개념이 다르다.
- Parquet는 디스크에서의 파티셔닝을 말하고 RDD는 메모리에서의 파티셔닝을 말한다.
- Pandas Dataframe은 메모리에서 파티셔닝을 안하지만 RDD는 한다.
