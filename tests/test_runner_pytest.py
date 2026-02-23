import importlib

def test_tc1_create_invalid_empty_name():
    mod = importlib.import_module("tests.test_damncrud")
    mod.tc1_create_invalid_empty_name()

def test_tc2_create_valid():
    mod = importlib.import_module("tests.test_damncrud")
    mod.tc2_create_valid()

def test_tc3_update_kontak_change_title():
    mod = importlib.import_module("tests.test_damncrud")
    created = mod.tc2_create_valid()
    mod.tc3_update_kontak_change_title(created)

def test_tc4_delete_kontak():
    mod = importlib.import_module("tests.test_damncrud")
    created = mod.tc2_create_valid()
    mod.tc4_delete_kontak(created)

def test_tc5_create_invalid_empty_phone():
    mod = importlib.import_module("tests.test_damncrud")
    mod.tc5_create_invalid_empty_phone()