from django.test import TestCase

from jungblog.utils import *


class jungblogTest(TestCase):
    def setUp(self):
        pass

    def test_utils(self):
        md5 = get_sha256('test')
        self.assertIsNotNone(md5)
        c = CommonMarkdown.get_markdown('''
        # Title1

        ```python
        import os
        ```

        [url](https://www.tycng.com/)

        [ddd](http://www.baidu.com)


        ''')
        self.assertIsNotNone(c)
        d = {
            'd': 'key1',
            'd2': 'key2'
        }
        data = parse_dict_to_url(d)
        self.assertIsNotNone(data)
