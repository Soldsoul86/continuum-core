from collections import defaultdict

class ActorInterpreter:
    def __init__(self, events):
        self.events = events

    def actor_timelines(self):
        actors = defaultdict(list)

        for event in self.events:
            actor = event.get("actor")
            if actor:
                actors[actor].append(event)

        return dict(actors)

