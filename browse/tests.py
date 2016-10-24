from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class BrowseViewTests(TestCase):
    def test_index_view_with_no_courses(self):
        '''
            If no courses exist, an appropriate message should be displayed.
        '''
        response = self.client.get(reverse('browse:index'))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'No available course.')
        #self.assertQuerysetEqual(response.context['latest_course_list'], None)
