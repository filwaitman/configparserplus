# -*- coding: utf-8 -*-
import unittest
from configparserplus import ConfigParserPlus
import os

fixtures_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')


class MainTestCase(unittest.TestCase):
    def assertDoesNotHaveSection(self, config, section_name):
        return section_name not in config.sections()

    def assertDoesNotHaveItem(self, config, section_name, item_name):
        try:
            config.get(section_name, item_name)
            self.fail()
        except:
            pass

    def test_case1(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case1', 'common.ini'))

        self.assertEquals(config.get('main', 'bla'), 'ble')
        self.assertEquals(config.get('oi', 'x'), 'y')

    def test_case2_grandfather(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case2', 'grandfather.ini'))

        self.assertEquals(config.get('person', 'name'), 'gf')
        self.assertEquals(config.get('person', 'age'), '100')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertDoesNotHaveSection(config, 'father')
        self.assertDoesNotHaveSection(config, 'child')
        self.assertDoesNotHaveSection(config, 'foo')
        self.assertDoesNotHaveSection(config, 'entire_block')

    def test_case2_father(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case2', 'father.ini'))

        self.assertEquals(config.get('person', 'name'), 'f')
        self.assertEquals(config.get('person', 'age'), '50')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertEquals(config.get('father', 'profession'), 'woodworker')

        self.assertEquals(config.get('foo', 'only_father'), 'true')

        self.assertEquals(config.get('entire_block', 'x'), 'x')
        self.assertEquals(config.get('entire_block', 'y'), 'y')

        self.assertDoesNotHaveSection(config, 'child')

    def test_case2_child(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case2', 'child.ini'))

        self.assertEquals(config.get('person', 'name'), 'c')
        self.assertEquals(config.get('person', 'age'), '30')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertEquals(config.get('father', 'profession'), 'woodworker')

        self.assertEquals(config.get('child', 'profession'), 'systems analyst')

        self.assertEquals(config.get('entire_block', 'z'), 'z')

        self.assertDoesNotHaveSection(config, 'foo')

    def test_case3_grandfather(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case3', 'father', 'grandfather', 'base.ini'))

        self.assertEquals(config.get('person', 'name'), 'gf')
        self.assertEquals(config.get('person', 'age'), '100')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertDoesNotHaveSection(config, 'father')
        self.assertDoesNotHaveSection(config, 'child')
        self.assertDoesNotHaveSection(config, 'foo')
        self.assertDoesNotHaveSection(config, 'entire_block')

    def test_case3_father(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case3', 'father', 'base.ini'))

        self.assertEquals(config.get('person', 'name'), 'f')
        self.assertEquals(config.get('person', 'age'), '50')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertEquals(config.get('father', 'profession'), 'woodworker')

        self.assertEquals(config.get('foo', 'only_father'), 'true')

        self.assertEquals(config.get('entire_block', 'x'), 'x')
        self.assertEquals(config.get('entire_block', 'y'), 'y')

        self.assertDoesNotHaveSection(config, 'child')

    def test_case3_child(self):
        config = ConfigParserPlus()
        config.read(os.path.join(fixtures_dir, 'case3', 'child.ini'))

        self.assertEquals(config.get('person', 'name'), 'c')
        self.assertEquals(config.get('person', 'age'), '30')
        self.assertEquals(config.get('person', 'family'), 'Waitman')

        self.assertEquals(config.get('grandfather', 'profession'), 'slave')

        self.assertEquals(config.get('father', 'profession'), 'woodworker')

        self.assertEquals(config.get('child', 'profession'), 'systems analyst')

        self.assertEquals(config.get('entire_block', 'z'), 'z')

        self.assertDoesNotHaveSection(config, 'foo')
