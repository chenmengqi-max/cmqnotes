# CSS入门

## 使用css来修改元素的样式

		### 第一种方式（内联样式，行内样式）

​		在标签内部通过style属性来设置元素的样式。冒号接值，分号用来分割不同样式。内联样式缺点是样式只能对一个标签生效。当样式发生变化时必须要一个一个修改。

​		注意：开发时绝对不要使用内联样式！！！

```html
<p style="color:red; font-size: 60px;">
    CSS入门
</p>
```

### 第二种方式(内部样式表)

​		将样式编写到head中的style标签里，然后通过css的选择器来选中元素并为其设置各种样式，例如 p{} (选择器选中页面中的指定元素，p的作用是选中页面中所有的p元素；{}被称为声明块) 。内部样式表更加方便对样式表进行复用。缺点是不能跨页面进行复用。

```html
<head>
    <style>
        p{color:green;font-size: 50px;}
    </style>
</head>
```

### 第三种方式（外部样式表）

​		可以将css样式编写到一个外部的css文件中，然后通过link标签引入外部的css文件。最佳的实现，开发中最推荐的方式。可以使用到浏览器的缓存机制，从而加快网页的加载速度。rel="stylesheet"一定要有。

```html
<link rel="stylesheet" href="style.css">
```

## CSS语法

​		html文件中的style标签中不属于html页面，里面的语法规范要符合css语法。css中注释为/*  xx */

### 选择器和声明块

#### 元素选择器

​		选择器选中页面中的指定元素，p的作用是选中页面中所有的p元素；{}被称为声明块

```css
p{
    color:green;
    font-size: 50px;
}
h1{
    color: red;
    font-size: 100px;
}
```

#### id选择器

​		标签可以定义一个唯一的id号，在style标签里或者外部样式表里定义的时候，用#+id号+声明块。

```html
<style>
#red{
color：red;
}
</style>
<p id="red">xxxx</p>
```

#### 类选择器

​		根据class属性值来选择一组元素。声明块之前用   .

​		给一个标签定义多个类时，中间用空格隔开，例如： 

```html
<p class="a b c d">xxxx</p>
<style>
.blue{
color：blue;
}
</style>
<p class="blue">xxxx</p>
```

#### 通配选择器

​		*{} 所有的元素样式都被定义。

#### 交集选择器

​		语法：选择器1选择器2选择器n{} ，例如：div.red{ } 。如果有元素选择器，必须使用元素选择器开头。

```css
div.red{
	color:red;
}
.a.b.c.d{
    color:green;
}
```

#### 并集选择器

​		语法：用逗号来分隔。可以同时选择多个选择器对应的元素。例如：

```css
#a,.b,h1,div.red{
    color:red
}
```

#### 子元素选择器

​		语法：父元素 > 子元素。这种方式只能是子元素被定义，子元素的子元素不能被定义。如果给div设置class属性，则还可以写div.class名 > span 。 >  可以有多个。

```css
div > span{
color:orange
}
```

#### 后代元素选择器

​		作用是可以选中指定元素内的指定后代元素。

​		语法：祖先 后代。符号是空格。

#### 兄弟元素选择器

​		作用：选择下一个兄弟。

​		语法：前一个 + 下一个。选择p标签的下一个span标签。必须紧挨着，中间不能有别的标签。

```css
p + span{
    color:red;
}
```

​		作用：选择下边所有的兄弟。

​		语法：前一个 ~ 下面的标签（兄 ~ 弟）。波浪号

#### 属性选择器

​		[属性名]  选择含有指定属性的元素。

​		[属性名 = 属性值]  选择含有指定属性和属性值的元素，值要完全一样。

​		[属性名 ^= abc]  选择属性值是以abc为开头的元素。

​		[属性名 $= abc]  选择属性值是以abc为结尾的元素。

```html
<style>
    p[title]{
        color:red;
    }
</style>

<p title = "abc">
    我是p标签，我的title值是abc
</p>
<p title = "abcdef">
    我是p标签，我的title值是abc开头的
</p>
<p title = "qweabc">
    我是p标签，我的title值是abc结尾的
</p>

```

#### 伪类选择器

​		伪类一般情况下都是用：开头。

​		：first-child 第一个子元素。

​		：last-child 最后一个子元素。

​		：nth-child（）选中第n个子元素。

​				特殊值：

​							n    选中0到第n个，n的范围0到正无穷。

​							2n或者even    选中偶数位的元素。

​							2n+1 或者 odd    选中奇数位的元素。

​		以上这些伪类都是根据所有的子元素进行排序的，当我们选择第一个 li 的时候，要是 ul 所有元素中的第一个，如果第一个假如有个span标签，那ul > li:first-child 就不能找到，因为第一个是span而不是 li。

​		：first-of-type  这个是找同类型的第一个。

​		相似的有

​		：last-of-type

​		：nth-of-type（）

比如

```css
ul > li:first-of-type{
    我是选择ul里面的li标签里面的第一个。我只在同类型里面排序。
}
```

​		：not()否定伪类：除了第三个li标签，别的全部设置为蓝色。00

```css
 ul > li:not(:nth-child(3)){
        color:blue;
        }
```





