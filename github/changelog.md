# change log

## v2.4

#### 功能特性

- 支持批量替换图标 指定文件
- 支持单块上传资源文件
- 超时提示

#### 代码重构

- Python 版本升级到 3.13
- 迁移环境管理为 uv

## v2.3

#### 功能特性

- 支持PicGo
- 支持批量替换图标

#### 错误修复

- 一些常规错误修复

## v2.2

#### 错误修复

- 无法下载网络图片
- 无法初始化

#### 性能优化

- Record不在记录已删除的文件资源

#### 功能特性

- 支持多个工作空间使用

## v2.1

#### 错误修复

- 修复了变量在赋值前就被引用的错误，避免了潜在的错误和异常。

#### 代码重构

- 合并请求逻辑。
- 优化了 `/config` POST 请求的错误处理，现在错误返回会包含更详细的错误信息。
- 更新了字段名称以匹配外部提供者的变更，确保了数据交互的一致性。
- 将配置信息提取到一个单独的配置类中，使得配置管理更加清晰和易于维护。

#### 风格调整

- 统一编码格式 - utf-8。
- 简化部分方法名称。

#### 代码清理

- 删除了代码中无用的请求部分。

#### 日志增强

- 添加了对缓存更新操作的日志记录，增强了问题的追踪和调试能力。
- 统一了日志结构，使日志输出更加规范。

## V2.0

#### 文档更新：

- README新增层级架构描述。

#### 性能优化：

- 提升代码架构性能。

#### 代码重构：

- 检查和改进路由代码
- 优化资源属性处理。

#### 日志增强：

- 记录HTTP请求来源
- 调整API错误日志级别。
- 优化日志提示

#### 错误修复：

- 处理重启后的加载错误
- 避免P块重复加载。

#### 功能添加：

- 实现思源信息同步推送。

#### 其他改进：

- 修正打字错误。
