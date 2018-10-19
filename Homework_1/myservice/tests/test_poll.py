from myservice.classes.poll import Poll, UserAlreadyVotedException, NonExistingOptionException
import unittest


class TestPoll(unittest.TestCase):

    def test_constructor(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)
        self.assertEqual(poll.title, "TestTitle")
        self.assertEqual(poll.id, 13)

        self.assertEqual(poll.get_winners(), ["1", "2", "3"])

    def test_single_vote(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)
        poll.vote("Wilma", "1")

        self.assertEqual(poll.get_winners(), ["1"])

    def test_votes(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)

        self.assertEqual(poll.get_winners(), ["1", "2", "3"])

        poll.vote("Wilma", "1")
        poll.vote("Fred", "2")

        self.assertEqual(poll.get_winners(), ["1", "2"])

    def test_votes_delete(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)
        poll.vote("Wilma", "1")
        poll.vote("Fred", "2")
        poll.delete_voted_options("Fred")

        self.assertEqual(poll.get_winners(), ["1"])

    def test_already_voted(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)
        poll.vote("Wilma", "1")

        self.assertRaises(UserAlreadyVotedException, poll.vote, "Wilma", "1")

    def test_not_existing_option(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)

        self.assertRaises(NonExistingOptionException, poll.vote, "Wilma", "5")

    def test_serialize(self):
        options = ["1", "2", "3"]
        poll = Poll(13, "TestTitle", options)

        self.assertEqual(poll.serialize(), {
            "id": poll.id,
            "title": poll.title,
            "options": poll.options,
            "winners": ["1", "2", "3"]
        })


if __name__ == '__main__':
    unittest.main()
