from posthog.utils import patchable


@patchable
def i_am_your_func(name: str) -> str:
    return f"you want some {name}?"