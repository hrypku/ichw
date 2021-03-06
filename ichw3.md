1.**详述通用的高速缓存存储器结构及工作原理**

答：结构：由静态存储芯片(SRAM)组成，容量比较小但速度比主存高，且常被置于CPU和主存之间。主要有三大部分：

Cache存储体:存放由主存调入的指令与数据块。

地址转换部件:建立目录表以实现主存地址到缓存地址的转换。

替换部件:在缓存已满时按一定策略进行数据块替换，并修改地址转换部件。

![存储器层次示意](http://a4.att.hudong.com/42/25/20300542526409139869252718422_s.jpg)

![结构示意](http://s9.sinaimg.cn/large/6472c4ccgae0b93f864a8&690)

工作原理：block放置策略可分为三种cache组织形式：直接映射（一个块放到cache的唯一位置上）、全相联（一个块放到cache的任意位置上）、组相联（一个块放到cache受限的组里，该块可以放置到组内任意一个块里）。cache在任何时候都含有主存中一部分内容的副本。当CPU要存取主存中的一个字时，先检查cache，若存在则复制，若不存在，在直接映射模式下，则从主存中复制一份字和整个数据块至cache中，CPU再进行存取并复制该字;在全相联、组相联模式下，则需要从多个块中进行选择。若Cache已满，则需要按一定的替换算法，替换掉一个旧块。

