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

​	where只能使用在分组之后，不能单独使用，必须要跟group。意义是进行二次筛选。where是第一次筛选。

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

## exists

​	https://blog.csdn.net/wxf_suzhou/article/details/82962515

​	内层查询为空，返回假，不为空返回真。

​	两个not exists可以实现全称量词。

​	例如：选修了全部课程的学生姓名。

​	s1 选修了所有课程 等同于 不存在一门课 s1 没选。 

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