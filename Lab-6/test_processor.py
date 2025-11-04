from hypothesis import given, strategies as st
import processor

@given(s=st.text())
def test_sanitize_string_no_crash(s):
    try:
        processor.sanitize_string(s)
    except Exception as e:
        assert False, f"Crash in sanitize_string: {e}"

@given(s=st.text() | st.none())
def test_parse_int_list_no_crash(s):
    try:
        processor.parse_int_list(s)
    except Exception as e:
        assert False, f"Crash in parse_int_list: {e}"

@given(s=st.text() | st.none())
def test_reverse_words_no_crash(s):
    try:
        processor.reverse_words(s)
    except Exception as e:
        assert False, f"Crash in reverse_words: {e}"
