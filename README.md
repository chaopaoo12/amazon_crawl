# amazon_crawl 轻量级亚马逊爬虫

-------------------------------------------------------------


零成本小卖家&爱好者爬虫方案

[点击右上角Star和Watch来跟踪项目进展! 点击Fork来创建属于你的亚马逊爬虫!]

==========================================

<!-- TOC -->


<!-- /TOC -->


##  1. 功能
======

已经实现：

### 1.1 亚马逊品类目录树

### 1.2 分频道采集

### 1.3 按店铺采集

### 1.4 按asin 关键词采集

### 1.5 产品详情采集 五点 评论采集

### 1.6 分频道采集的并发版本

### 1.7 待开发功能
根据五点+评论+title做词频分析;接chatgpt写五点与title

##  2. 零成本使用指南
使用请配合科学上网软件构建所需市场的网络环境.
就美区而言 推荐使用cloudflare的worker vless + V2ray + 伪装美区IP.
程序部署环境可以直接访问美区amazon为网络检测标准

##  3. 安装和部署

### 3.1 部署式安装


```
pip install amazon_crawl -U
```
### 3.2  本地代码 开发式安装

本地安装
```
git clone https://github.com/chaopaoo12/amazon_crawl --depth 1

cd amazon_crawl

pip install -e .
```
### 3.3 代码提交式安装

- fork amazon_crawl 到你的github账户

```
git clone https://github.com/你的账户名/amazon_crawl
```

##  4. 项目捐赠

写代码不易...请作者喝杯咖啡呗?


(PS: 支付的时候 请带上你的名字/昵称呀 会维护一个赞助列表~ )
