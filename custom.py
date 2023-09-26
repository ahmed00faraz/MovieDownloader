import threading


def get_input_with_timeout(x, default_value):
    """Waits for an input for x seconds, and if no input is provided it takes on the default value.

    Args:
      x: The number of seconds to wait for input.
      default_value: The default value to return if no input is provided.

    Returns:
      The input value, or the default value if no input is provided.
    """

    input_value = None

    def input_thread():
        nonlocal input_value
        input_value = input()

    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    # Use the time module to wait for the input thread to finish executing.
    input_thread.join(x)

    if input_value is None:
        return default_value
    else:
        return input_value


# # Example usage:
#
# default_value = "instant"
# input_value = get_input_with_timeout(5, default_value)
#
# print(input_value)
