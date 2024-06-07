spark部署：
1.Spark需要Java环境。确保安装了Java Development Kit (JDK)，并设置好JAVA_HOME环境变量：
        sudo apt-get update
        sudo apt-get install openjdk-??-jdk（注意，这个java安装需要看看当前系统支持哪个版本，所以中间加了问好，可以这样查询：sudo apt-cache search openjdk看看有什么版本）
2.从spark官网下载spark包并解压
3.（可选）加入spark环境变量，方便后面命令，或者也可以直接写路径，直接export也行，或者写在bashrc里面也行。
4.更改conf目录下spark-env.sh.template和works.template去掉template后缀
5.在spark-env.sh上写入以下配置:
              export JAVA_HOME=/path/to/java(写你自己的java路径，一般是export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64)
              export SPARK_MASTER_HOST='master-node-ip' (写主节点IP，可写可不写)
              export SPARK_WORKER_CORES=4（用四个核，可以自己设置）
              export SPARK_WORKER_MEMORY=8g（用8个G内存）
6.在works上写入：localhost
7.启动master节点和slave节点：
        $SPARK_HOME/sbin/start-master.sh
        $SPARK_HOME/sbin/start-worker.sh spark://localhost:7077（SPARK_HOME是前面第三步设的变量）
你可以通过在浏览器中访问http://localhost:8080或8081端口查看Spark的Web UI(注意端口权限要打开，我用云平台，需要在云端放开8080和8081端口)。
8.$SPARK_HOME/bin/spark-shell --master spark://localhost:7077，然后可以写一些代码自己测试一下


下面是一个简单的词频统计的demo，在projection_direction文件夹中，下面说说怎么使用：
1.运行前确保scala和sbt安装了，scala直接apt下载就好了，sbt需要添加软件源，操作步骤官网有https://www.scala-sbt.org/1.x/docs/zh-cn/Installing-sbt-on-Linux.html
2.看我目录里面的example.txt、build.sbt和wordcount.scala里面怎么写的以及所在文件夹位置，布置好一模一样的
3.在该项目根目录上运行命令：sbt packet。这会在target/scala-2.12目录下生成一个JAR文件（例如wordcount_2.12-0.1.jar）。
4.运行命令：$SPARK_HOME/bin/spark-submit --class WordCount --master local target/scala-2.12/wordcount_2.12-0.1.jar即可，会出现词频的统计
