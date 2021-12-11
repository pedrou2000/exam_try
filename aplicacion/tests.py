from django.test import TestCase

from aplicacion.models import Retweet, Usuario, Tweet
from django.urls import reverse


class ModelTests(TestCase):
    """Test that populate  has been saved data properly
       require files XXXX.pkl stored in the same directory that manage.py"""

    def test01_all(self):
        
        Usuario.objects.all().delete()
        Tweet.objects.all().delete()
        Retweet.objects.all().delete()

        u1 = Usuario(username='usuarioTw1', id=1001)
        u2 = Usuario(username='usuarioTw2', id=1002)
        u1.save()
        u2.save()
        t1 = Tweet(id=1001, texto='texto del tweet 01', usuario=u1, fecha='2021-01-05')
        t1.save()
        r1 = Retweet(id=1001, tweet=t1, usuario=u2, fechaDeRetweet='2021-01-25')


        response = self.client.get(reverse('usuario'), follow=True)
        response_txt = response.content.decode("utf-8")
        self.assertTrue(response_txt.find(r1.fechaDeRetweet) == -1)
        self.assertFalse(response_txt.find(str(1)) == -1)
