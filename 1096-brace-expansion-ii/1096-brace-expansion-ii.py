class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        words = set()
        def expand(current: str) -> None:
            close = current.find("}")
            if close == -1:
                words.add(current)
                return
            open_at = current.rfind("{", 0, close)
            prefix = current[:open_at]
            suffix = current[close + 1:]
            for choice in current[open_at + 1:close].split(","):
                expand(prefix + choice + suffix)

        expand(expression)
        return sorted(words)