��������flink������ѹ��Ȼ�����У�
./bin/start-cluster.sh
����flink����ģʽ�����С�Ĭ��IP��localhost/127.0.0.1��Ĭ�϶˿���8081����Ϊ����ssh���ӣ���ʱ����ֱ���������localhost/127.0.0.1:8081����ֱ�ӳ��������ݸ������������Ҫ�޸��������޸�conf/config.yaml�����ļ����޸�rest�µ����þͺ��ˣ����Լ��Ǹĳ������ӵģ�
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
ԭ����rest����ֻ��address��bind-address��û��ע�͵ģ���������ע�͵��ģ�address��bind-addressԭ�����þ���localhost���Ҹĳ�0.0.0.0�������ù���ipҲ���������ˣ��˿��Ҹĳ���8080��Ȼ��Ϳ��Է���flink��webUI�ˡ�


����������flink�Դ���һ���������
./bin/flink run examples/streaming/WordCount.jar --input ./test/wordcount.txt --output ./test/
������������flinkʹ�õ��ǰ����еĴ�Ƶͳ�ƣ����ú����������Ϳ��������ˣ����Լ���wordcount�������ģ�
hello flink
hello world
flink is great
hello flink
hello world
hello flink
hello world
flink is great
�����������������ģ�
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

���Է�������Ľ����ʵ�е���֣����Է�������ͳ�ƵĹ���Ҳ��������ˣ����������Ļ�ֻ�����14������ͺ��ˣ������ǹٷ��Լ�����д�������⣿�������˴��ţ������򵥲���һ�¶��ѡ����������ʱ��web����Ҳ��ͬ����¼��