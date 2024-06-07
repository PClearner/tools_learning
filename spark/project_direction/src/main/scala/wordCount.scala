import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object WordCount {
  def main(args: Array[String]) {
    // 设置Spark配置
    val conf = new SparkConf().setAppName("WordCount").setMaster("local")
    val sc = new SparkContext(conf)

    // 读取文件
    val textFile = sc.textFile("example.txt")

    // 执行词频统计
    val counts = textFile.flatMap(line => line.split(" "))
                         .map(word => (word, 1))
                         .reduceByKey(_ + _)

    // 打印结果
    counts.collect().foreach(println)

    // 停止Spark上下文
    sc.stop()
  }
}

