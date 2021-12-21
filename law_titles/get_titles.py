from typing import List

from lxml import etree


def get_testgb_titles() -> List[str]:
    """Extract the title fields for all <norm>-elements except the first one (it
    only contains metadata for the whole law). Return them as a list. For the expected
    result see the corresponding test."""

    # YOUR CODE HERE

    return all_titles


if __name__ == "__main__":
    all_titles = get_testgb_titles()
    print(all_titles)
