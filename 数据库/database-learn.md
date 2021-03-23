# 基本语法

## group by

​	https://www.cnblogs.com/jingfengling/p/5962182.html

![image-20201220141916873](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201220141916873.png)



## order by

​	用来排序显示

![image-20201220142145446](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201220142145446.png)

## convert（） and avg（）

​	convert是类型转换，avg是求平均值，avg里的参数一定只能是数值。

![image-20201220155609025](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201220155609025.png)

![image-20201220160006034](C:\Users\asus\AppData\Roaming\Typora\typora-user-images\image-20201220160006034.png)

## having 语句

​	在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。HAVING 子句可以让我们筛选分组后的各组数据。

​	having只能使用在分组之后，不能单独使用，必须要跟group。意义是进行二次筛选。where是第一次筛选。

## join

	### 内连接  inner join

​	inner join

```sql
select * from b inner join a on b.name = a.name
```



### 外连接 outer  join

​	left outer join ：返回左表的全部行和右表满足on条件的行。

```sql
select * from b left/rigth/full outer join A on b.name = A.name
```

​	right join 

​	full join

### 交叉连接 cross join 

​	笛卡尔积

```sql
select * from n cross join a
```

### 自连接

​	通过给一张表进行重命名。

### 自然连接

​	natural join											

## exists

​	https://blog.csdn.net/wxf_suzhou/article/details/82962515

​	内层查询为空，返回假，不为空返回真。

​	两个not exists可以实现全称量词。

​	例如：选修了全部课程的学生姓名。

​	s1 选修了所有课程 等同于 不存在一门课 s1 没选。 

https://blog.csdn.net/yuanren201/article/details/89298068

```sql
select sname from s
where not exists (	-->为空集返回真
    select * from c where not exists (	-->得到学生没选的课
    	select * from sc where sc.sno = s.sno and sc.cno = c.cno))
```

​	例如：查询至少选修了学生95002选修的全部课程的学生号码。

​	逆否命题: 不存在一门95002选过的课，s1却没选过。

```sql
select sno from sc x
where not exists(
    select * from sc y where y.sno = '95002' and not exists (
        select * from sc z where z.cno = y.cno and z.sno = x.sno))
```



## 聚合函数

### count(*)

​	计算元组的个数，也就是行数。

count（列名）

​	对一列中的值计算个数。

count（distinct 列名）

​	只求出现一次的。

​	例如：查询学生总人数。

```sql
select count(*) from s
```

​	例如：查询选修了课程的学生人数。

```sql
select count(distinct sno) from sc
```

​	例如：计算1号课程的学生平均成绩。

```sql
select avg(grade) from sc where cno = '1'
```

​	例如：求各个课程号及相应的选课人数。

```sql
select cno,count(*) from sc group by cno
```

​	例如：求各个课程号及相应的课程成绩在90分以上的学生人数。

```sql
select cno count(*) from sc
where grade >= 90 
group by cno
```

​	例如：求成绩在90分以上的学生学号。

```sql
select distinct sno from sc where grade >= 90
```



## any，all，some

https://www.cnblogs.com/feiquan/p/8654171.html

https://blog.csdn.net/gyc1105/article/details/8063624?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2.control

https://docs.microsoft.com/zh-cn/previous-versions/sql/sql-server-2005/ms187074(v=sql.90)?redirectedfrom=MSDN

< >ANY 运算符则不同于 NOT IN：< >ANY 表示不等于 a，或者不等于 b，或者不等于 c。NOT IN 表示不等于 a、不等于 b 并且不等于 c。<>ALL 与 NOT IN 表示的意思相同。

# 关系代数运算

​	五个基本运算是 ：并，差，积，选择和连接。别的运算可以用五个基本运算来描述。

## 并

​	并要求两个关系属性的性质必须一致。

## 交

​	R - (R - S)，不是基本运算。

## 差

​	R - S ，是R中但不是S中的。

​	一般应用在“不使用****，没有选修*****”类似的语境问题。先找出了使用 /  选修了的，再用全集去减。

## 积

## 选择 select

​	选择的是行，where的作用。选择符合条件的元组。

## 投影 π

​	自动消除重复行，把某一列或几列显示出来。 

## 连接

​	是笛卡尔积、选择和投影操作的组合。   

## 除

​	是笛卡尔积，投影，和差组合。

# 关系演算

## 原子公式

原子公式是最小的公式，公式经过有限次运算仍是公式。

# 复习汇总

## 表的创建，修改和撤销

  * create table A ( Pno char(4) not null,primary key(pno) );//创建及主键

  * foreign key (pno) references J(Jno) ;//外键

  * constraint y check （ x between 0 and 10000 );//检查约束 

  * alter table 基本表名 add 新属性名 新属性类型完整性约束 //增加新的属性的句法

  * 例如：alter table s add tele char(12);

* alter table 基本表名 drop 属性名 [cascade|restrict];//删除原有的属性

* alter table 基本表名 drop 约束名//删除指定的完整性约束

* drop alter table 基本表名  [cascade|restrict] //删除基本表

    

## 创建视图

		* create view 视图名(列表名1，列表名2···) as select 查询语句  //句法
		* drop view 视图名 //视图的撤销
		* 更新操作有三条规则：1.多个基本表连接操作导出的，不允许执行更新。2.导出视图时使用了分组和聚合操作，不允许更新。3.单个基本表使用选择投影导出的，并且包含了主键或某个候选键，这样的视图叫 行列子集视图，可以被执行更新操作。
	
	## 索引的创建和撤销
	
		* create index jno_index on J(JNO); //建立索引，表示对基本表J的列JNO建立索引，索引的名字为jno_index
		* create unique index jno_index on J(JNO); //如果要求列JNO的值在基本表J中你不重复，那么添加保留字unique
		* 一个索引键可以对应多个列，默认升序，可以降序。ASC/DESC
		* drop index jno_index on J ; //撤销索引

## 数据插入

* insert into 基本表名 [(列名序列)] values （元组值）//必须包含所有的非空属性，需要字符的话需要加单引号。
* insert into 基本表名 （列名序列） select语句 // 把select查询语句的查询结构插入到指定的基本表中。

## 数据删除

* delete from 基本表名 where 条件表达式 // 用于删除指定的基本表中满足条件表达式的元组，如果没有这个条件表达式，则会删除指定表中的所有元组。

* 注意：delete语句只能从一个关系中删除元组，而不能一次从多个关系中删除元组，要删除多个元组，就要写多个delete语句。

## 数据修改

* update 基本表名 set 列名 = 表达式  where 条件表达式 //省略where的话会修改所有元组的相应属性列值。 