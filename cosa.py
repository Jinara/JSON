import test.testCase


class TestCreatesAJsonOutOfAString(TestCase):
    def test_oeuidhdiue(self):
         json_string = '{"name":"nathaly","last_name":"villamor","ages":[1,2,3],"cosas":[{"a":4},{"b":4},{"c":5}],"age":21,"height":1.60,"document":{"algo":234}}'
         expected = MyClass(json_string).parse
         self.assertEqual(expected, {"name": "nathaly", "last_name": "villamor"})

class MyClass(Object):
    def __init__(self, data):
        pass


tree = {
  "-": {
        "0": None,
        "\d": {
            "\d": None,
            ".": None,
        },
      }
  "0": {
     ".": {
       "\d": None,
     },
  }

}
