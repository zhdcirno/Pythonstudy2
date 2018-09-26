# LOG
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- logging模块提供模块级别的函数记录日志
- 包括四大组件

## 1. 日志相关概念
- 日志
- 日志的级别（level）
    - 不同用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging

# 2. logging模块
- 日志级别
    - 级别可以定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，需要高于或者等于指定级别才被记录
- 使用方式
    - 直接使用logging(封装了其他组件）
    - logging四大组件直接定制

## 2.1 logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg, *args, **kwargs) 创建一条严重级别为Debug的日志记录
    - logging.info(msg, *args, **kwargs) 创建一条严重级别为  的日志记录
    - logging.warning(msg, *args, **kwargs) 创建一条严重级别为  的日志记录
    - logging.error(msg, *args, **kwargs) 创建一条严重级别为  的日志记录
    - logging.log(level, *args, **kwargs) 创建一条严重级别为  的日志记录
    - logging.basicConfig(**kwargs) 对root logger进行一次性配置

- logging.basicConfig(**kwargs) 对root logger进行一次性配置
    - 只在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr
        - 级别： WARNING
        - 格式：level：log_name:content
- 案例 01
- format参数

## 2.2 logging模块的处理流程
- 四大组件
    - 日志器（logger）：产生日志的接口
    - 处理器（handler）：把生产的日志发送到相应的目的地
    - 过滤器（filter）：精细控制日志输出
    - 格式器（formatter）：对输出信息进行格式化
- logger
    - 产生一个日志
    - 操作

            logger.setLevel(): 设置日志器处理日志消息的最低严重级别
            logger.addHandler():
            logger.addFilter():
            logger.debug():
            logger.exception():
            logger.log():
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()

- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter， removeFilter
    - 不需要直接使用，Handler是基类

            logging.StreamHandler
            logging.FileHandler
            logging.handlers.RotatingFileHandler
            logging.handlers.TimeRotatingFileHandler
            logging.handlers.HttpHandler
            logging.handlers.SMTPHandler
            logging.NullHander

- Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数
        - fmt
        - datefmt
        - style
- Filter类
    - 可以倍Handler和Logger使用
    - 控制传递过来的信息的具体内容
    - 案例02