"""
Homework #7
"""


class CourtCase:
    case_number = ""
    case_participants = []
    listening_datetimes = []
    is_finished = False
    verdict = ""

    def __init__(self, case_number):
        self.case_number = case_number

    def set_a_listening_datetime(self, date):
        self.listening_datetimes.append(date)

    def add_participant(self, party):
        self.case_participants.append(party)

    def remove_participant(self, party):
        self.case_participants.remove(party)

    def make_a_decision(self, verdict):
        self.verdict = verdict
        self.is_finished = True


if __name__ == '__main__':
    case = CourtCase("121")
