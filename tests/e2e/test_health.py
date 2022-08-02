import json
import unittest
import requests


class HeathTest(unittest.TestCase):
    def test_health_endpoint(self):
        r = requests.get("http://localhost:8000/health")

        self.assertEqual(200, r.status_code)

        j = json.loads(r.text)
        self.assertEqual(j["status"], "OK")



if __name__ == '__main__':
    unittest.main()
