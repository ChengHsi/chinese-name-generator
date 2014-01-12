# -*- coding: utf-8 -*-
from random import choice
def random_chinese_name():
    last_name = "李 王 張 劉 陳 楊 黃 趙 周 吳 徐 孫 朱 馬 胡 郭 林 何 高 梁 鄭 羅 宋 謝 唐 韓 曹 許 鄧 蕭 馮 曾 程 蔡 彭 潘 袁 董 蘇 葉 呂 魏 蔣 田 杜 丁 沈 姜 江 傅 鐘 盧 汪 戴 崔 任 陸 廖 姚 方 金 邱 夏 譚 韋 賈 鄒 石 熊 秦 閻 薛 侯 雷 白 龍 段 郝 孔 邵 毛 萬 顧 賴 武 嚴 尹 錢 施 牛 洪 龔".split(" ")
    first_name1 = "譯 慷 振 傑 諾 以 錫 世 中 仁 佳 宇 維 傑 恆 建 智 顯 璿 俊 信 倫 正 庭 謙 律 翔 濬 毅 孟 宏 俊 偉 傑 儀 元 冠 凱 君 哲 嘉 國 士 如 子 孟 宇 安 範 宏 宗 宜 家 建 弘 強 彥 彬 德 心 志 忠 慶 憲 成 政 孟 敏 文 昌 明 智 曉 柏 榮 欣 正 民 永 祥 秋 穎 立 維 翔 翰 聖 育 良 英 菁 華 裕 豪 賢 郁 銘 青 靜 龍 思 晉 鉦 軍 永 成 峻 庭 峻 寬 鎮 葳 毓 麟 柏 翔 達 祐 季 穎 順 嘉".split(" ")
    first_name2 = "譯 慷 振 傑 諾 以 錫 世 中 仁 佳 宇 維 傑 恆 建 智 顯 璿 俊 信 倫 正 庭 謙 律 翔 濬 毅 孟 宏 俊 偉 傑 儀 元 冠 凱 君 哲 嘉 國 如 子 孟 宇 安 宏 宗 宜 家 建 弘 強 彥 彬 德 志 忠 慶 憲 成 政 敏 文 孟 昌 明 智 曉 柏 榮 欣 正 民 永 祥 秋 穎 立 康 賀 維 翔 翰 聖 育 良 英 菁 華 裕 豪 賢 郁 銘 青 靜 龍 汗 晉 鉦 軍 永 成 峻 庭 峻 寬 鎮 葳 毓 麟 柏 翔 達 祐 季 穎 順 嘉".split(" ")
    
    ### allow possiblity of name with only two words ###
    for i in range(len(first_name2)/20):
    	first_name2.append(" ")
    ### get name ###
    for i in range(100):
    	name = choice(last_name) + choice(first_name1) + choice(first_name2)
        name = name.replace(' ', '')
    	print (name + ","),
    	i += 1

random_chinese_name()
