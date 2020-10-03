#-*-coding:utf-8—-*-
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
from imageio import imread
import matplotlib.pyplot as plt
import pygame
import sys
import numpy as np


def gen_cloud_img(word, text_file, font_file, out_file):

    pygame.init() 
    # 设置字体和字号
    # print(pygame.font.get_fonts())
    font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 1000)
    # 设置字体颜色和背景颜色
    word_img = font.render(word, True, (0, 0, 0), (255, 255, 255))

    # 因为没找到pygame.Surface转换为imageio.core.util.Array的方法，所以只能保存一遍然后再重新读取
    pygame.image.save(word_img, "temp.png")
    word_img = imread('temp.png')

    # 提取文本中的高频关键词
    with open(text_file, 'r') as f:
        tags = jieba.analyse.extract_tags(f.read(), topK=100)

    #font_path指的是字体文件路径，因为wordcloud自带的字体不支持中文所以我们要指定一个字体文件，否者输出的图片全是框框
    #background_color 默认是黑色　我设置成白色
    #max_words最大显示的词数
    #mask 背景图片
    #max_font_size　最大字体字号
    wc = WordCloud(width=word_img.shape[1], height=word_img.shape[0],font_path=font_file,background_color='white',max_words=200,mask=word_img,max_font_size=1000)
    cloud_image = wc.generate(' '.join(tags))
    plt.imshow(cloud_image)
    plt.axis('off')
    plt.savefig(out_file)


 
if __name__=='__main__':
    gen_cloud_img(sys.argv[1], 'test.txt','font.ttf', 'cloud.jpg')