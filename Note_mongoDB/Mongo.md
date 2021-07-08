# MongoDB



### 切换/创建数据库

```
use config;
```



### 查询所有数据库

```
 show dbs;
```



### 删除当前使用数据库

```
 db.dropDatabase();
```



### 从指定主机上克隆数据库

```
 //将指定机器上的数据库的数据克隆到当前数据库
 db.cloneDatabase(“127.0.0.1”);
 
 //从指定的机器上复制指定数据库数据到某个数据库
 //将本机的mydb的数据复制到temp数据库中
 db.copyDatabase("mydb", "temp", "127.0.0.1");
```



### 查看当前使用的数据库

```
 //db和getName方法是一样的效果，都可以查询当前使用的数据库
 
 db.getName();
 db; 
```



### 显示当前db状态

```
 db.stats();
```



### 当前db版本

```
 db.version();
```



### 查看当前db的链接机器地址

```
 db.getMongo();
```



# Collection聚集集合

### 创建一个聚集集合（table）

```
 db.createCollection(“collName”, {size: 20, capped: 5, max: 100});
```



### 得到指定名称的聚集集合（table）

```
 db.getCollection("account");
```



### 得到当前db的所有聚集集合

```
 db.getCollectionNames();
```



### 显示当前db所有聚集索引的状态

```
 db.printCollectionStats();
```



# 用户相关

### 添加一个用户

```
 db.addUser("name");
```



### 数据库认证、安全模式

```
 db.auth("userName", "123123");
```



### 显示当前所有用户

```
 show users;
```



### 删除用户

```
 db.removeUser("userName");
```



# 查看聚集集合基本信息

### 查询当前集合的数据条数

```
db.delmail.count();
```



### 查看数据空间的大小

```
db.delmail.dataSize();
```



### 得到当前聚集集合所在的db

```
db.delmail.getDB();
```



#### 得到当前聚集的状态

```
db.delmail.stats();
```

##### dataSize

```
dataSize 指标是存储在数据库中的所有文档和填充的大小（以字节为单位）的总和。

虽然删除文档时 dataSize 会减少，但当文档缩小时 dataSize 不会减少，因为原始文档使用的空间已经分配（给该特定文档）并且不能被其他文档使用。

或者，如果用户用更多数据更新文档，只要新文档适合其最初填充的预分配空间，dataSize 将保持不变。
```

##### storageSize

```
storageSize 指标等于数据库中所有数据区的大小（以字节为单位）。这个数字大于 dataSize，因为它包括尚未使用的空间（在数据范围内）和被删除或移动的文档在范围内腾出的空间。

storageSize 不会随着您删除或缩小文档而减少。
```

##### fileSize 

```
fileSize 指标等于数据库中所有数据范围、索引范围和尚未使用的空间（在数据文件中）的大小（以字节为单位）。此指标表示数据库在磁盘上的存储空间。fileSize 大于 storageSize，因为它包括索引范围和数据文件中尚未使用的空间。

虽然删除数据库时 fileSize 会减少，但删除集合、文档或索引时 fileSize 不会减少。
```



**storageSize指标等于数据库中所有数据扩展区的大小(以字节为单位).如果没有压缩,则此数字大于dataSize,因为它包含尚未使用的空间(在数据范围内)和由范围内已删除或移动的文档腾出的空间.但是,在使用WiredTiger存储引擎时,数据会在磁盘上压缩,因此小于dataSize.**



### 得到聚集集合总大小

```
db.delmail.totalSize();
```



### 聚集集合储存空间大小

```
db.delmail.storageSize();
```



### 聚集集合重命名

```
db.delmail.renameCollection("users")
```



### 删除当前聚集集合

```
db.delmail.drop();
```



# 聚集集合查询

### 查询所有记录

```
db.userInfo.find();

相当于：select* from userInfo;
默认每页显示20条记录，当显示不下的情况下，可以用it迭代命令查询下一页数据。注意：键入it命令不能带“；”
但是你可以设置每页显示数据的大小，用DBQuery.shellBatchSize= 50;这样每页就显示50条记录了。
```









