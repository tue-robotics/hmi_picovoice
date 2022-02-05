import rospy
from actionlib import SimpleActionClient
from hmi import AbstractHMIServer, HMIResult
from picovoice_msgs.msg import GetIntentAction, GetIntentGoal


class HMIServerPicovoiceClient(AbstractHMIServer):
    """
    HMIServerPicoVoiceClient
    Provide an hmi server which uses the picovoice speech recognition.
    """
    def __init__(self):
        super(HMIServerPicovoiceClient, self).__init__(rospy.get_name())
        self.ac_picovoice_ = SimpleActionClient("porcupine_node", GetIntentAction)

    def _determine_answer(self, description, grammar, target, is_preempt_requested):
        """
        Overwrites abstract method _determine_answer from parent class AbstractHMIServer to provide an implementation.
        :param description:
        :param grammar:
        :param target:
        :param is_preempt_requested:
        :return:
        """
        ac_goal = GetIntentGoal
        ac_goal.context_url = "gpsr_linux.rhn"

        result = self.ac_picovoice_.send_goal_and_wait(ac_goal)
        if result is None:
            return None

        if not result.is_understood:
            return None

        sentence = result.intent
        semantics = result.slots

        return HMIResult(sentence, semantics)
