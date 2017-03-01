class Segment(dict):

    def __init__(self, user=False):

        self.segment_type = "userSegment" if user else "sessionSegment"

        self["dynamicSegment"] = {
            "name": "arbitrary_segment",
            self.segment_type:
            {
                "segmentFilters": [
                    {
                        "simpleSegment":
                        {
                            "orFiltersForSegment": []
                        }
                    }]
            }
        }

    def add_filter(self, filter_clause):

        self[
            "dynamicSegment"
        ][self.segment_type]['segmentFilters'][0]["simpleSegment"][
            "orFiltersForSegment"
        ] += [filter_clause]

        return self
