import time
import pytest
from datetime import datetime

from hub_py.time import (
    FARCASTER_EPOCH,
    from_farcaster_time,
    get_farcaster_time,
    to_farcaster_time,
    datetime_from_farcaster_time,
)


def test_get_farcaster_time():
    farcaster_time = get_farcaster_time()
    assert farcaster_time is not None
    assert isinstance(farcaster_time, int)


def test_to_farcaster_time_valid():
    input_time = FARCASTER_EPOCH + 100_000
    expected_output = (input_time - FARCASTER_EPOCH) // 1000
    assert to_farcaster_time(input_time) == expected_output


def test_to_farcaster_time_invalid_before_epoch():
    input_time = FARCASTER_EPOCH - 100_000
    assert to_farcaster_time(input_time) is None


def test_to_farcaster_time_invalid_too_far_in_future():
    input_time = FARCASTER_EPOCH + (2**32) * 1000
    assert to_farcaster_time(input_time) is None


def test_from_farcaster_time():
    farcaster_time = 1_000
    expected_output = (farcaster_time * 1000) + FARCASTER_EPOCH
    assert from_farcaster_time(farcaster_time) == expected_output


def test_datetime_from_farcaster_time_now():
    now = datetime.now().replace(microsecond=0)
    current_time = int(now.timestamp() * 1000)
    farcaster_time = to_farcaster_time(current_time)
    assert datetime_from_farcaster_time(farcaster_time) == now


@pytest.mark.parametrize("time_value", [0, 1_000, 2_000, 10_000, 100_000])
def test_conversion_consistency(time_value):
    farcaster_time = to_farcaster_time(FARCASTER_EPOCH + time_value * 1000)
    assert farcaster_time is not None
    assert farcaster_time < 2**32 - 1  # uint32 max value
    assert from_farcaster_time(farcaster_time) == FARCASTER_EPOCH + time_value * 1000


def test_conversion_consistency_now():
    current_time = time.time_ns() // 1_000_000  # Get current time in milliseconds
    rounded_time = current_time // 1000 * 1000
    farcaster_time = to_farcaster_time(current_time)
    assert farcaster_time < 2**32 - 1  # uint32 max value
    assert from_farcaster_time(farcaster_time) == rounded_time
