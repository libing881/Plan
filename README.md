Plan
====

# 2014计划 #

----------
## 1. 6月份的PMP考试 ##
需要报名参加培训，满足35个小时的时间要求

## 2. python抓取论文可视化 ##
1. 入口是paper结构
2. 递归调用，首先在结果中查询，保证主表的唯一性
3. 到web页面去查询
4. 解析
5. 保存结果到数据库
6. 循环结果，递归调用
7. 终结条件是，a 结果中每一个都结束了
   b 层次太深，超过100次，待测试
   c 重复则中止
8. 记录在db中，有2张表，主表和从表，唯一的标示，表示唯一论文，引用计数主表保证不重复，从表可能会有重复。主表单一记录对应从表多条。记录格式，id、论文名字、唯一标示。
9. 如何保证论文唯一，**DOI号** 可以用，参加链接 [http://www.doi.org/](http://www.doi.org/ "doi官网")
10. 如何可视化，圆圈表示引用次数，引用次数越多圆形越大，中间用线连接。考虑用python或者R，利用现成的库函数，需要确认接口。
11. 可视化的目的是找到关键论文进行精读
12. 找到重点论文后，进行批量的自动翻译，重点摘要分析，词汇分析
### 参考资料 ###
1. 查询论文被引用次数的方法 [http://wynwynwyn11.blog.163.com/blog/static/411736782010101183623569/](http://wynwynwyn11.blog.163.com/blog/static/411736782010101183623569/ "查询论文被引用次数的方法")
2. 


## 3. 论文精读，开题 ##
大数据处理相关，bio方向

## 4. 敏捷实施


