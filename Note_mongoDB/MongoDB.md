# MongoDB



#### $inc

使用$inc操作符将一个字段的值增加或者减少

```
{ $inc: { <field1>: <amount1>, <field2>: <amount2>, ... } }
```

#### $set

$set操作符替换掉指定字段的值

```
{ $set: { <field1>: <value1>, ... } }
```

#### $unset

$unset操作符删除一个指定的字段

```
{ $unset: { <field1>: "", ... } }
```

#### $addToSet

$addToSet添加值到一个数组中去，如果数组中已经存在该值那么将不会有任何的操作

```
{ $addToSet: { <field1>: <value1>, ... } }
```

#### $each

$each修饰符允许$addToSet操作符添加多个元素到数组字段中

```
{ _id: 2, item: "cable", tags: [ "electronics", "supplies" ] }
```

#### $lt $lte $gt $gte

以上四个分别表示为：< 、 <= 、 > 、 >= 。 通常的做法是将他们组合起来，以便查找一个范围

```
//比如，查询年龄在18到25岁（含）的人，我们可以这样

db.user.find({"age":{"$gte":18,"$lte":25}})  
```

#### $pull

$pull修饰符会删除掉数组中符合条件的元素

```
{ $pull: { <field1>: <value|condition>, <field2>: <value|condition>, ... } } 
```

