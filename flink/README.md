官网下载flink包并解压，然后运行：
./bin/start-cluster.sh
这是flink本地模式下运行。默认IP是localhost/127.0.0.1，默认端口是8081，因为我用ssh连接，这时候我直接浏览器搜localhost/127.0.0.1:8081可以直接出来。根据个人需求假如需要修改配置则修改conf/config.yaml配置文件，修改rest下的配置就好了，我自己是改成这样子的：
rest:
  # The address to which the REST client will connect to
  #address: localhost
  address: 0.0.0.0
  # The address that the REST & web server binds to
  # By default, this is localhost, which prevents the REST & web server from
  # being able to communicate outside of the machine/container it is running on.
  #
  # To enable this, set the bind address to one that has access to outside-facing
  # network interface, such as 0.0.0.0.
  #bind-address: localhost
  bind-address: 0.0.0.0
  # # The port to which the REST client connects to. If rest.bind-port has
  # # not been specified, then the server will bind to this port as well.
  # port: 8081
  port: 8080
  # # Port range for the REST and web server to bind to.
  # bind-port: 8080-8090
原来的rest里面只有address和bind-address是没有注释的，其他都是注释掉的，address和bind-address原本配置就是localhost，我改成0.0.0.0这样我用公网ip也可以连接了，端口我改成了8080。然后就可以访问flink的webUI了。


下面是运行flink自带的一个简易命令：
./bin/flink run examples/streaming/WordCount.jar --input ./test/wordcount.txt --output ./test/
该命令是运行flink使用的是案例中的词频统计，设置好输入输出后就可以运行了，我自己的wordcount是这样的：
hello flink
hello world
flink is great
hello flink
hello world
hello flink
hello world
flink is great
但是输出结果是这样的：
(hello,1)
(flink,1)
(hello,2)
(world,1)
(flink,2)
(is,1)
(great,1)
(hello,3)
(flink,3)
(hello,4)
(world,2)
(hello,5)
(flink,4)
(hello,6)
(world,3)
(flink,5)
(is,2)
(great,2)

可以发现输出的结果其实有点奇怪，可以发现它把统计的过程也输出出来了，正常来讲的话只用输出14行往后就好了，可能是官方自己案例写的有问题？不过无伤大雅，用来简单测试一下而已。运行这个的时候web上面也会同步记录。