---
--- https://www.cnblogs.com/zhangdw/p/3339751.html 这个网址的相关语法很好
---
---函数---
--- function 与 end 成对出现
--- 8个基本类型：nil，boolean,number,string,userdata,function,thread,table,table既是数组又是字典。
days = {["name"]="table1","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}
table.insert(days,2,"插入的2") --插入函数
--concat可以把table元素全部连接起来。但前提是下标数字开始，键值不会包含进来。
--print(table.concat(days))
--print(days)会输出地址
print(days.name)
print(days["name"])
print(days[1])
days.name2="table2"; --也可以这样插入元素
print(days.name2);
for i,j,k,l in ipairs(days)
do
    print(i,j,k,l)
end
print(1>2)

---　　   and, or, not 其中，and 和 or 与C语言区别特别大。
---　　　在这里，请先记住，在Lua中，只有false和nil才计算为false，其它任何数据都计算为true，0也是true！ 　　　　
---　　　and 和 or的运算结果不是true和false，而是和它的两个操作数相关。 　　　　
---　　　a and b：如果a为false，则返回a；否则返回b 　　　　
---     a or b：如果 a 为true，则返回a；否则返回b
--a ,b ,c= 1,2,3;
----下行实现 x = a? b : c
--x = a and b or c;
--y = b or c;
--print(b ~= c)
--print(x)
--print(y)
--print(a>b and a or b)
--
lianjie = 0 .. 1
print(lianjie)
print(type(lianjie))