# ChatLaw 大模型文档对话消除幻觉
### 法律知识问答

* 法律文本转为向量

* 使用相似度搜索获取十个top-k

* 基于这十个top-k，上下十行，段落式截取

prompt

==>

法律文库相关文本=[搜索得到的相关法律条例]

我的问题=[用户的输入]

<==

### 需要改进的地方：

* 文本格式的多样化（目前仅支持pdf格式）

* 需要给出模型嵌入文本的样例

* 搭建一个轻量的向量数据库

