
from main import app

import webtest
import unittest

class MainPageTest( unittest.TestCase ):

	def setUp( self ):
		self.test_app = webtest.TestApp( app )

	def testHelloWorldHandler( self ):
		response = self.test_app.get( '/foo-bar' )
		self.assertEqual( response.status_int, 301 )
		self.assertEqual( response.location, 'http://your-new-domain.com' )

