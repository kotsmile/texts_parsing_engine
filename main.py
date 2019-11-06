from parsing_engine import random_parse
import time


def save(text, name='def'):
    with open(name, 'w') as f:
        f.write(text)


if __name__ == '__main__':

    # test
    print('0,score,time,url')
    i = 0
    csv = '0,score,time,url\n'
    with open('data/test_set_links.txt', 'r') as f:
        try:
            for link in f:
                i += 1
                time.sleep(2)
                t1 = time.time()
                p_r = random_parse(link.strip())
                t2 = time.time()

                new_line = f'{i},{p_r[3]},{t2 - t1:.2f},{link.strip()}'

                csv += new_line + '\n'

                print(new_line)
                save('\n'.join(p_r[0]), name=f'results/{link.replace("/", ".")}.txt')

        except KeyboardInterrupt:
            save(csv, name='data/res.csv')

    #
    # url = 'http://ai.googleblog.com/'
    # print(*web_parse(url=url, config=configuration.UNIV_DIV)[0], sep='\n')
    #
    #

    # random_parse('https://zillion.net/ru/blog/7402/chiem-zanimaietsia-project-manager')
    # urls = ['https://en.wikipedia.org/wiki/Alcohol',
    #         'https://medium.com/russian/вертикальная-интеграция-в-мире-технологий-6763606ac5cd',
    #         'https://medium.freecodecamp.org/a-beginners-guide-to-training-and-deploying-machine-learning-models-using-python-48a313502e5a',
    #         'https://edition.cnn.com/style/article/george-michael-art-scli-intl-gbr/index.html',
    #         'https://edition.cnn.com/style/article/nasa-60-years-taschen/index.html',
    #         'https://www.bbc.com/news/business-47592812', 'https://habr.com/ru/post/444596/',
    #         'https://www.forbes.com/sites/yayafanusie/2019/03/22/crypto-is-about-to-look-more-like-your-bank/?ss=crypto-blockchain#7ec79a1a5630',
    #         'https://ria.ru/20190323/1552054411.html',
    #         'https://www.cnbc.com/2019/03/23/trump-sends-top-officials-to-beijing-to-continue-china-trade-talks.html',
    #         'https://www.marketwatch.com/story/will-the-mueller-report-roil-the-stock-market-heres-what-it-would-take-2019-03-21?mod=mw_theo_homepage']
    #
    # for ur in urls:
    #     print(ur)
    #     s = fix(url=ur)[0]
    #     print(utils.remove_doubles('\n'.join(s)))
    #     print('----------------------')
