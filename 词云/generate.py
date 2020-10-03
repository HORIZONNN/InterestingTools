#-*-coding:utf-8—-*-
import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
from imageio import imread
import matplotlib.pyplot as plt
import pygame
import sys
 
class wc:
    def __init__(self,txt_file,img_file,font_file):
        self.f = open(txt_file,'r')
        self.txt = self.f.read()
        self.f.close()
        self.tags = jieba.analyse.extract_tags(self.txt,topK=100)
    #topK说白了就是返回几个关键词
        self.text = ' '.join(self.tags) #把分词链接起来，加空格因为英文靠空格分词
        self.img = imread(img_file)
        self.wc = WordCloud(width=2000, height=1000,font_path=font_file,background_color='white',max_words=200,mask=self.img,max_font_size=1000)
    ###直接在这里进行猜###
    #font_path指的是字体文件路径，因为wordcloud自带的字体不支持中文所以我们要指定一个字体文件，否者输出的图片全是框框
    #background_color 默认是黑色　我设置成白色
    #max_words最大显示的词数
    #mask 背景图片
    #max_font_size　最大字体字号
        self.word_cloud = self.wc.generate(self.text)
    
    def show_wc(self):
    #img_color = ImageColorGenerator(self.img)
        plt.imshow(self.word_cloud)
    #可以通过 plt.imshow(self.wc.recolor(color_func=img_color))使图片颜色跟字体颜色一样
        plt.axis("off")
        plt.savefig('jiqi.jpg')
        plt.show()


def gen_word_img(word, out_file):
    pygame.init() 
    # 设置字体和字号
    # print(pygame.font.get_fonts())
    font = pygame.font.SysFont("microsoftyaheimicrosoftyaheiuibold", 640)
    # 设置字体颜色和背景颜色
    word_img = font.render(word, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(word_img, out_file)
 

def gen_cloud_img(text_file, img_file, font_file, out_file):
    # 提取文本中的高频关键词
    with open(text_file, 'r') as f:
        tags = jieba.analyse.extract_tags(f.read(), topK=100)

    # 生成词云
    img = imread(img_file)
    wc = WordCloud(width=2000, height=1000,font_path=font_file,background_color='white',max_words=200,mask=img,max_font_size=1000)
    cloud_image = wc.generate(' '.join(tags))
    plt.imshow(cloud_image)
    plt.axis('off')
    plt.savefig(out_file)


 
if __name__=='__main__':

    gen_word_img(sys.argv[1], 'word.jpg')
    gen_cloud_img('test.txt','word.jpg','font.ttf', 'cloud.jpg')