import unittest
from lab3 import NPC

class TestNPC(unittest.TestCase):

    def setUp(self):
        self.npcs = [
            NPC("Aragorn", 10, 150.5, 80, "Warrior"),
            NPC("Gandalf", 20, 100.0, 95, "Mage"),
            NPC("Legolas", 15, 120.0, 70, "Archer"),
            NPC("Gimli", 15, 200.0, 85, "Warrior"),
            NPC("Frodo", 5, 80.0, 30, "Hobbit")
        ]

    def test_equality(self):
        npc1 = NPC("Gandalf", 20, 100.0, 95, "Mage")
        npc2 = NPC("Gandalf", 20, 100.0, 95, "Mage")
        npc3 = NPC("Frodo", 5, 80.0, 30, "Hobbit")

        self.assertEqual(npc1, npc2)
        self.assertNotEqual(npc1, npc3)

    def test_sorting(self):
        sorted_npcs = sorted(self.npcs, key=lambda x: (x.level, -x.health))
        actual_order = [npc.name for npc in sorted_npcs]

        expected_order = ["Frodo", "Aragorn", "Gimli", "Legolas", "Gandalf"]
        self.assertEqual(actual_order, expected_order)

    def test_search(self):
        target = NPC("Gandalf", 20, 100.0, 95, "Mage")

        found = any(npc == target for npc in self.npcs)

        self.assertTrue(found)