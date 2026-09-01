print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now... THIS WILL RAISE AN UNCAUGHT EXCEPTION")

if __name__ == "__main__":
    from alchemy.grimoire import dark_spellbook
    dark_spellbook.dark_spell_record("Curse", "bats, frogs, arsenic")
