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

