import unittest
from app.models import Pitch,User
from app import db

class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_mariga = User(username = 'mariga',password = 'ze11yjones', email = 'johnmariga8@gmail.com')
        self.new_comment = Comment(pitch_id=1234,pitch_title='create comment',comment_pitch='web developers are the best',user = self.user_mariga)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blogs,'An opening forum for youths')
        self.assertEquals(self.new_blog.user,self.user_mariga)

    def test_save_pitch(self):
        self.new_blog.save_blogs()
        self.assertTrue(len(blogs.query.all())>0)

    def test_get_blogs_by_id(self):

        self.new_blogs.save_blog()
        get_blogs = Blog.get_all_blogs()
        self.assertTrue(len(got_blogs) == 1)

