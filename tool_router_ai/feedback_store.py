from collections import defaultdict


class FeedbackStore:

    def __init__(self):

        self.success = defaultdict(int)
        self.failure = defaultdict(int)

    def record_success(self, tool_name):

        self.success[tool_name] += 1

    def record_failure(self, tool_name):

        self.failure[tool_name] += 1

    def score(self, tool_name):

        s = self.success[tool_name]
        f = self.failure[tool_name]

        if s + f == 0:
            return 0

        return s / (s + f)