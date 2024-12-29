# Qwen2.5-7b微调
基于Qwen2.5模型、使用DISC-Law-SFT-Pair数据集和[LLaMa-Factory](https://github.com/hiyouga/LLaMA-Factory/tree/main "访问LLa-Ma-Factory项目")微调的法律大模型

### 资源下载

下载并安装LLaMA-Factory：

```
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

下载[Qwen2.5-7b-Instruct](https://www.modelscope.cn/models/qwen/Qwen2.5-7B-Instruct "访问魔塔社区")，将下载好的模型放到LLaMa-Factory目录下，同时将本项目的所有文件也放到LLaMa-Factory目录下

### 文件目录结构

![image-20241229182935918](C:\Users\86188\AppData\Roaming\Typora\typora-user-images\image-20241229182935918.png)

### 模型训练

在终端使用命令`llamafactory-cli train qwen2.5-7b-lora-sft.yaml`来进行训练，训练完成后对权重进行合并`llamafactory-cli export qwen2.5-7b-merge-lora.yaml`（关于配置文件的详细信息可访问[LLaMA Factory](https://llamafactory.readthedocs.io/zh-cn/latest/index.html)）

### 模型使用

运行本项目的chat.py即可使用