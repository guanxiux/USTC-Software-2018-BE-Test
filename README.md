# USTC-Software-2018-BE-Test
USTC iGEM Software 2018 Back-end Test Project

## 目标

你的目标是使用 GitHub **fork 本仓库**，编写一个简单的 Django 程序，并且**修改本文件**完成文末的简单报告，完成之后**发起 Pull Request**。

截止日期是：2018 年 7 月 8 日 23:00。

### 完成目标的流程

一共有四个步骤：

- fork 本仓库；
- 编写 Django 程序（已经创建在 be_test）；
- 修改本文件完成报告；
- 发起 Pull Request；

### 约定

为了节约大家时间，尽量使用默认情况下的组件：

- 使用 Python 3.6；
- 使用 Django 2.0；
- 使用默认数据库（SQLite）和 ORM；
- 使用默认内建 HTTP Server；
- 使用默认监听端口；
- 不必使用 Template；
- 不必编写 HTML 页面（返回值是 json 或图片）；

### 目标功能

- 注册 login
- 登陆 register
- 个人信息 profile
- 登出 logout （选做）
- 生成图表 chart（选做）

### 功能描述

用户能注册新账号，登陆账号并且在个人信息中看到自己的用户名。

用户登出后将不能在个人信息中看到相关信息。

使用生成图表功能，用户可以传入一列数据，得到一张折线图（横坐标默认为 1, 2, ..., n）。

## 细节

### 数据格式

#### 传入参数

如果为 GET 请求类型，则以 `/api?key=value` 的方式传入；

如果为 POST 请求类型，则以 `/api` 并且附加 POST 参数 `key=value` 的方式传入。

#### 返回内容

返回内容使用 json 格式，如：

```json
{
    "err_code": 0,
    "err_msg": ""
}
```

### 注册

POST /user/register

| 参数 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| username | 不能为空 | 用户名 |
| password | 不能为空 | 密码 |

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |

注册一个新账号。

基础要求：

- 传入没有使用过的用户名时能够注册成功，并返回 `err_code` 为 0。

加分项：

- 用户名限制允许的字符集和长度，并返回相应的错误信息；
- 密码限制允许的字符集和长度，并返回相应的错误信息；
- 密码限制最低复杂度，并返回相应的错误信息；

### 登陆

POST /user/login

| 参数 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| username | 不能为空 | 用户名 |
| password | 不能为空 | 密码 |

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |

登陆一个账号。

基础要求：

- 用户名密码正确时，登陆成功，并设置 session 为登录状态，返回登陆成功的代码；
- 用户名密码错误时，返回错误信息；

加分项：

- 适当修改接口，使得可以定制保持登陆的时间；
- 记录用户最近一次登陆时间；
- 记录用户最近一次登陆 IP；

### 个人信息

GET /user/profile

| 返回值 | 默认 | 描述 |
| ------------- |:-------------:| -----:|
| err_code | 0 | 错误码 |
| err_msg  | 空 | 错误消息 |
| username  | 空 | 用户名 |

获得登陆账号的信息。

基础要求：

- 如果用户已经登陆，在 `username` 中返回登陆的用户名，否则为空；

加分项：

- 如果用户未登陆，返回错误信息；

### 登出

GET /user/logout

|  返回值  | 默认 |   描述   |
| ------------- |:-------------:| -----:|
| err_code | 0    |  错误码  |
| err_msg  | 空   | 错误消息 |

登出用户。

基本要求：

- 清除登陆的凭证（session）；

加分项：

- 记录用户最后一次登出时间；
- 记录用户最近一次登出 IP；

### 生成图表

POST /chart/simple

自行设置参数格式，返回一张可以在线预览的图片；

基本要求：

- 能够根据给出的数据画出折线图；

加分项：

- 返回的页面正确设置类型，使得图片能在浏览器中直接预览（而不是下载）；
- 对同一组数据不重复生成图片；
- 能够通过参数指定不同大小；

## 检查方式

### 基础要求

使用脚本进行自动检查。

### 加分项

采用人工检查。

### 其他

良好的代码风格（如变量命名）会有额外加分；

良好的文档会有额外加分；

良好的 Git 提交记录（每次提交有明确的信息）会有额外加分；

良好的安全性、鲁棒性、可扩展性会有额外加分；

良好的单元测试有额外加分；

## 报告（需要完成）

请面向该后端应用的使用者（前端组），完成下面报告。

### 调用方法

+   /user/login 登陆功能
    +   向 /user/login 用 post 方法传递字典{username: \$(username), password: \$(password)}
+   /user/register 注册功能
    +    向 /user/register 用 post 方法传递字典{username: \$(username), password: \$(password)}
+   /user/profile 查看详细信息功能
    +   直接跳转到 /user/profile
+   /user/logout 登出功能
    +   直接跳转到 /user/logout
+   /chart/simple 画图功能
    +   向 /chart/simple 用 post 方法传递字典 {array: $(array[])}

### 注意事项

（坑）

### 错误码约定

| err_code |                  err_msg                  |         出现的场所          |
| :------: | :---------------------------------------: | :-------------------------: |
|    0     |                    空                     |                             |
|    1     | Username or password should not be empty. | /user/login和/user/register |
|    2     |   This username is already registered.    |       /user/register        |
|    3     |         Username does not exist.          |         /user/login         |
|    4     |              Wrong password.              |         /user/login         |
|    5     |          You are not logged in.           |        /user/profile        |
|    6     |           User does not exist.            |        /user/logout         |

